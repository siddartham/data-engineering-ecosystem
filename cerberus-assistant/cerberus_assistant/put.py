import argparse
import sys
from collections import OrderedDict
from traceback import format_exception
from typing import Dict, List, Optional

import boto3  # type: ignore
from botocore.exceptions import ClientError, NoCredentialsError  # type: ignore
from cerberus import CerberusClientException  # type: ignore
from cerberus.client import CerberusClient  # type: ignore

from ._utilities import (
    disable_local_endpoints,
    enable_local_endpoints,
    get_boto3_session,
    split_secret_path,
    validate_secrets_path,
)
from .config import CERBERUS_URL

__all__: List[str] = ["put_secret", "put_secrets", "main"]


def put_secret(
    path: str,
    secret: str,
    url: str = CERBERUS_URL,
    arn: str = "",
) -> None:
    """
    Put a secret in Cerberus.

    Parameters:

    - path (str): The Cerberus path containing the desired secret(s)
    - secret (str): The secret as either a json string or a dictionary
    - url (str): The Cerberus API endpoint URL.
    - arn (str) = "": The Amazon Resource Name (ARN) of an assumed role to use
    """
    assert url
    key: str
    path, key = split_secret_path(path)
    put_secrets(
        path,
        {key: secret},
        merge=True,
        url=url,
        arn=arn,
    )


def put_secrets(
    path: str,
    secrets: Dict[str, str],
    merge: bool = False,
    url: str = CERBERUS_URL,
    arn: str = "",
) -> None:
    """
    Put secrets in Cerberus.

    Parameters:

    - path (str): The Cerberus path containing the desired secret(s)
    - secrets (dict)
    - url (str): The Cerberus API endpoint URL.
    - arn (str) = "": The Amazon Resource Name (ARN) of an assumed role to use
    """
    if not url:
        raise ValueError(url)
    validate_secrets_path(path)
    local_endpoints_disabled: bool = disable_local_endpoints()
    put_response: Optional[int] = None
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
                put_response = int(
                    CerberusClient(url, aws_session=session, verbose=False)
                    .put_secret(
                        secure_data_path=path,
                        secret=secrets,
                        merge=merge,
                    )
                    .status_code
                )
                assert 300 > put_response >= 200
                return
            except (
                CerberusClientException,
                ClientError,
                NoCredentialsError,
                ValueError,
                TypeError,
            ):
                errors[affected_arn or profile_name] = "".join(
                    format_exception(*sys.exc_info())
                )
        message: str = "\n".join(
            f'{key or "[default]"}:\n{value}\n'
            for key, value in errors.items()
        )
        raise RuntimeError(f"Failed to put secrets in {path}:\n{message}")
    finally:
        if local_endpoints_disabled:
            enable_local_endpoints()


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="cerberus-assistant put",
        description="Put a secret in a Cerberus secure drop box",
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
    parser.add_argument(
        "secret", type=str, help="The secret to put in the specified path."
    )
    namespace: argparse.Namespace = parser.parse_args()
    put_secret(
        namespace.path,
        secret=namespace.secret,
        url=namespace.url,
        arn=namespace.amazon_resource_name,
    )


if __name__ == "__main__":
    main()
