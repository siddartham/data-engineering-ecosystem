import unittest
from datetime import datetime, timedelta

from orm_framework.pyspark import (
    DELTA_CORE,
    SCALA_LIBRARY,
    SNOWFLAKE_JDBC,
    get_earliest_datetime,
    get_maven_package_url,
    get_safe_datetime,
)


class TestSpark(unittest.TestCase):
    def test_get_maven_package_url(self) -> None:
        scala_library_url: str = get_maven_package_url(SCALA_LIBRARY)
        print(scala_library_url)
        assert "scala-library" in scala_library_url
        delta_core_url: str = get_maven_package_url(DELTA_CORE)
        print(delta_core_url)
        assert "delta-core" in delta_core_url
        assert "0.7." not in delta_core_url
        delta_core_url = get_maven_package_url(f"{DELTA_CORE}:0.7.*")
        print(delta_core_url)
        assert "0.7." in delta_core_url
        snowflake_jdbc_url: str = get_maven_package_url(SNOWFLAKE_JDBC)
        print(snowflake_jdbc_url)
        assert "snowflake-jdbc" in snowflake_jdbc_url

    def test_get_earliest_datetime(self) -> None:
        assert get_earliest_datetime() <= datetime(1970, 1, 1)

    def test_get_safe_datetime(self) -> None:
        earliest: datetime = get_earliest_datetime()
        unsafe_datetime: datetime = earliest - timedelta(days=1)
        safe_datetime: datetime = earliest + timedelta(days=1)
        assert get_safe_datetime(unsafe_datetime) == earliest
        assert get_safe_datetime(safe_datetime) == safe_datetime


if __name__ == "__main__":
    unittest.main()
