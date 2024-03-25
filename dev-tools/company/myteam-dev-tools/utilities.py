import multiprocessing
import sys
import base64
import functools
import os
from subprocess import getstatusoutput
from typing import Any, Callable, Dict, Optional, Set, Tuple

from daves_dev_tools.utilities.cerberus import get_cerberus_secrets
from setuptools_setup_versions.find import setup_script_path  # type: ignore
from setuptools_setup_versions.parse import (  # type: ignore
    get_setup_script,
    SetupScript,
)

from .config import CERBERUS_URL

lru_cache: Callable[..., Any] = functools.lru_cache


def run(command: str, echo: bool = True) -> str:
    """
    This function runs a shell command, raises an error if a non-zero
    exit code is returned, and echo's both the command and output *if*
    the `echo` parameter is `True`.

    Parameters:

    - command (str): A shell command
    - echo (bool) = True: If `True`, the command and the output from the
      command will be printed to stdout
    """
    if echo:
        print(command)
    status: int
    output: str
    status, output = getstatusoutput(command)
    # Create an error if a non-zero exit status is encountered
    if status:
        raise OSError(output)
    else:
        output = output.strip()
        if output and echo:
            print(output)
    return output


@lru_cache()
def get_client_id_secret() -> Tuple[str, str]:
    """
    Returns OAuth client ID + credentials as a two-item tuple
    """
    secrets: Dict[str, str] = get_cerberus_secrets(
        CERBERUS_URL, "app/teamname/etl"
    )
    return secrets["client-id"], secrets["client-secret"]


def epctl_login() -> None:
    """
    Login to Okta with EPCtl
    """
    run(
        "epctl login "
        "--production "
        "--client-id {} "
        "--client-secret {} ".format(*get_client_id_secret())
    )


def _get_setup_script(
    package_directory_or_setup_script: Optional[str] = None,
) -> SetupScript:
    return get_setup_script(
        setup_script_path(package_directory_or_setup_script)
    )


def get_package_name(
    package_directory_or_setup_script: Optional[str] = None,
) -> str:
    setup_script: SetupScript = _get_setup_script(
        package_directory_or_setup_script
    )
    return setup_script["name"]


def get_package_version(
    package_directory_or_setup_script: Optional[str] = None,
) -> str:
    setup_script: SetupScript = _get_setup_script(
        package_directory_or_setup_script
    )
    return setup_script["version"]


def get_top_level_module_names(
    package_directory_or_setup_script: Optional[str] = None,
) -> Set[str]:
    setup_script: SetupScript = _get_setup_script(
        package_directory_or_setup_script
    )
    top_level_module_names: Set[str] = set()
    module_name: str
    for module_name in sorted(
        setup_script["packages"], key=lambda module_name: len(module_name)
    ):
        if not any(
            map(
                lambda top_level_module_name: module_name.startswith(
                    top_level_module_name
                ),
                top_level_module_names,
            )
        ):
            top_level_module_names.add(module_name)
    return top_level_module_names


def base64_encode(text: str) -> str:
    return str(
        base64.b64encode(bytes(text, encoding="utf-8")), encoding="utf-8"
    )


@lru_cache()
def is_bmx() -> bool:
    if "HUDSON_URL" in os.environ and (
        "jenkins.bmx.companycloud.com" in os.environ["HUDSON_URL"]
    ):
        return True
    return False


@lru_cache()
def is_ci() -> bool:
    if "CI" in os.environ and (os.environ["CI"].lower() == "true"):
        return True
    return is_bmx()


_DARWIN_MULTIPROCESSING_START_METHOD: str = "forkserver"


@lru_cache()
def multiprocessing_set_start_method() -> None:
    if sys.platform == "darwin":
        try:
            multiprocessing.set_start_method(
                _DARWIN_MULTIPROCESSING_START_METHOD
            )
        except RuntimeError:
            if multiprocessing.get_start_method() != (
                _DARWIN_MULTIPROCESSING_START_METHOD
            ):
                raise
