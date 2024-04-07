from logging import Logger, getLogger
from typing import Any, Callable, Optional, Tuple

import sob
from cerberus_assistant.decorate import apply_cerberus_path_arguments
from oapi.client import CLIENT_SLOTS
from oapi.client import Client as _Client

from . import model

log: Logger = getLogger(__name__)


class Client(_Client):
    """
    Instances of this class act as client for updating
    indicator values via the Enablon REST API.

    Initialization Parameters:

    - url (str): The base URL for API requests.
    - user (str) = "": A user name for use with HTTP basic authentication.
    - password (str) = "":  A password for use with HTTP basic authentication.
    - timeout (int): The number of seconds before a request will timeout
      and throw an error. If this is 0 (the default), the system default
      timeout will be used.
    - logger (logging.Logger|None) = None:
      A `logging.Logger` to which requests should be logged.
    - echo (bool) = False: If `True`, requests/responses are printed as
      they occur.
    - password_cerberus_path (str) = "": A Cerberus secure data
      path (including /key) wherein a password with which to
      authenticate can be found.
    """

    __slots__: Tuple[str, ...] = CLIENT_SLOTS

    @apply_cerberus_path_arguments(
        url="url_cerberus_path",
        user="user_cerberus_path",
        password="password_cerberus_path",
    )
    def __init__(
        self,
        url: str = "https://ehs.uat.eu.enablon.io/sample.uat",
        user: str = "",
        password: str = "",
        timeout: int = 0,
        logger: Optional[Logger] = log,
        echo: bool = False,
        url_cerberus_path: str = "",
        user_cerberus_path: str = "",
        password_cerberus_path: str = "",
    ) -> None:
        super().__init__(
            url=url,
            user=user,
            password=password,
            timeout=timeout,
            logger=logger,
            echo=echo,
        )

    def __reduce__(
        self,
    ) -> Tuple[  # Force line-break retention
        Callable[..., _Client], Tuple[Any, ...]
    ]:
        return self._resurrect_client, (
            # Initialization Parameters
            self.url,
            self.user,
            self.password,
            self.timeout,
            self.retry_number_of_attempts,
            self.retry_for_errors,
            self.retry_hook,
            self.logger,
            self.echo,
        )

    def update_indicator_value(
        self,
        update_indicator_value_request: model.UpdateIndicatorValueRequest,
    ) -> model.UpdateIndicatorValueResponse:
        """
        Update Indicator Value

        Parameters:

        - update_indicator_value_request (model.UpdateIndicatorValueRequest):
        """
        update_indicator_value_request.authentication = model.Authentication(
            userid=self.user,
            password=self.password,
        )
        response: sob.abc.Readable = self.request(
            "/go.aspx",
            method="POST",
            query={
                "v": "/SD/CS_DataFoundationImport",
            },
            data=update_indicator_value_request,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.UpdateIndicatorValueResponse,
            )
        )
