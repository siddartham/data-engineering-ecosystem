import argparse
import functools
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Union,
)

from daves_dev_tools.utilities.cerberus import get_cerberus_secrets

from ..utilities import get_package_name, get_package_version, run
from ..config import BMX_CERBERUS_PATH, BMX_USER, CERBERUS_URL
from .config import DOCKER_REGISTRY

lru_cache: Callable[..., Any] = functools.lru_cache


def _get_build_args_dict(
    build_arguments: Union[Dict[str, str], Sequence[str]]
) -> Dict[str, str]:
    build_arguments_dict: Dict[str, str]
    if isinstance(build_arguments, Mapping):
        build_arguments_dict = build_arguments
    else:
        build_arguments_dict = {}
        for value in build_arguments:
            if "=" in value:
                key, value = value.split("=", maxsplit=1)
                build_arguments_dict[key] = value
    return build_arguments_dict


def get_image_name(
    file_name: str = "Dockerfile",
    build_arguments: Union[Dict[str, str], Sequence[str], None] = None,
    setup_script: Optional[str] = None,
) -> str:
    """
    Infer a container name from the docker file name + package name and version
    """
    key: str
    value: str
    build_argument_suffix: List[str] = []
    if build_arguments:
        for key, value in sorted(
            _get_build_args_dict(build_arguments).items()
        ):
            if key.upper().endswith("_VERSION"):
                build_argument_suffix.append(
                    f"{key[:-8].lower()}{''.join(value.split('.')[:2])}"
                )
    package_name: str = get_package_name(setup_script)
    return "{}/company-teamname/{}{}{}".format(
        DOCKER_REGISTRY,
        (
            package_name[20:]
            if package_name.startswith("company-teamname-")
            else package_name[5:]
            if package_name.startswith("company-")
            else package_name
        )[: (-7 if package_name.endswith("-docker") else None)],
        (f"-{file_name[:-11]}" if file_name.endswith(".Dockerfile") else ""),
        (
            f"-{'-'.join(build_argument_suffix)}"
            if build_argument_suffix
            else ""
        ),
    )


def docker_login() -> None:
    """
    Login to our docker registry
    """
    secrets: Dict[str, str] = get_cerberus_secrets(
        CERBERUS_URL, BMX_CERBERUS_PATH
    )
    password: str = secrets[BMX_USER]
    run(
        f"docker login -u {BMX_USER} -p {password} {DOCKER_REGISTRY}",
        # Don't echo this command--we don't want passwords in our log
        echo=False,
    )


def distribute_container(
    file_name: str = "Dockerfile",
    build_arguments: Union[Dict[str, str], List[str], None] = None,
    setup_script: Optional[str] = None,
) -> None:
    """
    This function distributes a docker container with a version tag matching
    the python package version
    """
    docker_login()
    container_name: str = get_image_name(file_name, build_arguments)
    build_command: List[str] = [
        f"docker build "
        "--compress "
        f"-f {file_name} "
        f'-t "{container_name}"'
    ]
    key: str
    value: str
    if build_arguments:
        if isinstance(build_arguments, Mapping):
            for key, value in sorted(build_arguments.items()):
                build_command.append(f"--build-arg {key}={repr(value)}")
        else:
            for value in sorted(build_arguments):
                build_command.append(f"--build-arg {value}")
    build_command.append(".")
    version: str = get_package_version(setup_script)
    # The *commands* variable is a tuple of lists, with each list representing
    # contingencies where only one of the commands needs to succeed in order
    # to avoid raising an error
    command: str
    list(
        map(
            run,
            (
                " ".join(build_command),
                f'docker tag "{container_name}" "{container_name}:{version}"',
                f'docker push "{container_name}"',
                f'docker push "{container_name}:{version}"',
            ),
        )
    )


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        default="Dockerfile",
        help="The Dockerfile name/path",
    )
    parser.add_argument(
        "--build-arg",
        "-ba",
        action="append",
        type=str,
        help="The Dockerfile name/path",
    )
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=None,
        help="The directory containing the package setup script",
    )
    arguments: argparse.Namespace = parser.parse_args()
    distribute_container(
        file_name=arguments.file,
        build_arguments=arguments.build_arg,
        setup_script=arguments.directory,
    )
