#! /usr/bin/env python
"""Simple dedupe functionality (based on similarity thresholds) for small samples"""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import pandas as pd
import zope.interface
from dataclasses_jsonschema import JsonSchemaMixin

import colrev.env.package_manager
import colrev.exceptions as colrev_exceptions
import colrev.ops.built_in.dedupe.utils
import colrev.record
from colrev.constants import Colors
from colrev.constants import Fields

if TYPE_CHECKING:
    import colrev.ops.dedupe

# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods


@zope.interface.implementer(colrev.env.package_manager.DedupePackageEndpointInterface)
@dataclass
class SimpleDedupe(JsonSchemaMixin):
    """Simple duplicate identification (for small sample sizes)"""

    settings: SimpleDedupeSettings

    ci_supported: bool = True

    @dataclass
    class SimpleDedupeSettings(
        colrev.env.package_manager.DefaultSettings, JsonSchemaMixin
    ):
        """Settings for SimpleDedupe"""

        endpoint: str
        merging_non_dup_threshold: float = 0.7
        merging_dup_threshold: float = 0.95

        _details = {
            "merging_non_dup_threshold": {
                "tooltip": "Threshold: record pairs with a similarity "
                "below this threshold are considered non-duplicates"
            },
            "merging_dup_threshold": {
                "tooltip": "Threshold: record pairs with a similarity "
                "above this threshold are considered duplicates"
            },
        }

    settings_class = SimpleDedupeSettings

    def __init__(
        self,
        *,
        dedupe_operation: colrev.ops.dedupe.Dedupe,
        settings: dict,
    ):
        self.settings = self.settings_class.load_settings(data=settings)
        self.dedupe_operation = dedupe_operation
        self.review_manager = dedupe_operation.review_manager

        assert self.settings.merging_non_dup_threshold >= 0.0
        assert self.settings.merging_non_dup_threshold <= 1.0
        assert self.settings.merging_dup_threshold >= 0.0
        assert self.settings.merging_dup_threshold <= 1.0

    def __get_maximum_similarity_record(
        self,
        *,
        records_batch: list,
    ) -> dict:
        max_similarity_record = {
            "reference_record": records_batch[len(records_batch) - 1][Fields.ID],
            "record_id": "NA",
            "similarity": 0,
        }
        for i in range(0, len(records_batch) - 1):
            sim_details = colrev.record.Record.get_similarity_detailed(
                record_a=records_batch[i],
                record_b=records_batch[len(records_batch) - 1],
            )

            if sim_details["score"] > max_similarity_record["similarity"]:
                max_similarity_record["similarity"] = sim_details["score"]
                max_similarity_record["record_id"] = records_batch[i][Fields.ID]
                max_similarity_record["details"] = sim_details["details"]

        return max_similarity_record

    def __append_merges(self, *, batch_item: dict) -> dict:
        records_batch = batch_item["queue"]

        # if the record is the first one added to the records
        # (in a preceding processing step), it can be propagated
        if len(records_batch) < 2:
            return {
                "ID1": batch_item["record"],
                "ID2": "NA",
                "similarity": 1,
                "decision": "no_duplicate",
            }

        # df to get_similarities for each other record
        similarity_dict = self.__get_maximum_similarity_record(
            records_batch=records_batch
        )

        max_similarity = similarity_dict["similarity"]

        ret = {}
        if max_similarity <= self.settings.merging_non_dup_threshold:
            # Note: if no other record has a similarity exceeding the threshold,
            # it is considered a non-duplicate (in relation to all other records)
            # self.review_manager.logger.debug(
            #     f"max_similarity ({max_similarity})"
            # )
            ret = {
                "ID1": similarity_dict["reference_record"],
                "ID2": "NA",
                "similarity": max_similarity,
                "decision": "no_duplicate",
            }

        elif (
            self.settings.merging_non_dup_threshold
            < max_similarity
            < self.settings.merging_dup_threshold
        ):
            other_id = similarity_dict["record_id"]
            # self.review_manager.logger.debug(
            #     f"max_similarity ({max_similarity}): {batch_item['record']} {other_id}"
            # )
            # details = similarity_dict["details"]
            # self.review_manager.logger.debug(details)
            # record_a, record_b = sorted([ID, record[Fields.ID]])
            msg = (
                f'{similarity_dict["reference_record"]} - {other_id}'.ljust(35, " ")
                + f"  - potential duplicate (similarity: {max_similarity})"
            )
            # self.review_manager.report_logger.info(msg)
            self.review_manager.logger.info(msg)
            ret = {
                "ID1": similarity_dict["reference_record"],
                "ID2": other_id,
                "similarity": max_similarity,
                "decision": "potential_duplicate",
            }

        else:  # max_similarity >= self.settings.merging_dup_threshold:
            # note: the following status will not be saved in the bib file but
            # in the duplicate_tuples.csv (which will be applied to the bib file
            # in the end)
            other_id = similarity_dict["record_id"]

            # self.review_manager.logger.debug(
            #     f"max_similarity ({max_similarity}): {batch_item['record']} {other_id}"
            # )
            # details = similarity_dict["details"]

            # self.review_manager.logger.debug(details)
            msg = (
                "Dropped duplicate: "
                f'{similarity_dict["reference_record"]} (duplicate of {other_id})'
                # + f" (similarity: {max_similarity})\nDetails: {details}"
            )
            self.review_manager.report_logger.info(msg)
            self.review_manager.logger.info(msg)
            ret = {
                "ID1": similarity_dict["reference_record"],
                "ID2": other_id,
                "similarity": max_similarity,
                "decision": "duplicate",
            }
        return ret

    def __get_dedupe_data(self) -> dict:
        records_headers = self.review_manager.dataset.load_records_dict(
            header_only=True
        )
        record_header_list = list(records_headers.values())

        ids_to_dedupe = [
            x[Fields.ID]
            for x in record_header_list
            if x[Fields.STATUS] == colrev.record.RecordState.md_prepared
        ]
        processed_ids = [
            x[Fields.ID]
            for x in record_header_list
            if x[Fields.STATUS]
            not in [
                colrev.record.RecordState.md_imported,
                colrev.record.RecordState.md_prepared,
                colrev.record.RecordState.md_needs_manual_preparation,
            ]
        ]
        if len(ids_to_dedupe) > 40:
            if not self.review_manager.force_mode:
                self.review_manager.logger.warning(
                    "Simple duplicate identification selected despite sufficient sample size.\n"
                    "Active learning algorithms may perform better:\n"
                    f"{Colors.ORANGE}   colrev settings -m 'dedupe.dedupe_package_endpoints="
                    '[{"endpoint": "colrev.active_learning_training"},'
                    f'{{"endpoint": "colrev.active_learning_automated"}}]\'{Colors.END}'
                )
                raise colrev_exceptions.CoLRevException(
                    "To use simple duplicate identification, use\n"
                    f"{Colors.ORANGE}    colrev dedupe --force{Colors.END}"
                )

        nr_tasks = len(ids_to_dedupe)
        dedupe_data = {
            "nr_tasks": nr_tasks,
            "queue": processed_ids + ids_to_dedupe,
            "items_start": len(processed_ids),
        }
        # self.review_manager.logger.debug(
        #     self.review_manager.p_printer.pformat(dedupe_data)
        # )
        return dedupe_data

    def __get_record_batch(self, *, dedupe_data: dict) -> list:
        records = self.review_manager.dataset.load_records_dict()

        # Note: Because we only introduce individual (non-merged records),
        # there should be no semicolons in colrev_origin!
        records_queue = [
            record
            for ID, record in records.items()
            if ID in dedupe_data["queue"]  # type: ignore
        ]

        records_df_queue = pd.DataFrame.from_records(records_queue)
        records = self.dedupe_operation.prep_records(records_df=records_df_queue)
        # dedupe.review_manager.p_printer.pprint(records.values())

        items_start = dedupe_data["items_start"]
        items_start = 0
        batch_data = []
        for i in range(items_start, len(dedupe_data["queue"])):  # type: ignore
            batch_data.append(
                {
                    "record": dedupe_data["queue"][i],  # type: ignore
                    "queue": list(records.values())[: i + 1],
                }
            )
        return batch_data

    def __process_potential_duplicates(self, *, dedupe_batch_results: list) -> list:
        potential_duplicates = [
            r for r in dedupe_batch_results if "potential_duplicate" == r["decision"]
        ]

        records = self.review_manager.dataset.load_records_dict()
        records = self.dedupe_operation.prep_records(
            records_df=pd.DataFrame.from_records(list(records.values()))
        )
        # dedupe.review_manager.p_printer.pprint(records.values())
        records_df = pd.DataFrame(records.values())

        keys = list(records_df.columns)
        for key_to_drop in [
            Fields.ID,
            Fields.ORIGIN,
            Fields.STATUS,
            "colrev_id",
            "container_title",
        ]:
            if key_to_drop in keys:
                keys.remove(key_to_drop)

        n_match, n_distinct = 0, 0
        for potential_duplicate in potential_duplicates:
            rec1 = records_df.loc[
                records_df[Fields.ID] == potential_duplicate["ID1"], :
            ]
            rec2 = records_df.loc[
                records_df[Fields.ID] == potential_duplicate["ID2"], :
            ]

            record_pair = [rec1.to_dict("records")[0], rec2.to_dict("records")[0]]

            user_input = (
                colrev.ops.built_in.dedupe.utils.console_duplicate_instance_label(
                    record_pair, keys, True, "TODO", n_match, n_distinct, []
                )
            )

            # set potential_duplicates
            if user_input == "y":
                potential_duplicate["decision"] = "duplicate"
                n_match += 1
            if user_input == "n":
                potential_duplicate["decision"] = "no_duplicate"
                n_distinct += 1

        return potential_duplicates

    def run_dedupe(self, dedupe_operation: colrev.ops.dedupe.Dedupe) -> None:
        """Pairwise identification of duplicates based on static similarity measure

        This procedure should only be used in small samples on which active learning
        models cannot be trained.
        """

        # default='warn'
        pd.options.mode.chained_assignment = None  # type: ignore  # noqa

        self.review_manager.logger.info("Dedupe operation [colrev.simple_dedupe]")
        self.review_manager.logger.info(
            "Duplicate identification based on static similarity measure and record pairs"
        )

        dedupe_data = self.__get_dedupe_data()

        # the queue (order) matters for the incremental merging (make sure that each
        # additional record is compared to/merged with all prior records in
        # the queue)

        if not dedupe_data["queue"]:
            self.review_manager.logger.error("No records to dedupe")
            return

        batch_data = self.__get_record_batch(dedupe_data=dedupe_data)

        dedupe_batch_results = []
        for item in batch_data:
            merge_item = self.__append_merges(batch_item=item)
            dedupe_batch_results.append(merge_item)

        # dedupe_batch[-1]['queue'].to_csv('last_records.csv')

        dedupe_operation.apply_merges(
            results=dedupe_batch_results, complete_dedupe=True
        )
        if [x for x in dedupe_batch_results if x["decision"] == "duplicate"]:
            self.review_manager.logger.info("Completed application of merges")

        self.review_manager.create_commit(
            msg="Merge duplicate records",
        )

        self.review_manager.logger.info(
            "Potential duplicate identification based on static similarity measure and record pairs"
        )
        potential_duplicates = self.__process_potential_duplicates(
            dedupe_batch_results=dedupe_batch_results
        )

        # apply:
        dedupe_operation.apply_merges(results=potential_duplicates)

        # commit
        self.review_manager.create_commit(
            msg="Manual labeling of remaining duplicate candidates",
            manual_author=False,
        )
