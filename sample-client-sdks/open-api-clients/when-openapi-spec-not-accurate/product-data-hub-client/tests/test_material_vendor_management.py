import functools
import pickle
import unittest
from typing import Callable, Tuple

import sob
from pyspark import cloudpickle  # type: ignore

from product_data_hub_client.material_vendor_management.client import (
    Client,
)
from product_data_hub_client.material_vendor_management.model import (
    DataMaterialSupplierLocationsGetObjectId,
    DataMaterialSuppliersGetObjectId,
    Reference,
    SearchResponse,
    SearchResponseContent,
    SearchResponseContents,
    SupplierBulkResponse,
    SupplierLocationBulkResponse,
    SupplierLocationResponse,
    SupplierResponse,
)
from product_data_hub_client.material_vendor_management.reference_client import (  # noqa
    ReferenceClient,
)
from product_data_hub_client.material_vendor_management.reference_model import (  # noqa
    ResponsibleNikeLiaisonOfficeBulkResponse,
    ResponsibleNikeLiaisonOfficeBulkResponseContent,
    ResponsibleNikeLiaisonOfficeBulkResponseContents,
    ResponsibleNikeLiaisonOfficeResponse,
)
from product_data_hub_client.utilities import lru_cache


def _get_search_response_content_reference_key(
    content: SearchResponseContent,
) -> int:
    assert isinstance(content.relationships, Reference)
    assert isinstance(content.relationships.reference_key, str)
    return int(content.relationships.reference_key)


client_lru_cache: Callable[
    [], Callable[..., Callable[..., Client]]
] = functools.lru_cache  # type: ignore
reference_client_lru_cache: Callable[
    [], Callable[..., Callable[..., ReferenceClient]]
] = functools.lru_cache  # type: ignore


class TestMaterialVendorManagement(unittest.TestCase):
    @property  # type: ignore
    @client_lru_cache()
    def client(self) -> Client:
        return Client(
            api_key_cerberus_path="app/sustainability/pdh/x-api-key",
            oauth2_client_id_cerberus_path="app/sustainability/pdh/client_id",
            oauth2_client_secret_cerberus_path=(
                "app/sustainability/pdh/client_secret"
            ),
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
            echo=True,
        )

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        pickle.loads(pickle.dumps(self.client))
        cloudpickle.loads(cloudpickle.dumps(self.client))

    def test_get_data_responsible_nike_liaison_offices(self) -> None:
        bulk_response: ResponsibleNikeLiaisonOfficeBulkResponse = (
            self.reference_client.get_data_responsible_nike_liaison_offices()
        )
        assert isinstance(
            bulk_response, ResponsibleNikeLiaisonOfficeBulkResponse
        )
        sob.model.validate(bulk_response)

    def test_get_data_responsible_nike_liaison_offices_object_id(self) -> None:
        bulk_response: ResponsibleNikeLiaisonOfficeBulkResponse = (
            self.reference_client.get_data_responsible_nike_liaison_offices()
        )
        assert isinstance(
            bulk_response.content,
            ResponsibleNikeLiaisonOfficeBulkResponseContents,
        )
        content: ResponsibleNikeLiaisonOfficeBulkResponseContent
        for content in bulk_response.content:
            assert isinstance(content.object_id, str)
            response: ResponsibleNikeLiaisonOfficeResponse = (
                self.reference_client
            ).get_data_responsible_nike_liaison_offices_object_id(
                object_id=content.object_id
            )
            assert isinstance(response, ResponsibleNikeLiaisonOfficeResponse)
            sob.model.validate(response)

    @lru_cache()
    def _search_material_supplier_locations(self) -> SearchResponse:
        return self.client.get_search_material_supplier_locations(count=10)

    def test_get_search_material_supplier_locations(self) -> None:
        search_response: SearchResponse = (
            self._search_material_supplier_locations()
        )
        assert isinstance(search_response, SearchResponse)
        sob.model.validate(search_response)

    def test_get_data_material_supplier_locations(self) -> None:
        search_response: SearchResponse = (
            self._search_material_supplier_locations()
        )
        assert isinstance(search_response.content, SearchResponseContents)
        object_ids: Tuple[int, ...] = tuple(
            map(
                _get_search_response_content_reference_key,
                search_response.content,
            )
        )
        bulk_response: SupplierLocationBulkResponse = (
            self.client.get_data_material_supplier_locations(
                object_id=DataMaterialSupplierLocationsGetObjectId(object_ids)
            )
        )
        assert isinstance(bulk_response, SupplierLocationBulkResponse)
        sob.model.validate(bulk_response)

    def test_get_data_material_supplier_locations_object_id(self) -> None:
        search_response: SearchResponse = (
            self._search_material_supplier_locations()
        )
        assert isinstance(search_response.content, SearchResponseContents)
        object_id: int
        for object_id in map(
            _get_search_response_content_reference_key,
            search_response.content,
        ):
            response: SupplierLocationResponse = (
                self.client.get_data_material_supplier_locations_object_id(
                    object_id
                )
            )
            assert isinstance(response, SupplierLocationResponse)
            sob.model.validate(response)

    @lru_cache()
    def _search_material_suppliers(self) -> SearchResponse:
        return self.client.get_search_material_suppliers(count=10)

    def test_get_search_material_suppliers(self) -> None:
        search_response: SearchResponse = self._search_material_suppliers()
        assert isinstance(search_response, SearchResponse)
        sob.model.validate(search_response)

    def test_get_data_material_suppliers(self) -> None:
        search_response: SearchResponse = self._search_material_suppliers()
        assert isinstance(search_response.content, SearchResponseContents)
        object_ids: Tuple[int, ...] = tuple(
            map(
                _get_search_response_content_reference_key,
                search_response.content,
            )
        )
        bulk_response: SupplierBulkResponse = (
            self.client.get_data_material_suppliers(
                object_id=DataMaterialSuppliersGetObjectId(object_ids)
            )
        )
        assert isinstance(bulk_response, SupplierBulkResponse)
        sob.model.validate(bulk_response)

    def test_get_data_material_suppliers_object_id(self) -> None:
        search_response: SearchResponse = self._search_material_suppliers()
        assert isinstance(search_response.content, SearchResponseContents)
        object_id: int
        for object_id in map(
            _get_search_response_content_reference_key,
            search_response.content,
        ):
            response: SupplierResponse = (
                self.client.get_data_material_suppliers_object_id(object_id)
            )
            assert isinstance(response, SupplierResponse)
            sob.model.validate(response)


if __name__ == "__main__":
    unittest.main()
