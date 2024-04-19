import functools
import sys
import os
from functools import wraps
from logging import INFO, Formatter, Logger, StreamHandler, getLogger
from time import sleep
from typing import Any, Callable, Tuple, Type, Optional
from warnings import warn

import boto3
from file_system_client.errors import (
    append_exception_text,
    get_exception_text
)

lru_cache: Callable[..., Any] = functools.lru_cache
SMTP_USER: str = "a.EMAIL"


def get_print_logger(name: str = "") -> Logger:
    """
    Retrieve or create a logger which prints to `sys.stdout`.
    """
    log: Logger = getLogger(*((name,) if name else ()))
    log.setLevel(INFO)
    if not log.handlers:
        handler = StreamHandler(sys.stdout)
        handler.setLevel(INFO)
        handler.setFormatter(
            Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        log.addHandler(handler)
    return log

@lru_cache()
def url_is_local(url: str) -> bool:
    """
    Check to see if a URL references a local endpoint, such as would be used
    with localstack
    """
    localstack_hostname: str = os.environ.get(
        "LOCALSTACK_HOSTNAME", "localhost"
    )
    return bool(
        url.startswith(f"http://{localstack_hostname}")
        or url.startswith("http://127.0.0.1")
        or url.startswith("http://localhost")
    )


def s3_is_local(session: Optional[boto3.session.Session] = None) -> bool:
    """
    Determine if a boto3 session has been patched for use with a local
    s3 endpoint, such as would be the case if using localstack
    """
    if session is None:
        session = boto3.session.Session()
    endpoint_url: str = session.client("s3").meta.endpoint_url
    is_local: bool = url_is_local(endpoint_url)
    return is_local

def _default_retry_hook(error: Exception) -> bool:
    assert error
    return True


log: Logger = get_print_logger(__name__)


def retry(
    errors: Tuple[Type[Exception], ...],
    retry_hook: Callable[[Exception], bool] = _default_retry_hook,
    number_of_attempts: int = 1,
) -> Callable:
    def decorating_function(function: Callable) -> Callable:
        attempt_number: int = 1

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal attempt_number
            nonlocal number_of_attempts
            if number_of_attempts - attempt_number:
                try:
                    return function(*args, **kwargs)
                except errors as error:
                    if not retry_hook(error):
                        raise
                    warning_message: str = (
                        f"Attempt # {str(attempt_number)}:\n"
                        f"{get_exception_text()}"
                    )
                    warn(warning_message)
                    log.warning(warning_message)
                    sleep(2**attempt_number)
                    attempt_number += 1
                    return wrapper(*args, **kwargs)
            return function(*args, **kwargs)

        return wrapper

    return decorating_function


def _call_if_callable(function: Any) -> Any:
    if (not isinstance(function, type)) and callable(function):
        try:
            return function()
        except Exception as error:
            append_exception_text(error, f"Error calling {repr(function)}")
            raise error
    return function


def _call_item_value_if_callable(item: Tuple[str, Any]) -> Tuple[str, Any]:
    return item[0], _call_if_callable(item[1])


def call_arguments(function: Callable[..., Any]) -> Callable[..., Any]:
    """
    For all callable argument values, call the function and pass the result
    as the argument value
    """

    @functools.wraps(function)
    def wrapper(*args: Callable, **kwargs: Callable) -> Any:
        return function(
            *map(_call_if_callable, args),
            **dict(map(_call_item_value_if_callable, kwargs.items())),
        )

    return wrapper


def is_spark_path_not_found_error(error: Exception) -> bool:
    """
    Determine if an error is caused by files not being found
    for a Spark job
    """
    from pyspark.errors.exceptions.captured import (  # type: ignore
        AnalysisException,
    )

    if isinstance(error, AnalysisException):
        error_str: str = str(error)
        if ("[PATH_NOT_FOUND]" in error_str) or (
            "does not exist" in error_str
        ):
            return True
    return False
