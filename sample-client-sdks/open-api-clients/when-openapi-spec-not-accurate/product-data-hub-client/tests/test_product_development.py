import functools
import pickle
import unittest
from typing import Callable, cast
from urllib.error import HTTPError

import sob  # type: ignore
from pyspark import cloudpickle

from product_data_hub_client.material_management.model import (
    SuppliedMaterialResponse,
)
from product_data_hub_client.product_development.client import Client
from product_data_hub_client.product_development.model import (
    BillOfMaterialsDataunits,
    BillOfMaterialsResponse,
    BillOfMaterialsResponseContent,
    BillOfMaterialsSourceDataunits,
    BillOfMaterialsSourceResponse,
    BillOfMaterialsSourceResponseContent,
    BomLineItemDetail,
    BomLineItemDetails,
    BomLineItemDetailSource,
    BomLineItemDetailSources,
    DataBillOfMaterialsObjectIdGetDataunits,
    DataBillOfMaterialsSourcesObjectIdGetDataunits,
    Reference,
    SearchBillOfMaterialsSourcesGetBomGUID,
    SearchBillOfMaterialsSourcesGetBomIdentifier,
    SearchBillOfMaterialsSourcesGetCycleYear,
    SearchBillOfMaterialsSourcesGetProductIdentifier,
    SearchResponse,
    SearchResponseContent,
    SearchResponseContents,
)
from product_data_hub_client.product_development.reference_client import (
    ReferenceClient,
)
from product_data_hub_client.product_development.reference_model import (
    BillOfMaterialsSection,
    BillOfMaterialsSectionBulkResponse,
    BillOfMaterialsSectionResponse,
    BillOfMaterialsSectionResponseContent,
    BillOfMaterialsUnitOfMeasurementResponse,
    PartNameResponse,
)

client_lru_cache: Callable[
    [], Callable[..., Callable[..., Client]]
] = functools.lru_cache  # type: ignore
reference_client_lru_cache: Callable[
    [], Callable[..., Callable[..., ReferenceClient]]
] = functools.lru_cache  # type: ignore


