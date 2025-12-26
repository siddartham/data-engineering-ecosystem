import argparse
import sys
from importlib import import_module
from types import ModuleType

from . import __doc__, __name__ as _module_name


def _get_command() -> str:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument("command")
    arguments: argparse.Namespace = parser.parse_known_args()[0]
    sys.argv.remove(arguments.command)
    return arguments.command.lower().replace("-", "_")


def main() -> None:
    """
    Run a sub-module `main` function.
    """
    command = _get_command()
    module: ModuleType
    try:
        module = import_module(f"{_module_name}.{command}.__main__")
    except ImportError:
        module = import_module(f"{_module_name}.{command}")
    module.main()  # type: ignore


if __name__ == "__main__":
    main()
