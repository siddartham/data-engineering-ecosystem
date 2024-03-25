import functools
import unittest
from typing import Callable

from pyspark.sql.dataframe import DataFrame  # type: ignore

from my_datastore_etl_wrapper.broker import Broker

broker_lru_cache: Callable[[], Broker] = functools.lru_cache  # type: ignore


class TestDatabricks(unittest.TestCase):
    @property  # type: ignore
    @broker_lru_cache()
    def broker(self) -> Broker:
        return Broker("sole-prod")

    def test_get_databricks_table_dataframe(self) -> None:
        assert isinstance(
            self.broker.work.get_databricks_dataframe(
                table="TODO.TODO.TODO",
            ),
            DataFrame,
        )

    def test_get_databricks_select_statement_dataframe(self) -> None:
        assert isinstance(
            self.broker.work.get_databricks_dataframe(
                table=("(SELECT * FROM TODO.TODO.TODO)"),
            ),
            DataFrame,
        )


if __name__ == "__main__":
    unittest.main()
