import argparse
import runpy
import sys

from . import __name__ as _module_name


HELP: str = """
usage: mail-client mail [optional arguments]

optional arguments:
  -h, --help  show this help message and exit
""".lstrip()


def _get_command() -> str:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        usage="mail-client mail [optional arguments]",
        add_help=bool(len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h")),
    )
    parser.add_argument("command", default="", help=argparse.SUPPRESS)
    arguments: argparse.Namespace = parser.parse_known_args()[0]
    sys.argv.remove(arguments.command)
    return arguments.command.lower().replace("-", "_")


def main() -> None:
    """
    Run a sub-module corresponding to the indicated `operation`.

    Parameters:

    - command (str): The name of a sub-module to run as "__main__".
    """
    command: str = _get_command()
    if command:
        module_name: str = f"{_module_name}.{command}"
        runpy.run_module(module_name, run_name="__main__")


if __name__ == "__main__":
    main()
