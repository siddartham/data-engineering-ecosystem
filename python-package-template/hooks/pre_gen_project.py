#!/usr/bin/env python3
"""
cookiecutter identifies this file in this path(hooks/pre_gen_project.py/sh)
and runs it before generating the project.
"""
import re
from typing import Pattern

PROJECT_NAME_REGEX: str = r"^[a-z][a-z0-9\-]*[a-z0-9]$"
PROJECT_NAME_PATTERN: Pattern = re.compile(PROJECT_NAME_REGEX)
PACKAGE_NAME_REGEX: str = r"^[a-z_.0-9]*[a-z0-9]$"
PACKAGE_NAME_PATTERN: Pattern = re.compile(PACKAGE_NAME_REGEX)
PROJECT_NAME: str = "{{cookiecutter.name}}"
PACKAGE_NAME: str = "{{cookiecutter.package}}"


def main() -> None:
    if not PROJECT_NAME_PATTERN.match(PROJECT_NAME):
        raise ValueError(
            f"{repr(PROJECT_NAME)} is not a valid project name. "
            "Project names must match the following regular expression: "
            f"{repr(PROJECT_NAME_REGEX)}"
        )
    if not PACKAGE_NAME_PATTERN.match(PACKAGE_NAME):
        raise ValueError(
            f"{repr(PACKAGE_NAME)} is not a valid package name. "
            "Package names must match the following regular expression: "
            f"{repr(PACKAGE_NAME_REGEX)}"
        )


if __name__ == "__main__":
    main()
