import functools
import unittest
from pathlib import Path
from runpy import run_path
from typing import Any, Callable, Dict

lru_cache: Any = functools.lru_cache
PROJECT_PATH: Path = Path(__file__).absolute().parent.parent


REMODEL_NAMESPACE: Dict[str, Any] = run_path(
    str(PROJECT_PATH.joinpath("scripts", "remodel.py")), run_name="_"
)


class TestRemodel(unittest.TestCase):
    def test_class_name_from_pointer(self) -> None:
        class_name_from_pointer: Callable[[str], str] = REMODEL_NAMESPACE[
            "class_name_from_pointer"
        ]
        assert (
            class_name_from_pointer("CSR_ObjectivesTargetTypes#/value/0")
            == "CSRObjectiveTargetType"
        )
        assert (
            class_name_from_pointer("SD_EFDistributionLevels#/value/0")
            == "SDEfDistributionLevel"
        )


if __name__ == "__main__":
    unittest.main()
