import unittest
from pathlib import Path

from analytics_orm.utilities import lru_cache
from pyspark.sql.dataframe import DataFrame

from sample_etl.broker import Broker

TESTS_PATH: Path = Path(__file__).absolute().parent


class TestFull(unittest.TestCase):
    """
    This test case simply runs an abbreviated ETL job.
    """

    @property  # type: ignore
    def broker(self) -> Broker:
        return self._get_broker()

    @lru_cache()
    def _get_broker(self) -> Broker:
        return Broker("local", echo=True)

    def test_etl(self) -> None:
        sample_table: DataFrame = (
            self.broker.extract_transform()
        )
        self.broker.merge(
            sample_table, "SAMPLE_TABLE"
        )


if __name__ == "__main__":
    unittest.main()
