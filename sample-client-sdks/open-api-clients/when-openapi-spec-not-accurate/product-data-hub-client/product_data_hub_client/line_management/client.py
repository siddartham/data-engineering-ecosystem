import datetime
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

    def get_line_management_data_product_offerings_global_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsGlobalObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.GlobalOfferingResponse:
        """
        How you get a single global offering.

        Parameters:

        - object_id:
          A single Id of the object (in this case Line Management Product
          Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/global/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.GlobalOfferingResponse,
            )
        )

    def get_line_management_data_product_offerings_global(
        self,
        object_id: model.LineManagementDataProductOfferingsGlobalGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsGlobalGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.GlobalOfferingBulkResponse:
        """
        How you get global offering in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Line
          Management Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/global",
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
                model.GlobalOfferingBulkResponse,
            )
        )

    def get_line_management_data_product_offerings_geography_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsGeographyObjectIdGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.GeographyOfferingResponse:
        """
        How you get a single Geography Offering data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Line Management Geography
          Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/geography/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.GeographyOfferingResponse,
            )
        )

    def get_line_management_data_product_offerings_geography(
        self,
        object_id: model.LineManagementDataProductOfferingsGeographyGetObjectId,  # noqa
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsGeographyGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.GeographyOfferingBulkResponse:
        """
        How you get geography offering in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Line
          Management Geography Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/geography",
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
                model.GeographyOfferingBulkResponse,
            )
        )

    def get_line_management_data_product_offerings_country_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsCountryObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.CountryOfferingResponse:
        """
        How you get a single Country Offering data.

        Parameters:

        - object_id:
          A single Id of the object (in this case Line Management Country
          Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/country/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.CountryOfferingResponse,
            )
        )

    def get_line_management_data_product_offerings_country(
        self,
        object_id: model.LineManagementDataProductOfferingsCountryGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsCountryGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.CountryOfferingBulkResponse:
        """
        How you get country offering in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Line
          Management Country Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/country",
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
                model.CountryOfferingBulkResponse,
            )
        )

    def get_line_management_data_product_offerings_country_object_id_prices(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsCountryObjectIdPricesGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.CountryPriceResponse:
        """
        How you get Country Product Offering Price data.  Source data is CDB.

        Parameters:

        - object_id:
          A single Id of the object (in this case Line Management Country
          Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/country/{objectId}/prices".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.CountryPriceResponse,
            )
        )

    def get_line_management_data_product_offerings_country_prices(
        self,
        object_id: model.LineManagementDataProductOfferingsCountryPricesGetObjectId,  # noqa
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductOfferingsCountryPricesGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.CountryPriceBulkResponse:
        """
        How you get country product offering price in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Line
          Management Country Product Offering ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productOfferings/country/prices",
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
                model.CountryPriceBulkResponse,
            )
        )

    def get_line_management_data_product_style_translations_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductStyleTranslationsObjectIdGetDataunits  # noqa
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductStyleTranslationsResponse:
        """
        How you get product and style translation data by country and language.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productStyleTranslations/{objectId}".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductStyleTranslationsResponse,
            )
        )

    def get_line_management_data_product_style_translations(
        self,
        object_id: model.LineManagementDataProductStyleTranslationsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductStyleTranslationsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductStyleTranslationsBulkResponse:
        """
        How you get product and style translation data by country and language
        in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productStyleTranslations",
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
                model.ProductStyleTranslationsBulkResponse,
            )
        )

    def get_line_management_data_product_sizes_gtin_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductSizesGTINObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductSizeGTINResponse:
        """
        How you get GTIN data by size including alternate sizes.  Source data
        is CDB.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productSizesGTIN/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductSizeGTINResponse,
            )
        )

    def get_line_management_data_product_sizes_gtin(
        self,
        object_id: model.LineManagementDataProductSizesGTINGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductSizesGTINGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductSizeGTINBulkResponse:
        """
        How you get GTIN data by size including alternate sizes in a Bulk
        fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productSizesGTIN",
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
                model.ProductSizeGTINBulkResponse,
            )
        )

    def get_line_management_data_product_regions_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductRegionsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductRegionLMResponse:
        """
        How you get Product Region data from CDB for Line Management

        Parameters:

        - object_id:
          A single Id of the object (in this case the ID will be a combination
          of Product ID and Region)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productRegions/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductRegionLMResponse,
            )
        )

    def get_line_management_data_product_regions(
        self,
        object_id: model.LineManagementDataProductRegionsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductRegionsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductRegionLMBulkResponse:
        """
        How you get Product Region data from CDB for Line Management in a Bulk
        fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productRegions/",
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
                model.ProductRegionLMBulkResponse,
            )
        )

    def get_supply_chain_enablement_data_product_regions_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.SupplyChainEnablementDataProductRegionsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductRegionSCResponse:
        """
        How you get Product Region data from CDB for Supply Chain

        Parameters:

        - object_id:
          A single Id of the object (in this case the ID will be a combination
          of Product ID and Region)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/productRegions/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductRegionSCResponse,
            )
        )

    def get_supply_chain_enablement_data_product_regions(
        self,
        object_id: model.SupplyChainEnablementDataProductRegionsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.SupplyChainEnablementDataProductRegionsGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductRegionSCBulkResponse:
        """
        How you get Product Region data from CDB for Supply Chain in a Bulk
        fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/supplyChainEnablement/data/productRegions/",
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
                model.ProductRegionSCBulkResponse,
            )
        )

    def get_sales_operations_data_product_sizes_nrf_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.SalesOperationsDataProductSizesNRFObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductSizeNRFResponse:
        """
        How you get NRF data by size.

        Parameters:

        - object_id:
          A single Id of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/salesOperations/data/productSizesNRF/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductSizeNRFResponse,
            )
        )

    def get_sales_operations_data_product_sizes_nrf(
        self,
        object_id: model.SalesOperationsDataProductSizesNRFGetObjectId,
        *,
        dataunits: typing.Optional[
            model.SalesOperationsDataProductSizesNRFGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductSizeNRFBulkResponse:
        """
        How you get NRF data by size in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Product ID)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/salesOperations/data/productSizesNRF/",
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
                model.ProductSizeNRFBulkResponse,
            )
        )

    def get_line_management_data_product_styles_fedas_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductStylesFEDASObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductStyleFEDASResponse:
        """
        How you get FEDAS Code by style.

        Parameters:

        - object_id:
          A single Id of the object (in this case Style Number)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productStylesFEDAS/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.ProductStyleFEDASResponse,
            )
        )

    def get_line_management_data_product_styles_fedas(
        self,
        object_id: model.LineManagementDataProductStylesFEDASGetObjectId,
        *,
        dataunits: typing.Optional[
            model.LineManagementDataProductStylesFEDASGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ProductStyleFEDASBulkResponse:
        """
        How you get FEDAS Code by style in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Style
          Number)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/productStylesFEDAS/",
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
                model.ProductStyleFEDASBulkResponse,
            )
        )

    def get_line_management_search_product_offerings_global(
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
        change_start_time: typing.Optional[
            datetime.datetime
        ] = None,
        change_end_time: typing.Optional[
            datetime.datetime
        ] = None,
        product_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductIdentifier  # noqa
        ] = None,
        model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelOfferingIdentifier  # noqa
        ] = None,
        earliest_allowed_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetEarliestAllowedOfferDate  # noqa
        ] = None,
        restricted_to_location: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetRestrictedToLocation  # noqa
        ] = None,
        marketing_initiative: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetMarketingInitiative  # noqa
        ] = None,
        alternate_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetAlternateMarketingType  # noqa
        ] = None,
        product_alternate_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductAlternateTypeGroup  # noqa
        ] = None,
        special_offering_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSpecialOfferingType  # noqa
        ] = None,
        launch: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLaunch
        ] = None,
        primary_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPrimaryMarketingType  # noqa
        ] = None,
        product_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductTypeGroup
        ] = None,
        always_available_global_indicator: typing.Optional[
            bool
        ] = None,
        smu_account: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSmuAccount
        ] = None,
        development_team: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetDevelopmentTeam
        ] = None,
        initiating_product_line_manager_user_account_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetInitiatingProductLineManagerUserAccountCode  # noqa
        ] = None,
        category_information_analyst_user_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetCategoryInformationAnalystUserCode  # noqa
        ] = None,
        product_creation_initiator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductCreationInitiator  # noqa
        ] = None,
        sales_sample_type_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSalesSampleTypeDescription  # noqa
        ] = None,
        samm_sample_type_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSAMMSampleTypeDescription  # noqa
        ] = None,
        sales_sample_size_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSalesSampleSizeDescription  # noqa
        ] = None,
        style_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleCarryoverStatusIndicator  # noqa
        ] = None,
        product_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductCarryoverStatusIndicator  # noqa
        ] = None,
        product_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductOfferingStatusIndicator  # noqa
        ] = None,
        model_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelIdentifier
        ] = None,
        product_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductCode
        ] = None,
        style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleNumber
        ] = None,
        colorway_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetColorwayCode
        ] = None,
        dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetDimension
        ] = None,
        fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetFit
        ] = None,
        product_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductInitialSeasonYear  # noqa
        ] = None,
        master_size_grid: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetMasterSizeGrid
        ] = None,
        retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetRetailSizeRangeDescription  # noqa
        ] = None,
        retail_size_run_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetRetailSizeRunDescription  # noqa
        ] = None,
        retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetRetailSizeSelectionList  # noqa
        ] = None,
        promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPromoSizeRangeDescription  # noqa
        ] = None,
        promo_size_run_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPromoSizeRunDescription  # noqa
        ] = None,
        promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPromoSizeSelectionList  # noqa
        ] = None,
        colorway_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetColorwayIdentifier  # noqa
        ] = None,
        primary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPrimaryColor
        ] = None,
        secondary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSecondaryColor
        ] = None,
        tertiary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetTertiaryColor
        ] = None,
        quaternary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetQuaternaryColor
        ] = None,
        logo_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLogoColor
        ] = None,
        logo_accent_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLogoAccentColor
        ] = None,
        athlete: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetAthlete
        ] = None,
        playerway_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPlayerwayNumber
        ] = None,
        uniform_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetUniformType
        ] = None,
        royalty_intent_indicator: typing.Optional[
            bool
        ] = None,
        product_lifecycle: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductLifecycle
        ] = None,
        closeout_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetCloseoutDate
        ] = None,
        category: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetCategory
        ] = None,
        sub_category: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSubCategory
        ] = None,
        global_category_core_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetGlobalCategoryCoreFocus  # noqa
        ] = None,
        product_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductStatusIndicator  # noqa
        ] = None,
        final_adopt_indicator: typing.Optional[
            bool
        ] = None,
        style_fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleFit
        ] = None,
        style_dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleDimension
        ] = None,
        style_initial_season_year_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleInitialSeasonYearCode  # noqa
        ] = None,
        style_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleDescription
        ] = None,
        segment: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSegment
        ] = None,
        sub_brand: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSubBrand
        ] = None,
        sport_activity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSportActivity
        ] = None,
        silo: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSilo
        ] = None,
        sub_category_breakdown: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSubCategoryBreakdown  # noqa
        ] = None,
        style_merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleMerchandisingClassification  # noqa
        ] = None,
        harmonized_style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetHarmonizedStyleNumber  # noqa
        ] = None,
        construction_method: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConstructionMethod  # noqa
        ] = None,
        finished_goods_indicator: typing.Optional[
            bool
        ] = None,
        style_graphic_indicator: typing.Optional[
            bool
        ] = None,
        style_print_indicator: typing.Optional[
            bool
        ] = None,
        feature: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetFeature
        ] = None,
        material_intent: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetMaterialIntent
        ] = None,
        brand_mark: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetBrandMark
        ] = None,
        blank_usage_indicator: typing.Optional[
            bool
        ] = None,
        additional_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetAdditionalPlatform  # noqa
        ] = None,
        delivery_unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetDeliveryUnitOfMeasure  # noqa
        ] = None,
        consumer_package_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConsumerPackageQuantity  # noqa
        ] = None,
        unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetUnitOfMeasure
        ] = None,
        licensee_product_company: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLicenseeProductCompany  # noqa
        ] = None,
        licensed_indicator: typing.Optional[
            bool
        ] = None,
        technology: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetTechnology
        ] = None,
        style_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleGroup
        ] = None,
        style_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleGroupType
        ] = None,
        sport_level: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSportLevel
        ] = None,
        team: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetTeam
        ] = None,
        league: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLeague
        ] = None,
        style_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetStyleStatusIndicator  # noqa
        ] = None,
        season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSeasonYear
        ] = None,
        product_tier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProductTier
        ] = None,
        model_offering_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelOfferingGroup  # noqa
        ] = None,
        model_offering_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelOfferingGroupType  # noqa
        ] = None,
        target_wholesale_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetTargetWholesalePrice  # noqa
        ] = None,
        target_retail_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetTargetRetailPrice  # noqa
        ] = None,
        line_evolution: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetLineEvolution
        ] = None,
        forecast_sustainability_index_score: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetForecastSustainabilityIndexScore  # noqa
        ] = None,
        budget_freeon_board_cost: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetBudgetFreeonBoardCost  # noqa
        ] = None,
        prod_management_forecast_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetProdManagementForecastQuantity  # noqa
        ] = None,
        model_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelOfferingStatusIndicator  # noqa
        ] = None,
        consumer_purpose: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConsumerPurpose
        ] = None,
        consumer_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConsumerFocus
        ] = None,
        consumer_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConsumerGroup
        ] = None,
        consumer_use: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetConsumerUse
        ] = None,
        marketing_name: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetMarketingName
        ] = None,
        business_organization: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetBusinessOrganization  # noqa
        ] = None,
        division: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetDivision
        ] = None,
        gender: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetGender
        ] = None,
        age: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetAge
        ] = None,
        gender_age: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetGenderAge
        ] = None,
        silhouette: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSilhouette
        ] = None,
        silhouette_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetSilhouetteType
        ] = None,
        fit_preference: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetFitPreference
        ] = None,
        merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetMerchandisingClassification  # noqa
        ] = None,
        primary_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetPrimaryPlatform
        ] = None,
        model_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelInitialSeasonYear  # noqa
        ] = None,
        model_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelGroupType
        ] = None,
        model_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalGetModelGroup
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Line Management
        Global Offering entity

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
        - change_start_time:
          This is the Start Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - change_end_time:
          This is the End Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - product_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Identifier">Definition</a>
        - model_offering_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Offering%
          2520Identifier">Definition</a>
        - earliest_allowed_offer_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FEarliest%2520Allowed
          %2520Offer%2520Date">Definition</a>
        - restricted_to_location:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Restricted%2520To%2520Location%2520Identifier">Definition</a>
        - marketing_initiative:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FMarketing%2520Initiative">
          Definition</a>
        - alternate_marketing_type:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FConcept%252FAlternate%
          2520Marketing%2520Type">Definition</a>
        - product_alternate_type_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Group%2520Code">Definition</a>
        - special_offering_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FSpecial%2520Offering%2520Type"
          >Definition</a>
        - launch:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLaunch%2520Code">
          Definition</a>
        - primary_marketing_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Identifier">Definition</a>
        - product_type_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Group%2520Code">Definition</a>
        - always_available_global_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FAlways%
          2520Available%2520Global%2520Indicator">Definition</a>
        - smu_account:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSpecial%2520Make-up%
          2520Account%2520Code">Definition</a>
        - development_team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDevelopment%2520Team
          %2520Identifier">Definition</a>
        - initiating_product_line_manager_user_account_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitiating%
          2520Product%2520Line%2520Manager%2520User%2520Code">Definition</a>
        - category_information_analyst_user_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Creation
          %2520Initiator%2520Identifier">Definition</a>
        - product_creation_initiator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Creation
          %2520Initiator%2520Identifier">Definition</a>
        - sales_sample_type_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSales%2520Sample%
          2520Indicator">Definition</a>
        - samm_sample_type_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSeasonal%
          2520Alignment%2520Merchandising%2520Meeting%2520Sample%2520Indicator"
          >Definition</a>
        - sales_sample_size_description:
          The reference key associated with this item: <a target="_blank" http:
          //nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSales%2520Sample%
          2520Size%2520Description">Definition</a>
        - style_carryover_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Carryover%2520Status%2520Indicator">Definition</a>
        - product_carryover_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Carryover%2520Status%2520Indicator">Definition</a>
        - product_offering_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Offering
          %2520Status%2520Indicator">Definition</a>
        - model_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%
          2520Identifier">Definition</a>
        - product_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Code">
          Definition</a>
        - style_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Code">
          Definition</a>
        - colorway_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Colorway
          %2520Code">Definition</a>
        - dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - product_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - master_size_grid:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMaster%2520Size%
          2520Grid%2520Code">Definition</a>
        - retail_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Range%2520Description">Definition</a>
        - retail_size_run_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Run%2520Description">Definition</a>
        - retail_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Selection%2520List">Definition</a>
        - promo_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromotional%2520Size
          %2520Range%2520Description">Definition</a>
        - promo_size_run_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Run%2520Description">Definition</a>
        - promo_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Selection%2520List">Definition</a>
        - colorway_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FColorway%
          2520Identifier">Definition</a>
        - primary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Color%
          2520Code">Definition</a>
        - secondary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSecondary%2520Color%
          2520Code">Definition</a>
        - tertiary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTertiary%2520Color%
          2520Code">Definition</a>
        - quaternary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FQuaternary%2520Color
          %2520Code">Definition</a>
        - logo_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Color%
          2520Code">Definition</a>
        - logo_accent_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Accent%
          2520Color%2520Code">Definition</a>
        - athlete:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAthlete%
          2520Identifier">Definition</a>
        - playerway_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlayerway%
          2520Number">Definition</a>
        - uniform_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUniform%2520Type%
          2520Identifier">Definition</a>
        - royalty_intent_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FRoyalty%
          2520Intent%2520Indicator">Definition</a>
        - product_lifecycle:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Lifecycle%2520Code">Definition</a>
        - closeout_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FClose%2520Out%
          2520Date">Definition</a>
        - category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCategory%2520Code">
          Definition</a>
        - sub_category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Code">Definition</a>
        - global_category_core_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGlobal%2520Category%
          2520Core%2520Focus%2520Code">Definition</a>
        - product_status_indicator:
          The A or I flag associated with this item: <a target="_blank" href ="
          http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Status%
          2520Indicator">Definition</a>
        - final_adopt_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinal%
          2520Adoption%2520Indicator">Definition</a>
        - style_fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - style_dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - style_initial_season_year_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - style_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%
          2520Description">Definition</a>
        - segment:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSegment%2520Code">
          Definition</a>
        - sub_brand:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Brand%
          2520Code">Definition</a>
        - sport_activity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Activity%
          2520Code">Definition</a>
        - silo:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilo%2520Identifier"
          >Definition</a>
        - sub_category_breakdown:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - style_merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - harmonized_style_number:
          The reference key associated with this item: Harmonized Style Number
        - construction_method:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConstruction%
          2520Identifier">Definition</a>
        - finished_goods_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinished%
          2520Goods%2520Indicator">Definition</a>
        - style_graphic_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Graphic%2520Indicator">Definition</a>
        - style_print_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Print%2520Indicator">Definition</a>
        - feature:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFeature%
          2520Identifier">Definition</a>
        - material_intent:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___search___all___material
          %2520intent%2520identifier">Definition</a>
        - brand_mark:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBrand%2520Mark%
          2520Identifier">Definition</a>
        - blank_usage_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FBlank%
          2520Usage%2520Indicator">Definition</a>
        - additional_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlatform%
          2520Identifier">Definition</a>
        - delivery_unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDelivery%2520Unit%
          2520Quantity">Definition</a>
        - consumer_package_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Package
          %2520Quantity">Definition</a>
        - unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUnit%2520Of%
          2520Measure%2520Code">Definition</a>
        - licensee_product_company:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLicensee%2520Product
          %2520Company%2520Code">Definition</a>
        - licensed_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FLicensed%
          2520Indicator">Definition</a>
        - technology:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTechnology%2520Code"
          >Definition</a>
        - style_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Identifier">Definition</a>
        - style_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Type%2520Identifier">Definition</a>
        - sport_level:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Level%
          2520Identifier">Definition</a>
        - team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTeam%2520Identifier"
          >Definition</a>
        - league:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLeague%
          2520Identifier">Definition</a>
        - style_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStatus%
          2520Indicator">Definition</a>
        - season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCycle%2520Year%
          2520Abbreviation">Definition</a>
        - product_tier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Tier%
          2520Identifier">Definition</a>
        - model_offering_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        - model_offering_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - target_wholesale_price:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTarget%2520Wholesale
          %2520Price">Definition</a>
        - target_retail_price:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTarget%2520Retail%
          2520Price">Definition</a>
        - line_evolution:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLine%2520Evolution%
          2520Identifier">Definition</a>
        - forecast_sustainability_index_score:
          The reference key associated with this item: N/A
        - budget_freeon_board_cost:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBudget%2520Free%
          2520On%2520Board%2520Cost">Definition</a>
        - prod_management_forecast_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Management%2520Forecast%2520Quantity">Definition</a>
        - model_offering_status_indicator:
          The reference key associated with this item:<a target="_blank" href =
          "http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Offering%
          2520Status%2520Indicator">Definition</a>
        - consumer_purpose:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Purpose
          %2520Identifier">Definition</a>
        - consumer_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Focus%
          2520Identifier">Definition</a>
        - consumer_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Group%
          2520Identifier">Definition</a>
        - consumer_use:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Use%
          2520Identifier">Definition</a>
        - marketing_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Name">
          Definition</a>
        - business_organization:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBusiness%
          2520Organization%2520Code">Definition</a>
        - division:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDivision%2520Code">
          Definition</a>
        - gender:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Code">
          Definition</a>
        - age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAge%2520Code">
          Definition</a>
        - gender_age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Age%
          2520Code">Definition</a>
        - silhouette:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Code"
          >Definition</a>
        - silhouette_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Type%
          2520Code">Definition</a>
        - fit_preference:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Preference%
          2520Identifier">Definition</a>
        - merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMerchandising%
          2520Classification%2520Identifier">Definition</a>
        - primary_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Platform
          %2520Identifier">Definition</a>
        - model_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitial%2520Cycle%
          2520Year%2520Code">Definition</a>
        - model_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - model_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productOfferings/global",
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
                "changeStartTime": oapi.client.format_argument_value(
                    "changeStartTime",
                    change_start_time,
                    style="form",
                    explode=False,
                ),
                "changeEndTime": oapi.client.format_argument_value(
                    "changeEndTime",
                    change_end_time,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "modelOfferingIdentifier": oapi.client.format_argument_value(
                    "modelOfferingIdentifier",
                    model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "earliestAllowedOfferDate": oapi.client.format_argument_value(
                    "earliestAllowedOfferDate",
                    earliest_allowed_offer_date,
                    style="form",
                    explode=False,
                ),
                "restrictedToLocation": oapi.client.format_argument_value(
                    "restrictedToLocation",
                    restricted_to_location,
                    style="form",
                    explode=False,
                ),
                "marketingInitiative": oapi.client.format_argument_value(
                    "marketingInitiative",
                    marketing_initiative,
                    style="form",
                    explode=False,
                ),
                "alternateMarketingType": oapi.client.format_argument_value(
                    "alternateMarketingType",
                    alternate_marketing_type,
                    style="form",
                    explode=False,
                ),
                "productAlternateTypeGroup": oapi.client.format_argument_value(
                    "productAlternateTypeGroup",
                    product_alternate_type_group,
                    style="form",
                    explode=False,
                ),
                "specialOfferingType": oapi.client.format_argument_value(
                    "specialOfferingType",
                    special_offering_type,
                    style="form",
                    explode=False,
                ),
                "launch": oapi.client.format_argument_value(
                    "launch",
                    launch,
                    style="form",
                    explode=False,
                ),
                "primaryMarketingType": oapi.client.format_argument_value(
                    "primaryMarketingType",
                    primary_marketing_type,
                    style="form",
                    explode=False,
                ),
                "productTypeGroup": oapi.client.format_argument_value(
                    "productTypeGroup",
                    product_type_group,
                    style="form",
                    explode=False,
                ),
                "alwaysAvailableGlobalIndicator": oapi.client.format_argument_value(  # noqa
                    "alwaysAvailableGlobalIndicator",
                    always_available_global_indicator,
                    style="form",
                    explode=False,
                ),
                "smuAccount": oapi.client.format_argument_value(
                    "smuAccount",
                    smu_account,
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    development_team,
                    style="form",
                    explode=False,
                ),
                "initiatingProductLineManagerUserAccountCode": oapi.client.format_argument_value(  # noqa
                    "initiatingProductLineManagerUserAccountCode",
                    initiating_product_line_manager_user_account_code,
                    style="form",
                    explode=False,
                ),
                "categoryInformationAnalystUserCode": oapi.client.format_argument_value(  # noqa
                    "categoryInformationAnalystUserCode",
                    category_information_analyst_user_code,
                    style="form",
                    explode=False,
                ),
                "productCreationInitiator": oapi.client.format_argument_value(
                    "productCreationInitiator",
                    product_creation_initiator,
                    style="form",
                    explode=False,
                ),
                "salesSampleTypeDescription": oapi.client.format_argument_value(  # noqa
                    "salesSampleTypeDescription",
                    sales_sample_type_description,
                    style="form",
                    explode=False,
                ),
                "SAMMSampleTypeDescription": oapi.client.format_argument_value(
                    "SAMMSampleTypeDescription",
                    samm_sample_type_description,
                    style="form",
                    explode=False,
                ),
                "salesSampleSizeDescription": oapi.client.format_argument_value(  # noqa
                    "salesSampleSizeDescription",
                    sales_sample_size_description,
                    style="form",
                    explode=False,
                ),
                "styleCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "styleCarryoverStatusIndicator",
                    style_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "productCarryoverStatusIndicator",
                    product_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "productOfferingStatusIndicator",
                    product_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "modelIdentifier": oapi.client.format_argument_value(
                    "modelIdentifier",
                    model_identifier,
                    style="form",
                    explode=False,
                ),
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
                    style="form",
                    explode=False,
                ),
                "styleNumber": oapi.client.format_argument_value(
                    "styleNumber",
                    style_number,
                    style="form",
                    explode=False,
                ),
                "colorwayCode": oapi.client.format_argument_value(
                    "colorwayCode",
                    colorway_code,
                    style="form",
                    explode=False,
                ),
                "dimension": oapi.client.format_argument_value(
                    "dimension",
                    dimension,
                    style="form",
                    explode=False,
                ),
                "fit": oapi.client.format_argument_value(
                    "fit",
                    fit,
                    style="form",
                    explode=False,
                ),
                "productInitialSeasonYear": oapi.client.format_argument_value(
                    "productInitialSeasonYear",
                    product_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "masterSizeGrid": oapi.client.format_argument_value(
                    "masterSizeGrid",
                    master_size_grid,
                    style="form",
                    explode=False,
                ),
                "retailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "retailSizeRangeDescription",
                    retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeRunDescription": oapi.client.format_argument_value(
                    "retailSizeRunDescription",
                    retail_size_run_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeSelectionList": oapi.client.format_argument_value(
                    "retailSizeSelectionList",
                    retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "promoSizeRangeDescription": oapi.client.format_argument_value(
                    "promoSizeRangeDescription",
                    promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeRunDescription": oapi.client.format_argument_value(
                    "promoSizeRunDescription",
                    promo_size_run_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeSelectionList": oapi.client.format_argument_value(
                    "promoSizeSelectionList",
                    promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "colorwayIdentifier": oapi.client.format_argument_value(
                    "colorwayIdentifier",
                    colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "primaryColor": oapi.client.format_argument_value(
                    "primaryColor",
                    primary_color,
                    style="form",
                    explode=False,
                ),
                "secondaryColor": oapi.client.format_argument_value(
                    "secondaryColor",
                    secondary_color,
                    style="form",
                    explode=False,
                ),
                "tertiaryColor": oapi.client.format_argument_value(
                    "tertiaryColor",
                    tertiary_color,
                    style="form",
                    explode=False,
                ),
                "quaternaryColor": oapi.client.format_argument_value(
                    "quaternaryColor",
                    quaternary_color,
                    style="form",
                    explode=False,
                ),
                "logoColor": oapi.client.format_argument_value(
                    "logoColor",
                    logo_color,
                    style="form",
                    explode=False,
                ),
                "logoAccentColor": oapi.client.format_argument_value(
                    "logoAccentColor",
                    logo_accent_color,
                    style="form",
                    explode=False,
                ),
                "athlete": oapi.client.format_argument_value(
                    "athlete",
                    athlete,
                    style="form",
                    explode=False,
                ),
                "playerwayNumber": oapi.client.format_argument_value(
                    "playerwayNumber",
                    playerway_number,
                    style="form",
                    explode=False,
                ),
                "uniformType": oapi.client.format_argument_value(
                    "uniformType",
                    uniform_type,
                    style="form",
                    explode=False,
                ),
                "royaltyIntentIndicator": oapi.client.format_argument_value(
                    "royaltyIntentIndicator",
                    royalty_intent_indicator,
                    style="form",
                    explode=False,
                ),
                "productLifecycle": oapi.client.format_argument_value(
                    "productLifecycle",
                    product_lifecycle,
                    style="form",
                    explode=False,
                ),
                "closeoutDate": oapi.client.format_argument_value(
                    "closeoutDate",
                    closeout_date,
                    style="form",
                    explode=False,
                ),
                "category": oapi.client.format_argument_value(
                    "category",
                    category,
                    style="form",
                    explode=False,
                ),
                "subCategory": oapi.client.format_argument_value(
                    "subCategory",
                    sub_category,
                    style="form",
                    explode=False,
                ),
                "globalCategoryCoreFocus": oapi.client.format_argument_value(
                    "globalCategoryCoreFocus",
                    global_category_core_focus,
                    style="form",
                    explode=False,
                ),
                "productStatusIndicator": oapi.client.format_argument_value(
                    "productStatusIndicator",
                    product_status_indicator,
                    style="form",
                    explode=False,
                ),
                "finalAdoptIndicator": oapi.client.format_argument_value(
                    "finalAdoptIndicator",
                    final_adopt_indicator,
                    style="form",
                    explode=False,
                ),
                "styleFit": oapi.client.format_argument_value(
                    "styleFit",
                    style_fit,
                    style="form",
                    explode=False,
                ),
                "styleDimension": oapi.client.format_argument_value(
                    "styleDimension",
                    style_dimension,
                    style="form",
                    explode=False,
                ),
                "styleInitialSeasonYearCode": oapi.client.format_argument_value(  # noqa
                    "styleInitialSeasonYearCode",
                    style_initial_season_year_code,
                    style="form",
                    explode=False,
                ),
                "styleDescription": oapi.client.format_argument_value(
                    "styleDescription",
                    style_description,
                    style="form",
                    explode=False,
                ),
                "segment": oapi.client.format_argument_value(
                    "segment",
                    segment,
                    style="form",
                    explode=False,
                ),
                "subBrand": oapi.client.format_argument_value(
                    "subBrand",
                    sub_brand,
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    sport_activity,
                    style="form",
                    explode=False,
                ),
                "silo": oapi.client.format_argument_value(
                    "silo",
                    silo,
                    style="form",
                    explode=False,
                ),
                "subCategoryBreakdown": oapi.client.format_argument_value(
                    "subCategoryBreakdown",
                    sub_category_breakdown,
                    style="form",
                    explode=False,
                ),
                "styleMerchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "styleMerchandisingClassification",
                    style_merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "harmonizedStyleNumber": oapi.client.format_argument_value(
                    "harmonizedStyleNumber",
                    harmonized_style_number,
                    style="form",
                    explode=False,
                ),
                "constructionMethod": oapi.client.format_argument_value(
                    "constructionMethod",
                    construction_method,
                    style="form",
                    explode=False,
                ),
                "finishedGoodsIndicator": oapi.client.format_argument_value(
                    "finishedGoodsIndicator",
                    finished_goods_indicator,
                    style="form",
                    explode=False,
                ),
                "styleGraphicIndicator": oapi.client.format_argument_value(
                    "styleGraphicIndicator",
                    style_graphic_indicator,
                    style="form",
                    explode=False,
                ),
                "stylePrintIndicator": oapi.client.format_argument_value(
                    "stylePrintIndicator",
                    style_print_indicator,
                    style="form",
                    explode=False,
                ),
                "feature": oapi.client.format_argument_value(
                    "feature",
                    feature,
                    style="form",
                    explode=False,
                ),
                "materialIntent": oapi.client.format_argument_value(
                    "materialIntent",
                    material_intent,
                    style="form",
                    explode=False,
                ),
                "brandMark": oapi.client.format_argument_value(
                    "brandMark",
                    brand_mark,
                    style="form",
                    explode=False,
                ),
                "blankUsageIndicator": oapi.client.format_argument_value(
                    "blankUsageIndicator",
                    blank_usage_indicator,
                    style="form",
                    explode=False,
                ),
                "additionalPlatform": oapi.client.format_argument_value(
                    "additionalPlatform",
                    additional_platform,
                    style="form",
                    explode=False,
                ),
                "deliveryUnitOfMeasure": oapi.client.format_argument_value(
                    "deliveryUnitOfMeasure",
                    delivery_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "consumerPackageQuantity": oapi.client.format_argument_value(
                    "consumerPackageQuantity",
                    consumer_package_quantity,
                    style="form",
                    explode=False,
                ),
                "unitOfMeasure": oapi.client.format_argument_value(
                    "unitOfMeasure",
                    unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "licenseeProductCompany": oapi.client.format_argument_value(
                    "licenseeProductCompany",
                    licensee_product_company,
                    style="form",
                    explode=False,
                ),
                "licensedIndicator": oapi.client.format_argument_value(
                    "licensedIndicator",
                    licensed_indicator,
                    style="form",
                    explode=False,
                ),
                "technology": oapi.client.format_argument_value(
                    "technology",
                    technology,
                    style="form",
                    explode=False,
                ),
                "styleGroup": oapi.client.format_argument_value(
                    "styleGroup",
                    style_group,
                    style="form",
                    explode=False,
                ),
                "styleGroupType": oapi.client.format_argument_value(
                    "styleGroupType",
                    style_group_type,
                    style="form",
                    explode=False,
                ),
                "sportLevel": oapi.client.format_argument_value(
                    "sportLevel",
                    sport_level,
                    style="form",
                    explode=False,
                ),
                "team": oapi.client.format_argument_value(
                    "team",
                    team,
                    style="form",
                    explode=False,
                ),
                "league": oapi.client.format_argument_value(
                    "league",
                    league,
                    style="form",
                    explode=False,
                ),
                "styleStatusIndicator": oapi.client.format_argument_value(
                    "styleStatusIndicator",
                    style_status_indicator,
                    style="form",
                    explode=False,
                ),
                "seasonYear": oapi.client.format_argument_value(
                    "seasonYear",
                    season_year,
                    style="form",
                    explode=False,
                ),
                "productTier": oapi.client.format_argument_value(
                    "productTier",
                    product_tier,
                    style="form",
                    explode=False,
                ),
                "modelOfferingGroup": oapi.client.format_argument_value(
                    "modelOfferingGroup",
                    model_offering_group,
                    style="form",
                    explode=False,
                ),
                "modelOfferingGroupType": oapi.client.format_argument_value(
                    "modelOfferingGroupType",
                    model_offering_group_type,
                    style="form",
                    explode=False,
                ),
                "targetWholesalePrice": oapi.client.format_argument_value(
                    "targetWholesalePrice",
                    target_wholesale_price,
                    style="form",
                    explode=False,
                ),
                "targetRetailPrice": oapi.client.format_argument_value(
                    "targetRetailPrice",
                    target_retail_price,
                    style="form",
                    explode=False,
                ),
                "lineEvolution": oapi.client.format_argument_value(
                    "lineEvolution",
                    line_evolution,
                    style="form",
                    explode=False,
                ),
                "forecastSustainabilityIndexScore": oapi.client.format_argument_value(  # noqa
                    "forecastSustainabilityIndexScore",
                    forecast_sustainability_index_score,
                    style="form",
                    explode=False,
                ),
                "budgetFreeonBoardCost": oapi.client.format_argument_value(
                    "budgetFreeonBoardCost",
                    budget_freeon_board_cost,
                    style="form",
                    explode=False,
                ),
                "prodManagementForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "prodManagementForecastQuantity",
                    prod_management_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "modelOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "modelOfferingStatusIndicator",
                    model_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "consumerPurpose": oapi.client.format_argument_value(
                    "consumerPurpose",
                    consumer_purpose,
                    style="form",
                    explode=False,
                ),
                "consumerFocus": oapi.client.format_argument_value(
                    "consumerFocus",
                    consumer_focus,
                    style="form",
                    explode=False,
                ),
                "consumerGroup": oapi.client.format_argument_value(
                    "consumerGroup",
                    consumer_group,
                    style="form",
                    explode=False,
                ),
                "consumerUse": oapi.client.format_argument_value(
                    "consumerUse",
                    consumer_use,
                    style="form",
                    explode=False,
                ),
                "marketingName": oapi.client.format_argument_value(
                    "marketingName",
                    marketing_name,
                    style="form",
                    explode=False,
                ),
                "businessOrganization": oapi.client.format_argument_value(
                    "businessOrganization",
                    business_organization,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "gender": oapi.client.format_argument_value(
                    "gender",
                    gender,
                    style="form",
                    explode=False,
                ),
                "age": oapi.client.format_argument_value(
                    "age",
                    age,
                    style="form",
                    explode=False,
                ),
                "genderAge": oapi.client.format_argument_value(
                    "genderAge",
                    gender_age,
                    style="form",
                    explode=False,
                ),
                "silhouette": oapi.client.format_argument_value(
                    "silhouette",
                    silhouette,
                    style="form",
                    explode=False,
                ),
                "silhouetteType": oapi.client.format_argument_value(
                    "silhouetteType",
                    silhouette_type,
                    style="form",
                    explode=False,
                ),
                "fitPreference": oapi.client.format_argument_value(
                    "fitPreference",
                    fit_preference,
                    style="form",
                    explode=False,
                ),
                "merchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "merchandisingClassification",
                    merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "primaryPlatform": oapi.client.format_argument_value(
                    "primaryPlatform",
                    primary_platform,
                    style="form",
                    explode=False,
                ),
                "modelInitialSeasonYear": oapi.client.format_argument_value(
                    "modelInitialSeasonYear",
                    model_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "modelGroupType": oapi.client.format_argument_value(
                    "modelGroupType",
                    model_group_type,
                    style="form",
                    explode=False,
                ),
                "modelGroup": oapi.client.format_argument_value(
                    "modelGroup",
                    model_group,
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

    def get_line_management_search_product_offerings_global_distinct(
        self,
        distinct_fields: model.LineManagementSearchProductOfferingsGlobalDistinctGetDistinctFields,  # noqa
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
        change_start_time: typing.Optional[
            datetime.datetime
        ] = None,
        change_end_time: typing.Optional[
            datetime.datetime
        ] = None,
        product_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductIdentifier  # noqa
        ] = None,
        model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelOfferingIdentifier  # noqa
        ] = None,
        earliest_allowed_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetEarliestAllowedOfferDate  # noqa
        ] = None,
        restricted_to_location: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetRestrictedToLocation  # noqa
        ] = None,
        marketing_initiative: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetMarketingInitiative  # noqa
        ] = None,
        alternate_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetAlternateMarketingType  # noqa
        ] = None,
        product_alternate_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductAlternateTypeGroup  # noqa
        ] = None,
        special_offering_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSpecialOfferingType  # noqa
        ] = None,
        launch: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLaunch
        ] = None,
        primary_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPrimaryMarketingType  # noqa
        ] = None,
        product_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductTypeGroup  # noqa
        ] = None,
        always_available_global_indicator: typing.Optional[
            bool
        ] = None,
        smu_account: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSmuAccount  # noqa
        ] = None,
        development_team: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetDevelopmentTeam  # noqa
        ] = None,
        initiating_product_line_manager_user_account_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetInitiatingProductLineManagerUserAccountCode  # noqa
        ] = None,
        category_information_analyst_user_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetCategoryInformationAnalystUserCode  # noqa
        ] = None,
        product_creation_initiator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductCreationInitiator  # noqa
        ] = None,
        sales_sample_type_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSalesSampleTypeDescription  # noqa
        ] = None,
        samm_sample_type_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSAMMSampleTypeDescription  # noqa
        ] = None,
        sales_sample_size_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSalesSampleSizeDescription  # noqa
        ] = None,
        style_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleCarryoverStatusIndicator  # noqa
        ] = None,
        product_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductCarryoverStatusIndicator  # noqa
        ] = None,
        product_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductOfferingStatusIndicator  # noqa
        ] = None,
        model_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelIdentifier  # noqa
        ] = None,
        product_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductCode  # noqa
        ] = None,
        style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleNumber  # noqa
        ] = None,
        colorway_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetColorwayCode  # noqa
        ] = None,
        dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetDimension  # noqa
        ] = None,
        fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetFit
        ] = None,
        product_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductInitialSeasonYear  # noqa
        ] = None,
        master_size_grid: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetMasterSizeGrid  # noqa
        ] = None,
        retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetRetailSizeRangeDescription  # noqa
        ] = None,
        retail_size_run_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetRetailSizeRunDescription  # noqa
        ] = None,
        retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetRetailSizeSelectionList  # noqa
        ] = None,
        promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPromoSizeRangeDescription  # noqa
        ] = None,
        promo_size_run_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPromoSizeRunDescription  # noqa
        ] = None,
        promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPromoSizeSelectionList  # noqa
        ] = None,
        colorway_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetColorwayIdentifier  # noqa
        ] = None,
        primary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPrimaryColor  # noqa
        ] = None,
        secondary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSecondaryColor  # noqa
        ] = None,
        tertiary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetTertiaryColor  # noqa
        ] = None,
        quaternary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetQuaternaryColor  # noqa
        ] = None,
        logo_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLogoColor  # noqa
        ] = None,
        logo_accent_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLogoAccentColor  # noqa
        ] = None,
        athlete: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetAthlete
        ] = None,
        playerway_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPlayerwayNumber  # noqa
        ] = None,
        uniform_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetUniformType  # noqa
        ] = None,
        royalty_intent_indicator: typing.Optional[
            bool
        ] = None,
        product_lifecycle: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductLifecycle  # noqa
        ] = None,
        closeout_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetCloseoutDate  # noqa
        ] = None,
        category: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetCategory
        ] = None,
        sub_category: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSubCategory  # noqa
        ] = None,
        global_category_core_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetGlobalCategoryCoreFocus  # noqa
        ] = None,
        product_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductStatusIndicator  # noqa
        ] = None,
        final_adopt_indicator: typing.Optional[
            bool
        ] = None,
        style_fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleFit
        ] = None,
        style_dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleDimension  # noqa
        ] = None,
        style_initial_season_year_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleInitialSeasonYearCode  # noqa
        ] = None,
        style_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleDescription  # noqa
        ] = None,
        segment: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSegment
        ] = None,
        sub_brand: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSubBrand
        ] = None,
        sport_activity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSportActivity  # noqa
        ] = None,
        silo: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSilo
        ] = None,
        sub_category_breakdown: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSubCategoryBreakdown  # noqa
        ] = None,
        style_merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleMerchandisingClassification  # noqa
        ] = None,
        harmonized_style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetHarmonizedStyleNumber  # noqa
        ] = None,
        construction_method: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConstructionMethod  # noqa
        ] = None,
        finished_goods_indicator: typing.Optional[
            bool
        ] = None,
        style_graphic_indicator: typing.Optional[
            bool
        ] = None,
        style_print_indicator: typing.Optional[
            bool
        ] = None,
        feature: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetFeature
        ] = None,
        material_intent: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetMaterialIntent  # noqa
        ] = None,
        brand_mark: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetBrandMark  # noqa
        ] = None,
        blank_usage_indicator: typing.Optional[
            bool
        ] = None,
        additional_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetAdditionalPlatform  # noqa
        ] = None,
        delivery_unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetDeliveryUnitOfMeasure  # noqa
        ] = None,
        consumer_package_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConsumerPackageQuantity  # noqa
        ] = None,
        unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetUnitOfMeasure  # noqa
        ] = None,
        licensee_product_company: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLicenseeProductCompany  # noqa
        ] = None,
        licensed_indicator: typing.Optional[
            bool
        ] = None,
        technology: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetTechnology  # noqa
        ] = None,
        style_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleGroup  # noqa
        ] = None,
        style_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleGroupType  # noqa
        ] = None,
        sport_level: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSportLevel  # noqa
        ] = None,
        team: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetTeam
        ] = None,
        league: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLeague
        ] = None,
        style_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetStyleStatusIndicator  # noqa
        ] = None,
        season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSeasonYear  # noqa
        ] = None,
        product_tier: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProductTier  # noqa
        ] = None,
        model_offering_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelOfferingGroup  # noqa
        ] = None,
        model_offering_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelOfferingGroupType  # noqa
        ] = None,
        target_wholesale_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetTargetWholesalePrice  # noqa
        ] = None,
        target_retail_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetTargetRetailPrice  # noqa
        ] = None,
        line_evolution: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetLineEvolution  # noqa
        ] = None,
        forecast_sustainability_index_score: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetForecastSustainabilityIndexScore  # noqa
        ] = None,
        budget_freeon_board_cost: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetBudgetFreeonBoardCost  # noqa
        ] = None,
        prod_management_forecast_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetProdManagementForecastQuantity  # noqa
        ] = None,
        model_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelOfferingStatusIndicator  # noqa
        ] = None,
        consumer_purpose: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConsumerPurpose  # noqa
        ] = None,
        consumer_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConsumerFocus  # noqa
        ] = None,
        consumer_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConsumerGroup  # noqa
        ] = None,
        consumer_use: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetConsumerUse  # noqa
        ] = None,
        marketing_name: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetMarketingName  # noqa
        ] = None,
        business_organization: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetBusinessOrganization  # noqa
        ] = None,
        division: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetDivision
        ] = None,
        gender: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetGender
        ] = None,
        age: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetAge
        ] = None,
        gender_age: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetGenderAge  # noqa
        ] = None,
        silhouette: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSilhouette  # noqa
        ] = None,
        silhouette_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetSilhouetteType  # noqa
        ] = None,
        fit_preference: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetFitPreference  # noqa
        ] = None,
        merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetMerchandisingClassification  # noqa
        ] = None,
        primary_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetPrimaryPlatform  # noqa
        ] = None,
        model_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelInitialSeasonYear  # noqa
        ] = None,
        model_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelGroupType  # noqa
        ] = None,
        model_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGlobalDistinctGetModelGroup  # noqa
        ] = None,
    ) -> model.DistinctResponse:
        """
        How you search against all fields contained within the Line Management
        Global Offering entity

        Parameters:

        - distinct_fields:
          This is a comma separated list of referenced or Identifier fields
          from the global offering service you wish to get distinct values for
          based on the search paramaters given. NOTE: Only referenced fields or
          Identifier fields are supported
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        - change_start_time:
          This is the Start Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - change_end_time:
          This is the End Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - product_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Identifier">Definition</a>
        - model_offering_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Offering%
          2520Identifier">Definition</a>
        - earliest_allowed_offer_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FEarliest%2520Allowed
          %2520Offer%2520Date">Definition</a>
        - restricted_to_location:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Restricted%2520To%2520Location%2520Identifier">Definition</a>
        - marketing_initiative:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FMarketing%2520Initiative">
          Definition</a>
        - alternate_marketing_type:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FConcept%252FAlternate%
          2520Marketing%2520Type">Definition</a>
        - product_alternate_type_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Group%2520Code">Definition</a>
        - special_offering_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FSpecial%2520Offering%2520Type"
          >Definition</a>
        - launch:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLaunch%2520Code">
          Definition</a>
        - primary_marketing_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Identifier">Definition</a>
        - product_type_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Type%
          2520Group%2520Code">Definition</a>
        - always_available_global_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FAlways%
          2520Available%2520Global%2520Indicator">Definition</a>
        - smu_account:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSpecial%2520Make-up%
          2520Account%2520Code">Definition</a>
        - development_team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDevelopment%2520Team
          %2520Identifier">Definition</a>
        - initiating_product_line_manager_user_account_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitiating%
          2520Product%2520Line%2520Manager%2520User%2520Code">Definition</a>
        - category_information_analyst_user_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Creation
          %2520Initiator%2520Identifier">Definition</a>
        - product_creation_initiator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Creation
          %2520Initiator%2520Identifier">Definition</a>
        - sales_sample_type_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSales%2520Sample%
          2520Indicator">Definition</a>
        - samm_sample_type_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSeasonal%
          2520Alignment%2520Merchandising%2520Meeting%2520Sample%2520Indicator"
          >Definition</a>
        - sales_sample_size_description:
          The reference key associated with this item: <a target="_blank" http:
          //nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSales%2520Sample%
          2520Size%2520Description">Definition</a>
        - style_carryover_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Carryover%2520Status%2520Indicator">Definition</a>
        - product_carryover_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Carryover%2520Status%2520Indicator">Definition</a>
        - product_offering_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Offering
          %2520Status%2520Indicator">Definition</a>
        - model_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%
          2520Identifier">Definition</a>
        - product_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Code">
          Definition</a>
        - style_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Code">
          Definition</a>
        - colorway_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Colorway
          %2520Code">Definition</a>
        - dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - product_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - master_size_grid:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMaster%2520Size%
          2520Grid%2520Code">Definition</a>
        - retail_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Range%2520Description">Definition</a>
        - retail_size_run_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Run%2520Description">Definition</a>
        - retail_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Selection%2520List">Definition</a>
        - promo_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromotional%2520Size
          %2520Range%2520Description">Definition</a>
        - promo_size_run_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Run%2520Description">Definition</a>
        - promo_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Selection%2520List">Definition</a>
        - colorway_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FColorway%
          2520Identifier">Definition</a>
        - primary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Color%
          2520Code">Definition</a>
        - secondary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSecondary%2520Color%
          2520Code">Definition</a>
        - tertiary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTertiary%2520Color%
          2520Code">Definition</a>
        - quaternary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FQuaternary%2520Color
          %2520Code">Definition</a>
        - logo_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Color%
          2520Code">Definition</a>
        - logo_accent_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Accent%
          2520Color%2520Code">Definition</a>
        - athlete:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAthlete%
          2520Identifier">Definition</a>
        - playerway_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlayerway%
          2520Number">Definition</a>
        - uniform_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUniform%2520Type%
          2520Identifier">Definition</a>
        - royalty_intent_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FRoyalty%
          2520Intent%2520Indicator">Definition</a>
        - product_lifecycle:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Lifecycle%2520Code">Definition</a>
        - closeout_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FClose%2520Out%
          2520Date">Definition</a>
        - category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCategory%2520Code">
          Definition</a>
        - sub_category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Code">Definition</a>
        - global_category_core_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGlobal%2520Category%
          2520Core%2520Focus%2520Code">Definition</a>
        - product_status_indicator:
          The A or I flag associated with this item: <a target="_blank" href ="
          http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Status%
          2520Indicator">Definition</a>
        - final_adopt_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinal%
          2520Adoption%2520Indicator">Definition</a>
        - style_fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - style_dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - style_initial_season_year_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - style_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%
          2520Description">Definition</a>
        - segment:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSegment%2520Code">
          Definition</a>
        - sub_brand:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Brand%
          2520Code">Definition</a>
        - sport_activity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Activity%
          2520Code">Definition</a>
        - silo:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilo%2520Identifier"
          >Definition</a>
        - sub_category_breakdown:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - style_merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - harmonized_style_number:
          The reference key associated with this item: Harmonized Style Number
        - construction_method:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConstruction%
          2520Identifier">Definition</a>
        - finished_goods_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinished%
          2520Goods%2520Indicator">Definition</a>
        - style_graphic_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Graphic%2520Indicator">Definition</a>
        - style_print_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Print%2520Indicator">Definition</a>
        - feature:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFeature%
          2520Identifier">Definition</a>
        - material_intent:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___search___all___material
          %2520intent%2520identifier">Definition</a>
        - brand_mark:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBrand%2520Mark%
          2520Identifier">Definition</a>
        - blank_usage_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FBlank%
          2520Usage%2520Indicator">Definition</a>
        - additional_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlatform%
          2520Identifier">Definition</a>
        - delivery_unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDelivery%2520Unit%
          2520Quantity">Definition</a>
        - consumer_package_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Package
          %2520Quantity">Definition</a>
        - unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUnit%2520Of%
          2520Measure%2520Code">Definition</a>
        - licensee_product_company:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLicensee%2520Product
          %2520Company%2520Code">Definition</a>
        - licensed_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FLicensed%
          2520Indicator">Definition</a>
        - technology:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTechnology%2520Code"
          >Definition</a>
        - style_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Identifier">Definition</a>
        - style_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Type%2520Identifier">Definition</a>
        - sport_level:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Level%
          2520Identifier">Definition</a>
        - team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTeam%2520Identifier"
          >Definition</a>
        - league:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLeague%
          2520Identifier">Definition</a>
        - style_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStatus%
          2520Indicator">Definition</a>
        - season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCycle%2520Year%
          2520Abbreviation">Definition</a>
        - product_tier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Tier%
          2520Identifier">Definition</a>
        - model_offering_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        - model_offering_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - target_wholesale_price:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTarget%2520Wholesale
          %2520Price">Definition</a>
        - target_retail_price:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTarget%2520Retail%
          2520Price">Definition</a>
        - line_evolution:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLine%2520Evolution%
          2520Identifier">Definition</a>
        - forecast_sustainability_index_score:
          The reference key associated with this item: N/A
        - budget_freeon_board_cost:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBudget%2520Free%
          2520On%2520Board%2520Cost">Definition</a>
        - prod_management_forecast_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Management%2520Forecast%2520Quantity">Definition</a>
        - model_offering_status_indicator:
          The reference key associated with this item:<a target="_blank" href =
          "http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Offering%
          2520Status%2520Indicator">Definition</a>
        - consumer_purpose:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Purpose
          %2520Identifier">Definition</a>
        - consumer_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Focus%
          2520Identifier">Definition</a>
        - consumer_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Group%
          2520Identifier">Definition</a>
        - consumer_use:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Use%
          2520Identifier">Definition</a>
        - marketing_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMarketing%2520Name">
          Definition</a>
        - business_organization:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBusiness%
          2520Organization%2520Code">Definition</a>
        - division:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDivision%2520Code">
          Definition</a>
        - gender:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Code">
          Definition</a>
        - age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAge%2520Code">
          Definition</a>
        - gender_age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Age%
          2520Code">Definition</a>
        - silhouette:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Code"
          >Definition</a>
        - silhouette_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Type%
          2520Code">Definition</a>
        - fit_preference:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Preference%
          2520Identifier">Definition</a>
        - merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMerchandising%
          2520Classification%2520Identifier">Definition</a>
        - primary_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Platform
          %2520Identifier">Definition</a>
        - model_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitial%2520Cycle%
          2520Year%2520Code">Definition</a>
        - model_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - model_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productOfferings/global/distinct/",
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
                "distinctFields": oapi.client.format_argument_value(
                    "distinctFields",
                    distinct_fields,
                    style="form",
                    explode=False,
                ),
                "changeStartTime": oapi.client.format_argument_value(
                    "changeStartTime",
                    change_start_time,
                    style="form",
                    explode=False,
                ),
                "changeEndTime": oapi.client.format_argument_value(
                    "changeEndTime",
                    change_end_time,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "modelOfferingIdentifier": oapi.client.format_argument_value(
                    "modelOfferingIdentifier",
                    model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "earliestAllowedOfferDate": oapi.client.format_argument_value(
                    "earliestAllowedOfferDate",
                    earliest_allowed_offer_date,
                    style="form",
                    explode=False,
                ),
                "restrictedToLocation": oapi.client.format_argument_value(
                    "restrictedToLocation",
                    restricted_to_location,
                    style="form",
                    explode=False,
                ),
                "marketingInitiative": oapi.client.format_argument_value(
                    "marketingInitiative",
                    marketing_initiative,
                    style="form",
                    explode=False,
                ),
                "alternateMarketingType": oapi.client.format_argument_value(
                    "alternateMarketingType",
                    alternate_marketing_type,
                    style="form",
                    explode=False,
                ),
                "productAlternateTypeGroup": oapi.client.format_argument_value(
                    "productAlternateTypeGroup",
                    product_alternate_type_group,
                    style="form",
                    explode=False,
                ),
                "specialOfferingType": oapi.client.format_argument_value(
                    "specialOfferingType",
                    special_offering_type,
                    style="form",
                    explode=False,
                ),
                "launch": oapi.client.format_argument_value(
                    "launch",
                    launch,
                    style="form",
                    explode=False,
                ),
                "primaryMarketingType": oapi.client.format_argument_value(
                    "primaryMarketingType",
                    primary_marketing_type,
                    style="form",
                    explode=False,
                ),
                "productTypeGroup": oapi.client.format_argument_value(
                    "productTypeGroup",
                    product_type_group,
                    style="form",
                    explode=False,
                ),
                "alwaysAvailableGlobalIndicator": oapi.client.format_argument_value(  # noqa
                    "alwaysAvailableGlobalIndicator",
                    always_available_global_indicator,
                    style="form",
                    explode=False,
                ),
                "smuAccount": oapi.client.format_argument_value(
                    "smuAccount",
                    smu_account,
                    style="form",
                    explode=False,
                ),
                "developmentTeam": oapi.client.format_argument_value(
                    "developmentTeam",
                    development_team,
                    style="form",
                    explode=False,
                ),
                "initiatingProductLineManagerUserAccountCode": oapi.client.format_argument_value(  # noqa
                    "initiatingProductLineManagerUserAccountCode",
                    initiating_product_line_manager_user_account_code,
                    style="form",
                    explode=False,
                ),
                "categoryInformationAnalystUserCode": oapi.client.format_argument_value(  # noqa
                    "categoryInformationAnalystUserCode",
                    category_information_analyst_user_code,
                    style="form",
                    explode=False,
                ),
                "productCreationInitiator": oapi.client.format_argument_value(
                    "productCreationInitiator",
                    product_creation_initiator,
                    style="form",
                    explode=False,
                ),
                "salesSampleTypeDescription": oapi.client.format_argument_value(  # noqa
                    "salesSampleTypeDescription",
                    sales_sample_type_description,
                    style="form",
                    explode=False,
                ),
                "SAMMSampleTypeDescription": oapi.client.format_argument_value(
                    "SAMMSampleTypeDescription",
                    samm_sample_type_description,
                    style="form",
                    explode=False,
                ),
                "salesSampleSizeDescription": oapi.client.format_argument_value(  # noqa
                    "salesSampleSizeDescription",
                    sales_sample_size_description,
                    style="form",
                    explode=False,
                ),
                "styleCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "styleCarryoverStatusIndicator",
                    style_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "productCarryoverStatusIndicator",
                    product_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "productOfferingStatusIndicator",
                    product_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "modelIdentifier": oapi.client.format_argument_value(
                    "modelIdentifier",
                    model_identifier,
                    style="form",
                    explode=False,
                ),
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
                    style="form",
                    explode=False,
                ),
                "styleNumber": oapi.client.format_argument_value(
                    "styleNumber",
                    style_number,
                    style="form",
                    explode=False,
                ),
                "colorwayCode": oapi.client.format_argument_value(
                    "colorwayCode",
                    colorway_code,
                    style="form",
                    explode=False,
                ),
                "dimension": oapi.client.format_argument_value(
                    "dimension",
                    dimension,
                    style="form",
                    explode=False,
                ),
                "fit": oapi.client.format_argument_value(
                    "fit",
                    fit,
                    style="form",
                    explode=False,
                ),
                "productInitialSeasonYear": oapi.client.format_argument_value(
                    "productInitialSeasonYear",
                    product_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "masterSizeGrid": oapi.client.format_argument_value(
                    "masterSizeGrid",
                    master_size_grid,
                    style="form",
                    explode=False,
                ),
                "retailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "retailSizeRangeDescription",
                    retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeRunDescription": oapi.client.format_argument_value(
                    "retailSizeRunDescription",
                    retail_size_run_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeSelectionList": oapi.client.format_argument_value(
                    "retailSizeSelectionList",
                    retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "promoSizeRangeDescription": oapi.client.format_argument_value(
                    "promoSizeRangeDescription",
                    promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeRunDescription": oapi.client.format_argument_value(
                    "promoSizeRunDescription",
                    promo_size_run_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeSelectionList": oapi.client.format_argument_value(
                    "promoSizeSelectionList",
                    promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "colorwayIdentifier": oapi.client.format_argument_value(
                    "colorwayIdentifier",
                    colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "primaryColor": oapi.client.format_argument_value(
                    "primaryColor",
                    primary_color,
                    style="form",
                    explode=False,
                ),
                "secondaryColor": oapi.client.format_argument_value(
                    "secondaryColor",
                    secondary_color,
                    style="form",
                    explode=False,
                ),
                "tertiaryColor": oapi.client.format_argument_value(
                    "tertiaryColor",
                    tertiary_color,
                    style="form",
                    explode=False,
                ),
                "quaternaryColor": oapi.client.format_argument_value(
                    "quaternaryColor",
                    quaternary_color,
                    style="form",
                    explode=False,
                ),
                "logoColor": oapi.client.format_argument_value(
                    "logoColor",
                    logo_color,
                    style="form",
                    explode=False,
                ),
                "logoAccentColor": oapi.client.format_argument_value(
                    "logoAccentColor",
                    logo_accent_color,
                    style="form",
                    explode=False,
                ),
                "athlete": oapi.client.format_argument_value(
                    "athlete",
                    athlete,
                    style="form",
                    explode=False,
                ),
                "playerwayNumber": oapi.client.format_argument_value(
                    "playerwayNumber",
                    playerway_number,
                    style="form",
                    explode=False,
                ),
                "uniformType": oapi.client.format_argument_value(
                    "uniformType",
                    uniform_type,
                    style="form",
                    explode=False,
                ),
                "royaltyIntentIndicator": oapi.client.format_argument_value(
                    "royaltyIntentIndicator",
                    royalty_intent_indicator,
                    style="form",
                    explode=False,
                ),
                "productLifecycle": oapi.client.format_argument_value(
                    "productLifecycle",
                    product_lifecycle,
                    style="form",
                    explode=False,
                ),
                "closeoutDate": oapi.client.format_argument_value(
                    "closeoutDate",
                    closeout_date,
                    style="form",
                    explode=False,
                ),
                "category": oapi.client.format_argument_value(
                    "category",
                    category,
                    style="form",
                    explode=False,
                ),
                "subCategory": oapi.client.format_argument_value(
                    "subCategory",
                    sub_category,
                    style="form",
                    explode=False,
                ),
                "globalCategoryCoreFocus": oapi.client.format_argument_value(
                    "globalCategoryCoreFocus",
                    global_category_core_focus,
                    style="form",
                    explode=False,
                ),
                "productStatusIndicator": oapi.client.format_argument_value(
                    "productStatusIndicator",
                    product_status_indicator,
                    style="form",
                    explode=False,
                ),
                "finalAdoptIndicator": oapi.client.format_argument_value(
                    "finalAdoptIndicator",
                    final_adopt_indicator,
                    style="form",
                    explode=False,
                ),
                "styleFit": oapi.client.format_argument_value(
                    "styleFit",
                    style_fit,
                    style="form",
                    explode=False,
                ),
                "styleDimension": oapi.client.format_argument_value(
                    "styleDimension",
                    style_dimension,
                    style="form",
                    explode=False,
                ),
                "styleInitialSeasonYearCode": oapi.client.format_argument_value(  # noqa
                    "styleInitialSeasonYearCode",
                    style_initial_season_year_code,
                    style="form",
                    explode=False,
                ),
                "styleDescription": oapi.client.format_argument_value(
                    "styleDescription",
                    style_description,
                    style="form",
                    explode=False,
                ),
                "segment": oapi.client.format_argument_value(
                    "segment",
                    segment,
                    style="form",
                    explode=False,
                ),
                "subBrand": oapi.client.format_argument_value(
                    "subBrand",
                    sub_brand,
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    sport_activity,
                    style="form",
                    explode=False,
                ),
                "silo": oapi.client.format_argument_value(
                    "silo",
                    silo,
                    style="form",
                    explode=False,
                ),
                "subCategoryBreakdown": oapi.client.format_argument_value(
                    "subCategoryBreakdown",
                    sub_category_breakdown,
                    style="form",
                    explode=False,
                ),
                "styleMerchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "styleMerchandisingClassification",
                    style_merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "harmonizedStyleNumber": oapi.client.format_argument_value(
                    "harmonizedStyleNumber",
                    harmonized_style_number,
                    style="form",
                    explode=False,
                ),
                "constructionMethod": oapi.client.format_argument_value(
                    "constructionMethod",
                    construction_method,
                    style="form",
                    explode=False,
                ),
                "finishedGoodsIndicator": oapi.client.format_argument_value(
                    "finishedGoodsIndicator",
                    finished_goods_indicator,
                    style="form",
                    explode=False,
                ),
                "styleGraphicIndicator": oapi.client.format_argument_value(
                    "styleGraphicIndicator",
                    style_graphic_indicator,
                    style="form",
                    explode=False,
                ),
                "stylePrintIndicator": oapi.client.format_argument_value(
                    "stylePrintIndicator",
                    style_print_indicator,
                    style="form",
                    explode=False,
                ),
                "feature": oapi.client.format_argument_value(
                    "feature",
                    feature,
                    style="form",
                    explode=False,
                ),
                "materialIntent": oapi.client.format_argument_value(
                    "materialIntent",
                    material_intent,
                    style="form",
                    explode=False,
                ),
                "brandMark": oapi.client.format_argument_value(
                    "brandMark",
                    brand_mark,
                    style="form",
                    explode=False,
                ),
                "blankUsageIndicator": oapi.client.format_argument_value(
                    "blankUsageIndicator",
                    blank_usage_indicator,
                    style="form",
                    explode=False,
                ),
                "additionalPlatform": oapi.client.format_argument_value(
                    "additionalPlatform",
                    additional_platform,
                    style="form",
                    explode=False,
                ),
                "deliveryUnitOfMeasure": oapi.client.format_argument_value(
                    "deliveryUnitOfMeasure",
                    delivery_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "consumerPackageQuantity": oapi.client.format_argument_value(
                    "consumerPackageQuantity",
                    consumer_package_quantity,
                    style="form",
                    explode=False,
                ),
                "unitOfMeasure": oapi.client.format_argument_value(
                    "unitOfMeasure",
                    unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "licenseeProductCompany": oapi.client.format_argument_value(
                    "licenseeProductCompany",
                    licensee_product_company,
                    style="form",
                    explode=False,
                ),
                "licensedIndicator": oapi.client.format_argument_value(
                    "licensedIndicator",
                    licensed_indicator,
                    style="form",
                    explode=False,
                ),
                "technology": oapi.client.format_argument_value(
                    "technology",
                    technology,
                    style="form",
                    explode=False,
                ),
                "styleGroup": oapi.client.format_argument_value(
                    "styleGroup",
                    style_group,
                    style="form",
                    explode=False,
                ),
                "styleGroupType": oapi.client.format_argument_value(
                    "styleGroupType",
                    style_group_type,
                    style="form",
                    explode=False,
                ),
                "sportLevel": oapi.client.format_argument_value(
                    "sportLevel",
                    sport_level,
                    style="form",
                    explode=False,
                ),
                "team": oapi.client.format_argument_value(
                    "team",
                    team,
                    style="form",
                    explode=False,
                ),
                "league": oapi.client.format_argument_value(
                    "league",
                    league,
                    style="form",
                    explode=False,
                ),
                "styleStatusIndicator": oapi.client.format_argument_value(
                    "styleStatusIndicator",
                    style_status_indicator,
                    style="form",
                    explode=False,
                ),
                "seasonYear": oapi.client.format_argument_value(
                    "seasonYear",
                    season_year,
                    style="form",
                    explode=False,
                ),
                "productTier": oapi.client.format_argument_value(
                    "productTier",
                    product_tier,
                    style="form",
                    explode=False,
                ),
                "modelOfferingGroup": oapi.client.format_argument_value(
                    "modelOfferingGroup",
                    model_offering_group,
                    style="form",
                    explode=False,
                ),
                "modelOfferingGroupType": oapi.client.format_argument_value(
                    "modelOfferingGroupType",
                    model_offering_group_type,
                    style="form",
                    explode=False,
                ),
                "targetWholesalePrice": oapi.client.format_argument_value(
                    "targetWholesalePrice",
                    target_wholesale_price,
                    style="form",
                    explode=False,
                ),
                "targetRetailPrice": oapi.client.format_argument_value(
                    "targetRetailPrice",
                    target_retail_price,
                    style="form",
                    explode=False,
                ),
                "lineEvolution": oapi.client.format_argument_value(
                    "lineEvolution",
                    line_evolution,
                    style="form",
                    explode=False,
                ),
                "forecastSustainabilityIndexScore": oapi.client.format_argument_value(  # noqa
                    "forecastSustainabilityIndexScore",
                    forecast_sustainability_index_score,
                    style="form",
                    explode=False,
                ),
                "budgetFreeonBoardCost": oapi.client.format_argument_value(
                    "budgetFreeonBoardCost",
                    budget_freeon_board_cost,
                    style="form",
                    explode=False,
                ),
                "prodManagementForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "prodManagementForecastQuantity",
                    prod_management_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "modelOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "modelOfferingStatusIndicator",
                    model_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "consumerPurpose": oapi.client.format_argument_value(
                    "consumerPurpose",
                    consumer_purpose,
                    style="form",
                    explode=False,
                ),
                "consumerFocus": oapi.client.format_argument_value(
                    "consumerFocus",
                    consumer_focus,
                    style="form",
                    explode=False,
                ),
                "consumerGroup": oapi.client.format_argument_value(
                    "consumerGroup",
                    consumer_group,
                    style="form",
                    explode=False,
                ),
                "consumerUse": oapi.client.format_argument_value(
                    "consumerUse",
                    consumer_use,
                    style="form",
                    explode=False,
                ),
                "marketingName": oapi.client.format_argument_value(
                    "marketingName",
                    marketing_name,
                    style="form",
                    explode=False,
                ),
                "businessOrganization": oapi.client.format_argument_value(
                    "businessOrganization",
                    business_organization,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "gender": oapi.client.format_argument_value(
                    "gender",
                    gender,
                    style="form",
                    explode=False,
                ),
                "age": oapi.client.format_argument_value(
                    "age",
                    age,
                    style="form",
                    explode=False,
                ),
                "genderAge": oapi.client.format_argument_value(
                    "genderAge",
                    gender_age,
                    style="form",
                    explode=False,
                ),
                "silhouette": oapi.client.format_argument_value(
                    "silhouette",
                    silhouette,
                    style="form",
                    explode=False,
                ),
                "silhouetteType": oapi.client.format_argument_value(
                    "silhouetteType",
                    silhouette_type,
                    style="form",
                    explode=False,
                ),
                "fitPreference": oapi.client.format_argument_value(
                    "fitPreference",
                    fit_preference,
                    style="form",
                    explode=False,
                ),
                "merchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "merchandisingClassification",
                    merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "primaryPlatform": oapi.client.format_argument_value(
                    "primaryPlatform",
                    primary_platform,
                    style="form",
                    explode=False,
                ),
                "modelInitialSeasonYear": oapi.client.format_argument_value(
                    "modelInitialSeasonYear",
                    model_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "modelGroupType": oapi.client.format_argument_value(
                    "modelGroupType",
                    model_group_type,
                    style="form",
                    explode=False,
                ),
                "modelGroup": oapi.client.format_argument_value(
                    "modelGroup",
                    model_group,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DistinctResponse,
            )
        )

    def get_line_management_search_product_offerings_geography(
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
        geo_product_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoProductOfferingIdentifier  # noqa
        ] = None,
        product_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductOfferingIdentifier  # noqa
        ] = None,
        geo_model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoModelOfferingIdentifier  # noqa
        ] = None,
        product_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductIdentifier  # noqa
        ] = None,
        geo_first_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoFirstOfferDate  # noqa
        ] = None,
        geo_restricted_region: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoRestrictedRegion  # noqa
        ] = None,
        geo_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoMarketingType  # noqa
        ] = None,
        geo_alternate_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoAlternateMarketingType  # noqa
        ] = None,
        geo_smu_product_account: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoSMUProductAccount  # noqa
        ] = None,
        geo_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoTypeGroup
        ] = None,
        geo_marketing_initiative: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoMarketingInitiative  # noqa
        ] = None,
        geo_launch: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoLaunch
        ] = None,
        geo_launch_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoLaunchDate
        ] = None,
        geo_retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoRetailSizeRangeDescription  # noqa
        ] = None,
        geo_retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoRetailSizeSelectionList  # noqa
        ] = None,
        geo_promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoPromoSizeRangeDescription  # noqa
        ] = None,
        geo_promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoPromoSizeSelectionList  # noqa
        ] = None,
        geo_sales_sample_indicator: typing.Optional[
            bool
        ] = None,
        geo_sales_sample_size_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoSalesSampleSizeDescription  # noqa
        ] = None,
        geo_sales_sample_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoSalesSampleQuantity  # noqa
        ] = None,
        geo_sales_sample_comment: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoSalesSampleComment  # noqa
        ] = None,
        geo_product_offering_merchandising_forecast_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoProductOfferingMerchandisingForecastQuantity  # noqa
        ] = None,
        geo_product_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoProductCarryoverStatusIndicator  # noqa
        ] = None,
        geo_product_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoProductOfferingStatusIndicator  # noqa
        ] = None,
        geo_status_change_timestamp: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoStatusChangeTimestamp  # noqa
        ] = None,
        geo_region: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoRegion
        ] = None,
        model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelOfferingIdentifier  # noqa
        ] = None,
        cycle_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetCycleYear
        ] = None,
        geo_target_wholesale_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoTargetWholesalePrice  # noqa
        ] = None,
        geo_target_retail_price: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoTargetRetailPrice  # noqa
        ] = None,
        geo_currency: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoCurrency
        ] = None,
        geo_merchandising_manager_user_account_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoMerchandisingManagerUserAccountCode  # noqa
        ] = None,
        geo_model_offering_merchandising_forecast_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoModelOfferingMerchandisingForecastQuantity  # noqa
        ] = None,
        territory_merchandising_region: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetTerritoryMerchandisingRegion  # noqa
        ] = None,
        territory_merchandising_forecast_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetTerritoryMerchandisingForecastQuantity  # noqa
        ] = None,
        geo_model_offering_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoModelOfferingCarryoverStatusIndicator  # noqa
        ] = None,
        geo_model_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGeoModelOfferingStatusIndicator  # noqa
        ] = None,
        product_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductCode
        ] = None,
        model_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelIdentifier  # noqa
        ] = None,
        style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleNumber
        ] = None,
        colorway_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetColorwayCode
        ] = None,
        dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetDimension
        ] = None,
        fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetFit
        ] = None,
        product_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductInitialSeasonYear  # noqa
        ] = None,
        retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetRetailSizeRangeDescription  # noqa
        ] = None,
        retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetRetailSizeSelectionList  # noqa
        ] = None,
        promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetPromoSizeRangeDescription  # noqa
        ] = None,
        promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetPromoSizeSelectionList  # noqa
        ] = None,
        colorway_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetColorwayIdentifier  # noqa
        ] = None,
        primary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetPrimaryColor
        ] = None,
        secondary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSecondaryColor  # noqa
        ] = None,
        tertiary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetTertiaryColor
        ] = None,
        quaternary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetQuaternaryColor  # noqa
        ] = None,
        logo_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetLogoColor
        ] = None,
        logo_accent_color: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetLogoAccentColor  # noqa
        ] = None,
        athlete: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetAthlete
        ] = None,
        playerway_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetPlayerwayNumber  # noqa
        ] = None,
        uniform_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetUniformType
        ] = None,
        royalty_intent_indicator: typing.Optional[
            bool
        ] = None,
        product_lifecycle: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductLifecycle  # noqa
        ] = None,
        closeout_date: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetCloseoutDate
        ] = None,
        category: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetCategory
        ] = None,
        sub_category: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSubCategory
        ] = None,
        global_category_core_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGlobalCategoryCoreFocus  # noqa
        ] = None,
        product_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetProductStatusIndicator  # noqa
        ] = None,
        final_adopt_indicator: typing.Optional[
            bool
        ] = None,
        division: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetDivision
        ] = None,
        model_name: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelName
        ] = None,
        gender: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGender
        ] = None,
        age: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetAge
        ] = None,
        gender_age: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetGenderAge
        ] = None,
        silhouette: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSilhouette
        ] = None,
        silhouette_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSilhouetteType  # noqa
        ] = None,
        fit_preference: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetFitPreference
        ] = None,
        merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetMerchandisingClassification  # noqa
        ] = None,
        primary_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetPrimaryPlatform  # noqa
        ] = None,
        model_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelInitialSeasonYear  # noqa
        ] = None,
        model_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelGroupType  # noqa
        ] = None,
        model_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetModelGroup
        ] = None,
        style_name: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleName
        ] = None,
        style_fit: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleFit
        ] = None,
        style_dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleDimension  # noqa
        ] = None,
        style_initial_season_year_code: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleInitialSeasonYearCode  # noqa
        ] = None,
        style_description: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleDescription  # noqa
        ] = None,
        segment: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSegment
        ] = None,
        sub_brand: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSubBrand
        ] = None,
        sport_activity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSportActivity
        ] = None,
        silo: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSilo
        ] = None,
        sub_category_breakdown: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSubCategoryBreakdown  # noqa
        ] = None,
        style_merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleMerchandisingClassification  # noqa
        ] = None,
        harmonized_style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetHarmonizedStyleNumber  # noqa
        ] = None,
        construction_method: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetConstructionMethod  # noqa
        ] = None,
        finished_goods_indicator: typing.Optional[
            bool
        ] = None,
        style_graphic_indicator: typing.Optional[
            bool
        ] = None,
        style_print_indicator: typing.Optional[
            bool
        ] = None,
        feature: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetFeature
        ] = None,
        material_intent: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetMaterialIntent  # noqa
        ] = None,
        brand_mark: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetBrandMark
        ] = None,
        blank_usage_indicator: typing.Optional[
            bool
        ] = None,
        additional_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetAdditionalPlatform  # noqa
        ] = None,
        master_size_grid: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetMasterSizeGrid  # noqa
        ] = None,
        delivery_unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetDeliveryUnitOfMeasure  # noqa
        ] = None,
        consumer_package_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetConsumerPackageQuantity  # noqa
        ] = None,
        unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetUnitOfMeasure
        ] = None,
        licensee_product_company: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetLicenseeProductCompany  # noqa
        ] = None,
        licensed_indicator: typing.Optional[
            bool
        ] = None,
        technology: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetTechnology
        ] = None,
        style_group: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleGroup
        ] = None,
        style_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleGroupType  # noqa
        ] = None,
        sport_level: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetSportLevel
        ] = None,
        team: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetTeam
        ] = None,
        league: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetLeague
        ] = None,
        style_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsGeographyGetStyleStatusIndicator  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Line Management
        Geography Offering entity

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
        - geo_product_offering_identifier:
          The reference key associated with this item: No Definition Available
        - product_offering_identifier:
          The reference key associated with this item: No Definition Available
        - geo_model_offering_identifier:
          The reference key associated with this item: No Definition Available
        - product_identifier:
          The reference key associated with this item: No Definition Available
        - geo_first_offer_date:
          The reference key associated with this item: No Definition Available
        - geo_restricted_region:
          The reference key associated with this item: No Definition Available
        - geo_marketing_type:
          The reference key associated with this item: No Definition Available
        - geo_alternate_marketing_type:
          The reference key associated with this item: No Definition Available
        - geo_smu_product_account:
          The reference key associated with this item: No Definition Available
        - geo_type_group:
          The reference key associated with this item: No Definition Available
        - geo_marketing_initiative:
          The reference key associated with this item: No Definition Available
        - geo_launch:
          The reference key associated with this item: No Definition Available
        - geo_launch_date:
          The reference key associated with this item: No Definition Available
        - geo_retail_size_range_description:
          The reference key associated with this item: No Definition Available
        - geo_retail_size_selection_list:
          The reference key associated with this item: No Definition Available
        - geo_promo_size_range_description:
          The reference key associated with this item: No Definition Available
        - geo_promo_size_selection_list:
          The reference key associated with this item: No Definition Available
        - geo_sales_sample_indicator:
          The true or false flag associated with this item: No Definition
          Available
        - geo_sales_sample_size_description:
          The reference key associated with this item: No Definition Available
        - geo_sales_sample_quantity:
          The reference key associated with this item: No Definition Available
        - geo_sales_sample_comment:
          The reference key associated with this item: No Definition Available
        - geo_product_offering_merchandising_forecast_quantity:
          The reference key associated with this item: No Definition Available
        - geo_product_carryover_status_indicator:
          The reference key associated with this item: No Definition Available
        - geo_product_offering_status_indicator:
          The reference key associated with this item: No Definition Available
        - geo_status_change_timestamp
        - geo_region:
          The reference key associated with this item: No Definition Available
        - model_offering_identifier:
          The reference key associated with this item: No Definition Available
        - cycle_year:
          The reference key associated with this item: No Definition Available
        - geo_target_wholesale_price:
          The reference key associated with this item: No Definition Available
        - geo_target_retail_price:
          The reference key associated with this item: No Definition Available
        - geo_currency:
          The reference key associated with this item: No Definition Available
        - geo_merchandising_manager_user_account_code:
          The reference key associated with this item: No Definition Available
        - geo_model_offering_merchandising_forecast_quantity:
          The reference key associated with this item: No Definition Available
        - territory_merchandising_region:
          The reference key associated with this item: No Definition Available
        - territory_merchandising_forecast_quantity:
          The reference key associated with this item: No Definition Available
        - geo_model_offering_carryover_status_indicator:
          The reference key associated with this item: No Definition Available
        - geo_model_offering_status_indicator:
          The reference key associated with this item: No Definition Available
        - product_code:
          The reference key associated with this item: No Definition Available
        - model_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%
          2520Identifier">Definition</a>
        - style_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Code">
          Definition</a>
        - colorway_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Colorway
          %2520Code">Definition</a>
        - dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - product_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - retail_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Range%2520Description">Definition</a>
        - retail_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Selection%2520List">Definition</a>
        - promo_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromotional%2520Size
          %2520Range%2520Description">Definition</a>
        - promo_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Selection%2520List">Definition</a>
        - colorway_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FColorway%
          2520Identifier">Definition</a>
        - primary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Color%
          2520Code">Definition</a>
        - secondary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSecondary%2520Color%
          2520Code">Definition</a>
        - tertiary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTertiary%2520Color%
          2520Code">Definition</a>
        - quaternary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FQuaternary%2520Color
          %2520Code">Definition</a>
        - logo_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Color%
          2520Code">Definition</a>
        - logo_accent_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Accent%
          2520Color%2520Code">Definition</a>
        - athlete:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAthlete%
          2520Identifier">Definition</a>
        - playerway_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlayerway%
          2520Number">Definition</a>
        - uniform_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUniform%2520Type%
          2520Identifier">Definition</a>
        - royalty_intent_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FRoyalty%
          2520Intent%2520Indicator">Definition</a>
        - product_lifecycle:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Lifecycle%2520Code">Definition</a>
        - closeout_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FClose%2520Out%
          2520Date">Definition</a>
        - category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCategory%2520Code">
          Definition</a>
        - sub_category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Code">Definition</a>
        - global_category_core_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGlobal%2520Category%
          2520Core%2520Focus%2520Code">Definition</a>
        - product_status_indicator:
          The A or I flag associated with this item: <a target="_blank" href ="
          http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Status%
          2520Indicator">Definition</a>
        - final_adopt_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinal%
          2520Adoption%2520Indicator">Definition</a>
        - division:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDivision%2520Code">
          Definition</a>
        - model_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Name">
          Definition</a>
        - gender:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Code">
          Definition</a>
        - age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAge%2520Code">
          Definition</a>
        - gender_age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Age%
          2520Code">Definition</a>
        - silhouette:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Code"
          >Definition</a>
        - silhouette_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Type%
          2520Code">Definition</a>
        - fit_preference:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Preference%
          2520Identifier">Definition</a>
        - merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMerchandising%
          2520Classification%2520Identifier">Definition</a>
        - primary_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Platform
          %2520Identifier">Definition</a>
        - model_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitial%2520Cycle%
          2520Year%2520Code">Definition</a>
        - model_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - model_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        - style_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Name">
          Definition</a>
        - style_fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - style_dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - style_initial_season_year_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - style_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%
          2520Description">Definition</a>
        - segment:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSegment%2520Code">
          Definition</a>
        - sub_brand:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Brand%
          2520Code">Definition</a>
        - sport_activity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Activity%
          2520Code">Definition</a>
        - silo:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilo%2520Identifier"
          >Definition</a>
        - sub_category_breakdown:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - style_merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - harmonized_style_number:
          The reference key associated with this item: Harmonized Style Number
        - construction_method:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConstruction%
          2520Identifier">Definition</a>
        - finished_goods_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinished%
          2520Goods%2520Indicator">Definition</a>
        - style_graphic_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Graphic%2520Indicator">Definition</a>
        - style_print_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Print%2520Indicator">Definition</a>
        - feature:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFeature%
          2520Identifier">Definition</a>
        - material_intent:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___search___all___material
          %2520intent%2520identifier">Definition</a>
        - brand_mark:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBrand%2520Mark%
          2520Identifier">Definition</a>
        - blank_usage_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FBlank%
          2520Usage%2520Indicator">Definition</a>
        - additional_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlatform%
          2520Identifier">Definition</a>
        - master_size_grid:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMaster%2520Size%
          2520Grid%2520Code">Definition</a>
        - delivery_unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDelivery%2520Unit%
          2520Quantity">Definition</a>
        - consumer_package_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Package
          %2520Quantity">Definition</a>
        - unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUnit%2520Of%
          2520Measure%2520Code">Definition</a>
        - licensee_product_company:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLicensee%2520Product
          %2520Company%2520Code">Definition</a>
        - licensed_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FLicensed%
          2520Indicator">Definition</a>
        - technology:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTechnology%2520Code"
          >Definition</a>
        - style_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Identifier">Definition</a>
        - style_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Type%2520Identifier">Definition</a>
        - sport_level:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Level%
          2520Identifier">Definition</a>
        - team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTeam%2520Identifier"
          >Definition</a>
        - league:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLeague%
          2520Identifier">Definition</a>
        - style_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStatus%
          2520Indicator">Definition</a>
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productOfferings/geography",
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
                "geoProductOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "geoProductOfferingIdentifier",
                    geo_product_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "productOfferingIdentifier": oapi.client.format_argument_value(
                    "productOfferingIdentifier",
                    product_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "geoModelOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "geoModelOfferingIdentifier",
                    geo_model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "geoFirstOfferDate": oapi.client.format_argument_value(
                    "geoFirstOfferDate",
                    geo_first_offer_date,
                    style="form",
                    explode=False,
                ),
                "geoRestrictedRegion": oapi.client.format_argument_value(
                    "geoRestrictedRegion",
                    geo_restricted_region,
                    style="form",
                    explode=False,
                ),
                "geoMarketingType": oapi.client.format_argument_value(
                    "geoMarketingType",
                    geo_marketing_type,
                    style="form",
                    explode=False,
                ),
                "geoAlternateMarketingType": oapi.client.format_argument_value(
                    "geoAlternateMarketingType",
                    geo_alternate_marketing_type,
                    style="form",
                    explode=False,
                ),
                "geoSMUProductAccount": oapi.client.format_argument_value(
                    "geoSMUProductAccount",
                    geo_smu_product_account,
                    style="form",
                    explode=False,
                ),
                "geoTypeGroup": oapi.client.format_argument_value(
                    "geoTypeGroup",
                    geo_type_group,
                    style="form",
                    explode=False,
                ),
                "geoMarketingInitiative": oapi.client.format_argument_value(
                    "geoMarketingInitiative",
                    geo_marketing_initiative,
                    style="form",
                    explode=False,
                ),
                "geoLaunch": oapi.client.format_argument_value(
                    "geoLaunch",
                    geo_launch,
                    style="form",
                    explode=False,
                ),
                "geoLaunchDate": oapi.client.format_argument_value(
                    "geoLaunchDate",
                    geo_launch_date,
                    style="form",
                    explode=False,
                ),
                "geoRetailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "geoRetailSizeRangeDescription",
                    geo_retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "geoRetailSizeSelectionList": oapi.client.format_argument_value(  # noqa
                    "geoRetailSizeSelectionList",
                    geo_retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "geoPromoSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "geoPromoSizeRangeDescription",
                    geo_promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "geoPromoSizeSelectionList": oapi.client.format_argument_value(
                    "geoPromoSizeSelectionList",
                    geo_promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "geoSalesSampleIndicator": oapi.client.format_argument_value(
                    "geoSalesSampleIndicator",
                    geo_sales_sample_indicator,
                    style="form",
                    explode=False,
                ),
                "geoSalesSampleSizeDescription": oapi.client.format_argument_value(  # noqa
                    "geoSalesSampleSizeDescription",
                    geo_sales_sample_size_description,
                    style="form",
                    explode=False,
                ),
                "geoSalesSampleQuantity": oapi.client.format_argument_value(
                    "geoSalesSampleQuantity",
                    geo_sales_sample_quantity,
                    style="form",
                    explode=False,
                ),
                "geoSalesSampleComment": oapi.client.format_argument_value(
                    "geoSalesSampleComment",
                    geo_sales_sample_comment,
                    style="form",
                    explode=False,
                ),
                "geoProductOfferingMerchandisingForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "geoProductOfferingMerchandisingForecastQuantity",
                    geo_product_offering_merchandising_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "geoProductCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "geoProductCarryoverStatusIndicator",
                    geo_product_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "geoProductOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "geoProductOfferingStatusIndicator",
                    geo_product_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "geoStatusChangeTimestamp": oapi.client.format_argument_value(
                    "geoStatusChangeTimestamp",
                    geo_status_change_timestamp,
                    style="form",
                    explode=False,
                ),
                "geoRegion": oapi.client.format_argument_value(
                    "geoRegion",
                    geo_region,
                    style="form",
                    explode=False,
                ),
                "modelOfferingIdentifier": oapi.client.format_argument_value(
                    "modelOfferingIdentifier",
                    model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "geoTargetWholesalePrice": oapi.client.format_argument_value(
                    "geoTargetWholesalePrice",
                    geo_target_wholesale_price,
                    style="form",
                    explode=False,
                ),
                "geoTargetRetailPrice": oapi.client.format_argument_value(
                    "geoTargetRetailPrice",
                    geo_target_retail_price,
                    style="form",
                    explode=False,
                ),
                "geoCurrency": oapi.client.format_argument_value(
                    "geoCurrency",
                    geo_currency,
                    style="form",
                    explode=False,
                ),
                "geoMerchandisingManagerUserAccountCode": oapi.client.format_argument_value(  # noqa
                    "geoMerchandisingManagerUserAccountCode",
                    geo_merchandising_manager_user_account_code,
                    style="form",
                    explode=False,
                ),
                "geoModelOfferingMerchandisingForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "geoModelOfferingMerchandisingForecastQuantity",
                    geo_model_offering_merchandising_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "territoryMerchandisingRegion": oapi.client.format_argument_value(  # noqa
                    "territoryMerchandisingRegion",
                    territory_merchandising_region,
                    style="form",
                    explode=False,
                ),
                "territoryMerchandisingForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "territoryMerchandisingForecastQuantity",
                    territory_merchandising_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "geoModelOfferingCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "geoModelOfferingCarryoverStatusIndicator",
                    geo_model_offering_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "geoModelOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "geoModelOfferingStatusIndicator",
                    geo_model_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
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
                "colorwayCode": oapi.client.format_argument_value(
                    "colorwayCode",
                    colorway_code,
                    style="form",
                    explode=False,
                ),
                "dimension": oapi.client.format_argument_value(
                    "dimension",
                    dimension,
                    style="form",
                    explode=False,
                ),
                "fit": oapi.client.format_argument_value(
                    "fit",
                    fit,
                    style="form",
                    explode=False,
                ),
                "productInitialSeasonYear": oapi.client.format_argument_value(
                    "productInitialSeasonYear",
                    product_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "retailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "retailSizeRangeDescription",
                    retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeSelectionList": oapi.client.format_argument_value(
                    "retailSizeSelectionList",
                    retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "promoSizeRangeDescription": oapi.client.format_argument_value(
                    "promoSizeRangeDescription",
                    promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeSelectionList": oapi.client.format_argument_value(
                    "promoSizeSelectionList",
                    promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "colorwayIdentifier": oapi.client.format_argument_value(
                    "colorwayIdentifier",
                    colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "primaryColor": oapi.client.format_argument_value(
                    "primaryColor",
                    primary_color,
                    style="form",
                    explode=False,
                ),
                "secondaryColor": oapi.client.format_argument_value(
                    "secondaryColor",
                    secondary_color,
                    style="form",
                    explode=False,
                ),
                "tertiaryColor": oapi.client.format_argument_value(
                    "tertiaryColor",
                    tertiary_color,
                    style="form",
                    explode=False,
                ),
                "quaternaryColor": oapi.client.format_argument_value(
                    "quaternaryColor",
                    quaternary_color,
                    style="form",
                    explode=False,
                ),
                "logoColor": oapi.client.format_argument_value(
                    "logoColor",
                    logo_color,
                    style="form",
                    explode=False,
                ),
                "logoAccentColor": oapi.client.format_argument_value(
                    "logoAccentColor",
                    logo_accent_color,
                    style="form",
                    explode=False,
                ),
                "athlete": oapi.client.format_argument_value(
                    "athlete",
                    athlete,
                    style="form",
                    explode=False,
                ),
                "playerwayNumber": oapi.client.format_argument_value(
                    "playerwayNumber",
                    playerway_number,
                    style="form",
                    explode=False,
                ),
                "uniformType": oapi.client.format_argument_value(
                    "uniformType",
                    uniform_type,
                    style="form",
                    explode=False,
                ),
                "royaltyIntentIndicator": oapi.client.format_argument_value(
                    "royaltyIntentIndicator",
                    royalty_intent_indicator,
                    style="form",
                    explode=False,
                ),
                "productLifecycle": oapi.client.format_argument_value(
                    "productLifecycle",
                    product_lifecycle,
                    style="form",
                    explode=False,
                ),
                "closeoutDate": oapi.client.format_argument_value(
                    "closeoutDate",
                    closeout_date,
                    style="form",
                    explode=False,
                ),
                "category": oapi.client.format_argument_value(
                    "category",
                    category,
                    style="form",
                    explode=False,
                ),
                "subCategory": oapi.client.format_argument_value(
                    "subCategory",
                    sub_category,
                    style="form",
                    explode=False,
                ),
                "globalCategoryCoreFocus": oapi.client.format_argument_value(
                    "globalCategoryCoreFocus",
                    global_category_core_focus,
                    style="form",
                    explode=False,
                ),
                "productStatusIndicator": oapi.client.format_argument_value(
                    "productStatusIndicator",
                    product_status_indicator,
                    style="form",
                    explode=False,
                ),
                "finalAdoptIndicator": oapi.client.format_argument_value(
                    "finalAdoptIndicator",
                    final_adopt_indicator,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "modelName": oapi.client.format_argument_value(
                    "modelName",
                    model_name,
                    style="form",
                    explode=False,
                ),
                "gender": oapi.client.format_argument_value(
                    "gender",
                    gender,
                    style="form",
                    explode=False,
                ),
                "age": oapi.client.format_argument_value(
                    "age",
                    age,
                    style="form",
                    explode=False,
                ),
                "genderAge": oapi.client.format_argument_value(
                    "genderAge",
                    gender_age,
                    style="form",
                    explode=False,
                ),
                "silhouette": oapi.client.format_argument_value(
                    "silhouette",
                    silhouette,
                    style="form",
                    explode=False,
                ),
                "silhouetteType": oapi.client.format_argument_value(
                    "silhouetteType",
                    silhouette_type,
                    style="form",
                    explode=False,
                ),
                "fitPreference": oapi.client.format_argument_value(
                    "fitPreference",
                    fit_preference,
                    style="form",
                    explode=False,
                ),
                "merchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "merchandisingClassification",
                    merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "primaryPlatform": oapi.client.format_argument_value(
                    "primaryPlatform",
                    primary_platform,
                    style="form",
                    explode=False,
                ),
                "modelInitialSeasonYear": oapi.client.format_argument_value(
                    "modelInitialSeasonYear",
                    model_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "modelGroupType": oapi.client.format_argument_value(
                    "modelGroupType",
                    model_group_type,
                    style="form",
                    explode=False,
                ),
                "modelGroup": oapi.client.format_argument_value(
                    "modelGroup",
                    model_group,
                    style="form",
                    explode=False,
                ),
                "styleName": oapi.client.format_argument_value(
                    "styleName",
                    style_name,
                    style="form",
                    explode=False,
                ),
                "styleFit": oapi.client.format_argument_value(
                    "styleFit",
                    style_fit,
                    style="form",
                    explode=False,
                ),
                "styleDimension": oapi.client.format_argument_value(
                    "styleDimension",
                    style_dimension,
                    style="form",
                    explode=False,
                ),
                "styleInitialSeasonYearCode": oapi.client.format_argument_value(  # noqa
                    "styleInitialSeasonYearCode",
                    style_initial_season_year_code,
                    style="form",
                    explode=False,
                ),
                "styleDescription": oapi.client.format_argument_value(
                    "styleDescription",
                    style_description,
                    style="form",
                    explode=False,
                ),
                "segment": oapi.client.format_argument_value(
                    "segment",
                    segment,
                    style="form",
                    explode=False,
                ),
                "subBrand": oapi.client.format_argument_value(
                    "subBrand",
                    sub_brand,
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    sport_activity,
                    style="form",
                    explode=False,
                ),
                "silo": oapi.client.format_argument_value(
                    "silo",
                    silo,
                    style="form",
                    explode=False,
                ),
                "subCategoryBreakdown": oapi.client.format_argument_value(
                    "subCategoryBreakdown",
                    sub_category_breakdown,
                    style="form",
                    explode=False,
                ),
                "styleMerchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "styleMerchandisingClassification",
                    style_merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "harmonizedStyleNumber": oapi.client.format_argument_value(
                    "harmonizedStyleNumber",
                    harmonized_style_number,
                    style="form",
                    explode=False,
                ),
                "constructionMethod": oapi.client.format_argument_value(
                    "constructionMethod",
                    construction_method,
                    style="form",
                    explode=False,
                ),
                "finishedGoodsIndicator": oapi.client.format_argument_value(
                    "finishedGoodsIndicator",
                    finished_goods_indicator,
                    style="form",
                    explode=False,
                ),
                "styleGraphicIndicator": oapi.client.format_argument_value(
                    "styleGraphicIndicator",
                    style_graphic_indicator,
                    style="form",
                    explode=False,
                ),
                "stylePrintIndicator": oapi.client.format_argument_value(
                    "stylePrintIndicator",
                    style_print_indicator,
                    style="form",
                    explode=False,
                ),
                "feature": oapi.client.format_argument_value(
                    "feature",
                    feature,
                    style="form",
                    explode=False,
                ),
                "materialIntent": oapi.client.format_argument_value(
                    "materialIntent",
                    material_intent,
                    style="form",
                    explode=False,
                ),
                "brandMark": oapi.client.format_argument_value(
                    "brandMark",
                    brand_mark,
                    style="form",
                    explode=False,
                ),
                "blankUsageIndicator": oapi.client.format_argument_value(
                    "blankUsageIndicator",
                    blank_usage_indicator,
                    style="form",
                    explode=False,
                ),
                "additionalPlatform": oapi.client.format_argument_value(
                    "additionalPlatform",
                    additional_platform,
                    style="form",
                    explode=False,
                ),
                "masterSizeGrid": oapi.client.format_argument_value(
                    "masterSizeGrid",
                    master_size_grid,
                    style="form",
                    explode=False,
                ),
                "deliveryUnitOfMeasure": oapi.client.format_argument_value(
                    "deliveryUnitOfMeasure",
                    delivery_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "consumerPackageQuantity": oapi.client.format_argument_value(
                    "consumerPackageQuantity",
                    consumer_package_quantity,
                    style="form",
                    explode=False,
                ),
                "unitOfMeasure": oapi.client.format_argument_value(
                    "unitOfMeasure",
                    unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "licenseeProductCompany": oapi.client.format_argument_value(
                    "licenseeProductCompany",
                    licensee_product_company,
                    style="form",
                    explode=False,
                ),
                "licensedIndicator": oapi.client.format_argument_value(
                    "licensedIndicator",
                    licensed_indicator,
                    style="form",
                    explode=False,
                ),
                "technology": oapi.client.format_argument_value(
                    "technology",
                    technology,
                    style="form",
                    explode=False,
                ),
                "styleGroup": oapi.client.format_argument_value(
                    "styleGroup",
                    style_group,
                    style="form",
                    explode=False,
                ),
                "styleGroupType": oapi.client.format_argument_value(
                    "styleGroupType",
                    style_group_type,
                    style="form",
                    explode=False,
                ),
                "sportLevel": oapi.client.format_argument_value(
                    "sportLevel",
                    sport_level,
                    style="form",
                    explode=False,
                ),
                "team": oapi.client.format_argument_value(
                    "team",
                    team,
                    style="form",
                    explode=False,
                ),
                "league": oapi.client.format_argument_value(
                    "league",
                    league,
                    style="form",
                    explode=False,
                ),
                "styleStatusIndicator": oapi.client.format_argument_value(
                    "styleStatusIndicator",
                    style_status_indicator,
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

    def get_line_management_search_product_offerings_country(
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
        country_product_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryProductOfferingIdentifier  # noqa
        ] = None,
        geo_product_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGeoProductOfferingIdentifier  # noqa
        ] = None,
        product_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetProductIdentifier  # noqa
        ] = None,
        country_model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryModelOfferingIdentifier  # noqa
        ] = None,
        country_first_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryFirstOfferDate  # noqa
        ] = None,
        country_end_futures_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryEndFuturesOfferDate  # noqa
        ] = None,
        country_end_offer_date: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryEndOfferDate  # noqa
        ] = None,
        country_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryMarketingType  # noqa
        ] = None,
        country_alternate_marketing_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryAlternateMarketingType  # noqa
        ] = None,
        country_smu_product_account: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountrySMUProductAccount  # noqa
        ] = None,
        country_type_group: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryTypeGroup  # noqa
        ] = None,
        country_marketing_initiative: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryMarketingInitiative  # noqa
        ] = None,
        country_retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryRetailSizeRangeDescription  # noqa
        ] = None,
        country_retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryRetailSizeSelectionList  # noqa
        ] = None,
        country_promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryPromoSizeRangeDescription  # noqa
        ] = None,
        country_promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryPromoSizeSelectionList  # noqa
        ] = None,
        country_sales_sample_indicator: typing.Optional[
            bool
        ] = None,
        country_sales_sample_size_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountrySalesSampleSizeDescription  # noqa
        ] = None,
        country_sales_sample_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountrySalesSampleQuantity  # noqa
        ] = None,
        country_sales_sample_comment: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountrySalesSampleComment  # noqa
        ] = None,
        country_product_offering_merchandising_forecast_quantity: typing.Optional[  # noqa
            model.LineManagementSearchProductOfferingsCountryGetCountryProductOfferingMerchandisingForecastQuantity  # noqa
        ] = None,
        country_product_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryProductCarryoverStatusIndicator  # noqa
        ] = None,
        country_product_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryProductOfferingStatusIndicator  # noqa
        ] = None,
        country_product_offering_status_change_timestamp: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryProductOfferingStatusChangeTimestamp  # noqa
        ] = None,
        geo_model_offering_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGeoModelOfferingIdentifier  # noqa
        ] = None,
        geo_region: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGeoRegion
        ] = None,
        cycle_year: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCycleYear
        ] = None,
        country_model_offering_merchandising_forecast_quantity: typing.Optional[  # noqa
            model.LineManagementSearchProductOfferingsCountryGetCountryModelOfferingMerchandisingForecastQuantity  # noqa
        ] = None,
        country_model_offering_carryover_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryModelOfferingCarryoverStatusIndicator  # noqa
        ] = None,
        country_model_offering_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCountryModelOfferingStatusIndicator  # noqa
        ] = None,
        product_code: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetProductCode
        ] = None,
        model_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetModelIdentifier
        ] = None,
        style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleNumber
        ] = None,
        colorway_code: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetColorwayCode
        ] = None,
        dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetDimension
        ] = None,
        fit: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetFit
        ] = None,
        product_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetProductInitialSeasonYear  # noqa
        ] = None,
        retail_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetRetailSizeRangeDescription  # noqa
        ] = None,
        retail_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetRetailSizeSelectionList  # noqa
        ] = None,
        promo_size_range_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetPromoSizeRangeDescription  # noqa
        ] = None,
        promo_size_selection_list: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetPromoSizeSelectionList  # noqa
        ] = None,
        colorway_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetColorwayIdentifier  # noqa
        ] = None,
        primary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetPrimaryColor
        ] = None,
        secondary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSecondaryColor
        ] = None,
        tertiary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetTertiaryColor
        ] = None,
        quaternary_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetQuaternaryColor
        ] = None,
        logo_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetLogoColor
        ] = None,
        logo_accent_color: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetLogoAccentColor
        ] = None,
        athlete: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetAthlete
        ] = None,
        playerway_number: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetPlayerwayNumber
        ] = None,
        uniform_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetUniformType
        ] = None,
        royalty_intent_indicator: typing.Optional[
            bool
        ] = None,
        product_lifecycle: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetProductLifecycle  # noqa
        ] = None,
        closeout_date: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCloseoutDate
        ] = None,
        category: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetCategory
        ] = None,
        sub_category: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSubCategory
        ] = None,
        global_category_core_focus: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGlobalCategoryCoreFocus  # noqa
        ] = None,
        product_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetProductStatusIndicator  # noqa
        ] = None,
        final_adopt_indicator: typing.Optional[
            bool
        ] = None,
        division: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetDivision
        ] = None,
        model_name: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetModelName
        ] = None,
        gender: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGender
        ] = None,
        age: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetAge
        ] = None,
        gender_age: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetGenderAge
        ] = None,
        silhouette: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSilhouette
        ] = None,
        silhouette_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSilhouetteType
        ] = None,
        fit_preference: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetFitPreference
        ] = None,
        merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetMerchandisingClassification  # noqa
        ] = None,
        primary_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetPrimaryPlatform
        ] = None,
        model_initial_season_year: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetModelInitialSeasonYear  # noqa
        ] = None,
        model_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetModelGroupType
        ] = None,
        model_group: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetModelGroup
        ] = None,
        style_name: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleName
        ] = None,
        style_fit: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleFit
        ] = None,
        style_dimension: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleDimension
        ] = None,
        style_initial_season_year_code: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleInitialSeasonYearCode  # noqa
        ] = None,
        style_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleDescription  # noqa
        ] = None,
        segment: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSegment
        ] = None,
        sub_brand: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSubBrand
        ] = None,
        sport_activity: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSportActivity
        ] = None,
        silo: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSilo
        ] = None,
        sub_category_breakdown: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSubCategoryBreakdown  # noqa
        ] = None,
        style_merchandising_classification: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleMerchandisingClassification  # noqa
        ] = None,
        harmonized_style_number: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetHarmonizedStyleNumber  # noqa
        ] = None,
        construction_method: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetConstructionMethod  # noqa
        ] = None,
        finished_goods_indicator: typing.Optional[
            bool
        ] = None,
        style_graphic_indicator: typing.Optional[
            bool
        ] = None,
        style_print_indicator: typing.Optional[
            bool
        ] = None,
        feature: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetFeature
        ] = None,
        material_intent: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetMaterialIntent
        ] = None,
        brand_mark: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetBrandMark
        ] = None,
        blank_usage_indicator: typing.Optional[
            bool
        ] = None,
        additional_platform: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetAdditionalPlatform  # noqa
        ] = None,
        master_size_grid: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetMasterSizeGrid
        ] = None,
        delivery_unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetDeliveryUnitOfMeasure  # noqa
        ] = None,
        consumer_package_quantity: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetConsumerPackageQuantity  # noqa
        ] = None,
        unit_of_measure: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetUnitOfMeasure
        ] = None,
        licensee_product_company: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetLicenseeProductCompany  # noqa
        ] = None,
        licensed_indicator: typing.Optional[
            bool
        ] = None,
        technology: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetTechnology
        ] = None,
        style_group_identifier: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleGroupIdentifier  # noqa
        ] = None,
        style_group_description: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleGroupDescription  # noqa
        ] = None,
        style_group_type: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleGroupType
        ] = None,
        sport_level: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetSportLevel
        ] = None,
        team: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetTeam
        ] = None,
        league: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetLeague
        ] = None,
        style_status_indicator: typing.Optional[
            model.LineManagementSearchProductOfferingsCountryGetStyleStatusIndicator  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Line Management
        Country Offering entity

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
        - country_product_offering_identifier:
          The reference key associated with this item: No Definition Available
        - geo_product_offering_identifier:
          The reference key associated with this item: No Definition Available
        - product_identifier:
          The reference key associated with this item: No Definition Available
        - country_model_offering_identifier:
          The reference key associated with this item: No Definition Available
        - country_first_offer_date:
          The reference key associated with this item: No Definition Available
        - country_end_futures_offer_date:
          The reference key associated with this item: No Definition Available
        - country_end_offer_date:
          The reference key associated with this item: No Definition Available
        - country_marketing_type:
          The reference key associated with this item: No Definition Available
        - country_alternate_marketing_type:
          The reference key associated with this item: No Definition Available
        - country_smu_product_account:
          The reference key associated with this item: No Definition Available
        - country_type_group:
          The reference key associated with this item: No Definition Available
        - country_marketing_initiative:
          The reference key associated with this item: No Definition Available
        - country_retail_size_range_description:
          The reference key associated with this item: No Definition Available
        - country_retail_size_selection_list:
          The reference key associated with this item: No Definition Available
        - country_promo_size_range_description:
          The reference key associated with this item: No Definition Available
        - country_promo_size_selection_list:
          The reference key associated with this item: No Definition Available
        - country_sales_sample_indicator:
          The true or false flag associated with this item: No Definition
          Available
        - country_sales_sample_size_description:
          The reference key associated with this item: No Definition Available
        - country_sales_sample_quantity:
          The reference key associated with this item: No Definition Available
        - country_sales_sample_comment:
          The reference key associated with this item: No Definition Available
        - country_product_offering_merchandising_forecast_quantity:
          The reference key associated with this item: No Definition Available
        - country_product_carryover_status_indicator:
          The reference key associated with this item: No Definition Available
        - country_product_offering_status_indicator:
          The reference key associated with this item: No Definition Available
        - country_product_offering_status_change_timestamp
        - geo_model_offering_identifier:
          The reference key associated with this item: No Definition Available
        - geo_region:
          The reference key associated with this item: No Definition Available
        - cycle_year:
          The reference key associated with this item: No Definition Available
        - country_model_offering_merchandising_forecast_quantity:
          The reference key associated with this item: No Definition Available
        - country_model_offering_carryover_status_indicator:
          The reference key associated with this item: No Definition Available
        - country_model_offering_status_indicator:
          The reference key associated with this item: No Definition Available
        - product_code:
          The reference key associated with this item: No Definition Available
        - model_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%
          2520Identifier">Definition</a>
        - style_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Code">
          Definition</a>
        - colorway_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Colorway
          %2520Code">Definition</a>
        - dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - product_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - retail_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Range%2520Description">Definition</a>
        - retail_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FRetail%2520Size%
          2520Selection%2520List">Definition</a>
        - promo_size_range_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromotional%2520Size
          %2520Range%2520Description">Definition</a>
        - promo_size_selection_list:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPromo%2520Size%
          2520Selection%2520List">Definition</a>
        - colorway_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FColorway%
          2520Identifier">Definition</a>
        - primary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Color%
          2520Code">Definition</a>
        - secondary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSecondary%2520Color%
          2520Code">Definition</a>
        - tertiary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTertiary%2520Color%
          2520Code">Definition</a>
        - quaternary_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FQuaternary%2520Color
          %2520Code">Definition</a>
        - logo_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Color%
          2520Code">Definition</a>
        - logo_accent_color:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLogo%2520Accent%
          2520Color%2520Code">Definition</a>
        - athlete:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAthlete%
          2520Identifier">Definition</a>
        - playerway_number:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlayerway%
          2520Number">Definition</a>
        - uniform_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUniform%2520Type%
          2520Identifier">Definition</a>
        - royalty_intent_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FRoyalty%
          2520Intent%2520Indicator">Definition</a>
        - product_lifecycle:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Lifecycle%2520Code">Definition</a>
        - closeout_date:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FClose%2520Out%
          2520Date">Definition</a>
        - category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FCategory%2520Code">
          Definition</a>
        - sub_category:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Code">Definition</a>
        - global_category_core_focus:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGlobal%2520Category%
          2520Core%2520Focus%2520Code">Definition</a>
        - product_status_indicator:
          The A or I flag associated with this item: <a target="_blank" href ="
          http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%2520Status%
          2520Indicator">Definition</a>
        - final_adopt_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinal%
          2520Adoption%2520Indicator">Definition</a>
        - division:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDivision%2520Code">
          Definition</a>
        - model_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Name">
          Definition</a>
        - gender:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Code">
          Definition</a>
        - age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FAge%2520Code">
          Definition</a>
        - gender_age:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FGender%2520Age%
          2520Code">Definition</a>
        - silhouette:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Code"
          >Definition</a>
        - silhouette_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilhouette%2520Type%
          2520Code">Definition</a>
        - fit_preference:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Preference%
          2520Identifier">Definition</a>
        - merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMerchandising%
          2520Classification%2520Identifier">Definition</a>
        - primary_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPrimary%2520Platform
          %2520Identifier">Definition</a>
        - model_initial_season_year:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FInitial%2520Cycle%
          2520Year%2520Code">Definition</a>
        - model_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Type%2520Identifier">Definition</a>
        - model_group:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FModel%2520Group%
          2520Identifier">Definition</a>
        - style_name:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Name">
          Definition</a>
        - style_fit:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFit%2520Code">
          Definition</a>
        - style_dimension:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDimension%2520Code">
          Definition</a>
        - style_initial_season_year_code:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FConcept%252FStyle%2520Initial%2520Season">
          Definition</a>
        - style_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%
          2520Description">Definition</a>
        - segment:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSegment%2520Code">
          Definition</a>
        - sub_brand:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Brand%
          2520Code">Definition</a>
        - sport_activity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Activity%
          2520Code">Definition</a>
        - silo:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSilo%2520Identifier"
          >Definition</a>
        - sub_category_breakdown:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - style_merchandising_classification:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSub%2520Category%
          2520Breakdown%2520Identifier">Definition</a>
        - harmonized_style_number:
          The reference key associated with this item: Harmonized Style Number
        - construction_method:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConstruction%
          2520Identifier">Definition</a>
        - finished_goods_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FFinished%
          2520Goods%2520Indicator">Definition</a>
        - style_graphic_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Graphic%2520Indicator">Definition</a>
        - style_print_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FProduct%
          2520Print%2520Indicator">Definition</a>
        - feature:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FFeature%
          2520Identifier">Definition</a>
        - material_intent:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___search___all___material
          %2520intent%2520identifier">Definition</a>
        - brand_mark:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FBrand%2520Mark%
          2520Identifier">Definition</a>
        - blank_usage_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FBlank%
          2520Usage%2520Indicator">Definition</a>
        - additional_platform:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FPlatform%
          2520Identifier">Definition</a>
        - master_size_grid:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FMaster%2520Size%
          2520Grid%2520Code">Definition</a>
        - delivery_unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FDelivery%2520Unit%
          2520Quantity">Definition</a>
        - consumer_package_quantity:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FConsumer%2520Package
          %2520Quantity">Definition</a>
        - unit_of_measure:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FUnit%2520Of%
          2520Measure%2520Code">Definition</a>
        - licensee_product_company:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLicensee%2520Product
          %2520Company%2520Code">Definition</a>
        - licensed_indicator:
          The true or false flag associated with this item: <a target="_blank"
          href ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%
          252FNike%2520Approved%2520Terms%252FBusiness%2520Term%252FLicensed%
          2520Indicator">Definition</a>
        - technology:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTechnology%2520Code"
          >Definition</a>
        - style_group_identifier:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Identifier">Definition</a>
        - style_group_description:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Description">Definition</a>
        - style_group_type:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStyle%2520Group%
          2520Type%2520Identifier">Definition</a>
        - sport_level:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FSport%2520Level%
          2520Identifier">Definition</a>
        - team:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FTeam%2520Identifier"
          >Definition</a>
        - league:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FLeague%
          2520Identifier">Definition</a>
        - style_status_indicator:
          The reference key associated with this item: <a target="_blank" href
           ="http://nke-lnx-int-q013:10250/mm/#browse___glossary___MM%252FNike%
          2520Approved%2520Terms%252FBusiness%2520Term%252FStatus%
          2520Indicator">Definition</a>
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productOfferings/country",
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
                "countryProductOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "countryProductOfferingIdentifier",
                    country_product_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "geoProductOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "geoProductOfferingIdentifier",
                    geo_product_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "countryModelOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "countryModelOfferingIdentifier",
                    country_model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "countryFirstOfferDate": oapi.client.format_argument_value(
                    "countryFirstOfferDate",
                    country_first_offer_date,
                    style="form",
                    explode=False,
                ),
                "countryEndFuturesOfferDate": oapi.client.format_argument_value(  # noqa
                    "countryEndFuturesOfferDate",
                    country_end_futures_offer_date,
                    style="form",
                    explode=False,
                ),
                "countryEndOfferDate": oapi.client.format_argument_value(
                    "countryEndOfferDate",
                    country_end_offer_date,
                    style="form",
                    explode=False,
                ),
                "countryMarketingType": oapi.client.format_argument_value(
                    "countryMarketingType",
                    country_marketing_type,
                    style="form",
                    explode=False,
                ),
                "countryAlternateMarketingType": oapi.client.format_argument_value(  # noqa
                    "countryAlternateMarketingType",
                    country_alternate_marketing_type,
                    style="form",
                    explode=False,
                ),
                "countrySMUProductAccount": oapi.client.format_argument_value(
                    "countrySMUProductAccount",
                    country_smu_product_account,
                    style="form",
                    explode=False,
                ),
                "countryTypeGroup": oapi.client.format_argument_value(
                    "countryTypeGroup",
                    country_type_group,
                    style="form",
                    explode=False,
                ),
                "countryMarketingInitiative": oapi.client.format_argument_value(  # noqa
                    "countryMarketingInitiative",
                    country_marketing_initiative,
                    style="form",
                    explode=False,
                ),
                "countryRetailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "countryRetailSizeRangeDescription",
                    country_retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "countryRetailSizeSelectionList": oapi.client.format_argument_value(  # noqa
                    "countryRetailSizeSelectionList",
                    country_retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "countryPromoSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "countryPromoSizeRangeDescription",
                    country_promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "countryPromoSizeSelectionList": oapi.client.format_argument_value(  # noqa
                    "countryPromoSizeSelectionList",
                    country_promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "countrySalesSampleIndicator": oapi.client.format_argument_value(  # noqa
                    "countrySalesSampleIndicator",
                    country_sales_sample_indicator,
                    style="form",
                    explode=False,
                ),
                "countrySalesSampleSizeDescription": oapi.client.format_argument_value(  # noqa
                    "countrySalesSampleSizeDescription",
                    country_sales_sample_size_description,
                    style="form",
                    explode=False,
                ),
                "countrySalesSampleQuantity": oapi.client.format_argument_value(  # noqa
                    "countrySalesSampleQuantity",
                    country_sales_sample_quantity,
                    style="form",
                    explode=False,
                ),
                "countrySalesSampleComment": oapi.client.format_argument_value(
                    "countrySalesSampleComment",
                    country_sales_sample_comment,
                    style="form",
                    explode=False,
                ),
                "countryProductOfferingMerchandisingForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "countryProductOfferingMerchandisingForecastQuantity",
                    country_product_offering_merchandising_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "countryProductCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "countryProductCarryoverStatusIndicator",
                    country_product_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "countryProductOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "countryProductOfferingStatusIndicator",
                    country_product_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "countryProductOfferingStatusChangeTimestamp": oapi.client.format_argument_value(  # noqa
                    "countryProductOfferingStatusChangeTimestamp",
                    country_product_offering_status_change_timestamp,
                    style="form",
                    explode=False,
                ),
                "geoModelOfferingIdentifier": oapi.client.format_argument_value(  # noqa
                    "geoModelOfferingIdentifier",
                    geo_model_offering_identifier,
                    style="form",
                    explode=False,
                ),
                "geoRegion": oapi.client.format_argument_value(
                    "geoRegion",
                    geo_region,
                    style="form",
                    explode=False,
                ),
                "cycleYear": oapi.client.format_argument_value(
                    "cycleYear",
                    cycle_year,
                    style="form",
                    explode=False,
                ),
                "countryModelOfferingMerchandisingForecastQuantity": oapi.client.format_argument_value(  # noqa
                    "countryModelOfferingMerchandisingForecastQuantity",
                    country_model_offering_merchandising_forecast_quantity,
                    style="form",
                    explode=False,
                ),
                "countryModelOfferingCarryoverStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "countryModelOfferingCarryoverStatusIndicator",
                    country_model_offering_carryover_status_indicator,
                    style="form",
                    explode=False,
                ),
                "countryModelOfferingStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "countryModelOfferingStatusIndicator",
                    country_model_offering_status_indicator,
                    style="form",
                    explode=False,
                ),
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
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
                "colorwayCode": oapi.client.format_argument_value(
                    "colorwayCode",
                    colorway_code,
                    style="form",
                    explode=False,
                ),
                "dimension": oapi.client.format_argument_value(
                    "dimension",
                    dimension,
                    style="form",
                    explode=False,
                ),
                "fit": oapi.client.format_argument_value(
                    "fit",
                    fit,
                    style="form",
                    explode=False,
                ),
                "productInitialSeasonYear": oapi.client.format_argument_value(
                    "productInitialSeasonYear",
                    product_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "retailSizeRangeDescription": oapi.client.format_argument_value(  # noqa
                    "retailSizeRangeDescription",
                    retail_size_range_description,
                    style="form",
                    explode=False,
                ),
                "retailSizeSelectionList": oapi.client.format_argument_value(
                    "retailSizeSelectionList",
                    retail_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "promoSizeRangeDescription": oapi.client.format_argument_value(
                    "promoSizeRangeDescription",
                    promo_size_range_description,
                    style="form",
                    explode=False,
                ),
                "promoSizeSelectionList": oapi.client.format_argument_value(
                    "promoSizeSelectionList",
                    promo_size_selection_list,
                    style="form",
                    explode=False,
                ),
                "colorwayIdentifier": oapi.client.format_argument_value(
                    "colorwayIdentifier",
                    colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "primaryColor": oapi.client.format_argument_value(
                    "primaryColor",
                    primary_color,
                    style="form",
                    explode=False,
                ),
                "secondaryColor": oapi.client.format_argument_value(
                    "secondaryColor",
                    secondary_color,
                    style="form",
                    explode=False,
                ),
                "tertiaryColor": oapi.client.format_argument_value(
                    "tertiaryColor",
                    tertiary_color,
                    style="form",
                    explode=False,
                ),
                "quaternaryColor": oapi.client.format_argument_value(
                    "quaternaryColor",
                    quaternary_color,
                    style="form",
                    explode=False,
                ),
                "logoColor": oapi.client.format_argument_value(
                    "logoColor",
                    logo_color,
                    style="form",
                    explode=False,
                ),
                "logoAccentColor": oapi.client.format_argument_value(
                    "logoAccentColor",
                    logo_accent_color,
                    style="form",
                    explode=False,
                ),
                "athlete": oapi.client.format_argument_value(
                    "athlete",
                    athlete,
                    style="form",
                    explode=False,
                ),
                "playerwayNumber": oapi.client.format_argument_value(
                    "playerwayNumber",
                    playerway_number,
                    style="form",
                    explode=False,
                ),
                "uniformType": oapi.client.format_argument_value(
                    "uniformType",
                    uniform_type,
                    style="form",
                    explode=False,
                ),
                "royaltyIntentIndicator": oapi.client.format_argument_value(
                    "royaltyIntentIndicator",
                    royalty_intent_indicator,
                    style="form",
                    explode=False,
                ),
                "productLifecycle": oapi.client.format_argument_value(
                    "productLifecycle",
                    product_lifecycle,
                    style="form",
                    explode=False,
                ),
                "closeoutDate": oapi.client.format_argument_value(
                    "closeoutDate",
                    closeout_date,
                    style="form",
                    explode=False,
                ),
                "category": oapi.client.format_argument_value(
                    "category",
                    category,
                    style="form",
                    explode=False,
                ),
                "subCategory": oapi.client.format_argument_value(
                    "subCategory",
                    sub_category,
                    style="form",
                    explode=False,
                ),
                "globalCategoryCoreFocus": oapi.client.format_argument_value(
                    "globalCategoryCoreFocus",
                    global_category_core_focus,
                    style="form",
                    explode=False,
                ),
                "productStatusIndicator": oapi.client.format_argument_value(
                    "productStatusIndicator",
                    product_status_indicator,
                    style="form",
                    explode=False,
                ),
                "finalAdoptIndicator": oapi.client.format_argument_value(
                    "finalAdoptIndicator",
                    final_adopt_indicator,
                    style="form",
                    explode=False,
                ),
                "division": oapi.client.format_argument_value(
                    "division",
                    division,
                    style="form",
                    explode=False,
                ),
                "modelName": oapi.client.format_argument_value(
                    "modelName",
                    model_name,
                    style="form",
                    explode=False,
                ),
                "gender": oapi.client.format_argument_value(
                    "gender",
                    gender,
                    style="form",
                    explode=False,
                ),
                "age": oapi.client.format_argument_value(
                    "age",
                    age,
                    style="form",
                    explode=False,
                ),
                "genderAge": oapi.client.format_argument_value(
                    "genderAge",
                    gender_age,
                    style="form",
                    explode=False,
                ),
                "silhouette": oapi.client.format_argument_value(
                    "silhouette",
                    silhouette,
                    style="form",
                    explode=False,
                ),
                "silhouetteType": oapi.client.format_argument_value(
                    "silhouetteType",
                    silhouette_type,
                    style="form",
                    explode=False,
                ),
                "fitPreference": oapi.client.format_argument_value(
                    "fitPreference",
                    fit_preference,
                    style="form",
                    explode=False,
                ),
                "merchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "merchandisingClassification",
                    merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "primaryPlatform": oapi.client.format_argument_value(
                    "primaryPlatform",
                    primary_platform,
                    style="form",
                    explode=False,
                ),
                "modelInitialSeasonYear": oapi.client.format_argument_value(
                    "modelInitialSeasonYear",
                    model_initial_season_year,
                    style="form",
                    explode=False,
                ),
                "modelGroupType": oapi.client.format_argument_value(
                    "modelGroupType",
                    model_group_type,
                    style="form",
                    explode=False,
                ),
                "modelGroup": oapi.client.format_argument_value(
                    "modelGroup",
                    model_group,
                    style="form",
                    explode=False,
                ),
                "styleName": oapi.client.format_argument_value(
                    "styleName",
                    style_name,
                    style="form",
                    explode=False,
                ),
                "styleFit": oapi.client.format_argument_value(
                    "styleFit",
                    style_fit,
                    style="form",
                    explode=False,
                ),
                "styleDimension": oapi.client.format_argument_value(
                    "styleDimension",
                    style_dimension,
                    style="form",
                    explode=False,
                ),
                "styleInitialSeasonYearCode": oapi.client.format_argument_value(  # noqa
                    "styleInitialSeasonYearCode",
                    style_initial_season_year_code,
                    style="form",
                    explode=False,
                ),
                "styleDescription": oapi.client.format_argument_value(
                    "styleDescription",
                    style_description,
                    style="form",
                    explode=False,
                ),
                "segment": oapi.client.format_argument_value(
                    "segment",
                    segment,
                    style="form",
                    explode=False,
                ),
                "subBrand": oapi.client.format_argument_value(
                    "subBrand",
                    sub_brand,
                    style="form",
                    explode=False,
                ),
                "sportActivity": oapi.client.format_argument_value(
                    "sportActivity",
                    sport_activity,
                    style="form",
                    explode=False,
                ),
                "silo": oapi.client.format_argument_value(
                    "silo",
                    silo,
                    style="form",
                    explode=False,
                ),
                "subCategoryBreakdown": oapi.client.format_argument_value(
                    "subCategoryBreakdown",
                    sub_category_breakdown,
                    style="form",
                    explode=False,
                ),
                "styleMerchandisingClassification": oapi.client.format_argument_value(  # noqa
                    "styleMerchandisingClassification",
                    style_merchandising_classification,
                    style="form",
                    explode=False,
                ),
                "harmonizedStyleNumber": oapi.client.format_argument_value(
                    "harmonizedStyleNumber",
                    harmonized_style_number,
                    style="form",
                    explode=False,
                ),
                "constructionMethod": oapi.client.format_argument_value(
                    "constructionMethod",
                    construction_method,
                    style="form",
                    explode=False,
                ),
                "finishedGoodsIndicator": oapi.client.format_argument_value(
                    "finishedGoodsIndicator",
                    finished_goods_indicator,
                    style="form",
                    explode=False,
                ),
                "styleGraphicIndicator": oapi.client.format_argument_value(
                    "styleGraphicIndicator",
                    style_graphic_indicator,
                    style="form",
                    explode=False,
                ),
                "stylePrintIndicator": oapi.client.format_argument_value(
                    "stylePrintIndicator",
                    style_print_indicator,
                    style="form",
                    explode=False,
                ),
                "feature": oapi.client.format_argument_value(
                    "feature",
                    feature,
                    style="form",
                    explode=False,
                ),
                "materialIntent": oapi.client.format_argument_value(
                    "materialIntent",
                    material_intent,
                    style="form",
                    explode=False,
                ),
                "brandMark": oapi.client.format_argument_value(
                    "brandMark",
                    brand_mark,
                    style="form",
                    explode=False,
                ),
                "blankUsageIndicator": oapi.client.format_argument_value(
                    "blankUsageIndicator",
                    blank_usage_indicator,
                    style="form",
                    explode=False,
                ),
                "additionalPlatform": oapi.client.format_argument_value(
                    "additionalPlatform",
                    additional_platform,
                    style="form",
                    explode=False,
                ),
                "masterSizeGrid": oapi.client.format_argument_value(
                    "masterSizeGrid",
                    master_size_grid,
                    style="form",
                    explode=False,
                ),
                "deliveryUnitOfMeasure": oapi.client.format_argument_value(
                    "deliveryUnitOfMeasure",
                    delivery_unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "consumerPackageQuantity": oapi.client.format_argument_value(
                    "consumerPackageQuantity",
                    consumer_package_quantity,
                    style="form",
                    explode=False,
                ),
                "unitOfMeasure": oapi.client.format_argument_value(
                    "unitOfMeasure",
                    unit_of_measure,
                    style="form",
                    explode=False,
                ),
                "licenseeProductCompany": oapi.client.format_argument_value(
                    "licenseeProductCompany",
                    licensee_product_company,
                    style="form",
                    explode=False,
                ),
                "licensedIndicator": oapi.client.format_argument_value(
                    "licensedIndicator",
                    licensed_indicator,
                    style="form",
                    explode=False,
                ),
                "technology": oapi.client.format_argument_value(
                    "technology",
                    technology,
                    style="form",
                    explode=False,
                ),
                "styleGroupIdentifier": oapi.client.format_argument_value(
                    "styleGroupIdentifier",
                    style_group_identifier,
                    style="form",
                    explode=False,
                ),
                "styleGroupDescription": oapi.client.format_argument_value(
                    "styleGroupDescription",
                    style_group_description,
                    style="form",
                    explode=False,
                ),
                "styleGroupType": oapi.client.format_argument_value(
                    "styleGroupType",
                    style_group_type,
                    style="form",
                    explode=False,
                ),
                "sportLevel": oapi.client.format_argument_value(
                    "sportLevel",
                    sport_level,
                    style="form",
                    explode=False,
                ),
                "team": oapi.client.format_argument_value(
                    "team",
                    team,
                    style="form",
                    explode=False,
                ),
                "league": oapi.client.format_argument_value(
                    "league",
                    league,
                    style="form",
                    explode=False,
                ),
                "styleStatusIndicator": oapi.client.format_argument_value(
                    "styleStatusIndicator",
                    style_status_indicator,
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

    def get_line_management_search_product_sizes_gtin(
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
        product_code: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetProductCode
        ] = None,
        size_description: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetSizeDescription
        ] = None,
        gtin_type: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetGtinType
        ] = None,
        gtin: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetGtin
        ] = None,
        gtin_status_indicator: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetGtinStatusIndicator
        ] = None,
        gtin_product_company: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetGtinProductCompany
        ] = None,
        b_grade_gtin: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetBGradeGTIN
        ] = None,
        size_promo_indicator: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetSizePromoIndicator
        ] = None,
        master_size: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetMasterSize
        ] = None,
        alternate_size_type_code: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetAlternateSizeTypeCode
        ] = None,
        alternate_size_description: typing.Optional[
            model.LineManagementSearchProductSizesGTINGetAlternateSizeDescription  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Line Management
        Product Size GTIN entity

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
        - product_code
        - size_description
        - gtin_type
        - gtin:
          UPC
        - gtin_status_indicator
        - gtin_product_company
        - b_grade_gtin:
          B-Grade UPC
        - size_promo_indicator
        - master_size
        - alternate_size_type_code
        - alternate_size_description
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productSizesGTIN",
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
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
                    style="form",
                    explode=False,
                ),
                "sizeDescription": oapi.client.format_argument_value(
                    "sizeDescription",
                    size_description,
                    style="form",
                    explode=False,
                ),
                "gtinType": oapi.client.format_argument_value(
                    "gtinType",
                    gtin_type,
                    style="form",
                    explode=False,
                ),
                "gtin": oapi.client.format_argument_value(
                    "gtin",
                    gtin,
                    style="form",
                    explode=False,
                ),
                "gtinStatusIndicator": oapi.client.format_argument_value(
                    "gtinStatusIndicator",
                    gtin_status_indicator,
                    style="form",
                    explode=False,
                ),
                "gtinProductCompany": oapi.client.format_argument_value(
                    "gtinProductCompany",
                    gtin_product_company,
                    style="form",
                    explode=False,
                ),
                "bGradeGTIN": oapi.client.format_argument_value(
                    "bGradeGTIN",
                    b_grade_gtin,
                    style="form",
                    explode=False,
                ),
                "sizePromoIndicator": oapi.client.format_argument_value(
                    "sizePromoIndicator",
                    size_promo_indicator,
                    style="form",
                    explode=False,
                ),
                "masterSize": oapi.client.format_argument_value(
                    "masterSize",
                    master_size,
                    style="form",
                    explode=False,
                ),
                "alternateSizeTypeCode": oapi.client.format_argument_value(
                    "alternateSizeTypeCode",
                    alternate_size_type_code,
                    style="form",
                    explode=False,
                ),
                "alternateSizeDescription": oapi.client.format_argument_value(
                    "alternateSizeDescription",
                    alternate_size_description,
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

    def get_line_management_search_product_regions(
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
        product_code: typing.Optional[
            model.LineManagementSearchProductRegionsGetProductCode
        ] = None,
        product_identifier: typing.Optional[
            model.LineManagementSearchProductRegionsGetProductIdentifier
        ] = None,
        geo_region: typing.Optional[
            model.LineManagementSearchProductRegionsGetGeoRegion
        ] = None,
        region_lifecycle: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionLifecycle
        ] = None,
        product_closeout_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetProductCloseoutDate
        ] = None,
        region_wholesale_price: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionWholesalePrice
        ] = None,
        region_wholesale_currency: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionWholesaleCurrency
        ] = None,
        region_wholesale_effective_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionWholesaleEffectiveDate  # noqa
        ] = None,
        region_retail_price: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionRetailPrice
        ] = None,
        region_retail_currency: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionRetailCurrency
        ] = None,
        region_retail_effective_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionRetailEffectiveDate  # noqa
        ] = None,
        region_launch: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionLaunch
        ] = None,
        region_launch_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetRegionLaunchDate
        ] = None,
        rebuy_indicator: typing.Optional[
            model.LineManagementSearchProductRegionsGetRebuyIndicator
        ] = None,
        rebuy_begin_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetRebuyBeginDate
        ] = None,
        rebuy_end_date: typing.Optional[
            model.LineManagementSearchProductRegionsGetRebuyEndDate
        ] = None,
        cmp_indicator: typing.Optional[
            model.LineManagementSearchProductRegionsGetCMPIndicator
        ] = None,
        blank_indicator: typing.Optional[
            model.LineManagementSearchProductRegionsGetBlankIndicator
        ] = None,
        pre_pack_code: typing.Optional[
            model.LineManagementSearchProductRegionsGetPrePackCode
        ] = None,
        delivery_unit_quantity: typing.Optional[
            model.LineManagementSearchProductRegionsGetDeliveryUnitQuantity
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Line Management
        Product Region entity

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
        - product_code
        - product_identifier
        - geo_region
        - region_lifecycle
        - product_closeout_date
        - region_wholesale_price
        - region_wholesale_currency
        - region_wholesale_effective_date
        - region_retail_price
        - region_retail_currency
        - region_retail_effective_date
        - region_launch
        - region_launch_date
        - rebuy_indicator
        - rebuy_begin_date
        - rebuy_end_date
        - cmp_indicator
        - blank_indicator
        - pre_pack_code
        - delivery_unit_quantity
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/productRegions",
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
                "productCode": oapi.client.format_argument_value(
                    "productCode",
                    product_code,
                    style="form",
                    explode=False,
                ),
                "productIdentifier": oapi.client.format_argument_value(
                    "productIdentifier",
                    product_identifier,
                    style="form",
                    explode=False,
                ),
                "geoRegion": oapi.client.format_argument_value(
                    "geoRegion",
                    geo_region,
                    style="form",
                    explode=False,
                ),
                "regionLifecycle": oapi.client.format_argument_value(
                    "regionLifecycle",
                    region_lifecycle,
                    style="form",
                    explode=False,
                ),
                "productCloseoutDate": oapi.client.format_argument_value(
                    "productCloseoutDate",
                    product_closeout_date,
                    style="form",
                    explode=False,
                ),
                "regionWholesalePrice": oapi.client.format_argument_value(
                    "regionWholesalePrice",
                    region_wholesale_price,
                    style="form",
                    explode=False,
                ),
                "regionWholesaleCurrency": oapi.client.format_argument_value(
                    "regionWholesaleCurrency",
                    region_wholesale_currency,
                    style="form",
                    explode=False,
                ),
                "regionWholesaleEffectiveDate": oapi.client.format_argument_value(  # noqa
                    "regionWholesaleEffectiveDate",
                    region_wholesale_effective_date,
                    style="form",
                    explode=False,
                ),
                "regionRetailPrice": oapi.client.format_argument_value(
                    "regionRetailPrice",
                    region_retail_price,
                    style="form",
                    explode=False,
                ),
                "regionRetailCurrency": oapi.client.format_argument_value(
                    "regionRetailCurrency",
                    region_retail_currency,
                    style="form",
                    explode=False,
                ),
                "regionRetailEffectiveDate": oapi.client.format_argument_value(
                    "regionRetailEffectiveDate",
                    region_retail_effective_date,
                    style="form",
                    explode=False,
                ),
                "regionLaunch": oapi.client.format_argument_value(
                    "regionLaunch",
                    region_launch,
                    style="form",
                    explode=False,
                ),
                "regionLaunchDate": oapi.client.format_argument_value(
                    "regionLaunchDate",
                    region_launch_date,
                    style="form",
                    explode=False,
                ),
                "rebuyIndicator": oapi.client.format_argument_value(
                    "rebuyIndicator",
                    rebuy_indicator,
                    style="form",
                    explode=False,
                ),
                "rebuyBeginDate": oapi.client.format_argument_value(
                    "rebuyBeginDate",
                    rebuy_begin_date,
                    style="form",
                    explode=False,
                ),
                "rebuyEndDate": oapi.client.format_argument_value(
                    "rebuyEndDate",
                    rebuy_end_date,
                    style="form",
                    explode=False,
                ),
                "CMPIndicator": oapi.client.format_argument_value(
                    "CMPIndicator",
                    cmp_indicator,
                    style="form",
                    explode=False,
                ),
                "blankIndicator": oapi.client.format_argument_value(
                    "blankIndicator",
                    blank_indicator,
                    style="form",
                    explode=False,
                ),
                "prePackCode": oapi.client.format_argument_value(
                    "prePackCode",
                    pre_pack_code,
                    style="form",
                    explode=False,
                ),
                "deliveryUnitQuantity": oapi.client.format_argument_value(
                    "deliveryUnitQuantity",
                    delivery_unit_quantity,
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

    def get_line_management_data_products_object_id_selected_image_identifier(
        self,
        object_id: int,
        *,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.ImageResponse:
        """
        How you get the informaiton about an image (identifier) after the PLM
        has selected the images and display order

        Parameters:

        - object_id:
          A single Id of the object (in this case Product Id)
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/data/products/{objectId}/selectedImageIdentifier".format(**{  # noqa
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
            method="GET",
            headers={
                "X-B3-TraceId": oapi.client.format_argument_value(
                    "X-B3-TraceId",
                    x_b_3_trace_id,
                    style="form",
                    explode=False,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ImageResponse,
            )
        )

    def get_line_management_search_products_selected_image_identifier(
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
        change_start_time: typing.Optional[
            datetime.datetime
        ] = None,
        change_end_time: typing.Optional[
            datetime.datetime
        ] = None,
        colorway_identifier: typing.Optional[
            model.LineManagementSearchProductsSelectedImageIdentifierGetColorwayIdentifier  # noqa
        ] = None,
        product_representation_id: typing.Optional[
            model.LineManagementSearchProductsSelectedImageIdentifierGetProductRepresentationId  # noqa
        ] = None,
        product_line_manager_image_display_order_number: typing.Optional[
            model.LineManagementSearchProductsSelectedImageIdentifierGetProductLineManagerImageDisplayOrderNumber  # noqa
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Selected Image
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
        - change_start_time:
          This is the Start Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - change_end_time:
          This is the End Date Time (in ISO 8601 format) parameter to search
          for any Global Product Offering object changes within a specified
          time frame
        - colorway_identifier
        - product_representation_id
        - product_line_manager_image_display_order_number
        """
        response: sob.abc.Readable = self.request(
            "/lineManagement/search/products/selectedImageIdentifier",
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
                "changeStartTime": oapi.client.format_argument_value(
                    "changeStartTime",
                    change_start_time,
                    style="form",
                    explode=False,
                ),
                "changeEndTime": oapi.client.format_argument_value(
                    "changeEndTime",
                    change_end_time,
                    style="form",
                    explode=False,
                ),
                "colorwayIdentifier": oapi.client.format_argument_value(
                    "colorwayIdentifier",
                    colorway_identifier,
                    style="form",
                    explode=False,
                ),
                "productRepresentationId": oapi.client.format_argument_value(
                    "productRepresentationId",
                    product_representation_id,
                    style="form",
                    explode=False,
                ),
                "productLineManagerImageDisplayOrderNumber": oapi.client.format_argument_value(  # noqa
                    "productLineManagerImageDisplayOrderNumber",
                    product_line_manager_image_display_order_number,
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
