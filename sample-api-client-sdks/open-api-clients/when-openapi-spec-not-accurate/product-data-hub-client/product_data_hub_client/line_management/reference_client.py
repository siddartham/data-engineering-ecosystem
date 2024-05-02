import oapi
import sob
import typing
from . import reference_model
from ..abc.client import Client
from ..config import TOKEN_URL_PROD
from logging import Logger
from cerberus_assistant.config import CERBERUS_URL
from cerberus_assistant.decorate import apply_cerberus_path_arguments


class ReferenceClient(Client):
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
            "https://linemanagement.api-product.pes-prod.nike.com/v1"
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

    def get_line_management_data_ages_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AgeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the age object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ages/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.AgeResponse,
            )
        )

    def get_line_management_data_ages(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AgeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ages",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.AgeBulkResponse,
            )
        )

    def get_line_management_data_athletes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AthleteResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the athlete object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/athletes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.AthleteResponse,
            )
        )

    def get_line_management_data_athletes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AthleteBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/athletes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.AthleteBulkResponse,
            )
        )

    def get_line_management_data_brand_marks_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BrandMarkResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the brandMark object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/brandMarks/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.BrandMarkResponse,
            )
        )

    def get_line_management_data_brand_marks(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BrandMarkBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/brandMarks",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.BrandMarkBulkResponse,
            )
        )

    def get_line_management_data_business_organizations_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BusinessOrganizationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the businessOrganization object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/businessOrganizations/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.BusinessOrganizationResponse,
            )
        )

    def get_line_management_data_business_organizations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BusinessOrganizationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/businessOrganizations",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.BusinessOrganizationBulkResponse,
            )
        )

    def get_line_management_data_categories_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CategoryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the category object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/categories/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CategoryResponse,
            )
        )

    def get_line_management_data_categories(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CategoryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/categories",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CategoryBulkResponse,
            )
        )

    def get_line_management_data_construction_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConstructionMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the constructionMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/constructionMethods/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConstructionMethodResponse,
            )
        )

    def get_line_management_data_construction_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConstructionMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/constructionMethods",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConstructionMethodBulkResponse,
            )
        )

    def get_line_management_data_consumer_focuses_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerFocusResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the consumerFocus object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerFocuses/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerFocusResponse,
            )
        )

    def get_line_management_data_consumer_focuses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerFocusBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerFocuses",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerFocusBulkResponse,
            )
        )

    def get_line_management_data_consumer_groups_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerGroupResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the consumerGroup object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerGroups/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerGroupResponse,
            )
        )

    def get_line_management_data_consumer_groups(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerGroupBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerGroups",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerGroupBulkResponse,
            )
        )

    def get_line_management_data_consumer_purposes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerPurposeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the consumerPurpose object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerPurposes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerPurposeResponse,
            )
        )

    def get_line_management_data_consumer_purposes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerPurposeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerPurposes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerPurposeBulkResponse,
            )
        )

    def get_line_management_data_consumer_uses_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerUseResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the consumerUse object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerUses/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerUseResponse,
            )
        )

    def get_line_management_data_consumer_uses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsumerUseBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/consumerUses",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ConsumerUseBulkResponse,
            )
        )

    def get_line_management_data_currencies_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CurrencyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the currency object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/currencies/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CurrencyResponse,
            )
        )

    def get_line_management_data_currencies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CurrencyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/currencies",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CurrencyBulkResponse,
            )
        )

    def get_line_management_data_cycles_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CycleResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the cycle object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/cycles/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CycleResponse,
            )
        )

    def get_line_management_data_cycles(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CycleBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/cycles",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CycleBulkResponse,
            )
        )

    def get_line_management_data_cycle_years_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CycleYearResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the cycleYear object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/cycleYears/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CycleYearResponse,
            )
        )

    def get_line_management_data_cycle_years(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CycleYearBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/cycleYears",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.CycleYearBulkResponse,
            )
        )

    def get_line_management_data_development_teams_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTeamResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentTeam object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/developmentTeams/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DevelopmentTeamResponse,
            )
        )

    def get_line_management_data_development_teams(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTeamBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/developmentTeams",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DevelopmentTeamBulkResponse,
            )
        )

    def get_line_management_data_dimensions_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DimensionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the dimension object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/dimensions/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DimensionResponse,
            )
        )

    def get_line_management_data_dimensions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DimensionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/dimensions",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DimensionBulkResponse,
            )
        )

    def get_line_management_data_divisions_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DivisionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the division object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/divisions/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DivisionResponse,
            )
        )

    def get_line_management_data_divisions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DivisionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/divisions",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.DivisionBulkResponse,
            )
        )

    def get_line_management_data_exchange_rates_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ExchangeRateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the exchange rate object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/exchangeRates/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ExchangeRateResponse,
            )
        )

    def get_line_management_data_exchange_rates(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ExchangeRateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/exchangeRates",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ExchangeRateBulkResponse,
            )
        )

    def get_line_management_data_features_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FeatureResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the feature object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/features/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FeatureResponse,
            )
        )

    def get_line_management_data_features(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FeatureBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/features",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FeatureBulkResponse,
            )
        )

    def get_line_management_data_fits_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FitResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fit object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/fits/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FitResponse,
            )
        )

    def get_line_management_data_fits(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FitBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/fits",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FitBulkResponse,
            )
        )

    def get_line_management_data_fit_preferences_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FitPreferenceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fitPreference object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/fitPreferences/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FitPreferenceResponse,
            )
        )

    def get_line_management_data_fit_preferences(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FitPreferenceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/fitPreferences",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.FitPreferenceBulkResponse,
            )
        )

    def get_line_management_data_genders_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GenderResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the gender object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/genders/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GenderResponse,
            )
        )

    def get_line_management_data_genders(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GenderBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/genders",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GenderBulkResponse,
            )
        )

    def get_line_management_data_gender_ages_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GenderAgeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the genderAge object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/genderAges/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GenderAgeResponse,
            )
        )

    def get_line_management_data_gender_ages(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GenderAgeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/genderAges",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GenderAgeBulkResponse,
            )
        )

    def get_line_management_data_geographic_areas_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the geographicArea object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreas/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaResponse,
            )
        )

    def get_line_management_data_geographic_areas(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreas",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaBulkResponse,
            )
        )

    def get_line_management_data_geographic_area_to_regions_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaToRegionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the geographic Area to Region object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreaToRegions/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaToRegionResponse,
            )
        )

    def get_line_management_data_geographic_area_to_regions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaToRegionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreaToRegions",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaToRegionBulkResponse,
            )
        )

    def get_line_management_data_geographic_area_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the geographic AreaType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreaTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaTypeResponse,
            )
        )

    def get_line_management_data_geographic_area_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographicAreaTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographicAreaTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographicAreaTypeBulkResponse,
            )
        )

    def get_line_management_data_geography_regions_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographyRegionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the geographyRegion object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographyRegions/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographyRegionResponse,
            )
        )

    def get_line_management_data_geography_regions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeographyRegionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/geographyRegions",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GeographyRegionBulkResponse,
            )
        )

    def get_line_management_data_global_category_core_focuses_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GlobalCategoryCoreFocusResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the globalCategoryCoreFocus object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/globalCategoryCoreFocuses/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GlobalCategoryCoreFocusResponse,
            )
        )

    def get_line_management_data_global_category_core_focuses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GlobalCategoryCoreFocusBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/globalCategoryCoreFocuses",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GlobalCategoryCoreFocusBulkResponse,
            )
        )

    def get_line_management_data_global_category_summaries_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GlobalCategorySummaryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the globalCategorySummary object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/globalCategorySummaries/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GlobalCategorySummaryResponse,
            )
        )

    def get_line_management_data_global_category_summaries(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GlobalCategorySummaryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/globalCategorySummaries",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GlobalCategorySummaryBulkResponse,
            )
        )

    def get_line_management_data_gtin_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GTINTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the GTIN Type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/GTINTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GTINTypeResponse,
            )
        )

    def get_line_management_data_gtin_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GTINTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/GTINTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.GTINTypeBulkResponse,
            )
        )

    def get_line_management_data_iso_countries_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOCountryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the ISOCountries object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOCountries/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOCountryResponse,
            )
        )

    def get_line_management_data_iso_countries(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOCountryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOCountries",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOCountryBulkResponse,
            )
        )

    def get_line_management_data_iso_languages_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOLanguageResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the language object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOLanguages/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOLanguageResponse,
            )
        )

    def get_line_management_data_iso_languages(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOLanguageBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOLanguages",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOLanguageBulkResponse,
            )
        )

    def get_line_management_data_iso_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the ISOMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOMeasurements/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementResponse,
            )
        )

    def get_line_management_data_iso_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/ISOMeasurements",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementBulkResponse,
            )
        )

    def get_line_management_data_uomiso_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Unit of Measure ISOMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/UOMISOMeasurements/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementResponse,
            )
        )

    def get_line_management_data_uomiso_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/UOMISOMeasurements",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementBulkResponse,
            )
        )

    def get_line_management_data_muomiso_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Material Unit of Measure
          ISOMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/MUOMISOMeasurements/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementResponse,
            )
        )

    def get_line_management_data_muomiso_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/MUOMISOMeasurements",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementBulkResponse,
            )
        )

    def get_line_management_data_duomiso_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Delivery Unit of Measure
          ISOMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/DUOMISOMeasurements/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementResponse,
            )
        )

    def get_line_management_data_duomiso_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ISOMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/DUOMISOMeasurements",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ISOMeasurementBulkResponse,
            )
        )

    def get_line_management_data_launches_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaunchResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the launch object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/launches/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LaunchResponse,
            )
        )

    def get_line_management_data_launches(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaunchBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/launches",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LaunchBulkResponse,
            )
        )

    def get_line_management_data_leagues_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LeagueResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the league object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/leagues/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LeagueResponse,
            )
        )

    def get_line_management_data_leagues(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LeagueBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/leagues",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LeagueBulkResponse,
            )
        )

    def get_line_management_data_line_evolutions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LineEvolutionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the lineEvolution object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/lineEvolutions/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LineEvolutionResponse,
            )
        )

    def get_line_management_data_line_evolutions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LineEvolutionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/lineEvolutions",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.LineEvolutionBulkResponse,
            )
        )

    def get_line_management_data_marketing_initiatives_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MarketingInitiativeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the marketingInitiative object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/marketingInitiatives/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MarketingInitiativeResponse,
            )
        )

    def get_line_management_data_marketing_initiatives(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MarketingInitiativeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/marketingInitiatives",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MarketingInitiativeBulkResponse,
            )
        )

    def get_line_management_data_marketing_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MarketingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the marketingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/marketingTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MarketingTypeResponse,
            )
        )

    def get_line_management_data_marketing_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MarketingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/marketingTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MarketingTypeBulkResponse,
            )
        )

    def get_line_management_data_master_sizes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the masterSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeResponse,
            )
        )

    def get_line_management_data_master_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeBulkResponse,
            )
        )

    def get_line_management_data_master_size_grids_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeGridResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the masterSizeGrid object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizeGrids/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeGridResponse,
            )
        )

    def get_line_management_data_master_size_grids(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeGridBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizeGrids",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeGridBulkResponse,
            )
        )

    def get_line_management_data_master_size_translations_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeTranslationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Master Size Translation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizeTranslations/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeTranslationResponse,
            )
        )

    def get_line_management_data_master_size_translations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MasterSizeTranslationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/masterSizeTranslations",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MasterSizeTranslationBulkResponse,
            )
        )

    def get_line_management_data_material_intents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialIntentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialIntent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/materialIntents/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MaterialIntentResponse,
            )
        )

    def get_line_management_data_material_intents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialIntentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/materialIntents",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MaterialIntentBulkResponse,
            )
        )

    def get_line_management_data_merchandising_classifications_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MerchandisingClassificationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the merchandisingClassification object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/merchandisingClassifications/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MerchandisingClassificationResponse,
            )
        )

    def get_line_management_data_merchandising_classifications(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MerchandisingClassificationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/merchandisingClassifications",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.MerchandisingClassificationBulkResponse,
            )
        )

    def get_line_management_data_model_groups_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelGroupResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the modelGroup object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelGroups/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelGroupResponse,
            )
        )

    def get_line_management_data_model_groups(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelGroupBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelGroups",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelGroupBulkResponse,
            )
        )

    def get_line_management_data_model_group_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelGroupTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the modelGroupType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelGroupTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelGroupTypeResponse,
            )
        )

    def get_line_management_data_model_group_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelGroupTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelGroupTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelGroupTypeBulkResponse,
            )
        )

    def get_line_management_data_model_offering_groups_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelOfferingGroupResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the modelOfferingGroup object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelOfferingGroups/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelOfferingGroupResponse,
            )
        )

    def get_line_management_data_model_offering_groups(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelOfferingGroupBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelOfferingGroups",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelOfferingGroupBulkResponse,
            )
        )

    def get_line_management_data_model_offering_group_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelOfferingGroupTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the modelOfferingGroupType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelOfferingGroupTypes/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelOfferingGroupTypeResponse,
            )
        )

    def get_line_management_data_model_offering_group_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ModelOfferingGroupTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/modelOfferingGroupTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ModelOfferingGroupTypeBulkResponse,
            )
        )

    def get_line_management_data_platforms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PlatformResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the platform object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/platforms/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PlatformResponse,
            )
        )

    def get_line_management_data_platforms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PlatformBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/platforms",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PlatformBulkResponse,
            )
        )

    def get_line_management_data_price_list_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceListTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the priceListTypes object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/priceListTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PriceListTypeResponse,
            )
        )

    def get_line_management_data_price_list_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceListTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/priceListTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PriceListTypeBulkResponse,
            )
        )

    def get_line_management_data_price_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the priceType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/priceTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PriceTypeResponse,
            )
        )

    def get_line_management_data_price_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/priceTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.PriceTypeBulkResponse,
            )
        )

    def get_line_management_data_product_accounts_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductAccountResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productAccount object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productAccounts/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductAccountResponse,
            )
        )

    def get_line_management_data_product_accounts(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductAccountBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productAccounts",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductAccountBulkResponse,
            )
        )

    def get_line_management_data_product_companies_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductCompanyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productCompany object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productCompanies/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductCompanyResponse,
            )
        )

    def get_line_management_data_product_companies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductCompanyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productCompanies",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductCompanyBulkResponse,
            )
        )

    def get_line_management_data_product_creation_initiators_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductCreationInitiatorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productCreationInitiator object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productCreationInitiators/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductCreationInitiatorResponse,
            )
        )

    def get_line_management_data_product_creation_initiators(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductCreationInitiatorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productCreationInitiators",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductCreationInitiatorBulkResponse,
            )
        )

    def get_line_management_data_product_lifecycles_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductLifecycleResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productLifecycle object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productLifecycles/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductLifecycleResponse,
            )
        )

    def get_line_management_data_product_lifecycles(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductLifecycleBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productLifecycles",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductLifecycleBulkResponse,
            )
        )

    def get_supply_chain_enablement_data_product_refill_classes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductRefillClassResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Refill class object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/productRefillClasses/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductRefillClassResponse,
            )
        )

    def get_supply_chain_enablement_data_product_refill_classes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductRefillClassBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/productRefillClasses",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductRefillClassBulkResponse,
            )
        )

    def get_line_management_data_product_tiers_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductTierResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productTier object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productTiers/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductTierResponse,
            )
        )

    def get_line_management_data_product_tiers(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductTierBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productTiers",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.ProductTierBulkResponse,
            )
        )

    def get_line_management_data_region_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.RegionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the regionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/regionTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.RegionTypeResponse,
            )
        )

    def get_line_management_data_region_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.RegionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/regionTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.RegionTypeBulkResponse,
            )
        )

    def get_supply_chain_enablement_data_sales_organizations_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SalesOrganizationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Sales Organization object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/salesOrganizations/{objectId}".format(**{  # noqa
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SalesOrganizationResponse,
            )
        )

    def get_supply_chain_enablement_data_sales_organizations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SalesOrganizationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/salesOrganizations",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SalesOrganizationBulkResponse,
            )
        )

    def get_line_management_data_samples_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SampleResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sample object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/samples/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SampleResponse,
            )
        )

    def get_line_management_data_samples(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SampleBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/samples",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SampleBulkResponse,
            )
        )

    def get_line_management_data_sample_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SampleTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sampleType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sampleTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SampleTypeResponse,
            )
        )

    def get_line_management_data_sample_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SampleTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sampleTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SampleTypeBulkResponse,
            )
        )

    def get_line_management_data_segments_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SegmentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the segment object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/segments/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SegmentResponse,
            )
        )

    def get_line_management_data_segments(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SegmentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/segments",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SegmentBulkResponse,
            )
        )

    def get_line_management_data_silhouettes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SilhouetteResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the silhouette object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silhouettes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SilhouetteResponse,
            )
        )

    def get_line_management_data_silhouettes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SilhouetteBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silhouettes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SilhouetteBulkResponse,
            )
        )

    def get_line_management_data_silhouette_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SilhouetteTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the silhouetteType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silhouetteTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SilhouetteTypeResponse,
            )
        )

    def get_line_management_data_silhouette_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SilhouetteTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silhouetteTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SilhouetteTypeBulkResponse,
            )
        )

    def get_line_management_data_silos_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SiloResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the silo object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silos/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SiloResponse,
            )
        )

    def get_line_management_data_silos(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SiloBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/silos",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SiloBulkResponse,
            )
        )

    def get_line_management_data_special_offering_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialOfferingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the specialOfferingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/specialOfferingTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SpecialOfferingTypeResponse,
            )
        )

    def get_line_management_data_special_offering_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialOfferingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/specialOfferingTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SpecialOfferingTypeBulkResponse,
            )
        )

    def get_line_management_data_sport_activities_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SportActivityResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sportActivity object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sportActivities/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SportActivityResponse,
            )
        )

    def get_line_management_data_sport_activities(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SportActivityBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sportActivities",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SportActivityBulkResponse,
            )
        )

    def get_line_management_data_sport_levels_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SportLevelResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sportLevel object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sportLevels/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SportLevelResponse,
            )
        )

    def get_line_management_data_sport_levels(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SportLevelBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/sportLevels",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SportLevelBulkResponse,
            )
        )

    def get_line_management_data_style_group_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StyleGroupTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the styleGroupType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/styleGroupTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.StyleGroupTypeResponse,
            )
        )

    def get_line_management_data_style_group_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StyleGroupTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/styleGroupTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.StyleGroupTypeBulkResponse,
            )
        )

    def get_line_management_data_sub_brands_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubBrandResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the subBrand object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/subBrands/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SubBrandResponse,
            )
        )

    def get_line_management_data_sub_brands(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubBrandBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/subBrands",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SubBrandBulkResponse,
            )
        )

    def get_line_management_data_sub_categories_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubCategoryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the subCategory object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/subCategories/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SubCategoryResponse,
            )
        )

    def get_line_management_data_sub_categories(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubCategoryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/subCategories",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.SubCategoryBulkResponse,
            )
        )

    def get_line_management_data_teams_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TeamResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the team object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/teams/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TeamResponse,
            )
        )

    def get_line_management_data_teams(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TeamBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/teams",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TeamBulkResponse,
            )
        )

    def get_line_management_data_technologies_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TechnologyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the technology object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/technologies/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TechnologyResponse,
            )
        )

    def get_line_management_data_technologies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TechnologyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/technologies",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TechnologyBulkResponse,
            )
        )

    def get_line_management_data_type_groups_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TypeGroupResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the typeGroup object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/typeGroups/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TypeGroupResponse,
            )
        )

    def get_line_management_data_type_groups(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TypeGroupBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/typeGroups",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.TypeGroupBulkResponse,
            )
        )

    def get_line_management_data_uniform_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UniformTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the uniformType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/uniformTypes/{objectId}".format(**{
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
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.UniformTypeResponse,
            )
        )

    def get_line_management_data_uniform_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UniformTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/uniformTypes",
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                reference_model.UniformTypeBulkResponse,
            )
        )
