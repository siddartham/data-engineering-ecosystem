import functools
from pathlib import Path
import unittest
from typing import Any
from nike.enablon_client.utilities import (
    get_client_method_table_name,
    get_service_root_table_name,
)

lru_cache: Any = functools.lru_cache
PROJECT_PATH: Path = Path(__file__).absolute().parent.parent


class TestUtilities(unittest.TestCase):
    def test_get_client_method_table_name(self) -> None:
        assert (
            get_client_method_table_name("sd_ef_distribution_levels")
            == "SD_EF_DISTRIBUTION_LEVEL"
        )

    def test_get_service_root_table_name(self) -> None:
        assert (
            get_service_root_table_name("SD_EFDistributionLevels")
            == "SD_EF_DISTRIBUTION_LEVEL"
        )


if __name__ == "__main__":
    unittest.main()
