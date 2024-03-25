import os
import re
import sys
from collections import OrderedDict
from itertools import chain
from subprocess import getstatusoutput
from typing import Any, Dict, Iterable, Match, Optional, Pattern, Sequence, Set

import setuptools  # type: ignore

_INSTALL_REQUIRES: str = "install_requires"


_extras_pattern: Pattern = re.compile(r"^([^\[]+\[)([^\]]+)(\].*)$")


def consolidate_requirement_options(
    requirements: Iterable[str],
) -> Iterable[str]:
    requirement: str
    templates_options: Dict[str, Set[str]] = OrderedDict()
    traversed_requirements: Set[str] = set()
    template: str
    for requirement in requirements:
        match: Optional[Match] = _extras_pattern.match(requirement)
        if match:
            groups: Sequence[str] = match.groups()
            no_extras_requirement: str = f"{groups[0][:-1]}{groups[2][1:]}"
            template = f"{groups[0]}{{}}{groups[2]}"
            if template not in templates_options:
                templates_options[template] = set()
            templates_options[template] |= set(groups[1].split(","))
            if no_extras_requirement in templates_options:
                del templates_options[no_extras_requirement]
        elif requirement not in traversed_requirements:
            templates_options[requirement] = set()
    options: Set[str]
    for template, options in templates_options.items():
        if options:
            yield template.format(",".join(sorted(options)))
        else:
            yield template


def setup(**kwargs: Any) -> None:
    """
    This `setup` script intercepts arguments to be passed to
    `setuptools.setup` in order to dynamically alter setup requirements
    while retaining a function call which can be easily parsed and altered
    by `setuptools-setup-versions`.
    """
    # Require the package "dataclasses" for python 3.6, but not later
    # python versions (since it's part of the standard library after 3.6)
    if sys.version_info[:2] == (3, 6):
        if _INSTALL_REQUIRES not in kwargs:
            kwargs[_INSTALL_REQUIRES] = []
        kwargs[_INSTALL_REQUIRES].append("dataclasses")
    # Add an "all" extra which includes all extra requirements
    if "extras_require" in kwargs:
        if "all" not in kwargs["extras_require"]:
            kwargs["extras_require"]["all"] = list(
                consolidate_requirement_options(
                    chain(
                        *(
                            values
                            for key, values in kwargs["extras_require"].items()
                            if key not in ("dev", "test")
                        )
                    )
                )
            )
        kwargs["extras_require"]["test"] = list(
            consolidate_requirement_options(
                chain(
                    *(
                        values
                        for key, values in kwargs["extras_require"].items()
                        if key not in ("dev", "all")
                    )
                )
            )
        )
        print(
            "extras_require[all]:\n"
            + "\n".join(
                f"- {requirement}"
                for requirement in kwargs["extras_require"]["all"]
            )
        )
        print(
            "extras_require[test]:\n"
            + "\n".join(
                f"- {requirement}"
                for requirement in kwargs["extras_require"]["test"]
            )
        )
    # Pass the modified keyword arguments to `setuptools.setup`
    setuptools.setup(**kwargs)


def run(command: str) -> str:
    """
    This function runs a shell command, raises an error if a non-zero
    exit code is returned, and echo's both the command and output *if*
    the `echo` parameter is `True`.

    Parameters:

    - command (str): A shell command
    """
    status: int
    output: str
    status, output = getstatusoutput(command)
    # Raise an error if a non-zero exit status is returned
    if status:
        raise OSError(output)
    else:
        output = output.strip()
        print(output)
    return output


def install_epctl() -> None:
    """
    If the `epctl` command is not available, we attempt to install it,
    and raise an error if that is not possible
    """
    status: int
    output: str
    try:
        run("epctl update")
    except OSError:
        try:
            platform: str
            if sys.platform.startswith("darwin"):
                platform = "darwin"
            elif sys.platform.startswith("linux"):
                platform = "linux"
            elif os.name == "nt":
                platform = "windows"
            else:
                raise
            run(
                "curl https://epctl.platforms.company.com/binaries/latest/"
                f"epctl_{platform}_amd64 "
                "-o /usr/local/bin/epctl && "
                "chmod +rwx /usr/local/bin/epctl"
            )
        except OSError:
            raise RuntimeError(
                "`company-myteam-dev-tools` requires `epctl`, please see "
                "https://epctl.platforms.company.com for installation "
                "instructions."
            )


install_epctl()


setup(
    name="company-myteam-dev-tools",
    version="0.55.0",
    description=(
        "Deployment, distribution, and other dev tools for company-myteam"
    ),
    author="Siddartha Reddy",
    author_email="siddartha.reddy@company.com",
    python_requires=">=3.6",
    packages=[
        "company.myteam_dev_tools",
        "company.myteam_dev_tools.airflow",
        "company.myteam_dev_tools.docker",
        "company.myteam_dev_tools.pypi",
        "company.myteam_dev_tools.spark",
        "company.myteam_dev_tools.requirements",
    ],
    package_data={
        "company.myteam_dev_tools": ["py.typed"],
        "company.myteam_dev_tools.airflow": ["py.typed"],
        "company.myteam_dev_tools.docker": ["py.typed"],
        "company.myteam_dev_tools.pypi": ["py.typed"],
        "company.myteam_dev_tools.spark": ["py.typed"],
        "company.myteam_dev_tools.requirements": ["py.typed"],
    },
    install_requires=[
        "daves-dev-tools[cerberus,test]~=0.7",
        "setuptools-setup-versions~=1.17",
    ],
    extras_require={
        "airflow": [
            "company-map-airflow-client~=0.5",
            "apache-airflow[kubernetes]~=1.10",
            "ae-compute-ops~=2.0",
        ],
        "spark": ["company-file-system-client[s3]~=0.0"],
        "test": [],
        "dev": [],
    },
    entry_points={
        "console_scripts": [
            "company-myteam-dev-tools = "
            "company.myteam_dev_tools.__main__:main"
        ]
    },
)
