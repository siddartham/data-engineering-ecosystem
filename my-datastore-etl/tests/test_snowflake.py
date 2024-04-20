import functools
import unittest
from typing import Callable

from analytics_orm.utilities import is_ci
from pyspark.sql.dataframe import DataFrame  # type: ignore
from sqlalchemy import text  # type: ignore

from my_datastore_etl.broker import Broker

broker_lru_cache: Callable[[], Broker] = functools.lru_cache  # type: ignore

TEST_QUERY: str = (
    "SELECT * FROM MY_SNOWFLAKE_PROD.COMMON_DIMENSION.ALEMBIC_VERSION"
)


class TestSnowflake(unittest.TestCase):
    @property  # type: ignore
    @broker_lru_cache()
    def broker(self) -> Broker:
        return Broker("map-prod", echo=True)

    def test_snowflake_session(self) -> None:
        self.broker.work.snowflake_session.execute(text(TEST_QUERY))

    def test_get_snowflake_spark_dataframe_from_table(self) -> None:
        assert isinstance(
            self.broker.work.get_snowflake_spark_dataframe(
                table="GSA_FOUNDATION_PROD.COMMON_DIMENSION.CALCULATOR",
            ),
            DataFrame,
        )

    def test_get_snowflake_spark_dataframe_from_query(self) -> None:
        assert isinstance(
            self.broker.work.get_snowflake_spark_dataframe(
                table=f"({TEST_QUERY})",
            ),
            DataFrame,
        )

    def test_load(self) -> None:
        if not is_ci():
            qualified_table_name: str
            Broker(environment="map-dev", echo=True).snowflake_load(
                lambda qualified_table_name: (
                    qualified_table_name == "COMMON_DIMENSION.ALEMBIC_VERSION"
                )
            )


if __name__ == "__main__":
    unittest.main()
