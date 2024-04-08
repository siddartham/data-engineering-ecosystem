import unittest
from functools import lru_cache
from typing import Callable, Iterable, Tuple

from my_datastore_etl.broker import Broker
from my_datastore_orm import schema_a
from pyspark.sql.dataframe import DataFrame  # type: ignore

from analytics_etl.concurrency import Concurrency

broker_lru_cache: Callable[[], Broker] = lru_cache  # type: ignore


def iter_measure_names_ids() -> Iterable[Tuple[int, str]]:
    yield from enumerate(schema_a.MEASURES.enums, 1)


class TestTableDataFrame(unittest.TestCase):
    @property  # type: ignore
    @broker_lru_cache()
    def broker(self) -> Broker:
        return Broker("local", concurrency=Concurrency.SPARK)

    def _merge_measures(self) -> None:
        name: str
        measure_id: int
        self.broker.merge(
            (
                tuple(fnd_material.Measure(measure_id=measure_id, name=name))
                for measure_id, name in iter_measure_names_ids()
            ),
            "MEASURE",
        )

    def test_get_table_spark_dataframe(self) -> None:
        self._merge_measures()
        measures: DataFrame = self.broker.work.get_table_spark_dataframe(
            "MEASURE"
        )
        assert isinstance(
            measures,
            DataFrame,
        )
        assert tuple(sorted(map(tuple, measures.toLocalIterator()))) == tuple(
            iter_measure_names_ids()
        )


if __name__ == "__main__":
    unittest.main()
