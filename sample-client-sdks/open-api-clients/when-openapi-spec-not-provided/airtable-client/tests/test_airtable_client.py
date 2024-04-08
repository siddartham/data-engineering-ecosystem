import functools

import pickle
import unittest
from itertools import islice
from typing import Any, Callable

import sob

from pyspark import cloudpickle  # type: ignore
from airtable_client import model
from airtable_client.client import Client

lru_cache: Callable[..., Any] = functools.lru_cache

BEARER_TOKEN_CERBERUS_PATH: str = (
    "app/sustainability/airtable/a.AT.SUSTAINABILITY-personal-access-token"
)


class TestClient(unittest.TestCase):
    """
    This test case verifies the functionality of each endpoint method in
    `airtable_client.client.Client`
    """

    @property  # type: ignore
    @lru_cache()
    def client(self) -> Client:
        return Client(bearer_token_cerberus_path=BEARER_TOKEN_CERBERUS_PATH)

    def test_pickle(self) -> None:
        """
        Verify that the client is pickle-able
        """
        pickle.dumps(self.client)
        cloudpickle.dumps(self.client)

    @lru_cache()
    def _get_meta_bases(self) -> model.MetaBasesGetResponse:
        response: model.MetaBasesGetResponse = self.client.get_meta_bases()
        assert isinstance(response, model.MetaBasesGetResponse)
        sob.model.validate(response)
        return response

    def _iter_bases(self) -> model.Bases:
        meta_bases: model.MetaBasesGetResponse = self._get_meta_bases()
        assert meta_bases.bases is not None
        return meta_bases.bases

    @lru_cache()
    def _get_meta_bases_base_id_tables(
        self, base_id: str
    ) -> model.MetaBasesBaseIdTablesGetResponse:
        response: model.MetaBasesBaseIdTablesGetResponse = (
            self.client.get_meta_bases_base_id_tables(base_id=base_id)
        )
        assert isinstance(response, model.MetaBasesBaseIdTablesGetResponse)
        sob.model.validate(response)
        return response

    def _iter_base_id_tables(self, base_id: str) -> model.Tables:
        response: model.MetaBasesBaseIdTablesGetResponse = (
            self._get_meta_bases_base_id_tables(base_id)
        )
        assert response.tables is not None
        return response.tables

    def test_get_meta_bases(self) -> None:
        # We make this lookup + validation a private method for caching and
        # re-use of the return values
        list(self._iter_bases())

    def test_get_meta_bases_base_id_tables(self) -> None:
        base: model.Base
        for base in islice(
            # Limit the number of bases' tables we lookup to 3
            self._iter_bases(),
            3,
        ):
            # We make this lookup + validation a private method for caching and
            # re-use of the return values
            self._get_meta_bases_base_id_tables(base.id_)

    @lru_cache()
    def _get_base_id_table(
        self, base_id: str, table: str
    ) -> model.BaseIdTableGetResponse:
        response: model.BaseIdTableGetResponse = self.client.get_base_id_table(
            base_id=base_id, table=table
        )
        assert isinstance(
            response,
            model.BaseIdTableGetResponse,
        )
        sob.model.validate(response)
        return response

    def test_get_base_id_table(
        self,
    ) -> None:
        base: model.Base
        for base in islice(
            # Limit the number of bases' tables we lookup to 3
            self._iter_bases(),
            3,
        ):
            table: model.Table
            assert base.id_
            for table in islice(self._iter_base_id_tables(base.id_), 3):
                # We make this lookup + validation a private method for caching
                # and re-use of the return values
                self._get_base_id_table(base.id_, table.name)

    @lru_cache()
    def _get_base_id_table_record_id(
        self, base_id: str, table: str, record_id: str
    ) -> model.BaseIdTableRecordIdGetResponse:
        response: model.BaseIdTableRecordIdGetResponse = (
            self.client.get_base_id_table_record_id(
                base_id=base_id, table=table, record_id=record_id
            )
        )
        assert isinstance(
            response,
            model.BaseIdTableRecordIdGetResponse,
        )
        sob.model.validate(response)
        return response

    def test_get_base_id_table_record_id(
        self,
    ) -> None:
        base: model.Base
        for base in islice(
            # Limit the number of bases' tables we lookup to 3
            self._iter_bases(),
            3,
        ):
            table: model.Table
            assert base.id_
            for table in islice(self._iter_base_id_tables(base.id_), 3):
                record: model.Record
                for record in islice(
                    self._get_base_id_table(base.id_, table.name).records, 3
                ):
                    print(repr((base, table, record)))
                    # We make this lookup + validation a private method for
                    # caching and re-use of the return values
                    self._get_base_id_table_record_id(
                        base.id_, table.id_, record.id_
                    )


if __name__ == "__main__":
    unittest.main()
