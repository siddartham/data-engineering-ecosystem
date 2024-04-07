import oapi
import sob
import typing
from . import model
from ..abc.client import Client as _Client
from ..config import TOKEN_URL_PROD
from logging import Logger
from cerberus_assistant.config import CERBERUS_URL
from cerberus_assistant.decorate import apply_cerberus_path_arguments


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
            "https://productdevelopment.api-product.pes-prod.nike.com/v1/productDevelopment"  # noqa
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

    def get_data_colorway_seasons_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.DataColorwaySeasonsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentColorwayResponse:
        """
        How you get a single development colorway.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product Development
          Development Colorway)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/colorwaySeasons/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentColorwayResponse,
            )
        )

    def get_data_colorway_seasons(
        self,
        object_id: model.DataColorwaySeasonsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataColorwaySeasonsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentColorwayBulkResponse:
        """
        How you get development colorway in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product
          Development Development Colorway)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/colorwaySeasons",
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
                model.DevelopmentColorwayBulkResponse,
            )
        )

    def get_data_colorway_seasons_object_id_relationships(
        self,
        object_id: int,
        *,
        depth: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.RelationshipResponse:
        """
        How you get all the relationships to the single object requested, in
        other words the children in the hierarchy (BOMs) to the requested
        entity

        Parameters:

        - object_id:
          The Id of the object (in this case Product Development Development
          Colorway Style) where the relationships are desired
        - depth:
          This determines how many levels in the hierarcy you wish to traverse,
          default is 2
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/colorwaySeasons/{objectId}/relationships".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                "depth": oapi.client.format_argument_value(
                    "depth",
                    depth,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.RelationshipResponse,
            )
        )

    def get_search_colorway_seasons(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        development_colorway_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayIdentifier
        ] = None,
        development_style_season_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentStyleSeasonIdentifier
        ] = None,
        product_offering_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetProductOfferingIdentifier
        ] = None,
        development_colorway_season_status_indicator: typing.Optional[
            bool
        ] = None,
        prototype_quantity: typing.Optional[
            model.SearchColorwaySeasonsGetPrototypeQuantity
        ] = None,
        sample_quantity: typing.Optional[
            model.SearchColorwaySeasonsGetSampleQuantity
        ] = None,
        nike_production_trial: typing.Optional[
            model.SearchColorwaySeasonsGetNikeProductionTrial
        ] = None,
        target_fob: typing.Optional[
            model.SearchColorwaySeasonsGetTargetFOB
        ] = None,
        sourcing_configuration_colorway_season: typing.Optional[
            model.SearchColorwaySeasonsGetSourcingConfigurationColorwaySeason
        ] = None,
        development_style_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentStyleIdentifier
        ] = None,
        cycle_year: typing.Optional[
            model.SearchColorwaySeasonsGetCycleYear
        ] = None,
        whq_color_designer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqColorDesignerUserIdentifier
        ] = None,
        whq_costing_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqCostingUserIdentifier
        ] = None,
        whq_designer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqDesignerUserIdentifier
        ] = None,
        whq_developer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqDeveloperUserIdentifier
        ] = None,
        whq_footwear_development_director_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqFootwearDevelopmentDirectorUserIdentifier  # noqa
        ] = None,
        whq_knit_developer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqKnitDeveloperUserIdentifier
        ] = None,
        whq_knit_engineer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqKnitEngineerUserIdentifier
        ] = None,
        whq_knit_programmer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqKnitProgrammerUserIdentifier
        ] = None,
        whq_material_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqMaterialUserIdentifier
        ] = None,
        whq_product_engineer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqProductEngineerUserIdentifier
        ] = None,
        whq_product_testing_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetWhqProductTestingUserIdentifier
        ] = None,
        knit_center_developer_user_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetKnitCenterDeveloperUserIdentifier
        ] = None,
        new_upper_indicator: typing.Optional[
            bool
        ] = None,
        new_midsole_indicator: typing.Optional[
            bool
        ] = None,
        new_outsole_indicator: typing.Optional[
            bool
        ] = None,
        product_season_development_team: typing.Optional[
            model.SearchColorwaySeasonsGetProductSeasonDevelopmentTeam
        ] = None,
        technical_difficulty: typing.Optional[
            model.SearchColorwaySeasonsGetTechnicalDifficulty
        ] = None,
        development_colorway_target_fob: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayTargetFOB
        ] = None,
        development_track: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentTrack
        ] = None,
        product_track: typing.Optional[
            model.SearchColorwaySeasonsGetProductTrack
        ] = None,
        start_date: typing.Optional[
            model.SearchColorwaySeasonsGetStartDate
        ] = None,
        development_style_season_status_indicator: typing.Optional[
            bool
        ] = None,
        last_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetLastIdentifier
        ] = None,
        additional_last_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetAdditionalLastIdentifier
        ] = None,
        development_style_status_indicator: typing.Optional[
            bool
        ] = None,
        development_colorway_description: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayDescription
        ] = None,
        development_colorway_type: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayType
        ] = None,
        development_colorway_state: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayState
        ] = None,
        development_colorway_gate: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentColorwayGate
        ] = None,
        product_identifier: typing.Optional[
            model.SearchColorwaySeasonsGetProductIdentifier
        ] = None,
        development_colorway_status_indicator: typing.Optional[
            bool
        ] = None,
        development_style_type: typing.Optional[
            model.SearchColorwaySeasonsGetDevelopmentStyleType
        ] = None,
        division: typing.Optional[
            model.SearchColorwaySeasonsGetDivision
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the development
        colorway by Season entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - development_colorway_identifier:
          The reference key associated with this item
        - development_style_season_identifier:
          The reference key associated with this item
        - product_offering_identifier:
          The reference key associated with this item
        - development_colorway_season_status_indicator:
          The true or false flag associated with this item:
        - prototype_quantity:
          The number associated with prototypeQuantity
        - sample_quantity:
          The number associated with sampleQuantity
        - nike_production_trial:
          The reference key associated with this item
        - target_fob:
          The number for target FOB
        - sourcing_configuration_colorway_season:
          The reference key associated with this item
        - development_style_identifier:
          The Id for develpment style season
        - cycle_year:
          The reference key associated with this item: cycleYear
        - whq_color_designer_user_identifier:
          The email address for this user
        - whq_costing_user_identifier:
          The email address for this user
        - whq_designer_user_identifier:
          The email address for this user
        - whq_developer_user_identifier:
          The email address for this user
        - whq_footwear_development_director_user_identifier:
          The email address for this user
        - whq_knit_developer_user_identifier:
          The email address for this user
        - whq_knit_engineer_user_identifier:
          The email address for this user
        - whq_knit_programmer_user_identifier:
          The email address for this user
        - whq_material_user_identifier:
          The email address for this user
        - whq_product_engineer_user_identifier:
          The email address for this user
        - whq_product_testing_user_identifier:
          The email address for this user
        - knit_center_developer_user_identifier:
          The email address for this user
        - new_upper_indicator:
          The true or false flag associated with this item
        - new_midsole_indicator:
          The true or false flag associated with this item
        - new_outsole_indicator:
          The true or false flag associated with this item
        - product_season_development_team:
          The reference key associated with this item
        - technical_difficulty:
          The reference key associated with this item
        - development_colorway_target_fob:
          The reference key associated with this item
        - development_track:
          The reference key associated with this item
        - product_track:
          The reference key associated with this item
        - start_date:
          The date assocated with the start of development
        - development_style_season_status_indicator:
          The true or false flag associated with this item
        - last_identifier:
          The reference key associated with this item
        - additional_last_identifier:
          The reference key associated with this item
        - development_style_status_indicator:
          The true or false flag associated with this item
        - development_colorway_description:
          The reference key associated with this item
        - development_colorway_type:
          The reference key associated with this item
        - development_colorway_state:
          The reference key associated with this item
        - development_colorway_gate:
          The reference key associated with this item
        - product_identifier:
          The reference key associated with this item
        - development_colorway_status_indicator:
          The true or false flag associated with this item:
        - development_style_type:
          The reference key associated with this item
        - division:
          The reference key associated with this item
        """
        response: sob.abc.Readable = self.request(
            "/search/colorwaySeasons",
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
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayIdentifier",
                    development_colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentStyleSeasonIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentStyleSeasonIdentifier",
                    development_style_season_identifier,
                    style="form",
                    explode=False,
                ),
                "productOfferingIdentifier": oapi.client.format_argument_value(
                    "productOfferingIdentifier",
                    product_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentColorwaySeasonStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "developmentColorwaySeasonStatusIndicator",
                    development_colorway_season_status_indicator,
                    style="form",
                    explode=False,
                ),
                "prototypeQuantity": oapi.client.format_argument_value(
                    "prototypeQuantity",
                    prototype_quantity,
                    style="form",
                    explode=False,
                ),
                "sampleQuantity": oapi.client.format_argument_value(
                    "sampleQuantity",
                    sample_quantity,
                    style="form",
                    explode=False,
                ),
                "nikeProductionTrial": oapi.client.format_argument_value(
                    "nikeProductionTrial",
                    nike_production_trial,
                    style="form",
                    explode=False,
                ),
                "targetFOB": oapi.client.format_argument_value(
                    "targetFOB",
                    target_fob,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationColorwaySeason": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationColorwaySeason",
                    sourcing_configuration_colorway_season,
                    style="form",
                    explode=False,
                ),
                "developmentStyleIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentStyleIdentifier",
                    development_style_identifier,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "whqColorDesignerUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqColorDesignerUserIdentifier",
                    whq_color_designer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqCostingUserIdentifier": oapi.client.format_argument_value(
                    "whqCostingUserIdentifier",
                    whq_costing_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqDesignerUserIdentifier": oapi.client.format_argument_value(
                    "whqDesignerUserIdentifier",
                    whq_designer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqDeveloperUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqDeveloperUserIdentifier",
                    whq_developer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqFootwearDevelopmentDirectorUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqFootwearDevelopmentDirectorUserIdentifier",
                    whq_footwear_development_director_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqKnitDeveloperUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqKnitDeveloperUserIdentifier",
                    whq_knit_developer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqKnitEngineerUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqKnitEngineerUserIdentifier",
                    whq_knit_engineer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqKnitProgrammerUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqKnitProgrammerUserIdentifier",
                    whq_knit_programmer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqMaterialUserIdentifier": oapi.client.format_argument_value(
                    "whqMaterialUserIdentifier",
                    whq_material_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqProductEngineerUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqProductEngineerUserIdentifier",
                    whq_product_engineer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "whqProductTestingUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "whqProductTestingUserIdentifier",
                    whq_product_testing_user_identifier,
                    style="form",
                    explode=False,
                ),
                "knitCenterDeveloperUserIdentifier": oapi.client.format_argument_value(  # noqa
                    "knitCenterDeveloperUserIdentifier",
                    knit_center_developer_user_identifier,
                    style="form",
                    explode=False,
                ),
                "newUpperIndicator": oapi.client.format_argument_value(
                    "newUpperIndicator",
                    new_upper_indicator,
                    style="form",
                    explode=False,
                ),
                "newMidsoleIndicator": oapi.client.format_argument_value(
                    "newMidsoleIndicator",
                    new_midsole_indicator,
                    style="form",
                    explode=False,
                ),
                "newOutsoleIndicator": oapi.client.format_argument_value(
                    "newOutsoleIndicator",
                    new_outsole_indicator,
                    style="form",
                    explode=False,
                ),
                "productSeasonDevelopmentTeam": oapi.client.format_argument_value(  # noqa
                    "productSeasonDevelopmentTeam",
                    product_season_development_team,
                    style="form",
                    explode=False,
                ),
                "technicalDifficulty": oapi.client.format_argument_value(
                    "technicalDifficulty",
                    technical_difficulty,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayTargetFOB": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayTargetFOB",
                    development_colorway_target_fob,
                    style="form",
                    explode=False,
                ),
                "developmentTrack": oapi.client.format_argument_value(
                    "developmentTrack",
                    development_track,
                    style="form",
                    explode=False,
                ),
                "productTrack": oapi.client.format_argument_value(
                    "productTrack",
                    product_track,
                    style="form",
                    explode=False,
                ),
                "startDate": oapi.client.format_argument_value(
                    "startDate",
                    start_date,
                    style="form",
                    explode=False,
                ),
                "developmentStyleSeasonStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "developmentStyleSeasonStatusIndicator",
                    development_style_season_status_indicator,
                    style="form",
                    explode=False,
                ),
                "lastIdentifier": oapi.client.format_argument_value(
                    "lastIdentifier",
                    last_identifier,
                    style="form",
                    explode=False,
                ),
                "additionalLastIdentifier": oapi.client.format_argument_value(
                    "additionalLastIdentifier",
                    additional_last_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentStyleStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "developmentStyleStatusIndicator",
                    development_style_status_indicator,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayDescription": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayDescription",
                    development_colorway_description,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayType": oapi.client.format_argument_value(
                    "developmentColorwayType",
                    development_colorway_type,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayState": oapi.client.format_argument_value(
                    "developmentColorwayState",
                    development_colorway_state,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayGate": oapi.client.format_argument_value(
                    "developmentColorwayGate",
                    development_colorway_gate,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayStatusIndicator",
                    development_colorway_status_indicator,
                    style="form",
                    explode=False,
                ),
                "developmentStyleType": oapi.client.format_argument_value(
                    "developmentStyleType",
                    development_style_type,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_data_development_styles_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.DataDevelopmentStylesObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentStyleResponse:
        """
        How you get a single development style data

        Parameters:

        - object_id:
          A single Id of the object (in this case Development Style Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/developmentStyles/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentStyleResponse,
            )
        )

    def get_search_development_styles(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        development_style_name: typing.Optional[
            model.SearchDevelopmentStylesGetDevelopmentStyleName
        ] = None,
        model_identifier: typing.Optional[
            model.SearchDevelopmentStylesGetModelIdentifier
        ] = None,
        style_number: typing.Optional[
            model.SearchDevelopmentStylesGetStyleNumber
        ] = None,
        last_identifier: typing.Optional[
            model.SearchDevelopmentStylesGetLastIdentifier
        ] = None,
        additional_last_identifier: typing.Optional[
            model.SearchDevelopmentStylesGetAdditionalLastIdentifier
        ] = None,
        development_style_status_indicator: typing.Optional[
            bool
        ] = None,
        development_style_type: typing.Optional[
            model.SearchDevelopmentStylesGetDevelopmentStyleType
        ] = None,
        division: typing.Optional[
            model.SearchDevelopmentStylesGetDivision
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the development
        style entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - development_style_name:
          The reference key associated with this item
        - model_identifier:
          The reference key associated with this item
        - style_number:
          The reference key associated with this item
        - last_identifier:
          The reference key associated with this item
        - additional_last_identifier:
          The reference key associated with this item
        - development_style_status_indicator:
          The true or false flag associated with this item
        - development_style_type:
          The reference key associated with this item
        - division:
          The reference key associated with this item
        """
        response: sob.abc.Readable = self.request(
            "/search/developmentStyles",
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
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "developmentStyleName": oapi.client.format_argument_value(
                    "developmentStyleName",
                    development_style_name,
                    style="form",
                    explode=False,
                ),
                "modelIdentifier": oapi.client.format_argument_value(
                    "modelIdentifier",
                    model_identifier,
                    style="form",
                    explode=False,
                ),
                "styleNumber": oapi.client.format_argument_value(
                    "styleNumber",
                    style_number,
                    style="form",
                    explode=False,
                ),
                "lastIdentifier": oapi.client.format_argument_value(
                    "lastIdentifier",
                    last_identifier,
                    style="form",
                    explode=False,
                ),
                "additionalLastIdentifier": oapi.client.format_argument_value(
                    "additionalLastIdentifier",
                    additional_last_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentStyleStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "developmentStyleStatusIndicator",
                    development_style_status_indicator,
                    style="form",
                    explode=False,
                ),
                "developmentStyleType": oapi.client.format_argument_value(
                    "developmentStyleType",
                    development_style_type,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_data_bill_of_materials_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataBillOfMaterialsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.BillOfMaterialsResponse:
        """
        How you get a single bill of materials.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product Development Bill Of
          Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/billOfMaterials/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.BillOfMaterialsResponse,
            )
        )

    def get_data_bill_of_materials(
        self,
        object_id: model.DataBillOfMaterialsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataBillOfMaterialsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.BillOfMaterialsBulkResponse:
        """
        How you get bill of materials in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product
          Development Bill Of Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/billOfMaterials",
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
                model.BillOfMaterialsBulkResponse,
            )
        )

    def get_search_bill_of_materials(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        bom_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetBomIdentifier
        ] = None,
        development_colorway_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetDevelopmentColorwayIdentifier
        ] = None,
        bom_name: typing.Optional[
            model.SearchBillOfMaterialsGetBomName
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetDevelopmentColorwaySeasonIdentifier
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetSourcingConfigurationIdentifier
        ] = None,
        sourcing_configuration_season: typing.Optional[
            model.SearchBillOfMaterialsGetSourcingConfigurationSeason
        ] = None,
        development_style_type: typing.Optional[
            model.SearchBillOfMaterialsGetDevelopmentStyleType
        ] = None,
        division: typing.Optional[
            model.SearchBillOfMaterialsGetDivision
        ] = None,
        bom_description: typing.Optional[
            model.SearchBillOfMaterialsGetBomDescription
        ] = None,
        bom_comments: typing.Optional[
            model.SearchBillOfMaterialsGetBomComments
        ] = None,
        bill_of_material_status_indicator: typing.Optional[
            model.SearchBillOfMaterialsGetBillOfMaterialStatusIndicator
        ] = None,
        bom_line_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetBomLineItemIdentifier
        ] = None,
        bom_line_item_comments: typing.Optional[
            model.SearchBillOfMaterialsGetBomLineItemComments
        ] = None,
        bom_line_item_number: typing.Optional[
            model.SearchBillOfMaterialsGetBomLineItemNumber
        ] = None,
        parent_bom_line_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetParentBomLineItemIdentifier
        ] = None,
        line_item_quantity: typing.Optional[
            model.SearchBillOfMaterialsGetLineItemQuantity
        ] = None,
        color: typing.Optional[
            model.SearchBillOfMaterialsGetColor
        ] = None,
        bill_of_materials_section: typing.Optional[
            model.SearchBillOfMaterialsGetBillOfMaterialsSection
        ] = None,
        part_primary: typing.Optional[
            model.SearchBillOfMaterialsGetPartPrimary
        ] = None,
        part_secondary: typing.Optional[
            model.SearchBillOfMaterialsGetPartSecondary
        ] = None,
        part_modifier: typing.Optional[
            model.SearchBillOfMaterialsGetPartModifier
        ] = None,
        part_suffix: typing.Optional[
            model.SearchBillOfMaterialsGetPartSuffix
        ] = None,
        part_name: typing.Optional[
            model.SearchBillOfMaterialsGetPartName
        ] = None,
        material_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetMaterialItemIdentifier
        ] = None,
        supplied_material: typing.Optional[
            model.SearchBillOfMaterialsGetSuppliedMaterial
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            model.SearchBillOfMaterialsGetSuppliedMaterialColorIdentifier
        ] = None,
        supplied_material_color_is_multiple_colors: typing.Optional[
            model.SearchBillOfMaterialsGetSuppliedMaterialColorIsMultipleColors
        ] = None,
        color_placeholder_description: typing.Optional[
            model.SearchBillOfMaterialsGetColorPlaceholderDescription
        ] = None,
        material_item_placeholder_description: typing.Optional[
            model.SearchBillOfMaterialsGetMaterialItemPlaceholderDescription
        ] = None,
        bom_guid: typing.Optional[
            model.SearchBillOfMaterialsGetBomGUID
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the BOM entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - bom_identifier:
          The reference key associated with this item
        - development_colorway_identifier:
          The reference key associated with this item
        - bom_name:
          The reference key associated with this item
        - development_colorway_season_identifier:
          The reference key associated with this item
        - sourcing_configuration_identifier:
          The reference key associated with this item
        - sourcing_configuration_season:
          The reference key associated with this item
        - development_style_type:
          The reference key associated with this item
        - division:
          The reference key associated with this item
        - bom_description:
          The reference key associated with this item
        - bom_comments:
          The reference key associated with this item
        - bill_of_material_status_indicator:
          The reference key associated with this item
        - bom_line_item_identifier:
          The reference key associated with this item
        - bom_line_item_comments:
          The reference key associated with this item
        - bom_line_item_number:
          The reference key associated with this item
        - parent_bom_line_item_identifier:
          The reference key associated with this item
        - line_item_quantity:
          The reference key associated with this item
        - color:
          The reference key associated with this item
        - bill_of_materials_section:
          The reference key associated with this item
        - part_primary:
          The reference key associated with this item
        - part_secondary:
          The reference key associated with this item
        - part_modifier:
          The reference key associated with this item
        - part_suffix:
          The reference key associated with this item
        - part_name:
          The reference key associated with this item
        - material_item_identifier:
          The reference key associated with this item
        - supplied_material:
          The reference key associated with this item
        - supplied_material_color_identifier:
          The reference key associated with this item
        - supplied_material_color_is_multiple_colors:
          The reference key associated with this item
        - color_placeholder_description:
          The reference key associated with this item
        - material_item_placeholder_description:
          The reference key associated with this item
        - bom_guid:
          The Bill of Material's Universally Unique Identifier
        """
        response: sob.abc.Readable = self.request(
            "/search/billOfMaterials",
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
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "bomIdentifier": oapi.client.format_argument_value(
                    "bomIdentifier",
                    bom_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayIdentifier",
                    development_colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "bomName": oapi.client.format_argument_value(
                    "bomName",
                    bom_name,
                    style="form",
                    explode=False,
                ),
                "developmentColorwaySeasonIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentColorwaySeasonIdentifier",
                    development_colorway_season_identifier,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationIdentifier": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationIdentifier",
                    sourcing_configuration_identifier,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationSeason": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationSeason",
                    sourcing_configuration_season,
                    style="form",
                    explode=False,
                ),
                "developmentStyleType": oapi.client.format_argument_value(
                    "developmentStyleType",
                    development_style_type,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "bomDescription": oapi.client.format_argument_value(
                    "bomDescription",
                    bom_description,
                    style="form",
                    explode=False,
                ),
                "bomComments": oapi.client.format_argument_value(
                    "bomComments",
                    bom_comments,
                    style="form",
                    explode=False,
                ),
                "billOfMaterialStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "billOfMaterialStatusIndicator",
                    bill_of_material_status_indicator,
                    style="form",
                    explode=False,
                ),
                "bomLineItemIdentifier": oapi.client.format_argument_value(
                    "bomLineItemIdentifier",
                    bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "bomLineItemComments": oapi.client.format_argument_value(
                    "bomLineItemComments",
                    bom_line_item_comments,
                    style="form",
                    explode=False,
                ),
                "bomLineItemNumber": oapi.client.format_argument_value(
                    "bomLineItemNumber",
                    bom_line_item_number,
                    style="form",
                    explode=False,
                ),
                "parentBomLineItemIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentBomLineItemIdentifier",
                    parent_bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "lineItemQuantity": oapi.client.format_argument_value(
                    "lineItemQuantity",
                    line_item_quantity,
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    color,
                    style="form",
                    explode=False,
                ),
                "billOfMaterialsSection": oapi.client.format_argument_value(
                    "billOfMaterialsSection",
                    bill_of_materials_section,
                    style="form",
                    explode=False,
                ),
                "partPrimary": oapi.client.format_argument_value(
                    "partPrimary",
                    part_primary,
                    style="form",
                    explode=False,
                ),
                "partSecondary": oapi.client.format_argument_value(
                    "partSecondary",
                    part_secondary,
                    style="form",
                    explode=False,
                ),
                "partModifier": oapi.client.format_argument_value(
                    "partModifier",
                    part_modifier,
                    style="form",
                    explode=False,
                ),
                "partSuffix": oapi.client.format_argument_value(
                    "partSuffix",
                    part_suffix,
                    style="form",
                    explode=False,
                ),
                "partName": oapi.client.format_argument_value(
                    "partName",
                    part_name,
                    style="form",
                    explode=False,
                ),
                "materialItemIdentifier": oapi.client.format_argument_value(
                    "materialItemIdentifier",
                    material_item_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterial": oapi.client.format_argument_value(
                    "suppliedMaterial",
                    supplied_material,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    supplied_material_color_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIsMultipleColors",
                    supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "colorPlaceholderDescription": oapi.client.format_argument_value(  # noqa
                    "colorPlaceholderDescription",
                    color_placeholder_description,
                    style="form",
                    explode=False,
                ),
                "materialItemPlaceholderDescription": oapi.client.format_argument_value(  # noqa
                    "materialItemPlaceholderDescription",
                    material_item_placeholder_description,
                    style="form",
                    explode=False,
                ),
                "bomGUID": oapi.client.format_argument_value(
                    "bomGUID",
                    bom_guid,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_data_bill_of_materials_sources_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataBillOfMaterialsSourcesObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.BillOfMaterialsSourceResponse:
        """
        How you get a single bill of materials by Source.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product Development Bill Of
          Materials by Source)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/billOfMaterials/sources/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.BillOfMaterialsSourceResponse,
            )
        )

    def get_data_bill_of_materials_sources(
        self,
        object_id: model.DataBillOfMaterialsSourcesGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataBillOfMaterialsSourcesGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.BillOfMaterialsSourceBulkResponse:
        """
        How you get bill of materials by Source in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product
          Development Bill Of Materials)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/billOfMaterials/sources",
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
                model.BillOfMaterialsSourceBulkResponse,
            )
        )

    def get_search_bill_of_materials_sources(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        bom_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBomIdentifier
        ] = None,
        development_colorway_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetDevelopmentColorwayIdentifier
        ] = None,
        bom_name: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBomName
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetDevelopmentColorwaySeasonIdentifier  # noqa
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetSourcingConfigurationIdentifier  # noqa
        ] = None,
        product_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetProductIdentifier
        ] = None,
        style_number: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetStyleNumber
        ] = None,
        sourcing_configuration_season: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetSourcingConfigurationSeason
        ] = None,
        cycle_year: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetCycleYear
        ] = None,
        development_style_type: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetDevelopmentStyleType
        ] = None,
        division: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetDivision
        ] = None,
        bill_of_material_status_indicator: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBillOfMaterialStatusIndicator
        ] = None,
        bom_line_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBomLineItemIdentifier
        ] = None,
        bom_line_item_number: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBomLineItemNumber
        ] = None,
        parent_bom_line_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetParentBomLineItemIdentifier
        ] = None,
        line_item_quantity: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetLineItemQuantity
        ] = None,
        color: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetColor
        ] = None,
        bill_of_materials_section: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBillOfMaterialsSection
        ] = None,
        part: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetPart
        ] = None,
        material_item_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetMaterialItemIdentifier
        ] = None,
        supplied_material: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetSuppliedMaterial
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIdentifier  # noqa
        ] = None,
        supplied_material_color_is_multiple_colors: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIsMultipleColors  # noqa
        ] = None,
        color_placeholder_description: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetColorPlaceholderDescription
        ] = None,
        material_item_placeholder_description: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetMaterialItemPlaceholderDescription  # noqa
        ] = None,
        net_usage: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetNetUsage
        ] = None,
        waste_usage: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetWasteUsage
        ] = None,
        gross_usage: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetGrossUsage
        ] = None,
        usage_unit_of_measure: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetUsageUnitOfMeasure
        ] = None,
        bom_guid: typing.Optional[
            model.SearchBillOfMaterialsSourcesGetBomGUID
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the BOM by Source
        entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - bom_identifier:
          The reference key associated with this item
        - development_colorway_identifier:
          The reference key associated with this item
        - bom_name:
          The reference key associated with this item
        - development_colorway_season_identifier:
          The reference key associated with this item
        - sourcing_configuration_identifier:
          The reference key associated with this item
        - product_identifier:
          The reference key associated with this item
        - style_number:
          The reference key associated with this item
        - sourcing_configuration_season:
          The reference key associated with this item
        - cycle_year:
          The reference key associated with this item
        - development_style_type:
          The reference key associated with this item
        - division:
          The reference key associated with this item
        - bill_of_material_status_indicator:
          The reference key associated with this item
        - bom_line_item_identifier:
          The reference key associated with this item
        - bom_line_item_number:
          The reference key associated with this item
        - parent_bom_line_item_identifier:
          The reference key associated with this item
        - line_item_quantity:
          The reference key associated with this item
        - color:
          The reference key associated with this item
        - bill_of_materials_section:
          The reference key associated with this item
        - part:
          The reference key associated with this item
        - material_item_identifier:
          The reference key associated with this item
        - supplied_material:
          The reference key associated with this item
        - supplied_material_color_identifier:
          The reference key associated with this item
        - supplied_material_color_is_multiple_colors:
          The reference key associated with this item
        - color_placeholder_description:
          The reference key associated with this item
        - material_item_placeholder_description:
          The reference key associated with this item
        - net_usage:
          The number (float) for netUsage
        - waste_usage:
          The number (float) for wasteUsage
        - gross_usage:
          The number (float) for grossUsage
        - usage_unit_of_measure:
          The reference key associated with this item
        - bom_guid:
          The Bill of Material's Universally Unique Identifier
        """
        response: sob.abc.Readable = self.request(
            "/search/billOfMaterials/sources",
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
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "bomIdentifier": oapi.client.format_argument_value(
                    "bomIdentifier",
                    bom_identifier,
                    style="form",
                    explode=False,
                ),
                "developmentColorwayIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentColorwayIdentifier",
                    development_colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "bomName": oapi.client.format_argument_value(
                    "bomName",
                    bom_name,
                    style="form",
                    explode=False,
                ),
                "developmentColorwaySeasonIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentColorwaySeasonIdentifier",
                    development_colorway_season_identifier,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationIdentifier": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationIdentifier",
                    sourcing_configuration_identifier,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "styleNumber": oapi.client.format_argument_value(
                    "styleNumber",
                    style_number,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationSeason": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationSeason",
                    sourcing_configuration_season,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "developmentStyleType": oapi.client.format_argument_value(
                    "developmentStyleType",
                    development_style_type,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "billOfMaterialStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "billOfMaterialStatusIndicator",
                    bill_of_material_status_indicator,
                    style="form",
                    explode=False,
                ),
                "bomLineItemIdentifier": oapi.client.format_argument_value(
                    "bomLineItemIdentifier",
                    bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "bomLineItemNumber": oapi.client.format_argument_value(
                    "bomLineItemNumber",
                    bom_line_item_number,
                    style="form",
                    explode=False,
                ),
                "parentBomLineItemIdentifier": oapi.client.format_argument_value(  # noqa
                    "parentBomLineItemIdentifier",
                    parent_bom_line_item_identifier,
                    style="form",
                    explode=False,
                ),
                "lineItemQuantity": oapi.client.format_argument_value(
                    "lineItemQuantity",
                    line_item_quantity,
                    style="form",
                    explode=False,
                ),
                "color": oapi.client.format_argument_value(
                    "color",
                    color,
                    style="form",
                    explode=False,
                ),
                "billOfMaterialsSection": oapi.client.format_argument_value(
                    "billOfMaterialsSection",
                    bill_of_materials_section,
                    style="form",
                    explode=False,
                ),
                "part": oapi.client.format_argument_value(
                    "part",
                    part,
                    style="form",
                    explode=False,
                ),
                "materialItemIdentifier": oapi.client.format_argument_value(
                    "materialItemIdentifier",
                    material_item_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterial": oapi.client.format_argument_value(
                    "suppliedMaterial",
                    supplied_material,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIdentifier": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIdentifier",
                    supplied_material_color_identifier,
                    style="form",
                    explode=False,
                ),
                "suppliedMaterialColorIsMultipleColors": oapi.client.format_argument_value(  # noqa
                    "suppliedMaterialColorIsMultipleColors",
                    supplied_material_color_is_multiple_colors,
                    style="form",
                    explode=False,
                ),
                "colorPlaceholderDescription": oapi.client.format_argument_value(  # noqa
                    "colorPlaceholderDescription",
                    color_placeholder_description,
                    style="form",
                    explode=False,
                ),
                "materialItemPlaceholderDescription": oapi.client.format_argument_value(  # noqa
                    "materialItemPlaceholderDescription",
                    material_item_placeholder_description,
                    style="form",
                    explode=False,
                ),
                "netUsage": oapi.client.format_argument_value(
                    "netUsage",
                    net_usage,
                    style="form",
                    explode=False,
                ),
                "wasteUsage": oapi.client.format_argument_value(
                    "wasteUsage",
                    waste_usage,
                    style="form",
                    explode=False,
                ),
                "grossUsage": oapi.client.format_argument_value(
                    "grossUsage",
                    gross_usage,
                    style="form",
                    explode=False,
                ),
                "usageUnitOfMeasure": oapi.client.format_argument_value(
                    "usageUnitOfMeasure",
                    usage_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "bomGUID": oapi.client.format_argument_value(
                    "bomGUID",
                    bom_guid,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_data_sourcing_configurations_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataSourcingConfigurationsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SourcingConfigurationsResponse:
        """
        How you get a single Source Configuration Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Source Configuration
          Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/sourcingConfigurations/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.SourcingConfigurationsResponse,
            )
        )

    def get_data_sourcing_configurations(
        self,
        object_id: model.DataSourcingConfigurationsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataSourcingConfigurationsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SourcingConfigurationsBulkResponse:
        """
        How you get Source Configuration Data in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Source
          Configuration Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/sourcingConfigurations/",
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
                model.SourcingConfigurationsBulkResponse,
            )
        )

    def get_data_sourcing_configurations_colorway_seasons_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataSourcingConfigurationsColorwaySeasonsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SourcingConfigurationsColorwaySeasonResponse:
        """
        How you get a single Source Configuration Colorway Season Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Source Configuration Colorway
          Season Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/sourcingConfigurations/colorwaySeasons/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.SourcingConfigurationsColorwaySeasonResponse,
            )
        )

    def get_data_sourcing_configurations_colorway_seasons(
        self,
        object_id: model.DataSourcingConfigurationsColorwaySeasonsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataSourcingConfigurationsColorwaySeasonsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SourcingConfigurationsColorwaySeasonBulkResponse:
        """
        How you get Source Configuration Colorway Season Data in a Bulk
        fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Source
          Configuration Colorway Season Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/sourcingConfigurations/colorwaySeasons",
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
                model.SourcingConfigurationsColorwaySeasonBulkResponse,
            )
        )

    def get_data_development_samples_samples_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataDevelopmentSamplesSamplesObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentSampleResponse:
        """
        How you get a single Development Sample Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Development Sample Identifier
          )
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/developmentSamples/samples/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentSampleResponse,
            )
        )

    def get_data_development_samples_shipments_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataDevelopmentSamplesShipmentsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentSampleShipmentResponse:
        """
        How you get a single Development Sample Shipment Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Development Sample Identifier
          )
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/developmentSamples/shipments/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentSampleShipmentResponse,
            )
        )

    def get_data_measurement_sets_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataMeasurementSetsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentMeasurementResponse:
        """
        How you get a single Development Measurement Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Development Measurement
          Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/measurementSets/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentMeasurementResponse,
            )
        )

    def get_search_measurement_sets(
        self,
        *,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        q: typing.Optional[
            str
        ] = "",
        measurement_set_name: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementSetName
        ] = None,
        measurement_set_state: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementSetState
        ] = None,
        development_style_identifier: typing.Optional[
            model.SearchMeasurementSetsGetDevelopmentStyleIdentifier
        ] = None,
        style_number: typing.Optional[
            model.SearchMeasurementSetsGetStyleNumber
        ] = None,
        cycle_year: typing.Optional[
            model.SearchMeasurementSetsGetCycleYear
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            model.SearchMeasurementSetsGetSourcingConfigurationIdentifier
        ] = None,
        sourcing_configuration_season_identifier: typing.Optional[
            model.SearchMeasurementSetsGetSourcingConfigurationSeasonIdentifier
        ] = None,
        measurement_set_template_name: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementSetTemplateName
        ] = None,
        size_definition_template: typing.Optional[
            model.SearchMeasurementSetsGetSizeDefinitionTemplate
        ] = None,
        grade_rule_template: typing.Optional[
            model.SearchMeasurementSetsGetGradeRuleTemplate
        ] = None,
        measurement_template_type: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementTemplateType
        ] = None,
        development_style_size_definition: typing.Optional[
            model.SearchMeasurementSetsGetDevelopmentStyleSizeDefinition
        ] = None,
        measurement_value_unit_of_measure: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementValueUnitOfMeasure
        ] = None,
        base_size: typing.Optional[
            model.SearchMeasurementSetsGetBaseSize
        ] = None,
        size_selection_list: typing.Optional[
            model.SearchMeasurementSetsGetSizeSelectionList
        ] = None,
        size: typing.Optional[
            model.SearchMeasurementSetsGetSize
        ] = None,
        measurement_code: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementCode
        ] = None,
        point_of_measurement_name: typing.Optional[
            model.SearchMeasurementSetsGetPointOfMeasurementName
        ] = None,
        sort_order: typing.Optional[
            model.SearchMeasurementSetsGetSortOrder
        ] = None,
        measurement_instructions: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementInstructions
        ] = None,
        measurement_detail: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementDetail
        ] = None,
        point_of_measurement_criticality: typing.Optional[
            model.SearchMeasurementSetsGetPointOfMeasurementCriticality
        ] = None,
        tolerance_negative: typing.Optional[
            model.SearchMeasurementSetsGetToleranceNegative
        ] = None,
        tolerance_positive: typing.Optional[
            model.SearchMeasurementSetsGetTolerancePositive
        ] = None,
        measurement_size_value: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementSizeValue
        ] = None,
        point_of_measurement: typing.Optional[
            model.SearchMeasurementSetsGetPointOfMeasurement
        ] = None,
        measurement_set_status_indicator: typing.Optional[
            model.SearchMeasurementSetsGetMeasurementSetStatusIndicator
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Development
        Measurement Set entity

        Parameters:

        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - q:
          This parameter is how you pass free text search, if any string is
          passed here it will be searched as free text
        - measurement_set_name
        - measurement_set_state
        - development_style_identifier
        - style_number
        - cycle_year
        - sourcing_configuration_identifier
        - sourcing_configuration_season_identifier
        - measurement_set_template_name
        - size_definition_template
        - grade_rule_template
        - measurement_template_type
        - development_style_size_definition
        - measurement_value_unit_of_measure
        - base_size
        - size_selection_list
        - size
        - measurement_code
        - point_of_measurement_name
        - sort_order
        - measurement_instructions
        - measurement_detail
        - point_of_measurement_criticality
        - tolerance_negative
        - tolerance_positive
        - measurement_size_value
        - point_of_measurement
        - measurement_set_status_indicator
        """
        response: sob.abc.Readable = self.request(
            "/search/measurementSets",
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
                "count": oapi.client.format_argument_value(
                    "count",
                    count,
                    style="form",
                    explode=False,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=False,
                ),
                "q": oapi.client.format_argument_value(
                    "q",
                    q,
                    style="form",
                    explode=False,
                ),
                "measurementSetName": oapi.client.format_argument_value(
                    "measurementSetName",
                    measurement_set_name,
                    style="form",
                    explode=False,
                ),
                "measurementSetState": oapi.client.format_argument_value(
                    "measurementSetState",
                    measurement_set_state,
                    style="form",
                    explode=False,
                ),
                "developmentStyleIdentifier": oapi.client.format_argument_value(  # noqa
                    "developmentStyleIdentifier",
                    development_style_identifier,
                    style="form",
                    explode=False,
                ),
                "styleNumber": oapi.client.format_argument_value(
                    "styleNumber",
                    style_number,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationIdentifier": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationIdentifier",
                    sourcing_configuration_identifier,
                    style="form",
                    explode=False,
                ),
                "sourcingConfigurationSeasonIdentifier": oapi.client.format_argument_value(  # noqa
                    "sourcingConfigurationSeasonIdentifier",
                    sourcing_configuration_season_identifier,
                    style="form",
                    explode=False,
                ),
                "measurementSetTemplateName": oapi.client.format_argument_value(  # noqa
                    "measurementSetTemplateName",
                    measurement_set_template_name,
                    style="form",
                    explode=False,
                ),
                "sizeDefinitionTemplate": oapi.client.format_argument_value(
                    "sizeDefinitionTemplate",
                    size_definition_template,
                    style="form",
                    explode=False,
                ),
                "gradeRuleTemplate": oapi.client.format_argument_value(
                    "gradeRuleTemplate",
                    grade_rule_template,
                    style="form",
                    explode=False,
                ),
                "measurementTemplateType": oapi.client.format_argument_value(
                    "measurementTemplateType",
                    measurement_template_type,
                    style="form",
                    explode=False,
                ),
                "developmentStyleSizeDefinition": oapi.client.format_argument_value(  # noqa
                    "developmentStyleSizeDefinition",
                    development_style_size_definition,
                    style="form",
                    explode=False,
                ),
                "measurementValueUnitOfMeasure": oapi.client.format_argument_value(  # noqa
                    "measurementValueUnitOfMeasure",
                    measurement_value_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "baseSize": oapi.client.format_argument_value(
                    "baseSize",
                    base_size,
                    style="form",
                    explode=False,
                ),
                "sizeSelectionList": oapi.client.format_argument_value(
                    "sizeSelectionList",
                    size_selection_list,
                    style="form",
                    explode=False,
                ),
                "size": oapi.client.format_argument_value(
                    "size",
                    size,
                    style="form",
                    explode=False,
                ),
                "measurementCode": oapi.client.format_argument_value(
                    "measurementCode",
                    measurement_code,
                    style="form",
                    explode=False,
                ),
                "pointOfMeasurementName": oapi.client.format_argument_value(
                    "pointOfMeasurementName",
                    point_of_measurement_name,
                    style="form",
                    explode=False,
                ),
                "sortOrder": oapi.client.format_argument_value(
                    "sortOrder",
                    sort_order,
                    style="form",
                    explode=False,
                ),
                "measurementInstructions": oapi.client.format_argument_value(
                    "measurementInstructions",
                    measurement_instructions,
                    style="form",
                    explode=False,
                ),
                "measurementDetail": oapi.client.format_argument_value(
                    "measurementDetail",
                    measurement_detail,
                    style="form",
                    explode=False,
                ),
                "pointOfMeasurementCriticality": oapi.client.format_argument_value(  # noqa
                    "pointOfMeasurementCriticality",
                    point_of_measurement_criticality,
                    style="form",
                    explode=False,
                ),
                "toleranceNegative": oapi.client.format_argument_value(
                    "toleranceNegative",
                    tolerance_negative,
                    style="form",
                    explode=False,
                ),
                "tolerancePositive": oapi.client.format_argument_value(
                    "tolerancePositive",
                    tolerance_positive,
                    style="form",
                    explode=False,
                ),
                "measurementSizeValue": oapi.client.format_argument_value(
                    "measurementSizeValue",
                    measurement_size_value,
                    style="form",
                    explode=False,
                ),
                "pointOfMeasurement": oapi.client.format_argument_value(
                    "pointOfMeasurement",
                    point_of_measurement,
                    style="form",
                    explode=False,
                ),
                "measurementSetStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "measurementSetStatusIndicator",
                    measurement_set_status_indicator,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SearchResponse,
            )
        )

    def get_data_points_of_measurement_object_id(
        self,
        object_id: str,
        *,
        dataunits: typing.Optional[
            model.DataPointsOfMeasurementObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.DevelopmentPointOfMeasurementResponse:
        """
        How you get a single Development Point of Measurement Data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Development Point of
          Measurement Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/pointsOfMeasurement/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.DevelopmentPointOfMeasurementResponse,
            )
        )
