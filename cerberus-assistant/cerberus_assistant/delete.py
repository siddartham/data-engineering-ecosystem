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
    validate_secrets_path,
)
from .config import CERBERUS_URL

__all__: List[str] = ["delete_secrets", "main"]


def delete_secrets(
    path: str,
    url: str = CERBERUS_URL,
    arn: str = "",
) -> None:
    """
    This function attempts to access Cerberus and delete the supplied `secret`
    with each AWS profile until successful, or until
    having run out of profiles, and returns `True` if successful (or raises an
    error if not).

    Parameters:

    - path (str): The Cerberus path containing the desired secret(s)
    - url (str): The Cerberus API endpoint URL.
    - arn (str) = "": The ARN of an assumed role to use.
    """
    if not url:
        raise ValueError(url)
    validate_secrets_path(path)
    local_endpoints_disabled: bool = disable_local_endpoints()
    delete_response: Optional[int] = None
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
                delete_response = int(
                    CerberusClient(url, aws_session=session, verbose=False)
                    .delete_secret(secure_data_path=path)
                    .status_code
                )
                assert 300 > delete_response >= 200
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
        raise RuntimeError(f"Failed to delete secrets in {path}:\n{message}")
    finally:
        if local_endpoints_disabled:
            enable_local_endpoints()


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="cerberus-assistant delete",
        description=("Delete a Cerberus secret path."),
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
            "The Cerberus path containing the desired secret, *not* including"
            'a dictionary key. For example: "path/to/secrets".'
        ),
    )
    namespace: argparse.Namespace = parser.parse_args()
    delete_secrets(
        namespace.path,
        url=namespace.url,
        arn=namespace.amazon_resource_name,
    )


if __name__ == "__main__":
    main()
