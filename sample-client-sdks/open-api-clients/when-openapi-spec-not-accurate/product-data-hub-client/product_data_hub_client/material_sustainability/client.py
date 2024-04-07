import oapi
import sob
import typing
from . import model
from ..abc.client import Client as _Client
from ..config import TOKEN_URL_PROD
from logging import Logger
from nike.cerberus_assistant.config import CERBERUS_URL
from nike.cerberus_assistant.decorate import apply_cerberus_path_arguments


class Client(_Client):
    """
    Initialization Parameters:

    - url (str): The base URL for API requests.
    - api_key (str): An API key with which to authenticate requests.
    - api_key_name (str): The name of the header, query parameter, or
      cookie parameter in which to convey the API key.
    - oauth2_client_id (str): An OAuth2 client ID.
    - oauth2_client_secret (str): An OAuth2 client secret.
    - oauth2_token_url (str): The token URL to use for OAuth2
      authentication.
      Can be relative to `url`.
    - timeout (int): The number of seconds before a request will timeout
      and throw an error. If this is 0 (the default), the system default
      timeout will be used.
    - retry_number_of_attempts (int): The number of times to retry
      a request which results in an error.
    - retry_for_errors: A tuple of one or more exception types
      on which to retry a request. To retry for *all* errors,
      pass `(Exception,)` for this argument.
    - retry_hook: A function, accepting one argument (an Exception),
      and returning a boolean value indicating whether to retry the
      request (if retries have not been exhausted). This hook applies
      *only* for exceptions which are a sub-class of an exception
      included in `retry_for_errors`.
    - logger (logging.Logger|None):
      A `logging.Logger` to which requests should be logged.
    - echo (bool): If `True`, requests/responses are printed as
      they occur.
    - cerberus_url (str): The root URL for the Cerberus API where
      your secrets are stored.
    - api_key_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein an API key with which to authenticate can be found.
    - oauth2_client_id_cerberus_path (str) = "": A Cerberus secure data path (
      including /key) wherein an OAuth2 client ID with which to authenticate
      can be found.
    - oauth2_client_secret_cerberus_path (str) = "": A Cerberus secure data
      path (including /key) wherein an OAuth2 client secret with which to
      authenticate can be found.
    """

    __slots__: typing.Tuple[str, ...] = oapi.client.CLIENT_SLOTS

    @apply_cerberus_path_arguments(
        api_key="api_key_cerberus_path",
        cerberus_url_parameter_name="cerberus_url",
        oauth2_client_id="oauth2_client_id_cerberus_path",
        oauth2_client_secret="oauth2_client_secret_cerberus_path",
    )
    def __init__(
        self,
        url: str = (
            "https://materialmanagement.api-product.pes-prod.nike.com/v1"
        ),
        api_key: str = "",
        api_key_name: str = "X-API-KEY",
        oauth2_client_id: str = "",
        oauth2_client_secret: str = "",
        oauth2_token_url: str = TOKEN_URL_PROD,
        timeout: int = 0,
        retry_number_of_attempts: int = 3,
        retry_for_errors: typing.Tuple[
            typing.Type[Exception], ...
        ] = oapi.client.DEFAULT_RETRY_FOR_ERRORS,
        retry_hook: typing.Callable[
            [Exception], bool
        ] = oapi.client.default_retry_hook,
        logger: typing.Optional[Logger] = None,
        echo: bool = False,
        cerberus_url: str = CERBERUS_URL,
        api_key_cerberus_path: str = "",
        oauth2_client_id_cerberus_path: str = "",
        oauth2_client_secret_cerberus_path: str = "",
    ) -> None:
        super().__init__(
            url=url,
            api_key=api_key,
            api_key_name=api_key_name,
            oauth2_client_id=oauth2_client_id,
            oauth2_client_secret=oauth2_client_secret,
            oauth2_token_url=oauth2_token_url,
            timeout=timeout,
            retry_number_of_attempts=retry_number_of_attempts,
            retry_for_errors=retry_for_errors,
            retry_hook=retry_hook,
            logger=logger,
            echo=echo,
        )

    def get_sustainability_data_supplied_material_indicies_object_id_current(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.SustainabilityDataSuppliedMaterialIndiciesObjectIdCurrentGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialIndexResponse:
        """
        How you get a single MSI Score for the most recent season.

        Parameters:

        - object_id:
          A single Id of the object (in this case Supplied Material)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/sustainability/data/suppliedMaterialIndicies/{objectId}/current".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialIndexResponse,
            )
        )

    def get_sustainability_data_supplied_material_indicies_current(
        self,
        object_id: model.SustainabilityDataSuppliedMaterialIndiciesCurrentGetObjectId,  # noqa
        *,
        dataunits: typing.Optional[
            model.SustainabilityDataSuppliedMaterialIndiciesCurrentGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SuppliedMaterialIndexBulkResponse:
        """
        How you get MSI Score in a Bulk fashion for the Most Recent Season.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplied
          Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/sustainability/data/suppliedMaterialIndicies/current",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "objectId": oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                ),
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SuppliedMaterialIndexBulkResponse,
            )
        )

    def get_sustainability_data_seasons_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.SustainabilityDataSeasonsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SustainabilityDateResponse:
        """
        How you get a single date for the most recent season.

        Parameters:

        - object_id:
          A single Id of the object (in this case Supplied Material)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/sustainability/data/seasons/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
            query={
                "_dataunits": oapi.client.format_argument_value(
                    "_dataunits",
                    dataunits,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SustainabilityDateResponse,
            )
        )

    def put_pdh_streams_adaptor_data(
        self,
        events: model.PdhStreamsAdaptorDataPut0,
    ) -> None:
        """
        Update a pdhStreamAdaptor resource by objectId

        Parameters:

        - events:
          The request body
        """
        self.request(
            "/pdhStreamsAdaptor/data",
            method="PUT",
            json=events,
        )
