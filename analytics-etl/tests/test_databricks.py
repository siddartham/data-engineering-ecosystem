import functools
import unittest
from typing import Callable, Tuple

from delta import DeltaTable
from my_datastore_etl.broker import Broker
from pyspark.sql.dataframe import DataFrame  # type: ignore
from sqlalchemy import text  # type: ignore

broker_lru_cache: Callable[[], Broker] = functools.lru_cache  # type: ignore

TEST_QUERY: str = "select * from calculator"


def test_map_databricks_session(map_prod_broker: Broker) -> None:
    map_prod_broker.work.databricks_session.execute(text(TEST_QUERY))


def test_map_get_databricks_spark_dataframe_from_table(
    map_prod_broker: Broker,
) -> None:
    assert isinstance(
        map_prod_broker.work.get_databricks_spark_dataframe(
            table="calculator",
        ),
        DataFrame,
    )


def test_map_get_databricks_spark_dataframe_from_query(
    map_prod_broker: Broker,
) -> None:
    assert isinstance(
        map_prod_broker.work.get_databricks_spark_dataframe(
            table=f"({TEST_QUERY})",
        ),
        DataFrame,
    )


def test_local_get_delta_table(
    local_broker: Broker,
) -> None:
    assert isinstance(
        local_broker.work.get_delta_table(
            "calculator",
        ),
        DeltaTable,
    )


def test_local_merge(
    local_broker: Broker,
) -> None:
    rows: Tuple[Tuple[str, int, int], ...] = tuple(
        sorted(
            (
                ("0.0.1", 2, 0),
                ("0.0.2", 3, 0),
                ("0.1.0", 4, 0),
                ("1.0.0", 5, 0),
                ("1.0.1", 6, 0),
                ("1.1.0", 7, 1),
            )
        )
    )
    calculator: DataFrame = local_broker.work.spark_session.createDataFrame(
        rows, ["CALCULATOR_VERSION", "ORDINAL", "CURRENT"]
    )
    local_broker.merge(calculator, "calculator")
    assert rows == tuple(
        sorted(
            map(
                tuple,
                local_broker.work.get_table_spark_dataframe(
                    "calculator"
                ).toLocalIterator(),  # type: ignore
            )
        )
    )


if __name__ == "__main__":
    unittest.main()
