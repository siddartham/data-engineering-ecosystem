import oapi
import sob
import typing
from . import reference_model
from ..abc.client import Client
from ..config import TOKEN_URL_PROD
from logging import Logger
from nike.cerberus_assistant.config import CERBERUS_URL
from nike.cerberus_assistant.decorate import apply_cerberus_path_arguments


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
            "https://productdevelopment.api-product.pes-prod.nike.com/v1/productDevelopment/data"  # noqa
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

    def get_bill_of_materials_unit_of_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BillOfMaterialsUnitOfMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the BOM UOM object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/billOfMaterialsUnitOfMeasurements/{objectId}".format(**{
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
                reference_model.BillOfMaterialsUnitOfMeasurementResponse,
            )
        )

    def get_bill_of_materials_unit_of_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BillOfMaterialsUnitOfMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/billOfMaterialsUnitOfMeasurements",
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
                reference_model.BillOfMaterialsUnitOfMeasurementBulkResponse,
            )
        )

    def get_bill_of_materials_sections_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BillOfMaterialsSectionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the billOfMaterialsSection object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/billOfMaterialsSections/{objectId}".format(**{
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
                reference_model.BillOfMaterialsSectionResponse,
            )
        )

    def get_bill_of_materials_sections(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BillOfMaterialsSectionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/billOfMaterialsSections",
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
                reference_model.BillOfMaterialsSectionBulkResponse,
            )
        )

    def get_development_colorway_gates_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayGateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentColorwayGate object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayGates/{objectId}".format(**{
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
                reference_model.DevelopmentColorwayGateResponse,
            )
        )

    def get_development_colorway_gates(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayGateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayGates",
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
                reference_model.DevelopmentColorwayGateBulkResponse,
            )
        )

    def get_development_colorway_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentColorwayState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayStates/{objectId}".format(**{
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
                reference_model.DevelopmentColorwayStateResponse,
            )
        )

    def get_development_colorway_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayStates",
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
                reference_model.DevelopmentColorwayStateBulkResponse,
            )
        )

    def get_development_colorway_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentColorwayType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayTypes/{objectId}".format(**{
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
                reference_model.DevelopmentColorwayTypeResponse,
            )
        )

    def get_development_colorway_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentColorwayTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentColorwayTypes",
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
                reference_model.DevelopmentColorwayTypeBulkResponse,
            )
        )

    def get_development_sample_change_request_reasons_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleChangeRequestReasonResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Change Request
          Reason object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleChangeRequestReasons/{objectId}".format(**{
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
                reference_model.DevelopmentSampleChangeRequestReasonResponse,
            )
        )

    def get_development_sample_change_request_reasons(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleChangeRequestReasonBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleChangeRequestReasons",
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
                reference_model.DevelopmentSampleChangeRequestReasonBulkResponse,  # noqa
            )
        )

    def get_development_sample_evaluation_states_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleEvaluationStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Evaluation State
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleEvaluationStates/{objectId}".format(**{
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
                reference_model.DevelopmentSampleEvaluationStateResponse,
            )
        )

    def get_development_sample_evaluation_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleEvaluationStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleEvaluationStates",
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
                reference_model.DevelopmentSampleEvaluationStateBulkResponse,
            )
        )

    def get_development_sample_fabric_instructions_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleFabricInstructionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Fabric Instruction
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleFabricInstructions/{objectId}".format(**{
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
                reference_model.DevelopmentSampleFabricInstructionResponse,
            )
        )

    def get_development_sample_fabric_instructions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleFabricInstructionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleFabricInstructions",
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
                reference_model.DevelopmentSampleFabricInstructionBulkResponse,
            )
        )

    def get_development_sample_formats_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleFormatResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Format object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleFormats/{objectId}".format(**{
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
                reference_model.DevelopmentSampleFormatResponse,
            )
        )

    def get_development_sample_formats(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleFormatBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleFormats",
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
                reference_model.DevelopmentSampleFormatBulkResponse,
            )
        )

    def get_development_sample_purposes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSamplePurposeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Purpose object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSamplePurposes/{objectId}".format(**{
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
                reference_model.DevelopmentSamplePurposeResponse,
            )
        )

    def get_development_sample_purpose(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSamplePurposeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSamplePurpose",
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
                reference_model.DevelopmentSamplePurposeBulkResponse,
            )
        )

    def get_development_sample_quote_requirements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleQuoteRequirementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Quote Requirement
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleQuoteRequirements/{objectId}".format(**{
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
                reference_model.DevelopmentSampleQuoteRequirementResponse,
            )
        )

    def get_development_sample_quote_requirements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleQuoteRequirementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleQuoteRequirements",
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
                reference_model.DevelopmentSampleQuoteRequirementBulkResponse,
            )
        )

    def get_development_sample_states_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample State object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleStates/{objectId}".format(**{
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
                reference_model.DevelopmentSampleStateResponse,
            )
        )

    def get_development_sample_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleStates",
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
                reference_model.DevelopmentSampleStateBulkResponse,
            )
        )

    def get_development_sample_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Development Sample Type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleTypes/{objectId}".format(**{
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
                reference_model.DevelopmentSampleTypeResponse,
            )
        )

    def get_development_sample_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentSampleTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentSampleTypes",
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
                reference_model.DevelopmentSampleTypeBulkResponse,
            )
        )

    def get_development_style_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentStyleTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Dev Style Type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentStyleTypes/{objectId}".format(**{
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
                reference_model.DevelopmentStyleTypeResponse,
            )
        )

    def get_development_style_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentStyleTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentStyleTypes",
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
                reference_model.DevelopmentStyleTypeBulkResponse,
            )
        )

    def get_development_teams_object_id(
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
            "/developmentTeams/{objectId}".format(**{
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

    def get_development_teams(
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
            "/developmentTeams",
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

    def get_development_team_groups_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTeamGroupResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentTeamGroup object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentTeamGroups/{objectId}".format(**{
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
                reference_model.DevelopmentTeamGroupResponse,
            )
        )

    def get_development_team_groups(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTeamGroupBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentTeamGroups",
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
                reference_model.DevelopmentTeamGroupBulkResponse,
            )
        )

    def get_development_tracks_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTrackResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentTrack object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentTracks/{objectId}".format(**{
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
                reference_model.DevelopmentTrackResponse,
            )
        )

    def get_development_tracks(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentTrackBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/developmentTracks",
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
                reference_model.DevelopmentTrackBulkResponse,
            )
        )

    def get_goods_at_consolidator_reasons_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GoodsAtConsolidatorReasonResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Goods at Consolidator Reason object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/goodsAtConsolidatorReasons/{objectId}".format(**{
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
                reference_model.GoodsAtConsolidatorReasonResponse,
            )
        )

    def get_goods_at_consolidator_reasons(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GoodsAtConsolidatorReasonBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/goodsAtConsolidatorReasons",
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
                reference_model.GoodsAtConsolidatorReasonBulkResponse,
            )
        )

    def get_measurement_template_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MeasurementTemplateTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the measurementTemplateType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/measurementTemplateTypes/{objectId}".format(**{
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
                reference_model.MeasurementTemplateTypeResponse,
            )
        )

    def get_measurement_template_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MeasurementTemplateTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/measurementTemplateTypes",
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
                reference_model.MeasurementTemplateTypeBulkResponse,
            )
        )

    def get_nike_production_trials_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NikeProductionTrialResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nikeProductionTrial object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/nikeProductionTrials/{objectId}".format(**{
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
                reference_model.NikeProductionTrialResponse,
            )
        )

    def get_nike_production_trials(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NikeProductionTrialBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/nikeProductionTrials",
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
                reference_model.NikeProductionTrialBulkResponse,
            )
        )

    def get_part_names_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartNameResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the BOM Part Name object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partNames/{objectId}".format(**{
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
                reference_model.PartNameResponse,
            )
        )

    def get_part_names(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartNameBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partNames",
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
                reference_model.PartNameBulkResponse,
            )
        )

    def get_part_modifiers_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartModifierResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partModifier object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partModifiers/{objectId}".format(**{
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
                reference_model.PartModifierResponse,
            )
        )

    def get_part_modifiers(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartModifierBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partModifiers",
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
                reference_model.PartModifierBulkResponse,
            )
        )

    def get_part_prefixes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartPrefixResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partPrefix object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partPrefixes/{objectId}".format(**{
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
                reference_model.PartPrefixResponse,
            )
        )

    def get_part_prefixes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartPrefixBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partPrefixes",
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
                reference_model.PartPrefixBulkResponse,
            )
        )

    def get_part_primaries_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartPrimaryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partPrimary object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partPrimaries/{objectId}".format(**{
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
                reference_model.PartPrimaryResponse,
            )
        )

    def get_part_primaries(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartPrimaryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partPrimaries",
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
                reference_model.PartPrimaryBulkResponse,
            )
        )

    def get_part_secondaries_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartSecondaryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partSecondary object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partSecondaries/{objectId}".format(**{
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
                reference_model.PartSecondaryResponse,
            )
        )

    def get_part_secondaries(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartSecondaryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partSecondaries",
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
                reference_model.PartSecondaryBulkResponse,
            )
        )

    def get_part_suffixes_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartSuffixResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partSuffix object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partSuffixes/{objectId}".format(**{
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
                reference_model.PartSuffixResponse,
            )
        )

    def get_part_suffixes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartSuffixBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/partSuffixes",
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
                reference_model.PartSuffixBulkResponse,
            )
        )

    def get_point_of_measurement_criticalities_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PointOfMeasurementCriticalityResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the pointOfMeasurementCriticality object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/pointOfMeasurementCriticalities/{objectId}".format(**{
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
                reference_model.PointOfMeasurementCriticalityResponse,
            )
        )

    def get_point_of_measurement_criticalities(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PointOfMeasurementCriticalityBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/pointOfMeasurementCriticalities",
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
                reference_model.PointOfMeasurementCriticalityBulkResponse,
            )
        )

    def get_product_tracks_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductTrackResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the productTrack object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/productTracks/{objectId}".format(**{
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
                reference_model.ProductTrackResponse,
            )
        )

    def get_product_tracks(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductTrackBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/productTracks",
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
                reference_model.ProductTrackBulkResponse,
            )
        )

    def get_shipping_services_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingServiceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Shipping Service object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/shippingServices/{objectId}".format(**{
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
                reference_model.ShippingServiceResponse,
            )
        )

    def get_shipping_services(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingServiceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/shippingServices",
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
                reference_model.ShippingServiceBulkResponse,
            )
        )

    def get_technical_difficulties_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TechnicalDifficultyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the technicalDifficulty object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/technicalDifficulties/{objectId}".format(**{
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
                reference_model.TechnicalDifficultyResponse,
            )
        )

    def get_technical_difficulties(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TechnicalDifficultyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/technicalDifficulties",
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
                reference_model.TechnicalDifficultyBulkResponse,
            )
        )

    def get_measurement_set_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MeasurementSetStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the measurementSetState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/measurementSetStates/{objectId}".format(**{
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
                reference_model.MeasurementSetStateResponse,
            )
        )

    def get_measurement_set_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MeasurementSetStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/measurementSetStates",
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
                reference_model.MeasurementSetStateBulkResponse,
            )
        )
