import argparse
import functools
import sys
from collections import OrderedDict
from traceback import format_exception
from typing import Callable, Dict, List, Optional

import boto3  # type: ignore
from botocore.exceptions import ClientError, NoCredentialsError  # type: ignore
from cerberus import CerberusClientException  # type: ignore
from cerberus.client import CerberusClient  # type: ignore

from ._utilities import (
    disable_local_endpoints,
    enable_local_endpoints,
    get_boto3_session,
    split_secret_path,
)
from .config import CERBERUS_URL

__all__: List[str] = ["get_secrets", "get_secret", "main"]
_dict_str_str_lru_cache: Callable[
    [], Callable[..., Callable[..., Dict[str, str]]]
] = functools.lru_cache  # type: ignore


@_dict_str_str_lru_cache()
def get_secrets(
    path: str, url: str = CERBERUS_URL, arn: str = ""
) -> Dict[str, str]:
    """
    This function attempts to access Cerberus secrets at the given `path`
    with each AWS profile until successful, or until having run out of
    profiles, and returns the secrets if successful (or raises an error if
    not).

    Parameters:

    - path (str): The Cerberus path containing the desired secret(s)
    - url (str): The Cerberus API endpoint URL.
    - arn (str) = "": The ARN of an assumed role to use.
    """
    local_endpoints_disabled: bool = disable_local_endpoints()
    secrets: Optional[Dict[str, str]] = None
    errors: Dict[str, str] = OrderedDict()
    try:
        for profile_name in tuple(
            boto3.session.Session().available_profiles
        ) + ("",):
            affected_arn: str = ""
            try:
                session = get_boto3_session(
                    profile_name=profile_name,
                    arn=arn,
                )
                affected_arn = (
                    session.client("sts").get_caller_identity().get("Arn")
                )
                secrets = CerberusClient(
                    url, aws_session=session, verbose=False
                ).get_secrets_data(path)
                break
            except (CerberusClientException, ClientError, NoCredentialsError):
                errors[affected_arn or profile_name] = "".join(
                    format_exception(*sys.exc_info())
                )
        if secrets is None:
            message: str = "\n".join(
                f'{key or "[default]"}:\n{value}\n'
                for key, value in errors.items()
            )
            raise PermissionError(
                "No AWS profile was found with access to the "
                f"secrets in {path}:\n{message}"
            )
    finally:
        if local_endpoints_disabled:
            enable_local_endpoints()
    return secrets


def get_secret(path: str, url: str = CERBERUS_URL, arn: str = "") -> str:
    """
    Retrieve a secret from a Cerberus secure data path.

    Parameters:

    - path (str): The Cerberus path containing the desired secret,
      *including* a dictionary key. For example: "path/to/secrets/key".
    - url (str): The Cerberus API endpoint.
    - arn (str) = "": The ARN of an assumed role to use.
    """
    if not url:
        raise ValueError(url)
    key: str
    path, key = split_secret_path(path)
    # Retrieve the secrets dictionary
    secrets: Dict[str, str] = get_secrets(path, url=url, arn=arn)
    # Return the value stored at the secret's "key" index
    return secrets[key]


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="cerberus-assistant get",
        description=("Retrieve a Cerberus secret."),
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        default=CERBERUS_URL,
        help=(
            "The base URL for the Cerberus API (default value: "
            f"{CERBERUS_URL})."
        ),
    )
    parser.add_argument(
        "-arn",
        "--amazon-resource-name",
        type=str,
        default="",
        help="The ARN of a role to assume.",
    )
    parser.add_argument(
        "path",
        type=str,
        help=(
            "The Cerberus path containing the desired secret, *including* "
            'a dictionary key. For example: "path/to/secrets/key".'
        ),
    )
    namespace: argparse.Namespace = parser.parse_args()
    print(
        get_secret(
            namespace.path,
            url=namespace.url,
            arn=namespace.amazon_resource_name,
        )
    )


if __name__ == "__main__":
    main()