class TestProductDevelopment(unittest.TestCase):
    @property  # type: ignore
    @client_lru_cache()
    def client(self) -> Client:
        return Client(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
            timeout=60,
            echo=True,
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
            timeout=60,
            echo=True,
        )

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        pickle.loads(pickle.dumps(self.client))
        cloudpickle.loads(cloudpickle.dumps(self.client))
        pickle.loads(pickle.dumps(self.reference_client))
        cloudpickle.loads(cloudpickle.dumps(self.reference_client))

    def test_get_search_bill_of_materials(
        self,
    ) -> None:
        search_response: SearchResponse = (
            self.client.get_search_bill_of_materials(count=3)
        )
        sob.model.validate(search_response)
        assert isinstance(search_response.content, SearchResponseContents)
        content: SearchResponseContent
        for content in search_response.content:
            print(repr(content.relationships))
            assert isinstance(content.relationships, Reference), type(
                content.relationships
            )
            assert isinstance(
                self.client.get_reference(content.relationships),
                BillOfMaterialsResponse,
            )

    def test_get_search_bill_of_materials_sources(
        self,
    ) -> None:
        search_response: SearchResponse = (
            self.client.get_search_bill_of_materials_sources(
                bom_identifier=SearchBillOfMaterialsSourcesGetBomIdentifier(
                    [43369]
                ),
                cycle_year=SearchBillOfMaterialsSourcesGetCycleYear(["SP24"]),
            )
        )
        sob.model.validate(search_response)
        assert isinstance(search_response.content, SearchResponseContents)
        content: SearchResponseContent
        for content in search_response.content:
            print(repr(content))
            assert isinstance(content.relationships, Reference), type(
                content.relationships
            )
            assert isinstance(
                self.client.get_reference(content.relationships),
                BillOfMaterialsSourceResponse,
            )

    def test_get_data_bill_of_materials_object_id(self) -> None:
        response: BillOfMaterialsResponse = (
            self.client
        ).get_data_bill_of_materials_object_id(
            "43369_1531020",
            dataunits=DataBillOfMaterialsObjectIdGetDataunits(
                [
                    "bomCore",
                    "bomSeason",
                    "bomSourcingConfiguration",
                    "bomClassification",
                    "bomDescription",
                    "bomStatus",
                    "bomHeaderAudit",
                    "bomLineItemDetail",
                    "bomLineItemComments",
                    "bomLineAudit",
                    "bomSeason",
                ]
            ),
        )
        assert isinstance(response.content, BillOfMaterialsResponseContent)
        assert isinstance(response.content.data, BillOfMaterialsDataunits)
        data: BillOfMaterialsDataunits = cast(
            BillOfMaterialsDataunits,
            cast(BillOfMaterialsResponseContent, response.content).data,
        )
        reference: Reference
        if data.bom_line_item_detail:
            bom_line_item_detail: BomLineItemDetail
            for bom_line_item_detail in cast(
                BomLineItemDetails, data.bom_line_item_detail
            ):
                if bom_line_item_detail.bill_of_materials_section:
                    section_response: BillOfMaterialsSectionResponse = cast(
                        BillOfMaterialsSectionResponse,
                        self.client.get_reference(
                            cast(
                                Reference,
                                bom_line_item_detail.bill_of_materials_section,
                            )
                        ),
                    )
                    sob.model.validate(section_response)
                    if section_response.content:
                        content: BillOfMaterialsSectionResponseContent = cast(
                            BillOfMaterialsSectionResponseContent,
                            section_response.content,
                        )
                        if content.data:
                            section: BillOfMaterialsSection = cast(
                                BillOfMaterialsSection, content.data
                            )
                            assert isinstance(section, BillOfMaterialsSection)
                if bom_line_item_detail.supplied_material:
                    try:
                        supplied_material_response: SuppliedMaterialResponse
                        supplied_material_response = cast(
                            SuppliedMaterialResponse,
                            self.reference_client.get_reference(
                                cast(
                                    Reference,
                                    bom_line_item_detail.supplied_material,
                                ),
                                query=(
                                    (
                                        "_dataunits",
                                        (
                                            "supmatDimension",
                                            "supmatDesignUsageSpecification",
                                        ),
                                    ),
                                ),
                            ),
                        )
                        assert isinstance(
                            supplied_material_response,
                            SuppliedMaterialResponse,
                        )
                        sob.model.validate(supplied_material_response)
                    except HTTPError as error:
                        if error.code != 404:
                            raise
                        continue

    def test_get_data_bill_of_materials_sources_object_id(self) -> None:
        response: BillOfMaterialsSourceResponse = (
            self.client
        ).get_data_bill_of_materials_sources_object_id(
            "43369_1531020_441914",
            dataunits=DataBillOfMaterialsSourcesObjectIdGetDataunits(
                [
                    "bomCore",
                    "bomLineItemDetail",
                ]
            ),
        )
        assert isinstance(
            response.content, BillOfMaterialsSourceResponseContent
        ) and isinstance(response.content.data, BillOfMaterialsSourceDataunits)
        data: BillOfMaterialsSourceDataunits = cast(
            BillOfMaterialsSourceDataunits,
            cast(BillOfMaterialsResponseContent, response.content).data,
        )
        if data.bom_line_item_detail:
            bom_line_item_detail_source: BomLineItemDetailSource
            for bom_line_item_detail_source in cast(
                BomLineItemDetailSources, data.bom_line_item_detail
            ):
                if isinstance(
                    bom_line_item_detail_source.usage_unit_of_measure,
                    Reference,
                ):
                    assert isinstance(
                        self.client.get_reference(
                            bom_line_item_detail_source.usage_unit_of_measure
                        ),
                        BillOfMaterialsUnitOfMeasurementResponse,
                    )
                if isinstance(
                    bom_line_item_detail_source.part,
                    Reference,
                ):
                    part_name_response: PartNameResponse = (
                        self.client.get_reference(
                            bom_line_item_detail_source.part
                        )
                    )
                    assert isinstance(part_name_response, PartNameResponse)
                if isinstance(
                    bom_line_item_detail_source.bill_of_materials_section,
                    Reference,
                ):
                    section_response: BillOfMaterialsSectionResponse = (
                        self.client.get_reference(
                            (
                                bom_line_item_detail_source
                            ).bill_of_materials_section
                        )
                    )
                    assert isinstance(
                        section_response, BillOfMaterialsSectionResponse
                    )

    def test_get_bill_of_materials_sections(self) -> None:
        response: BillOfMaterialsSectionBulkResponse = (
            self.reference_client
        ).get_bill_of_materials_sections()
        sob.model.validate(response)

    def test_get_search_bill_of_materials_bom_guid(self) -> None:
        search_response: SearchResponse = (
            self.client.get_search_bill_of_materials_sources(
                bom_guid=SearchBillOfMaterialsSourcesGetBomGUID(
                    ["30ef2edd-8ef0-46ad-83fa-1f0a409d855b"]
                ),
            )
        )
        sob.model.validate(search_response)
        content: SearchResponseContent
        for content in cast(SearchResponseContents, search_response.content):
            response: BillOfMaterialsSourceResponse = (
                self.client.get_reference(
                    cast(Reference, content.relationships)
                )
            )
            sob.model.validate(response)

    def test_get_search_bill_of_materials_sources_product_id_cycle_year(
        self,
    ) -> None:
        search_response: SearchResponse = (
            self.client.get_search_bill_of_materials_sources(
                product_identifier=(
                    SearchBillOfMaterialsSourcesGetProductIdentifier([1162415])
                ),
                cycle_year=SearchBillOfMaterialsSourcesGetCycleYear(["HO19"]),
            )
        )
        sob.model.validate(search_response)
        content: SearchResponseContent
        for content in cast(SearchResponseContents, search_response.content):
            response: BillOfMaterialsSourceResponse = (
                self.client.get_reference(
                    cast(Reference, content.relationships)
                )
            )
            print(repr(response))
            sob.model.validate(response)


if __name__ == "__main__":
    unittest.main()
