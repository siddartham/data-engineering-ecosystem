import csv
import functools
import unittest
import warnings
from copy import copy
from io import BytesIO, StringIO
from itertools import islice
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import pyarrow  # type: ignore
import pytest
from etl_framework.concurrency import Concurrency
from orm_framework.declarative import (
    get_class_column_names,
    get_class_table_name,
)
from orm_framework.pyarrow import get_schema_from_mapping
from file_system_client import local
from file_system_client.base import FileSystem
from my_datastore_orm.common_dimension import Calculator

from my_datastore_etl_wrapper.broker import Broker, Work

lru_cache: Any = functools.lru_cache
TEST_CSV: str = "test_csv/"
TEST1_TXT: str = f"{TEST_CSV}test1.csv"
TEST2_TXT: str = f"{TEST_CSV}test2.csv"
TEST_PARQUET: str = "test_parquet/"
CALCULATOR_SOURCE: str = f"{TEST_PARQUET}calculator/source/"
CALCULATOR_TARGET: str = f"{TEST_PARQUET}calculator/target/"
TESTS_PATH: Path = Path(__file__).absolute().parent


class TestLocal(unittest.TestCase):
    """
    This test case verifies local file system functionality
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._csv1_bytes: Optional[bytes] = None
        self._csv2_bytes: Optional[bytes] = None
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls) -> None:
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    @property  # type: ignore
    def csv1(self) -> BytesIO:
        if self._csv1_bytes is None:
            with StringIO() as string_io:
                dict_writer: csv.DictWriter = csv.DictWriter(
                    string_io, ("a", "b", "c")
                )
                dict_writer.writerow(dict(a=1, b=2, c=3))
                string_io.seek(0)
                self._csv1_bytes = bytes(string_io.read(), encoding="utf-8")
        return BytesIO(self._csv1_bytes)

    @property  # type: ignore
    def csv2(self) -> BytesIO:
        if self._csv2_bytes is None:
            with StringIO() as string_io:
                dict_writer: csv.DictWriter = csv.DictWriter(
                    string_io, ("a", "b", "c")
                )
                dict_writer.writerow(dict(a=4, b=5, c=6))
                string_io.seek(0)
                self._csv2_bytes = bytes(string_io.read(), encoding="utf-8")
        return BytesIO(self._csv2_bytes)

    @property  # type: ignore
    @lru_cache()
    def broker(self) -> Broker:
        return Broker("local")

    @property  # type: ignore
    @lru_cache()
    def work(self) -> Work:
        return self.broker.work

    @property  # type: ignore
    @lru_cache()
    def file_system(self) -> local.Local:
        return self.work.file_system

    def test_iter_file_paths(self) -> None:
        """
        This method tests retrieving file names from the local filesystem
        """
        file_path: str
        for file_path in islice(self.file_system.iter_file_paths(), 10):
            assert isinstance(file_path, str)
            print(file_path)

    def test_put(self) -> None:
        """
        This method tests saving a file to the local filesystem
        """
        self.file_system.put(self.csv1, TEST1_TXT)
        assert TEST1_TXT in self.file_system.get_file_paths(f"{TEST_CSV}")
        self.file_system.delete(TEST1_TXT)

    def test_get(self) -> None:
        """
        This method tests loading a file from the local filesystem
        """
        self.file_system.put(self.csv1, TEST1_TXT)
        assert self.file_system.get(TEST1_TXT).read() == self.csv1.read()
        self.file_system.delete(TEST1_TXT)

    def test_delete(self) -> None:
        """
        This method verifies that we can successfully delete a file.
        """
        self.file_system.put(self.csv1, TEST1_TXT)
        assert TEST1_TXT in self.file_system.iter_file_paths(TEST_CSV)
        self.file_system.delete(TEST1_TXT)
        assert TEST1_TXT not in self.file_system.iter_file_paths(TEST_CSV)

    def test_delete_directory(self) -> None:
        """
        This method verifies that we can successfully delete a directory.
        """
        self.file_system.put(self.csv1, TEST1_TXT)
        self.file_system.put(self.csv2, TEST2_TXT)
        self.file_system.delete_directory(f"{TEST_CSV}")
        assert TEST1_TXT not in self.file_system.get_file_paths()
        assert TEST2_TXT not in self.file_system.get_file_paths()

    def test_get_url(self) -> None:
        """
        This method verifies that
        `my_datastore_etl_wrapper.file_system.local.Local.get_url` returns
        an local filesystem URL formatted in the expected fashion.
        """
        url: str = self.file_system.get_url(TEST1_TXT)
        expected_url: str = f"file://" f"{self.file_system.root}{TEST1_TXT}"
        assert url == expected_url, f"{url}\n!=\n{expected_url}"

    def test_map(self) -> None:
        sum_partition: int
        for sum_partition in self.broker.map(
            sum, [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        ):
            assert isinstance(sum_partition, int)

    def test_map_put_delete(self) -> None:
        self.broker.starmap(
            self.file_system.put,
            ((self.csv1, TEST1_TXT), (self.csv2, TEST2_TXT)),
        )
        self.broker.map(self.file_system.delete, (TEST1_TXT, TEST2_TXT))

    @pytest.mark.spark
    def test_spark_read(self) -> None:
        self.file_system.put(self.csv1, TEST1_TXT)
        self.work.spark_session.read.csv(self.file_system.get_url(TEST1_TXT))
        self.file_system.delete(TEST1_TXT)

    @property  # type: ignore
    def calculator_target(self) -> Dict[str, int]:
        return {
            "0.0.0": 1,
            "0.0.2": 2,
            "0.1.0": 3,
            "1.0.0": 4,
            "1.0.1": 5,
            "1.1.0": 6,
        }

    @property  # type: ignore
    def calculator_source(self) -> Dict[str, int]:
        return {
            "0.0.1": 2,
            "0.0.2": 3,
            "0.1.0": 4,
            "1.0.0": 5,
            "1.0.1": 6,
            "1.1.0": 7,
        }

    @property  # type: ignore
    def calculator(self) -> Dict[str, int]:
        calculator: Dict[str, int] = copy(self.calculator_target)
        calculator.update(**self.calculator_source)
        return calculator

    @pytest.mark.spark
    def test_consolidate_table(self) -> None:
        from pyspark.sql import DataFrame, SparkSession  # type: ignore

        broker: Broker = self.broker
        work: Work = broker.work
        spark_session: SparkSession = work.spark_session
        assert work.file_system
        file_system: FileSystem = work.file_system
        table_name: str = get_class_table_name(Calculator)
        column_names: Tuple[str, ...] = get_class_column_names(Calculator)
        schema: pyarrow.Schema = get_schema_from_mapping(Calculator)
        work.write_parquet(
            self.calculator_source.items(),
            f"{CALCULATOR_SOURCE}2.parquet",
            column_names=column_names,
            schema=schema,
        )
        work.write_parquet(
            self.calculator_target.items(),
            f"{CALCULATOR_TARGET}1.parquet",
            column_names=column_names,
            schema=schema,
        )
        broker.consolidate_table(
            CALCULATOR_SOURCE,
            CALCULATOR_TARGET,
            table_name=table_name,
            concurrency=Concurrency.SPARK,
            overwrite=False,
        )
        consolidated_data_frame: DataFrame = spark_session.read.parquet(
            f"{file_system.get_url(CALCULATOR_TARGET)}*.parquet"
        )
        assert tuple(
            sorted(map(tuple, consolidated_data_frame.toLocalIterator()))
        ) == tuple(sorted(self.calculator.items()))
        file_system.delete_directory(CALCULATOR_SOURCE)
        file_system.delete_directory(CALCULATOR_TARGET)


if __name__ == "__main__":
    unittest.main()
