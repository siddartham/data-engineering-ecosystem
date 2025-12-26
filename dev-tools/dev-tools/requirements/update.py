#!/usr/bin/env python3
"""
This script updates installation requirements in ../setup.py
"""
import argparse
import os
import re
import sys
from itertools import chain
from typing import Collection, Iterable, List, Set, Tuple, Union
from urllib.parse import urljoin

from setuptools_setup_versions.parse import (  # type: ignore
    get_distribution_freeze,
    get_setup_script,
)
from setuptools_setup_versions.requirements import update_setup  # type: ignore

from ..utilities import run

PROJECT_DIRECTORY: str = urljoin(os.path.abspath(__file__), "../")
_PYTHON_36_FORCED_REQUIREMENTS: Tuple[str, ...] = (
    "dataclasses",
    "types-dataclasses",
)


def _iter_parse_argument(values: Iterable[str]) -> Iterable[str]:
    """
    Yield a list of packages from an `--ignore` argument
    """
    values_str: str
    for values_str in values:
        for value in re.split(r"[, ]+", values_str):
            yield value


def get_package_name(setup_scripts: Union[Iterable[str], str]) -> str:
    name: str = ""
    setup_script: str
    for setup_script in (
        (setup_scripts,) if isinstance(setup_scripts, str) else setup_scripts
    ):
        try:
            name = get_setup_script(setup_script)["name"]
        except KeyError:
            pass
    return name


def update_requirements(
    path: str = "requirements.txt",
    setup_scripts: Collection[str] = ("setup.py",),
    exclude: Collection[str] = (),
    extras: Union[str, Iterable[str]] = "test",
) -> None:
    """
    This function infers a set of frozen/pinned requirements based on the
    dev environment in which the function is run + the package requirements.
    """
    if not isinstance(extras, str):
        extras = ",".join(extras)
    path = os.path.abspath(path)
    print(f"Updating {path}")
    distribution_freeze: Tuple[str, ...] = tuple(
        get_distribution_freeze(
            f"{get_package_name(setup_scripts)}[{extras}]", exclude=exclude
        )
    )

    def is_not_in_freeze(project_name: str) -> bool:
        return not any(
            map(
                lambda requirement: requirement.startswith(f"{project_name}="),
                distribution_freeze,
            )
        )

    requirement: str
    forced_requirements: Iterable[str] = ()
    if sys.version_info[:2] == (3, 6):
        forced_requirements = map(
            lambda requirement: f'{requirement};python_version=="3.6"',
            filter(is_not_in_freeze, _PYTHON_36_FORCED_REQUIREMENTS),
        )
    with open(path, "w") as requirements_io:
        text: str = "\n".join(
            chain(
                (
                    (
                        "--extra-index-url "
                        "https://artifactory.company.com/"
                        "artifactory/api/pypi/python-local/simple"
                    ),
                    "--trusted-host artifactory.company.com",
                ),
                forced_requirements,
                distribution_freeze,
                ("",),
            )
        )
        requirements_io.write(text)


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "--requirements",
        "-r",
        type=str,
        default="",
        help=(
            "The name of the file in which to save requirements "
            "(typically requirements.txt). If not provided, no requirements "
            "will be saved."
        ),
    )
    parser.add_argument(
        "--ignore",
        "-i",
        action="append",
        type=str,
        default=[],
        help=(
            "The name of one or more packages to ignore when updating "
            "requirement versions (space or comma separated)"
        ),
    )
    parser.add_argument(
        "--exclude",
        "-e",
        action="append",
        type=str,
        default=[],
        help=(
            "The name of one or more packages to exclude when generating the "
            "content of the requirements.txt file (space or comma separated)"
        ),
    )
    parser.add_argument(
        "--extras",
        action="append",
        type=str,
        default=[],
        help=(
            "The name of one or more extras to install with this project "
            '(the default is ["test"])'
        ),
    )
    parser.add_argument(
        "setup_script",
        default=["setup.py"],
        nargs="*",
        help="The path of one or more setup files or directories",
    )
    arguments: argparse.Namespace = parser.parse_args()
    ignore: Set[str] = set(_iter_parse_argument(arguments.ignore))
    setup_script: str
    setup_scripts: List[str] = []
    for setup_script in _iter_parse_argument(arguments.setup_script):
        if os.path.isdir(setup_script):
            setup_script = os.path.join(setup_script, "setup.py")
        setup_scripts.append(setup_script)
        # Update `setup.py` to require currently installed versions of all
        # packages except those which are explicitly ignored
        update_setup(setup_script, default_operator="~=", ignore=ignore)
        # Reformat the setup file
        run(f"black '{setup_script}'")
    if arguments.requirements:
        update_requirements(
            arguments.requirements,
            setup_scripts=setup_scripts,
            exclude=set(_iter_parse_argument(arguments.exclude)),
            extras=arguments.extras or ("test",),
        )
