import sys
from importlib import import_module
from types import ModuleType

from . import __name__ as _module_name


def _get_dialect() -> str:
    dialect: str = "sqlite"
    if len(sys.argv) > 1 and (sys.argv[1] in ("sqlite", "snowflake")):
        dialect = sys.argv.pop(1)
    return dialect


def main() -> None:
    """
    Run a dialect's sub-module `main()` function.
    """
    dialect = _get_dialect()
    module: ModuleType
    try:
        module = import_module(f"{_module_name}.dialects.{dialect}.__main__")
    except ImportError:
        module = import_module(f"{_module_name}.dialects.{dialect}")
    module.main()  # type: ignore


if __name__ == "__main__":
    main()
