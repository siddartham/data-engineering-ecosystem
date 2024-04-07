import os
import re
from datetime import datetime
from types import ModuleType
from typing import Any, Dict, Match, Optional, Tuple

import boto3  # type: ignore
from botocore.exceptions import ClientError  # type: ignore


def _is_boto3_localstack_patched() -> bool:
    """
    Determine if boto3 endpoints have been patched for use with localstack
    """
    patch: ModuleType
    try:
        from localstack_client import patch  # type: ignore
    except ImportError:
        # If the localstack client isn't installed, it can't be patched
        return False
    if patch._state.get("_client_orig"):
        return True
    return False


def disable_local_endpoints() -> bool:
    is_localstack_patched: bool = _is_boto3_localstack_patched()
    if is_localstack_patched:
        from localstack_client.patch import (  # type: ignore
            disable_local_endpoints,
        )

        disable_local_endpoints()

        return True
    return False


def enable_local_endpoints() -> bool:
    is_localstack_patched: bool = _is_boto3_localstack_patched()
    if is_localstack_patched:
        from localstack_client.patch import (  # type: ignore
            enable_local_endpoints,
        )

        enable_local_endpoints()
        return True
    return False


def get_aws_role_arn() -> str:
    return os.environ.get("AWS_ROLE_ARN", "")


def get_assume_role_session_name() -> str:
    return os.environ.get(
        "AWS_ROLE_SESSION_NAME",
        "cerberus-assistant-{}".format(
            datetime.now()
            .replace(microsecond=0, tzinfo=None)
            .isoformat()
            .replace(":", "-")
            .replace(".", "-")
        ),
    )


def get_web_identity_token() -> str:
    web_identity_token: str = ""
    web_identity_token_file: str = os.environ.get(
        "AWS_WEB_IDENTITY_TOKEN_FILE", ""
    )
    if web_identity_token_file:
        with open(web_identity_token_file, "r") as web_identity_token_file_io:
            web_identity_token = web_identity_token_file_io.read().strip()
    return web_identity_token


def get_boto3_session(
    profile_name: str = "", arn: str = ""
) -> boto3.session.Session:
    session_name: str
    credentials: Dict[str, Any]
    session: boto3.session.Session = boto3.session.Session(
        profile_name=profile_name or None
    )
    aws_role_arn: str = get_aws_role_arn()
    try:
        if aws_role_arn:
            web_identity_token: str = get_web_identity_token()
            session_name = get_assume_role_session_name()
            if web_identity_token:
                credentials = session.client(
                    "sts"
                ).assume_role_with_web_identity(
                    RoleArn=aws_role_arn,
                    RoleSessionName=session_name,
                    WebIdentityToken=web_identity_token,
                )[
                    "Credentials"
                ]
            else:
                credentials = session.client("sts").assume_role(
                    RoleArn=aws_role_arn,
                    RoleSessionName=session_name,
                )["Credentials"]
            session = boto3.session.Session(
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
            )
        if arn:
            credentials = session.client("sts").assume_role(
                RoleArn=arn,
                RoleSessionName=session_name,
            )["Credentials"]
            session = boto3.session.Session(
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
            )
    except ClientError:
        pass
    return session


def split_secret_path(path: str) -> Tuple[str, str]:
    """
    Split a secret path into a path + key.

    Parameters:

    - path (str): The Cerberus path containing the desired secret
    """
    matched: Optional[Match] = re.match(
        r"^([^/]+/[^/]+/)(?:([^/]+)/)?([^/]+)", path.replace("//", "/")
    )
    if not matched:
        raise ValueError(path)
    key: str
    suffix: str
    path, suffix, key = matched.groups()
    if suffix:
        path = f"{path}{suffix.rstrip('/')}"
    return path, key


def validate_secrets_path(path: str) -> None:
    matched: Optional[Match] = re.match(r"^([^/]+/[^/]+/[^/]*)", path)
    if not matched:
        raise ValueError(path)
