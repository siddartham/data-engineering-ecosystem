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
            "https://materialmanagement.api-product.pes-prod.nike.com/v3"
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

    def get_material_management_data_alternate_product_part_content_statements_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AlternateProductPartContentStatementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Alternate Product Part Content
          Statement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/alternateProductPartContentStatements/{objectId}".format(**{  # noqa
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
                reference_model.AlternateProductPartContentStatementResponse,
            )
        )

    def get_material_management_data_alternate_product_part_content_statements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AlternateProductPartContentStatementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/alternateProductPartContentStatements",
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
                reference_model.AlternateProductPartContentStatementBulkResponse,  # noqa
            )
        )

    def get_material_management_data_airbag_processes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AirbagProcessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the airbagProcess object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/airbagProcesses/{objectId}".format(**{
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
                reference_model.AirbagProcessResponse,
            )
        )

    def get_material_management_data_airbag_processes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AirbagProcessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/airbagProcesses",
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
                reference_model.AirbagProcessBulkResponse,
            )
        )

    def get_material_management_data_animal_sources_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AnimalSourceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the animalSource object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/animalSources/{objectId}".format(**{
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
                reference_model.AnimalSourceResponse,
            )
        )

    def get_material_management_data_animal_sources(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AnimalSourceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/animalSources",
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
                reference_model.AnimalSourceBulkResponse,
            )
        )

    def get_material_management_data_application_locations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ApplicationLocationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the applicationLocation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/applicationLocations/{objectId}".format(**{  # noqa
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
                reference_model.ApplicationLocationResponse,
            )
        )

    def get_material_management_data_application_locations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ApplicationLocationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/applicationLocations",
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
                reference_model.ApplicationLocationBulkResponse,
            )
        )

    def get_material_management_data_application_techniques_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ApplicationTechniqueResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the applicationTechnique object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/applicationTechniques/{objectId}".format(**{  # noqa
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
                reference_model.ApplicationTechniqueResponse,
            )
        )

    def get_material_management_data_application_techniques(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ApplicationTechniqueBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/applicationTechniques",
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
                reference_model.ApplicationTechniqueBulkResponse,
            )
        )

    def get_material_management_data_artwork_graphic_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ArtworkGraphicTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the artworkGraphicType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkGraphicTypes/{objectId}".format(**{  # noqa
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
                reference_model.ArtworkGraphicTypeResponse,
            )
        )

    def get_material_management_data_artwork_graphic_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ArtworkGraphicTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkGraphicTypes",
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
                reference_model.ArtworkGraphicTypeBulkResponse,
            )
        )

    def get_material_management_data_artwork_techniques_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ArtworkTechniqueResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the artworkTechnique object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkTechniques/{objectId}".format(**{
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
                reference_model.ArtworkTechniqueResponse,
            )
        )

    def get_material_management_data_artwork_techniques(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ArtworkTechniqueBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/artworkTechniques",
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
                reference_model.ArtworkTechniqueBulkResponse,
            )
        )

    def get_material_management_data_attachment_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AttachmentMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the attachmentMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/attachmentMethods/{objectId}".format(**{
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
                reference_model.AttachmentMethodResponse,
            )
        )

    def get_material_management_data_attachment_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.AttachmentMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/attachmentMethods",
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
                reference_model.AttachmentMethodBulkResponse,
            )
        )

    def get_material_management_data_bobbin_positions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BobbinPositionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the bobbinPositions object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/bobbinPositions/{objectId}".format(**{
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
                reference_model.BobbinPositionResponse,
            )
        )

    def get_material_management_data_bobbin_positions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BobbinPositionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/bobbinPositions",
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
                reference_model.BobbinPositionBulkResponse,
            )
        )

    def get_material_management_data_brand_names_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BrandNameResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the brandName object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/brandNames/{objectId}".format(**{
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
                reference_model.BrandNameResponse,
            )
        )

    def get_material_management_data_brand_names(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.BrandNameBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/brandNames",
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
                reference_model.BrandNameBulkResponse,
            )
        )

    def get_material_management_data_care_instructions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CareInstructionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the careInstruction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/careInstructions/{objectId}".format(**{
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
                reference_model.CareInstructionResponse,
            )
        )

    def get_material_management_data_care_instructions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CareInstructionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/careInstructions",
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
                reference_model.CareInstructionBulkResponse,
            )
        )

    def get_material_management_data_coating_surface_applications_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoatingSurfaceApplicationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the coatingSurfaceApplication object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coatingSurfaceApplications/{objectId}".format(**{  # noqa
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
                reference_model.CoatingSurfaceApplicationResponse,
            )
        )

    def get_material_management_data_coating_surface_applications(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoatingSurfaceApplicationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coatingSurfaceApplications",
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
                reference_model.CoatingSurfaceApplicationBulkResponse,
            )
        )

    def get_material_management_data_coating_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoatingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the coatingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coatingTypes/{objectId}".format(**{
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
                reference_model.CoatingTypeResponse,
            )
        )

    def get_material_management_data_coating_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoatingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coatingTypes",
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
                reference_model.CoatingTypeBulkResponse,
            )
        )

    def get_material_management_data_chemical_polymer_forms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ChemicalPolymerFormResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the chemicalPolymerForm object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/chemicalPolymerForms/{objectId}".format(**{  # noqa
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
                reference_model.ChemicalPolymerFormResponse,
            )
        )

    def get_material_management_data_chemical_polymer_forms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ChemicalPolymerFormBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/chemicalPolymerForms",
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
                reference_model.ChemicalPolymerFormBulkResponse,
            )
        )

    def get_material_management_data_chemical_polymer_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ChemicalPolymerTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the chemicalPolymerType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/chemicalPolymerTypes/{objectId}".format(**{  # noqa
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
                reference_model.ChemicalPolymerTypeResponse,
            )
        )

    def get_material_management_data_chemical_polymer_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ChemicalPolymerTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/chemicalPolymerTypes",
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
                reference_model.ChemicalPolymerTypeBulkResponse,
            )
        )

    def get_material_management_data_colorations_available_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorationAvailableResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the colorationAvailable object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorationsAvailable/{objectId}".format(**{  # noqa
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
                reference_model.ColorationAvailableResponse,
            )
        )

    def get_material_management_data_colorations_available(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorationAvailableBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorationsAvailable",
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
                reference_model.ColorationAvailableBulkResponse,
            )
        )

    def get_material_management_data_color_callouts_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorCalloutResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the colorCallout object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorCallouts/{objectId}".format(**{
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
                reference_model.ColorCalloutResponse,
            )
        )

    def get_material_management_data_color_callouts(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorCalloutBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorCallouts",
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
                reference_model.ColorCalloutBulkResponse,
            )
        )

    def get_material_management_data_color_dominances_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorDominanceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the colorDominance object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorDominances/{objectId}".format(**{
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
                reference_model.ColorDominanceResponse,
            )
        )

    def get_material_management_data_color_dominances(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorDominanceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorDominances",
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
                reference_model.ColorDominanceBulkResponse,
            )
        )

    def get_material_management_data_color_effects_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorEffectResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the color Effect object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorEffects/{objectId}".format(**{
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
                reference_model.ColorEffectResponse,
            )
        )

    def get_material_management_data_color_effects(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorEffectBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorEffects",
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
                reference_model.ColorEffectBulkResponse,
            )
        )

    def get_material_management_data_color_positions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorPositionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the color Position object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorPositions/{objectId}".format(**{
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
                reference_model.ColorPositionResponse,
            )
        )

    def get_material_management_data_color_positions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ColorPositionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/colorPositions",
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
                reference_model.ColorPositionBulkResponse,
            )
        )

    def get_material_management_data_component_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentConstructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentConstructionTypes/{objectId}".format(**{  # noqa
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
                reference_model.ComponentConstructionTypeResponse,
            )
        )

    def get_material_management_data_component_construction_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentConstructionTypes",
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
                reference_model.ComponentConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_component_forms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentFormResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentForm object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentForms/{objectId}".format(**{
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
                reference_model.ComponentFormResponse,
            )
        )

    def get_material_management_data_component_forms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentFormBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentForms",
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
                reference_model.ComponentFormBulkResponse,
            )
        )

    def get_material_management_data_component_general_constructions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentGeneralConstructionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentGeneralConstruction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentGeneralConstructions/{objectId}".format(**{  # noqa
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
                reference_model.ComponentGeneralConstructionResponse,
            )
        )

    def get_material_management_data_component_general_constructions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentGeneralConstructionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentGeneralConstructions",
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
                reference_model.ComponentGeneralConstructionBulkResponse,
            )
        )

    def get_material_management_data_component_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentTypes/{objectId}".format(**{
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
                reference_model.ComponentTypeResponse,
            )
        )

    def get_material_management_data_component_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentTypes",
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
                reference_model.ComponentTypeBulkResponse,
            )
        )

    def get_material_management_data_component_types_one_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentTypeOneResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentTypeOne object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentTypesOne/{objectId}".format(**{
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
                reference_model.ComponentTypeOneResponse,
            )
        )

    def get_material_management_data_component_types_one(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentTypeOneBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentTypesOne",
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
                reference_model.ComponentTypeOneBulkResponse,
            )
        )

    def get_material_management_data_component_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the componentVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentVariations/{objectId}".format(**{  # noqa
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
                reference_model.ComponentVariationResponse,
            )
        )

    def get_material_management_data_component_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ComponentVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/componentVariations",
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
                reference_model.ComponentVariationBulkResponse,
            )
        )

    def get_material_management_data_consideration_and_risks_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsiderationAndRiskResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Consideration And Risks object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/considerationAndRisks/{objectId}".format(**{  # noqa
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
                reference_model.ConsiderationAndRiskResponse,
            )
        )

    def get_material_management_data_consideration_and_risks(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConsiderationAndRiskBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/considerationAndRisks",
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
                reference_model.ConsiderationAndRiskBulkResponse,
            )
        )

    def get_material_management_data_construction_methods_object_id(
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
            "/materialManagement/data/constructionMethods/{objectId}".format(**{  # noqa
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

    def get_material_management_data_construction_methods(
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
            "/materialManagement/data/constructionMethods",
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

    def get_material_management_data_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the constructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/constructionTypes/{objectId}".format(**{
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
                reference_model.ConstructionTypeResponse,
            )
        )

    def get_material_management_data_construction_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/constructionTypes",
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
                reference_model.ConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_content_sources_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ContentSourceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the contentSource object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/contentSources/{objectId}".format(**{
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
                reference_model.ContentSourceResponse,
            )
        )

    def get_material_management_data_content_sources(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ContentSourceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/contentSources",
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
                reference_model.ContentSourceBulkResponse,
            )
        )

    def get_material_management_data_content_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ContentTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the contentType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/contentTypes/{objectId}".format(**{
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
                reference_model.ContentTypeResponse,
            )
        )

    def get_material_management_data_content_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ContentTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/contentTypes",
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
                reference_model.ContentTypeBulkResponse,
            )
        )

    def get_material_management_data_cores_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the core object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cores/{objectId}".format(**{
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
                reference_model.CoreResponse,
            )
        )

    def get_material_management_data_cores(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cores",
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
                reference_model.CoreBulkResponse,
            )
        )

    def get_material_management_data_core_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the coreConstructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coreConstructionTypes/{objectId}".format(**{  # noqa
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
                reference_model.CoreConstructionTypeResponse,
            )
        )

    def get_material_management_data_core_construction_type(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coreConstructionType",
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
                reference_model.CoreConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_core_measurement_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreMeasurementTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the coreMeasurementType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coreMeasurementTypes/{objectId}".format(**{  # noqa
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
                reference_model.CoreMeasurementTypeResponse,
            )
        )

    def get_material_management_data_core_measurement_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CoreMeasurementTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/coreMeasurementTypes",
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
                reference_model.CoreMeasurementTypeBulkResponse,
            )
        )

    def get_material_management_data_counter_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CounterTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the counterType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/counterTypes/{objectId}".format(**{
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
                reference_model.CounterTypeResponse,
            )
        )

    def get_material_management_data_counter_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CounterTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/counterTypes",
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
                reference_model.CounterTypeBulkResponse,
            )
        )

    def get_material_management_data_countries_of_origin_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CountryOfOriginResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the countryOfOrigin object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/countriesOfOrigin/{objectId}".format(**{
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
                reference_model.CountryOfOriginResponse,
            )
        )

    def get_material_management_data_countries_of_origin(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CountryOfOriginBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/countriesOfOrigin",
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
                reference_model.CountryOfOriginBulkResponse,
            )
        )

    def get_material_management_data_cure_processes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CureProcessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the cureProcess object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cureProcesses/{objectId}".format(**{
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
                reference_model.CureProcessResponse,
            )
        )

    def get_material_management_data_cure_processes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CureProcessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cureProcesses",
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
                reference_model.CureProcessBulkResponse,
            )
        )

    def get_material_management_data_cushioning_types_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CushioningTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the cushioningType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cushioningTypes/{objectId}".format(**{
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
                reference_model.CushioningTypeResponse,
            )
        )

    def get_material_management_data_currencies_object_id(
        self,
        object_id: str,
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
            "/materialManagement/data/currencies/{objectId}".format(**{
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

    def get_material_management_data_currencies(
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
            "/materialManagement/data/currencies",
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

    def get_material_management_data_customs_descriptions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CustomsDescriptionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the customsDescription object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/customsDescriptions/{objectId}".format(**{  # noqa
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
                reference_model.CustomsDescriptionResponse,
            )
        )

    def get_material_management_data_customs_descriptions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CustomsDescriptionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/customsDescriptions",
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
                reference_model.CustomsDescriptionBulkResponse,
            )
        )

    def get_material_management_data_custom_stops_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CustomStopResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the customStop object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/customStops/{objectId}".format(**{
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
                reference_model.CustomStopResponse,
            )
        )

    def get_material_management_data_custom_stops(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CustomStopBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/customStops",
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
                reference_model.CustomStopBulkResponse,
            )
        )

    def get_material_procurement_data_delivery_terms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DeliveryTermsResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the deliveryTerms object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/deliveryTerms/{objectId}".format(**{
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
                reference_model.DeliveryTermsResponse,
            )
        )

    def get_material_procurement_data_delivery_terms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DeliveryTermsBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/deliveryTerms",
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
                reference_model.DeliveryTermsBulkResponse,
            )
        )

    def get_material_management_data_development_reasons_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentReasonResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the developmentReason object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/developmentReasons/{objectId}".format(**{
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
                reference_model.DevelopmentReasonResponse,
            )
        )

    def get_material_management_data_development_reasons(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DevelopmentReasonBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/developmentReasons",
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
                reference_model.DevelopmentReasonBulkResponse,
            )
        )

    def get_material_management_data_dimension_width_indicators_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DimensionWidthIndicatorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the dimensionWidthIndicator object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dimensionWidthIndicators/{objectId}".format(**{  # noqa
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
                reference_model.DimensionWidthIndicatorResponse,
            )
        )

    def get_material_management_data_dimension_width_indicators(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DimensionWidthIndicatorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dimensionWidthIndicators",
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
                reference_model.DimensionWidthIndicatorBulkResponse,
            )
        )

    def get_material_management_data_down_cluster_statements_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DownClusterStatementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the downClusterStatement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/downClusterStatements/{objectId}".format(**{  # noqa
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
                reference_model.DownClusterStatementResponse,
            )
        )

    def get_material_management_data_down_cluster_statements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DownClusterStatementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/downClusterStatements",
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
                reference_model.DownClusterStatementBulkResponse,
            )
        )

    def get_material_management_data_down_colors_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DownColorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the downColor object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/downColors/{objectId}".format(**{
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
                reference_model.DownColorResponse,
            )
        )

    def get_material_management_data_down_colors(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DownColorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/downColors",
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
                reference_model.DownColorBulkResponse,
            )
        )

    def get_material_management_data_duties_and_compliance_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DutyAndComplianceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the dutyAndCompliance object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dutiesAndCompliance/{objectId}".format(**{  # noqa
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
                reference_model.DutyAndComplianceResponse,
            )
        )

    def get_material_management_data_duties_and_compliance(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DutyAndComplianceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dutiesAndCompliance",
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
                reference_model.DutyAndComplianceBulkResponse,
            )
        )

    def get_material_management_data_dye_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DyeMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the dyeMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dyeMethods/{objectId}".format(**{
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
                reference_model.DyeMethodResponse,
            )
        )

    def get_material_management_data_dye_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DyeMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dyeMethods",
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
                reference_model.DyeMethodBulkResponse,
            )
        )

    def get_material_management_data_dye_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DyeTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the dyeType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dyeTypes/{objectId}".format(**{
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
                reference_model.DyeTypeResponse,
            )
        )

    def get_material_management_data_dye_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.DyeTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/dyeTypes",
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
                reference_model.DyeTypeBulkResponse,
            )
        )

    def get_material_management_data_embellishment_techniques_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EmbellishmentTechniqueResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the embellishmentTechnique object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/embellishmentTechniques/{objectId}".format(**{  # noqa
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
                reference_model.EmbellishmentTechniqueResponse,
            )
        )

    def get_material_management_data_embellishment_techniques(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EmbellishmentTechniqueBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/embellishmentTechniques",
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
                reference_model.EmbellishmentTechniqueBulkResponse,
            )
        )

    def get_material_management_data_edge_end_finishes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EdgeEndFinishResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Edge End Finish object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/edgeEndFinishes/{objectId}".format(**{
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
                reference_model.EdgeEndFinishResponse,
            )
        )

    def get_material_management_data_edge_end_finish(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EdgeEndFinishBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/edgeEndFinish",
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
                reference_model.EdgeEndFinishBulkResponse,
            )
        )

    def get_material_management_data_emboss_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EmbossTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the embossType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/embossTypes/{objectId}".format(**{
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
                reference_model.EmbossTypeResponse,
            )
        )

    def get_material_management_data_emboss_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EmbossTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/embossTypes",
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
                reference_model.EmbossTypeBulkResponse,
            )
        )

    def get_material_management_data_entanglement_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EntanglementMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the entanglementMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/entanglementMethods/{objectId}".format(**{  # noqa
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
                reference_model.EntanglementMethodResponse,
            )
        )

    def get_material_management_data_entanglement_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EntanglementMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/entanglementMethods",
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
                reference_model.EntanglementMethodBulkResponse,
            )
        )

    def get_material_management_data_entanglement_bonding_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EntanglementBondingMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the entanglementBondingMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/entanglementBondingMethods/{objectId}".format(**{  # noqa
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
                reference_model.EntanglementBondingMethodResponse,
            )
        )

    def get_material_management_data_entanglement_bonding_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EntanglementBondingMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/entanglementBondingMethods",
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
                reference_model.EntanglementBondingMethodBulkResponse,
            )
        )

    def get_material_management_data_environmentally_preferred_materials_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EpmResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the epm object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/environmentallyPreferredMaterials/{objectId}".format(**{  # noqa
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
                reference_model.EpmResponse,
            )
        )

    def get_material_management_data_environmentally_preferred_materials(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.EpmBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/environmentallyPreferredMaterials",
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
                reference_model.EpmBulkResponse,
            )
        )

    def get_material_management_data_fancy_yarns_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FancyYarnResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fancyYarn object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fancyYarns/{objectId}".format(**{
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
                reference_model.FancyYarnResponse,
            )
        )

    def get_material_management_data_fancy_yarns(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FancyYarnBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fancyYarns",
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
                reference_model.FancyYarnBulkResponse,
            )
        )

    def get_material_management_data_feeders_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FeederResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the feeders object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/feeders/{objectId}".format(**{
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
                reference_model.FeederResponse,
            )
        )

    def get_material_management_data_feeders(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FeederBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/feeders",
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
                reference_model.FeederBulkResponse,
            )
        )

    def get_material_management_data_fiber_cross_sections_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberCrossSectionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fiberCrossSection object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberCrossSections/{objectId}".format(**{
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
                reference_model.FiberCrossSectionResponse,
            )
        )

    def get_material_management_data_fiber_cross_sections(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberCrossSectionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberCrossSections",
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
                reference_model.FiberCrossSectionBulkResponse,
            )
        )

    def get_material_management_data_fiber_diameter_units_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberDiameterUnitResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Fiber Diameter Unit object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberDiameterUnits/{objectId}".format(**{
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
                reference_model.FiberDiameterUnitResponse,
            )
        )

    def get_material_management_data_fiber_diameter_units(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberDiameterUnitBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberDiameterUnits",
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
                reference_model.FiberDiameterUnitBulkResponse,
            )
        )

    def get_material_management_data_fiber_orientations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberOrientationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fiberOrientation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberOrientations/{objectId}".format(**{
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
                reference_model.FiberOrientationResponse,
            )
        )

    def get_material_management_data_fiber_orientations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberOrientationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberOrientations",
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
                reference_model.FiberOrientationBulkResponse,
            )
        )

    def get_material_management_data_fiber_preparations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberPreparationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fiberPreparation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberPreparations/{objectId}".format(**{
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
                reference_model.FiberPreparationResponse,
            )
        )

    def get_material_management_data_fiber_preparations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberPreparationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberPreparations",
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
                reference_model.FiberPreparationBulkResponse,
            )
        )

    def get_material_management_data_fiber_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fiberType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberTypes/{objectId}".format(**{
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
                reference_model.FiberTypeResponse,
            )
        )

    def get_material_management_data_fiber_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FiberTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fiberTypes",
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
                reference_model.FiberTypeBulkResponse,
            )
        )

    def get_material_management_data_fill_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FillTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fillType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fillTypes/{objectId}".format(**{
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
                reference_model.FillTypeResponse,
            )
        )

    def get_material_management_data_fill_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FillTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fillTypes",
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
                reference_model.FillTypeBulkResponse,
            )
        )

    def get_material_management_data_finishing_locations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishingLocationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the finishingLocation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishingLocations/{objectId}".format(**{
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
                reference_model.FinishingLocationResponse,
            )
        )

    def get_material_management_data_finishing_locations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishingLocationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishingLocations",
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
                reference_model.FinishingLocationBulkResponse,
            )
        )

    def get_material_management_data_finish_processes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishProcessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the finishProcess object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishProcesses/{objectId}".format(**{
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
                reference_model.FinishProcessResponse,
            )
        )

    def get_material_management_data_finish_processes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishProcessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishProcesses",
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
                reference_model.FinishProcessBulkResponse,
            )
        )

    def get_material_management_data_finish_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the finishType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishTypes/{objectId}".format(**{
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
                reference_model.FinishTypeResponse,
            )
        )

    def get_material_management_data_finish_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FinishTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/finishTypes",
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
                reference_model.FinishTypeBulkResponse,
            )
        )

    def get_material_management_data_firmness_levels_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FirmnessLevelResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the firmnessLevel object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/firmnessLevels/{objectId}".format(**{
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
                reference_model.FirmnessLevelResponse,
            )
        )

    def get_material_management_data_firmness_levels(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FirmnessLevelBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/firmnessLevels",
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
                reference_model.FirmnessLevelBulkResponse,
            )
        )

    def get_material_management_data_fixed_colors_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FixedColorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the fixedColor object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fixedColors/{objectId}".format(**{
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
                reference_model.FixedColorResponse,
            )
        )

    def get_material_management_data_fixed_colors(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FixedColorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/fixedColors",
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
                reference_model.FixedColorBulkResponse,
            )
        )

    def get_material_management_data_flammability_ratings_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FlammabilityRatingResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the flammabilityRating object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/flammabilityRatings/{objectId}".format(**{  # noqa
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
                reference_model.FlammabilityRatingResponse,
            )
        )

    def get_material_management_data_flammability_ratings(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FlammabilityRatingBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/flammabilityRatings",
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
                reference_model.FlammabilityRatingBulkResponse,
            )
        )

    def get_material_management_data_fluting_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FlutingSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the flutingSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/flutingSizes/{objectId}".format(**{
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
                reference_model.FlutingSizeResponse,
            )
        )

    def get_material_management_data_fluting_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FlutingSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/flutingSizes",
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
                reference_model.FlutingSizeBulkResponse,
            )
        )

    def get_material_management_data_foam_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FoamTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the foamType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/foamTypes/{objectId}".format(**{
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
                reference_model.FoamTypeResponse,
            )
        )

    def get_material_management_data_foam_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FoamTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/foamTypes",
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
                reference_model.FoamTypeBulkResponse,
            )
        )

    def get_material_management_data_forms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FormResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the form object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/forms/{objectId}".format(**{
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
                reference_model.FormResponse,
            )
        )

    def get_material_management_data_forms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FormBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/forms",
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
                reference_model.FormBulkResponse,
            )
        )

    def get_material_management_data_fold_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FoldMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the foldMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/foldMethods/{objectId}".format(**{
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
                reference_model.FoldMethodResponse,
            )
        )

    def get_material_management_data_fold_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.FoldMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/foldMethods",
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
                reference_model.FoldMethodBulkResponse,
            )
        )

    def get_material_management_data_gas_contents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GasContentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the gasContent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/gasContents/{objectId}".format(**{
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
                reference_model.GasContentResponse,
            )
        )

    def get_material_management_data_gas_contents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GasContentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/gasContents",
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
                reference_model.GasContentBulkResponse,
            )
        )

    def get_material_management_data_general_constructions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeneralConstructionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the generalConstruction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/generalConstructions/{objectId}".format(**{  # noqa
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
                reference_model.GeneralConstructionResponse,
            )
        )

    def get_material_management_data_general_constructions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GeneralConstructionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/generalConstructions",
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
                reference_model.GeneralConstructionBulkResponse,
            )
        )

    def get_material_management_data_grain_leather_sub_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GrainLeatherSubTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the grainLeatherSubType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/grainLeatherSubTypes/{objectId}".format(**{  # noqa
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
                reference_model.GrainLeatherSubTypeResponse,
            )
        )

    def get_material_management_data_grain_leather_sub_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.GrainLeatherSubTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/grainLeatherSubTypes",
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
                reference_model.GrainLeatherSubTypeBulkResponse,
            )
        )

    def get_material_management_data_hard_or_soft_components_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HardOrSoftComponentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the hardOrSoftComponent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/hardOrSoftComponents/{objectId}".format(**{  # noqa
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
                reference_model.HardOrSoftComponentResponse,
            )
        )

    def get_material_management_data_hard_or_soft_components(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HardOrSoftComponentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/hardOrSoftComponents",
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
                reference_model.HardOrSoftComponentBulkResponse,
            )
        )

    def get_material_management_data_heat_sets_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HeatSetResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the heatSet object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/heatSets/{objectId}".format(**{
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
                reference_model.HeatSetResponse,
            )
        )

    def get_material_management_data_heat_sets(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HeatSetBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/heatSets",
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
                reference_model.HeatSetBulkResponse,
            )
        )

    def get_material_management_data_height_indicators_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HeightIndicatorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the heightIndicator object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/heightIndicators/{objectId}".format(**{
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
                reference_model.HeightIndicatorResponse,
            )
        )

    def get_material_management_data_height_indicators(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.HeightIndicatorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/heightIndicators",
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
                reference_model.HeightIndicatorBulkResponse,
            )
        )

    def get_material_management_data_insulation_padding_forms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingFormResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Insulation Padding Form object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingForms/{objectId}".format(**{  # noqa
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
                reference_model.InsulationPaddingFormResponse,
            )
        )

    def get_material_management_data_insulation_padding_forms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingFormBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingForms",
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
                reference_model.InsulationPaddingFormBulkResponse,
            )
        )

    def get_material_management_data_insulation_padding_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the insulationPaddingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingTypes/{objectId}".format(**{  # noqa
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
                reference_model.InsulationPaddingTypeResponse,
            )
        )

    def get_material_management_data_insulation_padding_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingTypes",
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
                reference_model.InsulationPaddingTypeBulkResponse,
            )
        )

    def get_material_management_data_insulation_padding_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the insulationPaddingVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingVariations/{objectId}".format(**{  # noqa
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
                reference_model.InsulationPaddingVariationResponse,
            )
        )

    def get_material_management_data_insulation_padding_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.InsulationPaddingVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/insulationPaddingVariations",
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
                reference_model.InsulationPaddingVariationBulkResponse,
            )
        )

    def get_material_management_data_intended_uses_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.IntendedUseResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the intendedUse object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/intendedUses/{objectId}".format(**{
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
                reference_model.IntendedUseResponse,
            )
        )

    def get_material_management_data_intended_uses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.IntendedUseBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/intendedUses",
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
                reference_model.IntendedUseBulkResponse,
            )
        )

    def get_material_management_data_knit_technologies_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.KnitTechnologiesResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the knitTechnologies object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/knitTechnologies/{objectId}".format(**{
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
                reference_model.KnitTechnologiesResponse,
            )
        )

    def get_material_management_data_knit_technologies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.KnitTechnologiesBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/knitTechnologies",
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
                reference_model.KnitTechnologiesBulkResponse,
            )
        )

    def get_material_management_data_lace_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaceConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the laceConstructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/laceConstructionTypes/{objectId}".format(**{  # noqa
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
                reference_model.LaceConstructionTypeResponse,
            )
        )

    def get_material_management_data_lace_construction_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaceConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/laceConstructionTypes",
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
                reference_model.LaceConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_lace_shapes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaceShapeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the laceShape object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/laceShapes/{objectId}".format(**{
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
                reference_model.LaceShapeResponse,
            )
        )

    def get_material_management_data_lace_shapes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LaceShapeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/laceShapes",
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
                reference_model.LaceShapeBulkResponse,
            )
        )

    def get_material_management_data_layer_locations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LayerLocationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the layerLocation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/layerLocations/{objectId}".format(**{
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
                reference_model.LayerLocationResponse,
            )
        )

    def get_material_management_data_layer_locations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LayerLocationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/layerLocations",
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
                reference_model.LayerLocationBulkResponse,
            )
        )

    def get_material_management_data_leather_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LeatherTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the leatherType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/leatherTypes/{objectId}".format(**{
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
                reference_model.LeatherTypeResponse,
            )
        )

    def get_material_management_data_leather_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LeatherTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/leatherTypes",
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
                reference_model.LeatherTypeBulkResponse,
            )
        )

    def get_material_management_data_liquid_base_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LiquidBaseTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the liquidBaseType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/liquidBaseTypes/{objectId}".format(**{
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
                reference_model.LiquidBaseTypeResponse,
            )
        )

    def get_material_management_data_liquid_base_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LiquidBaseTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/liquidBaseTypes",
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
                reference_model.LiquidBaseTypeBulkResponse,
            )
        )

    def get_material_management_data_logo_names_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoNameResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the logoName object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoNames/{objectId}".format(**{
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
                reference_model.LogoNameResponse,
            )
        )

    def get_material_management_data_logo_names(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoNameBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoNames",
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
                reference_model.LogoNameBulkResponse,
            )
        )

    def get_material_management_data_logo_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the logoSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoSizes/{objectId}".format(**{
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
                reference_model.LogoSizeResponse,
            )
        )

    def get_material_management_data_logo_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoSizes",
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
                reference_model.LogoSizeBulkResponse,
            )
        )

    def get_material_management_data_logo_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the logoType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoTypes/{objectId}".format(**{
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
                reference_model.LogoTypeResponse,
            )
        )

    def get_material_management_data_logo_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.LogoTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/logoTypes",
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
                reference_model.LogoTypeBulkResponse,
            )
        )

    def get_material_management_data_machinery_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MachineryTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the machineryType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/machineryTypes/{objectId}".format(**{
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
                reference_model.MachineryTypeResponse,
            )
        )

    def get_material_management_data_machinery_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MachineryTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/machineryTypes",
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
                reference_model.MachineryTypeBulkResponse,
            )
        )

    def get_material_management_data_material_benefits_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialBenefitResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialBenefit object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialBenefits/{objectId}".format(**{
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
                reference_model.MaterialBenefitResponse,
            )
        )

    def get_material_management_data_material_benefits(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialBenefitBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialBenefits",
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
                reference_model.MaterialBenefitBulkResponse,
            )
        )

    def get_material_management_data_material_color_control_modes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialColorControlModeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialColorControlMode object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialColorControlModes/{objectId}".format(**{  # noqa
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
                reference_model.MaterialColorControlModeResponse,
            )
        )

    def get_material_management_data_material_color_control_modes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialColorControlModeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialColorControlModes",
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
                reference_model.MaterialColorControlModeBulkResponse,
            )
        )

    def get_material_management_data_material_development_teams_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialDevelopmentTeamResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialDevelopmentTeam object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialDevelopmentTeams/{objectId}".format(**{  # noqa
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
                reference_model.MaterialDevelopmentTeamResponse,
            )
        )

    def get_material_management_data_material_development_teams(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialDevelopmentTeamBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialDevelopmentTeams",
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
                reference_model.MaterialDevelopmentTeamBulkResponse,
            )
        )

    def get_material_management_data_material_end_uses_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialEndUseResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialEndUse object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialEndUses/{objectId}".format(**{
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
                reference_model.MaterialEndUseResponse,
            )
        )

    def get_material_management_data_material_end_uses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialEndUseBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialEndUses",
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
                reference_model.MaterialEndUseBulkResponse,
            )
        )

    def get_material_management_data_material_palette_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPaletteStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Material Palette State object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPaletteStates/{objectId}".format(**{  # noqa
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
                reference_model.MaterialPaletteStateResponse,
            )
        )

    def get_material_management_data_material_palette_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPaletteStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPaletteStates",
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
                reference_model.MaterialPaletteStateBulkResponse,
            )
        )

    def get_material_management_data_material_part_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPartTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Material Part Type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPartTypes/{objectId}".format(**{
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
                reference_model.MaterialPartTypeResponse,
            )
        )

    def get_material_management_data_material_part_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPartTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPartTypes",
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
                reference_model.MaterialPartTypeBulkResponse,
            )
        )

    def get_material_management_data_material_pricing_modes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPricingModeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the materialPricingMode object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPricingModes/{objectId}".format(**{  # noqa
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
                reference_model.MaterialPricingModeResponse,
            )
        )

    def get_material_management_data_material_pricing_modes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialPricingModeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialPricingModes",
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
                reference_model.MaterialPricingModeBulkResponse,
            )
        )

    def get_material_management_data_material_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the MaterialState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialStates/{objectId}".format(**{
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
                reference_model.MaterialStateResponse,
            )
        )

    def get_material_management_data_material_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialStates",
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
                reference_model.MaterialStateBulkResponse,
            )
        )

    def get_material_management_data_material_technologies_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialTechnologyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Material Technique object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialTechnologies/{objectId}".format(**{  # noqa
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
                reference_model.MaterialTechnologyResponse,
            )
        )

    def get_material_management_data_material_technologies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MaterialTechnologyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/materialTechnologies",
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
                reference_model.MaterialTechnologyBulkResponse,
            )
        )

    def get_material_management_data_methods_of_make_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MethodOfMakeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the methodOfMake object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/methodsOfMake/{objectId}".format(**{
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
                reference_model.MethodOfMakeResponse,
            )
        )

    def get_material_management_data_methods_of_make(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MethodOfMakeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/methodsOfMake",
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
                reference_model.MethodOfMakeBulkResponse,
            )
        )

    def get_material_management_data_moldables_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MoldableResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the moldable object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/moldables/{objectId}".format(**{
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
                reference_model.MoldableResponse,
            )
        )

    def get_material_management_data_moldables(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.MoldableBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/moldables",
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
                reference_model.MoldableBulkResponse,
            )
        )

    def get_material_management_data_non_woven_fiber_web_laying_methods_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenFiberWebLayingMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nonWovenFiberWebLayingMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenFiberWebLayingMethods/{objectId}".format(**{  # noqa
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
                reference_model.NonWovenFiberWebLayingMethodResponse,
            )
        )

    def get_material_management_data_non_woven_fiber_web_laying_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenFiberWebLayingMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenFiberWebLayingMethods",
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
                reference_model.NonWovenFiberWebLayingMethodBulkResponse,
            )
        )

    def get_material_management_data_non_woven_microfiber_processing_types_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenMicrofiberProcessingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nonWovenMicrofiberProcessingType
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenMicrofiberProcessingTypes/{objectId}".format(**{  # noqa
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
                reference_model.NonWovenMicrofiberProcessingTypeResponse,
            )
        )

    def get_material_management_data_non_woven_microfiber_processing_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenMicrofiberProcessingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenMicrofiberProcessingTypes",
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
                reference_model.NonWovenMicrofiberProcessingTypeBulkResponse,
            )
        )

    def get_material_management_data_non_woven_substrate_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenSubstrateTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nonWovenSubstrateType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenSubstrateTypes/{objectId}".format(**{  # noqa
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
                reference_model.NonWovenSubstrateTypeResponse,
            )
        )

    def get_material_management_data_non_woven_substrate_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenSubstrateTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenSubstrateTypes",
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
                reference_model.NonWovenSubstrateTypeBulkResponse,
            )
        )

    def get_material_management_data_non_woven_uncoated_web_finishing_methods_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenUncoatedWebFinishingMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nonWovenUncoatedWebFinishingMethod
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenUncoatedWebFinishingMethods/{objectId}".format(**{  # noqa
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
                reference_model.NonWovenUncoatedWebFinishingMethodResponse,
            )
        )

    def get_material_management_data_non_woven_uncoated_web_finishing_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenUncoatedWebFinishingMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenUncoatedWebFinishingMethods",
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
                reference_model.NonWovenUncoatedWebFinishingMethodBulkResponse,
            )
        )

    def get_material_management_data_non_woven_web_bonding_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenWebBondingMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the nonWovenWebBondingMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenWebBondingMethods/{objectId}".format(**{  # noqa
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
                reference_model.NonWovenWebBondingMethodResponse,
            )
        )

    def get_material_management_data_non_woven_web_bonding_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NonWovenWebBondingMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/nonWovenWebBondingMethods",
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
                reference_model.NonWovenWebBondingMethodBulkResponse,
            )
        )

    def get_material_management_data_number_of_colors_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NumberOfColorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the number of color object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/numberOfColors/{objectId}".format(**{
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
                reference_model.NumberOfColorResponse,
            )
        )

    def get_material_management_data_number_of_colors(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.NumberOfColorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/numberOfColors",
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
                reference_model.NumberOfColorBulkResponse,
            )
        )

    def get_material_management_data_opacities_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.OpacityResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the opacity object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/opacities/{objectId}".format(**{
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
                reference_model.OpacityResponse,
            )
        )

    def get_material_management_data_opacities(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.OpacityBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/opacities",
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
                reference_model.OpacityBulkResponse,
            )
        )

    def get_material_management_data_outsourced_processes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.OutsourcedProcessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the outsourcedProcess object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/outsourcedProcesses/{objectId}".format(**{  # noqa
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
                reference_model.OutsourcedProcessResponse,
            )
        )

    def get_material_management_data_outsourced_processes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.OutsourcedProcessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/outsourcedProcesses",
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
                reference_model.OutsourcedProcessBulkResponse,
            )
        )

    def get_material_management_data_packaging_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the packagingConstructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingConstructionTypes/{objectId}".format(**{  # noqa
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
                reference_model.PackagingConstructionTypeResponse,
            )
        )

    def get_material_management_data_packaging_construction_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingConstructionTypes",
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
                reference_model.PackagingConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_packaging_intents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingIntentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the packagingIntent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingIntents/{objectId}".format(**{
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
                reference_model.PackagingIntentResponse,
            )
        )

    def get_material_management_data_packaging_intents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingIntentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingIntents",
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
                reference_model.PackagingIntentBulkResponse,
            )
        )

    def get_material_management_data_packaging_statements_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingStatementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the packagingStatement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingStatements/{objectId}".format(**{  # noqa
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
                reference_model.PackagingStatementResponse,
            )
        )

    def get_material_management_data_packaging_statements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingStatementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingStatements",
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
                reference_model.PackagingStatementBulkResponse,
            )
        )

    def get_material_management_data_packaging_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the packagingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingTypes/{objectId}".format(**{
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
                reference_model.PackagingTypeResponse,
            )
        )

    def get_material_management_data_packaging_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PackagingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/packagingTypes",
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
                reference_model.PackagingTypeBulkResponse,
            )
        )

    def get_material_management_data_palette_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PaletteTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the paletteType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/paletteTypes/{objectId}".format(**{
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
                reference_model.PaletteTypeResponse,
            )
        )

    def get_material_management_data_palette_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PaletteTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/paletteTypes",
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
                reference_model.PaletteTypeBulkResponse,
            )
        )

    def get_material_management_data_part_types_orientation_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartTypeOrientationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the partTypesOrientation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/partTypesOrientation/{objectId}".format(**{  # noqa
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
                reference_model.PartTypeOrientationResponse,
            )
        )

    def get_material_management_data_part_types_orientation(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PartTypeOrientationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/partTypesOrientation",
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
                reference_model.PartTypeOrientationBulkResponse,
            )
        )

    def get_material_management_data_payment_terms_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PaymentTermResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the payment term object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/paymentTerms/{objectId}".format(**{
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
                reference_model.PaymentTermResponse,
            )
        )

    def get_material_management_data_payment_terms(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PaymentTermBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/paymentTerms",
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
                reference_model.PaymentTermBulkResponse,
            )
        )

    def get_material_management_data_plastic_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PlasticTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the plasticType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/plasticTypes/{objectId}".format(**{
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
                reference_model.PlasticTypeResponse,
            )
        )

    def get_material_management_data_plastic_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PlasticTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/plasticTypes",
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
                reference_model.PlasticTypeBulkResponse,
            )
        )

    def get_material_management_data_price_impact_charge_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceImpactChargeTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the priceImpactChargeType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/priceImpactChargeTypes/{objectId}".format(**{  # noqa
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
                reference_model.PriceImpactChargeTypeResponse,
            )
        )

    def get_material_management_data_price_impact_charge_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceImpactChargeTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/priceImpactChargeTypes",
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
                reference_model.PriceImpactChargeTypeBulkResponse,
            )
        )

    def get_material_management_data_price_impact_finish_colors_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceImpactFinishColorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the priceImpactFinishColor object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/priceImpactFinishColors/{objectId}".format(**{  # noqa
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
                reference_model.PriceImpactFinishColorResponse,
            )
        )

    def get_material_management_data_price_impact_finish_colors(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PriceImpactFinishColorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/priceImpactFinishColors",
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
                reference_model.PriceImpactFinishColorBulkResponse,
            )
        )

    def get_material_management_data_print_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PrintTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the printType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/printTypes/{objectId}".format(**{
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
                reference_model.PrintTypeResponse,
            )
        )

    def get_material_management_data_print_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PrintTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/printTypes",
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
                reference_model.PrintTypeBulkResponse,
            )
        )

    def get_material_management_data_processes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProcessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the process object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/processes/{objectId}".format(**{
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
                reference_model.ProcessResponse,
            )
        )

    def get_material_management_data_processes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProcessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/processes",
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
                reference_model.ProcessBulkResponse,
            )
        )

    def get_material_management_data_process_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProcessTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the process type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/processTypes/{objectId}".format(**{
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
                reference_model.ProcessTypeResponse,
            )
        )

    def get_material_management_data_process_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProcessTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/processTypes",
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
                reference_model.ProcessTypeBulkResponse,
            )
        )

    def get_material_management_data_product_information_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductInformationStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Information State object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productInformationStates/{objectId}".format(**{  # noqa
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
                reference_model.ProductInformationStateResponse,
            )
        )

    def get_material_management_data_product_information_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductInformationStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productInformationStates",
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
                reference_model.ProductInformationStateBulkResponse,
            )
        )

    def get_material_management_data_product_information_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductInformationTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Information Type object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productInformationTypes/{objectId}".format(**{  # noqa
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
                reference_model.ProductInformationTypeResponse,
            )
        )

    def get_material_management_data_product_information_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductInformationTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productInformationTypes",
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
                reference_model.ProductInformationTypeBulkResponse,
            )
        )

    def get_material_management_data_product_parts_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductPartResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Part object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productParts/{objectId}".format(**{
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
                reference_model.ProductPartResponse,
            )
        )

    def get_material_management_data_product_parts(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductPartBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productParts",
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
                reference_model.ProductPartBulkResponse,
            )
        )

    def get_material_management_data_product_part_contents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductPartContentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Part Content object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productPartContents/{objectId}".format(**{  # noqa
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
                reference_model.ProductPartContentResponse,
            )
        )

    def get_material_management_data_product_part_contents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductPartContentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productPartContents",
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
                reference_model.ProductPartContentBulkResponse,
            )
        )

    def get_material_management_data_product_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Product Size object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productSizes/{objectId}".format(**{
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
                reference_model.ProductSizeResponse,
            )
        )

    def get_material_management_data_product_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProductSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/productSizes",
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
                reference_model.ProductSizeBulkResponse,
            )
        )

    def get_material_management_data_program_gates_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProgramGateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the programGate object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/programGates/{objectId}".format(**{
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
                reference_model.ProgramGateResponse,
            )
        )

    def get_material_management_data_program_gates(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ProgramGateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/programGates",
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
                reference_model.ProgramGateBulkResponse,
            )
        )

    def get_material_management_data_pu_chemistries_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PuChemistryResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the puChemistry object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/puChemistries/{objectId}".format(**{
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
                reference_model.PuChemistryResponse,
            )
        )

    def get_material_management_data_pu_chemistries(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.PuChemistryBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/puChemistries",
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
                reference_model.PuChemistryBulkResponse,
            )
        )

    def get_material_procurement_data_reference_price_unit_of_measurements_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ReferencePriceUnitOfMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the referencePriceUnitOfMeasurement
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/referencePriceUnitOfMeasurements/{objectId}".format(**{  # noqa
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
                reference_model.ReferencePriceUnitOfMeasurementResponse,
            )
        )

    def get_material_procurement_data_reference_price_unit_of_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ReferencePriceUnitOfMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/referencePriceUnitOfMeasurements",
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
                reference_model.ReferencePriceUnitOfMeasurementBulkResponse,
            )
        )

    def get_material_management_data_required_phrases_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.RequiredPhrasesResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the requiredPhrases object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/requiredPhrases/{objectId}".format(**{
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
                reference_model.RequiredPhrasesResponse,
            )
        )

    def get_material_management_data_required_phrases(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.RequiredPhrasesBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/requiredPhrases",
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
                reference_model.RequiredPhrasesBulkResponse,
            )
        )

    def get_material_management_data_re_tannages_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ReTannageResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the reTannage object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/reTannages/{objectId}".format(**{
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
                reference_model.ReTannageResponse,
            )
        )

    def get_material_management_data_re_tannages(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ReTannageBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/reTannages",
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
                reference_model.ReTannageBulkResponse,
            )
        )

    def get_material_management_data_scrims_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ScrimResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the scrim object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/scrims/{objectId}".format(**{
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
                reference_model.ScrimResponse,
            )
        )

    def get_material_management_data_scrims(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ScrimBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/scrims",
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
                reference_model.ScrimBulkResponse,
            )
        )

    def get_material_management_shapes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShapeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the shape object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/shapes/{objectId}".format(**{
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
                reference_model.ShapeResponse,
            )
        )

    def get_material_management_data_shapes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShapeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/shapes",
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
                reference_model.ShapeBulkResponse,
            )
        )

    def get_material_procurement_data_shipping_dimension_measurements_object_id(  # noqa
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingDimensionMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the shippingDimensionMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/shippingDimensionMeasurements/{objectId}".format(**{  # noqa
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
                reference_model.ShippingDimensionMeasurementResponse,
            )
        )

    def get_material_procurement_data_shipping_dimension_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingDimensionMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/shippingDimensionMeasurements",
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
                reference_model.ShippingDimensionMeasurementBulkResponse,
            )
        )

    def get_material_procurement_data_shipping_unit_measurements_object_id(
        self,
        object_id: str,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingUnitMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the shippingUnitMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/shippingUnitMeasurements/{objectId}".format(**{  # noqa
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
                reference_model.ShippingUnitMeasurementResponse,
            )
        )

    def get_material_procurement_data_shipping_unit_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ShippingUnitMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/shippingUnitMeasurements",
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
                reference_model.ShippingUnitMeasurementBulkResponse,
            )
        )

    def get_material_procurement_data_selling_unit_of_measurements_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SellingUnitOfMeasurementResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sellingUnitOfMeasurement object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/sellingUnitOfMeasurements/{objectId}".format(**{  # noqa
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
                reference_model.SellingUnitOfMeasurementResponse,
            )
        )

    def get_material_procurement_data_selling_unit_of_measurements(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SellingUnitOfMeasurementBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/sellingUnitOfMeasurements",
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
                reference_model.SellingUnitOfMeasurementBulkResponse,
            )
        )

    def get_material_management_data_slider_locking_functions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SliderLockingFunctionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sliderLockingFunction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/sliderLockingFunctions/{objectId}".format(**{  # noqa
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
                reference_model.SliderLockingFunctionResponse,
            )
        )

    def get_material_management_data_slider_locking_functions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SliderLockingFunctionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/sliderLockingFunctions",
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
                reference_model.SliderLockingFunctionBulkResponse,
            )
        )

    def get_material_management_data_for_ball_type_and_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> sob.abc.Dictionary:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the forBallTypeAndSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/forBallTypeAndSizes/{objectId}".format(**{  # noqa
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
                sob.model.Dictionary,
            )
        )

    def get_material_management_data_for_ball_type_and_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> sob.abc.Dictionary:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/forBallTypeAndSizes",
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
                sob.model.Dictionary,
            )
        )

    def get_material_management_data_special_cutting_directions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialCuttingDirectionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the specialCuttingDirection object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/specialCuttingDirections/{objectId}".format(**{  # noqa
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
                reference_model.SpecialCuttingDirectionResponse,
            )
        )

    def get_material_management_data_special_cutting_directions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialCuttingDirectionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/specialCuttingDirections",
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
                reference_model.SpecialCuttingDirectionBulkResponse,
            )
        )

    def get_material_management_data_special_treatments_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialTreatmentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the specialTreatment object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/specialTreatments/{objectId}".format(**{
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
                reference_model.SpecialTreatmentResponse,
            )
        )

    def get_material_management_data_special_treatments(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SpecialTreatmentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/specialTreatments",
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
                reference_model.SpecialTreatmentBulkResponse,
            )
        )

    def get_material_management_data_sport_activities_object_id(
        self,
        object_id: int,
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
            "/materialManagement/data/sportActivities/{objectId}".format(**{
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

    def get_material_management_data_sport_activities(
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
            "/materialManagement/data/sportActivities",
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

    def get_material_management_data_staple_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StapleSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the stapleSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stapleSizes/{objectId}".format(**{
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
                reference_model.StapleSizeResponse,
            )
        )

    def get_material_management_data_staple_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StapleSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stapleSizes",
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
                reference_model.StapleSizeBulkResponse,
            )
        )

    def get_material_management_data_statement_contents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StatementContentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the statementContent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/statementContents/{objectId}".format(**{
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
                reference_model.StatementContentResponse,
            )
        )

    def get_material_management_data_statement_contents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StatementContentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/statementContents",
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
                reference_model.StatementContentBulkResponse,
            )
        )

    def get_material_management_data_steam_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SteamMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the steamMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/steamMethods/{objectId}".format(**{
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
                reference_model.SteamMethodResponse,
            )
        )

    def get_material_management_data_steam_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SteamMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/steamMethods",
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
                reference_model.SteamMethodBulkResponse,
            )
        )

    def get_material_management_data_stock_or_customs_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StockOrCustomResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the stockOrCustom object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stockOrCustoms/{objectId}".format(**{
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
                reference_model.StockOrCustomResponse,
            )
        )

    def get_material_management_data_stock_or_customs(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StockOrCustomBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stockOrCustoms",
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
                reference_model.StockOrCustomBulkResponse,
            )
        )

    def get_material_management_data_stop_functions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StopFunctionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the stopFunction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stopFunctions/{objectId}".format(**{
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
                reference_model.StopFunctionResponse,
            )
        )

    def get_material_management_data_stop_functions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StopFunctionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stopFunctions",
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
                reference_model.StopFunctionBulkResponse,
            )
        )

    def get_material_management_data_stretch_directions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StretchDirectionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the stretchDirection object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stretchDirections/{objectId}".format(**{
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
                reference_model.StretchDirectionResponse,
            )
        )

    def get_material_management_data_stretch_directions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StretchDirectionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/stretchDirections",
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
                reference_model.StretchDirectionBulkResponse,
            )
        )

    def get_material_management_data_structure_testing_references_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StructureTestingReferenceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the structureTestingReference object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/structureTestingReferences/{objectId}".format(**{  # noqa
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
                reference_model.StructureTestingReferenceResponse,
            )
        )

    def get_material_management_data_structure_testing_references(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StructureTestingReferenceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/structureTestingReferences",
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
                reference_model.StructureTestingReferenceBulkResponse,
            )
        )

    def get_material_management_data_structure_coverages_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StructureCoverageResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the structureCoverage object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/structureCoverages/{objectId}".format(**{
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
                reference_model.StructureCoverageResponse,
            )
        )

    def get_material_management_data_structure_coverages(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.StructureCoverageBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/structureCoverages",
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
                reference_model.StructureCoverageBulkResponse,
            )
        )

    def get_material_management_data_sub_palette_contents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubPaletteContentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the subPaletteContent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/subPaletteContents/{objectId}".format(**{
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
                reference_model.SubPaletteContentResponse,
            )
        )

    def get_material_management_data_sub_palette_contents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubPaletteContentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/subPaletteContents",
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
                reference_model.SubPaletteContentBulkResponse,
            )
        )

    def get_material_management_data_substrate_constructions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubstrateConstructionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the substrateConstruction object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/substrateConstructions/{objectId}".format(**{  # noqa
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
                reference_model.SubstrateConstructionResponse,
            )
        )

    def get_material_management_data_substrate_constructions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubstrateConstructionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/substrateConstructions",
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
                reference_model.SubstrateConstructionBulkResponse,
            )
        )

    def get_material_management_data_substrate_processing_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubstrateProcessingTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the substrateProcessingType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/substrateProcessingTypes/{objectId}".format(**{  # noqa
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
                reference_model.SubstrateProcessingTypeResponse,
            )
        )

    def get_material_management_data_substrate_processing_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SubstrateProcessingTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/substrateProcessingTypes",
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
                reference_model.SubstrateProcessingTypeBulkResponse,
            )
        )

    def get_material_management_data_supplied_material_color_hues_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialColorHueResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the suppliedMaterialColorHue object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorHues/{objectId}".format(**{  # noqa
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
                reference_model.SuppliedMaterialColorHueResponse,
            )
        )

    def get_material_management_data_supplied_material_color_hues(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialColorHueBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorHues",
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
                reference_model.SuppliedMaterialColorHueBulkResponse,
            )
        )

    def get_material_management_data_supplied_material_color_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialColorStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the suppliedMaterialColorState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorStates/{objectId}".format(**{  # noqa
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
                reference_model.SuppliedMaterialColorStateResponse,
            )
        )

    def get_material_management_data_supplied_material_color_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialColorStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialColorStates",
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
                reference_model.SuppliedMaterialColorStateBulkResponse,
            )
        )

    def get_material_procurement_data_supplied_material_price_comment_types_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialPriceCommentTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the suppliedMaterialPriceCommentType
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/suppliedMaterialPriceCommentTypes/{objectId}".format(**{  # noqa
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
                reference_model.SuppliedMaterialPriceCommentTypeResponse,
            )
        )

    def get_material_procurement_data_supplied_material_price_comment_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialPriceCommentTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/suppliedMaterialPriceCommentTypes",
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
                reference_model.SuppliedMaterialPriceCommentTypeBulkResponse,
            )
        )

    def get_material_procurement_data_supplied_material_price_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialPriceStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the suppliedMaterialPriceState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/suppliedMaterialPriceStates/{objectId}".format(**{  # noqa
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
                reference_model.SuppliedMaterialPriceStateResponse,
            )
        )

    def get_material_procurement_data_supplied_material_price_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialPriceStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/suppliedMaterialPriceStates",
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
                reference_model.SuppliedMaterialPriceStateBulkResponse,
            )
        )

    def get_material_management_data_supplied_material_states_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialStateResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the suppliedMaterialState object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialStates/{objectId}".format(**{  # noqa
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
                reference_model.SuppliedMaterialStateResponse,
            )
        )

    def get_material_management_data_supplied_material_states(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SuppliedMaterialStateBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/suppliedMaterialStates",
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
                reference_model.SuppliedMaterialStateBulkResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_charge_types_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountChargeTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the surchargeDiscountChargeType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountChargeTypes/{objectId}".format(**{  # noqa
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
                reference_model.SurchargeDiscountChargeTypeResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_charge_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountChargeTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountChargeTypes",
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
                reference_model.SurchargeDiscountChargeTypeBulkResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_finish_colors_object_id(  # noqa
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountFinishColorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the surchargeDiscountFinishColor object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountFinishColors/{objectId}".format(**{  # noqa
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
                reference_model.SurchargeDiscountFinishColorResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_finish_colors(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountFinishColorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountFinishColors",
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
                reference_model.SurchargeDiscountFinishColorBulkResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the surchargeDiscountMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountMethods/{objectId}".format(**{  # noqa
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
                reference_model.SurchargeDiscountMethodResponse,
            )
        )

    def get_material_procurement_data_surcharge_discount_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurchargeDiscountMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialProcurement/data/surchargeDiscountMethods",
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
                reference_model.SurchargeDiscountMethodBulkResponse,
            )
        )

    def get_material_management_data_surface_texture_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurfaceTextureTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the surfaceTextureType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/surfaceTextureTypes/{objectId}".format(**{  # noqa
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
                reference_model.SurfaceTextureTypeResponse,
            )
        )

    def get_material_management_data_surface_texture_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SurfaceTextureTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/surfaceTextureTypes",
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
                reference_model.SurfaceTextureTypeBulkResponse,
            )
        )

    def get_material_management_data_teeth_sizes_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TeethSizeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the teethSize object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/teethSizes/{objectId}".format(**{
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
                reference_model.TeethSizeResponse,
            )
        )

    def get_material_management_data_teeth_sizes(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TeethSizeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/teethSizes",
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
                reference_model.TeethSizeBulkResponse,
            )
        )

    def get_material_management_data_textile_construction_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileConstructionTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the textileConstructionType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileConstructionTypes/{objectId}".format(**{  # noqa
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
                reference_model.TextileConstructionTypeResponse,
            )
        )

    def get_material_management_data_textile_construction_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileConstructionTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileConstructionTypes",
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
                reference_model.TextileConstructionTypeBulkResponse,
            )
        )

    def get_material_management_data_textile_sub_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileSubVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the textileSubVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileSubVariations/{objectId}".format(**{  # noqa
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
                reference_model.TextileSubVariationResponse,
            )
        )

    def get_material_management_data_textile_sub_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileSubVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileSubVariations",
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
                reference_model.TextileSubVariationBulkResponse,
            )
        )

    def get_material_management_data_textile_sub_variations_two_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileSubVariationTwoResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the textileSubVariationTwo object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileSubVariationsTwo/{objectId}".format(**{  # noqa
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
                reference_model.TextileSubVariationTwoResponse,
            )
        )

    def get_material_management_data_textile_sub_variations_two(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileSubVariationTwoBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileSubVariationsTwo",
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
                reference_model.TextileSubVariationTwoBulkResponse,
            )
        )

    def get_material_management_data_textile_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the textileVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileVariations/{objectId}".format(**{
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
                reference_model.TextileVariationResponse,
            )
        )

    def get_material_management_data_textile_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TextileVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/textileVariations",
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
                reference_model.TextileVariationBulkResponse,
            )
        )

    def get_material_management_data_thermoplastic_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ThermoplasticTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the thermoplasticType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/thermoplasticTypes/{objectId}".format(**{
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
                reference_model.ThermoplasticTypeResponse,
            )
        )

    def get_material_management_data_thermoplastic_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ThermoplasticTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/thermoplasticTypes",
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
                reference_model.ThermoplasticTypeBulkResponse,
            )
        )

    def get_material_management_data_thicknesses_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ThicknessResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the thickness object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/thicknesses/{objectId}".format(**{
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
                reference_model.ThicknessResponse,
            )
        )

    def get_material_management_data_thicknesses(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ThicknessBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/thicknesses",
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
                reference_model.ThicknessBulkResponse,
            )
        )

    def get_material_management_data_tip_contents_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TipContentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the tipContent object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/tipContents/{objectId}".format(**{
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
                reference_model.TipContentResponse,
            )
        )

    def get_material_management_data_tip_contents(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TipContentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/tipContents",
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
                reference_model.TipContentBulkResponse,
            )
        )

    def get_material_management_data_treatment_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TreatmentTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the treatmentType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/treatmentTypes/{objectId}".format(**{
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
                reference_model.TreatmentTypeResponse,
            )
        )

    def get_material_management_data_treatment_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TreatmentTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/treatmentTypes",
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
                reference_model.TreatmentTypeBulkResponse,
            )
        )

    def get_material_management_data_twill_directions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TwillDirectionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the twillDirection object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/twillDirections/{objectId}".format(**{
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
                reference_model.TwillDirectionResponse,
            )
        )

    def get_material_management_data_twill_directions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.TwillDirectionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/twillDirections",
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
                reference_model.TwillDirectionBulkResponse,
            )
        )

    def get_material_management_data_us_customs_descriptions_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UsCustomsDescriptionResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the usCustomsDescription object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/usCustomsDescriptions/{objectId}".format(**{  # noqa
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
                reference_model.UsCustomsDescriptionResponse,
            )
        )

    def get_material_management_data_us_customs_descriptions(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UsCustomsDescriptionBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/usCustomsDescriptions",
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
                reference_model.UsCustomsDescriptionBulkResponse,
            )
        )

    def get_material_management_data_use_considerations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UseConsiderationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the useConsideration object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/useConsiderations/{objectId}".format(**{
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
                reference_model.UseConsiderationResponse,
            )
        )

    def get_material_management_data_use_considerations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.UseConsiderationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/useConsiderations",
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
                reference_model.UseConsiderationBulkResponse,
            )
        )

    def get_material_management_data_visual_effects_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.VisualEffectResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the visualEffect object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/visualEffects/{objectId}".format(**{
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
                reference_model.VisualEffectResponse,
            )
        )

    def get_material_management_data_visual_effects(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.VisualEffectBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/visualEffects",
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
                reference_model.VisualEffectBulkResponse,
            )
        )

    def get_material_management_data_visual_material_name_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.VisualMaterialNameVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the visualMaterialNameVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/visualMaterialNameVariations/{objectId}".format(**{  # noqa
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
                reference_model.VisualMaterialNameVariationResponse,
            )
        )

    def get_material_management_data_visual_material_name_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.VisualMaterialNameVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/visualMaterialNameVariations",
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
                reference_model.VisualMaterialNameVariationBulkResponse,
            )
        )

    def get_material_management_data_web_formations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WebFormationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the webFormation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/webFormations/{objectId}".format(**{
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
                reference_model.WebFormationResponse,
            )
        )

    def get_material_management_data_web_formations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WebFormationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/webFormations",
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
                reference_model.WebFormationBulkResponse,
            )
        )

    def get_material_management_data_web_formation_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WebFormationMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the webFormationMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/webFormationMethods/{objectId}".format(**{  # noqa
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
                reference_model.WebFormationMethodResponse,
            )
        )

    def get_material_management_data_web_formation_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WebFormationMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/webFormationMethods",
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
                reference_model.WebFormationMethodBulkResponse,
            )
        )

    def get_material_management_data_weight_material_name_variations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WeightMaterialNameVariationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the weightMaterialNameVariation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/weightMaterialNameVariations/{objectId}".format(**{  # noqa
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
                reference_model.WeightMaterialNameVariationResponse,
            )
        )

    def get_material_management_data_weight_material_name_variations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WeightMaterialNameVariationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/weightMaterialNameVariations",
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
                reference_model.WeightMaterialNameVariationBulkResponse,
            )
        )

    def get_material_management_data_width_indicators_object_id(
        self,
        object_id: bool,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WidthIndicatorResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the widthIndicator object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/widthIndicators/{objectId}".format(**{
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
                reference_model.WidthIndicatorResponse,
            )
        )

    def get_material_management_data_width_indicators(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.WidthIndicatorBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/widthIndicators",
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
                reference_model.WidthIndicatorBulkResponse,
            )
        )

    def get_material_management_data_yarn_covering_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnCoveringMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnCoveringMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnCoveringMethods/{objectId}".format(**{  # noqa
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
                reference_model.YarnCoveringMethodResponse,
            )
        )

    def get_material_management_data_yarn_covering_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnCoveringMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnCoveringMethods",
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
                reference_model.YarnCoveringMethodBulkResponse,
            )
        )

    def get_material_management_data_yarn_locations_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnLocationResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnLocation object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnLocations/{objectId}".format(**{
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
                reference_model.YarnLocationResponse,
            )
        )

    def get_material_management_data_yarn_locations(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnLocationBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnLocations",
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
                reference_model.YarnLocationBulkResponse,
            )
        )

    def get_material_management_data_yarn_plies_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPly object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlies/{objectId}".format(**{
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
                reference_model.YarnPlyResponse,
            )
        )

    def get_material_management_data_yarn_plies(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlies",
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
                reference_model.YarnPlyBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_brands_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyBrandResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyBrand object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyBrands/{objectId}".format(**{
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
                reference_model.YarnPlyBrandResponse,
            )
        )

    def get_material_management_data_yarn_ply_brands(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyBrandBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyBrands",
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
                reference_model.YarnPlyBrandBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_dye_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyDyeMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyDyeMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyDyeMethods/{objectId}".format(**{
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
                reference_model.YarnPlyDyeMethodResponse,
            )
        )

    def get_material_management_data_yarn_ply_dye_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyDyeMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyDyeMethods",
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
                reference_model.YarnPlyDyeMethodBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_lusters_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyLusterResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyLuster object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyLusters/{objectId}".format(**{
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
                reference_model.YarnPlyLusterResponse,
            )
        )

    def get_material_management_data_yarn_ply_lusters(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyLusterBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyLusters",
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
                reference_model.YarnPlyLusterBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_number_systems_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyNumberSystemResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyNumberSystem object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyNumberSystems/{objectId}".format(**{  # noqa
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
                reference_model.YarnPlyNumberSystemResponse,
            )
        )

    def get_material_management_data_yarn_ply_number_systems(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyNumberSystemBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyNumberSystems",
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
                reference_model.YarnPlyNumberSystemBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_spinning_methods_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlySpinningMethodResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlySpinningMethod object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlySpinningMethods/{objectId}".format(**{  # noqa
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
                reference_model.YarnPlySpinningMethodResponse,
            )
        )

    def get_material_management_data_yarn_ply_spinning_methods(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlySpinningMethodBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlySpinningMethods",
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
                reference_model.YarnPlySpinningMethodBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_textures_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTextureResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyTexture object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTextures/{objectId}".format(**{
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
                reference_model.YarnPlyTextureResponse,
            )
        )

    def get_material_management_data_yarn_ply_textures(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTextureBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTextures",
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
                reference_model.YarnPlyTextureBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_types_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTypeResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyType object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTypes/{objectId}".format(**{
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
                reference_model.YarnPlyTypeResponse,
            )
        )

    def get_material_management_data_yarn_ply_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTypes",
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
                reference_model.YarnPlyTypeBulkResponse,
            )
        )

    def get_material_management_data_yarn_ply_twists_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTwistResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnPlyTwist object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTwists/{objectId}".format(**{
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
                reference_model.YarnPlyTwistResponse,
            )
        )

    def get_material_management_data_yarn_ply_twists(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnPlyTwistBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnPlyTwists",
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
                reference_model.YarnPlyTwistBulkResponse,
            )
        )

    def get_material_management_data_yarn_treatments_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnTreatmentResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnTreatment object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnTreatments/{objectId}".format(**{
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
                reference_model.YarnTreatmentResponse,
            )
        )

    def get_material_management_data_yarn_treatments(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnTreatmentBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnTreatments",
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
                reference_model.YarnTreatmentBulkResponse,
            )
        )

    def get_material_management_data_yarn_twists_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnTwistResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnTwist object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnTwists/{objectId}".format(**{
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
                reference_model.YarnTwistResponse,
            )
        )

    def get_material_management_data_yarn_twists(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnTwistBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnTwists",
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
                reference_model.YarnTwistBulkResponse,
            )
        )

    def get_material_management_data_yarn_visual_effects_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnVisualEffectResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the yarnVisualEffect object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnVisualEffects/{objectId}".format(**{
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
                reference_model.YarnVisualEffectResponse,
            )
        )

    def get_material_management_data_yarn_visual_effects(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.YarnVisualEffectBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/yarnVisualEffects",
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
                reference_model.YarnVisualEffectBulkResponse,
            )
        )

    def get_material_management_data_zipper_performances_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ZipperPerformanceResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the Zipper Performance object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/zipperPerformances/{objectId}".format(**{
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
                reference_model.ZipperPerformanceResponse,
            )
        )

    def get_material_management_data_zipper_performances(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.ZipperPerformanceBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/zipperPerformances",
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
                reference_model.ZipperPerformanceBulkResponse,
            )
        )

    def get_sustainability_data_sustainability_business_units_object_id(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SustainabilityBusinessUnitResponse:
        """
        How you get a single reference data resource

        Parameters:

        - object_id:
          The code associated with of the sustainabilitySeasonBusinessUnit
          object
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/sustainability/data/sustainabilityBusinessUnits/{objectId}".format(**{  # noqa
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
                reference_model.SustainabilityBusinessUnitResponse,
            )
        )

    def get_sustainability_data_sustainability_business_units(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.SustainabilityBusinessUnitBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/sustainability/data/sustainabilityBusinessUnits",
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
                reference_model.SustainabilityBusinessUnitBulkResponse,
            )
        )

    def get_material_management_data_cushioning_types(
        self,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> reference_model.CushioningTypeBulkResponse:
        """
        How you get all the reference data associated with a specific type of
        reference information

        Parameters:

        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/materialManagement/data/cushioningTypes",
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
                reference_model.CushioningTypeBulkResponse,
            )
        )
