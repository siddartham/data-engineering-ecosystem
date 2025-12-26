import argparse
import functools
from io import BytesIO
from typing import Iterable, Optional, Set, Tuple

from company.file_system_client.s3 import S3
from setuptools_setup_versions.parse import (  # type: ignore
    get_distribution_freeze,
    get_package_version,
)

from .config import PIP_FLAGS, PYTHON_EXECUTABLE
from ..config import (
    REGIONS_BIN_BUCKET_NAMES,
    BMX_myteamname_ENGINEERING_ARN,
    BMX_myteamname_ENGINEERING_NON_PROD_ARN,
)
from ..utilities import (
    is_ci,
    multiprocessing_set_start_method,
    get_package_name,
    get_top_level_module_names,
)

UNPIN_PACKAGE_NAMES: Set[str] = set()  # {"sasl", "thrift-sasl", "pyyaml"}
EXCLUDE_PACKAGE_NAMES: Set[str] = {
    "apache-airflow",
    "pyspark",
    "wheel",
    "ae-compute-ops",
    "setuptools",
    "numpy",
    "pyyaml",
}
multiprocessing_set_start_method()


def _unpin(requirement: str) -> str:
    name: str
    version: str
    name, version = requirement.split("==")
    if name.lower().strip() in UNPIN_PACKAGE_NAMES:
        return name
    return requirement


def get_pinned_requirements(
    package_name: Optional[str] = None,
    setup_path: Optional[str] = None,
) -> Tuple[str, ...]:
    """
    This function infers a set of frozen/pinned requirements based on the
    dev environment in which the function is run + the package requirements.

    Parameters:

    - package_name (str) = None: The name of the package. If none is provided,
      the name is inferred from the `setup.py` file.
    - setup_path (str) = None: The file or directory path to the `setup.py`
      file of the package for which we are generating requirements
      (defaults to the current directory).
    """
    if not package_name:
        package_name = get_package_name(setup_path)
    package_version: str = get_package_version(package_name)
    return (f"{package_name}=={package_version}",) + tuple(
        sorted(
            map(
                _unpin,
                get_distribution_freeze(
                    f"{package_name}[all]", exclude=EXCLUDE_PACKAGE_NAMES
                ),
            )
        )
    )


@functools.lru_cache()
def get_requirements(
    package_name: str, requirements: Tuple[str, ...] = ()
) -> Iterable[str]:
    """
    This function infers a set of frozen/pinned requirements based on the
    dev environment on which the function is run + the package requirements.
    """
    pinned_requirements: Iterable[str]
    pinned_requirements = []
    if requirements:
        requirements_file_path: str
        for requirements_file_path in requirements:
            with open(requirements_file_path, "r") as requirements_io:
                pinned_requirements += (
                    requirements_io.read().strip().split("\n")
                )
    else:
        pinned_requirements = get_pinned_requirements(package_name)
    return pinned_requirements


def _put_bootstrap_actions(
    file_system: S3, package_name: str, requirements: Tuple[str, ...] = ()
) -> None:
    # Updating `pip` prior to other packages is important to avoid setup
    # errors (usually from `pandas`)
    package_requirements: str = " ".join(
        get_requirements(package_name, requirements=requirements)
    )
    bootstrap_actions: str = (
        f"sudo yum install -y cyrus-sasl-devel\n"
        f"sudo yum upgrade -y cyrus-sasl-devel\n"
        f"sudo yum install -y python36-numpy\n"
        f"sudo yum upgrade -y python36-numpy\n"
        f"sudo yum install -y python36-PyYAML\n"
        f"sudo yum upgrade -y python36-PyYAML\n"
        f"sudo {PYTHON_EXECUTABLE} -m pip install --upgrade pip wheel numpy\n"
        f"sudo {PYTHON_EXECUTABLE} -m pip install --no-deps "
        f"{package_requirements} {PIP_FLAGS}\n"
    )
    prefix: str = (
        package_name[20:]
        if package_name.startswith("company-myteamname-")
        else package_name[5:]
        if package_name.startswith("company-")
        else package_name
    ).replace("-", "_")
    path: str = f"{prefix}_bootstrap_actions.sh"
    print(
        f"Putting in {file_system.get_url(path)}:\n\n" f"{bootstrap_actions}"
    )
    with BytesIO(
        bytes(bootstrap_actions, encoding="utf-8")
    ) as bootstrap_actions_io:
        file_system.put(bootstrap_actions_io, path)


def _put_spark_app(
    environment: str, file_system: S3, module_name: str
) -> None:
    spark_app: str = (
        "import runpy\n"
        "import sys\n"
        "from pyspark.sql import SparkSession  # type: ignore\n"
        "SparkSession.builder.enableHiveSupport().getOrCreate()\n"
        "if not set(argument.lower() for argument in sys.argv) & "
        "{'dev', 'qa', 'prod'}:\n"
        f"    sys.argv.append('{environment}')\n"
        f"runpy.run_module('{module_name}', run_name='__main__')"
    )
    path: str = (
        f"{module_name[20:]}.py"
        if module_name.startswith("company.myteamname_")
        else f"{module_name[5:]}.py"
        if module_name.startswith("company.")
        else f"{module_name}.py"
    )
    print(f"Putting in {file_system.get_url(path)}:\n{spark_app}\n")
    with BytesIO(bytes(spark_app, encoding="utf-8")) as spark_app_io:
        file_system.put(spark_app_io, path)


def put_bin(
    environments: Iterable[str] = ("dev",),
    regions: Iterable[str] = ("us-west-2", "us-east-1"),
    setup_path: Optional[str] = None,
    requirements: Tuple[str, ...] = (),
) -> None:
    """
    This function uploads Genie and Spark scripts to S3.

    Parameters:

    - environments ([str]): One or more environments for which to deploy
      Genie and Spark scripts ("dev", "qa", and/or "prod").
    """
    package_name: str = get_package_name(setup_path)
    module_names: Set[str] = get_top_level_module_names(setup_path)
    environment: str
    for environment in environments:
        for region in regions:
            file_system: S3 = S3(
                REGIONS_BIN_BUCKET_NAMES[region],
                "{}/{}".format(
                    (
                        "myteamnameengineering"
                        if environment == "prod"
                        else "myteamnameengineeringnonprod"
                    ),
                    environment,
                ),
                arn=(
                    (
                        BMX_myteamname_ENGINEERING_ARN
                        if environment == "prod"
                        else BMX_myteamname_ENGINEERING_NON_PROD_ARN
                    )
                    if is_ci()
                    else ""
                ),
            )
            _put_bootstrap_actions(
                file_system=file_system,
                package_name=package_name,
                requirements=requirements,
            )
            module_name: str
            for module_name in module_names:
                _put_spark_app(
                    environment, file_system, module_name=module_name
                )


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=None,
        help="A directory path containing the package setup script.",
    )
    parser.add_argument(
        "--requirement",
        action="append",
        type=str,
        default=[],
        help="One or more requirements file paths.",
    )
    parser.add_argument(
        "--region",
        "-r",
        action="append",
        type=str,
        default=[],
        help='One or more AWS regions ("us-west-2" or "us-east-1").',
    )
    parser.add_argument(
        "environments",
        nargs="*",
        default=[],
        help='Which environments ("dev", "qa", and/or "prod")?',
    )
    arguments: argparse.Namespace = parser.parse_args()
    put_bin(
        environments=tuple(arguments.environments) or ("dev",),
        regions=tuple(arguments.region) or ("us-west-2", "us-east-1"),
        setup_path=arguments.directory,
        requirements=tuple(arguments.requirement or ()),
    )
