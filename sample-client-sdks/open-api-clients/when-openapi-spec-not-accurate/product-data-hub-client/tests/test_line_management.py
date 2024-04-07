import functools
import pickle
import unittest
from typing import Callable, cast

import oapi
import sob
from pyspark import cloudpickle  # type: ignore

from product_data_hub_client.line_management.client import Client
from product_data_hub_client.line_management.model import (
    GlobalOfferingDataunits,
    GlobalOfferingResponse,
    GlobalOfferingResponseContent,
    LineManagementSearchProductOfferingsGlobalGetProductIdentifier,
    LineManagementSearchProductOfferingsGlobalGetStyleNumber,
    MoCore,
    PClassification,
    PInitialSeason,
    Reference,
    SearchResponse,
    SearchResponseContent,
    SearchResponseContents,
)
from product_data_hub_client.line_management.reference_client import (
    ReferenceClient,
)
from product_data_hub_client.line_management.reference_model import (
    CycleYearBulkResponse,
    DivisionBulkResponse,
    ISOMeasurementBulkResponse,
)
from product_data_hub_client.utilities import lru_cache

client_lru_cache: Callable[
    [], Callable[..., Callable[..., Client]]
] = functools.lru_cache  # type: ignore
reference_client_lru_cache: Callable[
    [], Callable[..., Callable[..., ReferenceClient]]
] = functools.lru_cache  # type: ignore


class TestLineManagement(unittest.TestCase):
    @property  # type: ignore
    @client_lru_cache()
    def client(self) -> Client:
        return Client(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
            echo=False,
        )

    @property  # type: ignore
    @reference_client_lru_cache()
    def reference_client(self) -> ReferenceClient:
        return ReferenceClient(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
            echo=False,
        )

    @lru_cache()
    def _get_line_management_data_cycle_years(self) -> CycleYearBulkResponse:
        cycle_year_bulk_response: CycleYearBulkResponse = (
            self.reference_client.get_line_management_data_cycle_years()
        )
        assert isinstance(cycle_year_bulk_response, CycleYearBulkResponse)
        return cycle_year_bulk_response

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        self._get_line_management_data_cycle_years()
        pickle.loads(pickle.dumps(self.client))
        cloudpickle.loads(cloudpickle.dumps(self.client))

    def test_get_line_management_data_cycle_years(self) -> None:
        sob.model.validate(self._get_line_management_data_cycle_years())

    def test_get_line_management_data_divisions(self) -> None:
        division_bulk_response: DivisionBulkResponse = (
            self.reference_client.get_line_management_data_divisions()
        )
        assert isinstance(division_bulk_response, DivisionBulkResponse)
        sob.model.validate(division_bulk_response)

    def test_get_line_management_data_iso_measurements(self) -> None:
        iso_measurement_bulk_response: ISOMeasurementBulkResponse = (
            self.reference_client.get_line_management_data_iso_measurements()
        )
        assert isinstance(
            iso_measurement_bulk_response, ISOMeasurementBulkResponse
        )
        sob.model.validate(iso_measurement_bulk_response)

    def test_get_line_management_search_product_offerings_global(self) -> None:
        product_identifiers: LineManagementSearchProductOfferingsGlobalGetProductIdentifier = LineManagementSearchProductOfferingsGlobalGetProductIdentifier(  # noqa
            [4946097]
        )
        style_numbers: LineManagementSearchProductOfferingsGlobalGetStyleNumber = LineManagementSearchProductOfferingsGlobalGetStyleNumber(  # noqa
            ["SX6889"]
        )
        search_response: SearchResponse = (
            self.client.get_line_management_search_product_offerings_global(
                product_identifier=product_identifiers,
                style_number=style_numbers,
            )
        )
        assert isinstance(search_response.content, SearchResponseContents)
        content: SearchResponseContent
        print(repr(search_response))
        for content in search_response.content:
            assert isinstance(content.relationships, Reference), repr(
                content.relationships
            )
            offering: GlobalOfferingResponse = self.client.get_reference(
                content.relationships,
                query={
                    "_dataunits": oapi.client.format_argument_value(
                        "_dataunits",
                        ("pClassification", "pInitialSeason"),
                        style="form",
                        explode=False,
                    )
                },
            )
            print(repr(offering))
            data: GlobalOfferingDataunits = cast(
                GlobalOfferingDataunits,
                cast(GlobalOfferingResponseContent, offering.content).data,
            )
            assert isinstance(data.p_classification, PClassification)
            assert isinstance(data.p_initial_season, PInitialSeason)
            assert isinstance(data.mo_core, MoCore)
            assert isinstance(
                cast(
                    PClassification,
                    cast(
                        GlobalOfferingDataunits,
                        cast(
                            GlobalOfferingResponseContent, offering.content
                        ).data,
                    ).p_classification,
                ).global_category_core_focus,
                Reference,
            )
            sob.model.validate(
                self.client.get_reference(
                    cast(
                        Reference,
                        cast(
                            PClassification,
                            cast(
                                GlobalOfferingDataunits,
                                cast(
                                    GlobalOfferingResponseContent,
                                    offering.content,
                                ).data,
                            ).p_classification,
                        ).global_category_core_focus,
                    )
                )
            )


if __name__ == "__main__":
    unittest.main()
