import argparse
import sys
from importlib import import_module

from . import __name__ as _module_name


def _get_command() -> str:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("command")
    arguments: argparse.Namespace = parser.parse_known_args()[0]
    sys.argv.remove(arguments.command)
    return arguments.command.lower().replace("-", "_")


def main() -> None:
    """
    Run a sub-module `main` function.
    """
    command = _get_command()
    module_name: str = f"{_module_name}.{command}"
    import_module(module_name).main()  # type: ignore
