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
            "https://vendormanagement.api-product.pes-prod.nike.com/v1/materialVendorManagement"  # noqa
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

    def get_data_material_suppliers_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.DataMaterialSuppliersObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SupplierResponse:
        """
        How you get a single supplier.

        Parameters:

        - object_id:
          A single Id of the object (in this case Material Vendor Management
          Supplier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/materialSuppliers/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.SupplierResponse,
            )
        )

    def get_data_material_suppliers(
        self,
        object_id: model.DataMaterialSuppliersGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataMaterialSuppliersGetDataunits
        ] = None,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SupplierBulkResponse:
        """
        How you get Material Vendor Management Supplier in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/materialSuppliers",
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
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SupplierBulkResponse,
            )
        )

    def get_search_material_suppliers(
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
        division_code: typing.Optional[
            model.SearchMaterialSuppliersGetDivisionCode
        ] = None,
        vendor_ownership_type: typing.Optional[
            model.SearchMaterialSuppliersGetVendorOwnershipType
        ] = None,
        has_agent_indicator: typing.Optional[
            bool
        ] = None,
        legacy_supplier_code: typing.Optional[
            model.SearchMaterialSuppliersGetLegacySupplierCode
        ] = None,
        supplier_state_identifier: typing.Optional[
            model.SearchMaterialSuppliersGetSupplierStateIdentifier
        ] = None,
        supplier_state_identifier_reference: typing.Optional[
            model.SearchMaterialSuppliersGetSupplierStateIdentifierReference
        ] = None,
        supplier_status_indicator: typing.Optional[
            bool
        ] = None,
        agent_identifier: typing.Optional[
            model.SearchMaterialSuppliersGetAgentIdentifier
        ] = None,
        legacy_agent_code: typing.Optional[
            model.SearchMaterialSuppliersGetLegacyAgentCode
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Material
        Supplier entity

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
          passed here it will be searched as free text includes (supplierName,
          parentCompanyName, legacySupplierName, agentFullName,
          agentParentCompanyName)
        - division_code:
          The reference key associated with this item
        - vendor_ownership_type:
          The reference key associated with this item
        - has_agent_indicator:
          The the boolean associated with this item
        - legacy_supplier_code:
          The balue associated with this item
        - supplier_state_identifier:
          The reference key associated with this item
        - supplier_state_identifier_reference:
          The reference key associated with this item
        - supplier_status_indicator:
          The boolean value associated with this item
        - agent_identifier:
          The reference key associated with this item
        - legacy_agent_code:
          The value associated with this item
        """
        response: sob.abc.Readable = self.request(
            "/search/materialSuppliers",
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
                "divisionCode": oapi.client.format_argument_value(
                    "divisionCode",
                    division_code,
                    style="form",
                    explode=False,
                ),
                "vendorOwnershipType": oapi.client.format_argument_value(
                    "vendorOwnershipType",
                    vendor_ownership_type,
                    style="form",
                    explode=False,
                ),
                "hasAgentIndicator": oapi.client.format_argument_value(
                    "hasAgentIndicator",
                    has_agent_indicator,
                    style="form",
                    explode=False,
                ),
                "legacySupplierCode": oapi.client.format_argument_value(
                    "legacySupplierCode",
                    legacy_supplier_code,
                    style="form",
                    explode=False,
                ),
                "supplierStateIdentifier": oapi.client.format_argument_value(
                    "supplierStateIdentifier",
                    supplier_state_identifier,
                    style="form",
                    explode=False,
                ),
                "supplierStateIdentifierReference": oapi.client.format_argument_value(  # noqa
                    "supplierStateIdentifierReference",
                    supplier_state_identifier_reference,
                    style="form",
                    explode=False,
                ),
                "supplierStatusIndicator": oapi.client.format_argument_value(
                    "supplierStatusIndicator",
                    supplier_status_indicator,
                    style="form",
                    explode=False,
                ),
                "agentIdentifier": oapi.client.format_argument_value(
                    "agentIdentifier",
                    agent_identifier,
                    style="form",
                    explode=False,
                ),
                "legacyAgentCode": oapi.client.format_argument_value(
                    "legacyAgentCode",
                    legacy_agent_code,
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

    def get_data_material_supplier_locations_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.DataMaterialSupplierLocationsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SupplierLocationResponse:
        """
        How you get a single Material Vendor Management Supplier location.

        Parameters:

        - object_id:
          A single Id of the object (in this case Material Vendor Management
          Supplier Location)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/materialSupplierLocations/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.SupplierLocationResponse,
            )
        )

    def get_data_material_supplier_locations(
        self,
        object_id: model.DataMaterialSupplierLocationsGetObjectId,
        *,
        dataunits: typing.Optional[
            model.DataMaterialSupplierLocationsGetDataunits
        ] = None,
        count: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.SupplierLocationBulkResponse:
        """
        How you get supplier location in a Bulk fashion.

        Parameters:

        - object_id:
          A comma separated list of Ids of the object (in this case Supplier
          Location)
        - dataunits:
          The data units that would be desired, default returns just core data
        - count:
          Number of entries the API should attempt to fetch, default is 10
        - offset:
          Offset of the entries the API should attempt to fetch, default is 0
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/materialSupplierLocations",
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
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.SupplierLocationBulkResponse,
            )
        )

    def get_search_material_supplier_locations(
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
        supplier_identifier: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierIdentifier
        ] = None,
        legacy_supplier_location_code: typing.Optional[
            model.SearchMaterialSupplierLocationsGetLegacySupplierLocationCode
        ] = None,
        responsible_nike_liaison_office_identifier: typing.Optional[
            model.SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifier  # noqa
        ] = None,
        supplier_reason_retired_identifier: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierReasonRetiredIdentifier  # noqa
        ] = None,
        supplier_location_founded_year_number: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationFoundedYearNumber  # noqa
        ] = None,
        accredited_test_facility: typing.Optional[
            bool
        ] = None,
        security_vendor_access_group: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSecurityVendorAccessGroup
        ] = None,
        global_development_center: typing.Optional[
            bool
        ] = None,
        responsible_nike_liaison_office_identifier_reference: typing.Optional[
            model.SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifierReference  # noqa
        ] = None,
        supplier_location_state_identifier: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifier  # noqa
        ] = None,
        supplier_location_state_identifier_reference: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifierReference  # noqa
        ] = None,
        supplier_location_status_indicator: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationStatusIndicator  # noqa
        ] = None,
        supplier_location_status_indicator_boolean: typing.Optional[
            bool
        ] = None,
        supplier_location_address_type: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationAddressType
        ] = None,
        state_province: typing.Optional[
            model.SearchMaterialSupplierLocationsGetStateProvince
        ] = None,
        geographic_area: typing.Optional[
            model.SearchMaterialSupplierLocationsGetGeographicArea
        ] = None,
        country: typing.Optional[
            model.SearchMaterialSupplierLocationsGetCountry
        ] = None,
        supplier_location_contact_role: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationContactRole
        ] = None,
        supplier_location_country: typing.Optional[
            model.SearchMaterialSupplierLocationsGetSupplierLocationCountry
        ] = None,
        port_of_origin_country: typing.Optional[
            model.SearchMaterialSupplierLocationsGetPortOfOriginCountry
        ] = None,
    ) -> model.SearchResponse:
        """
        How you search against all fields contained within the Material
        Supplier Location entity

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
          passed here it will be searched as free text includes (
          supplierLocationName, cityName)
        - supplier_identifier:
          The reference key associated with this item
        - legacy_supplier_location_code:
          The value associated with this item
        - responsible_nike_liaison_office_identifier:
          The value associated with this item
        - supplier_reason_retired_identifier:
          The value associated with this item
        - supplier_location_founded_year_number:
          The value associated with this item
        - accredited_test_facility:
          The boolean value associated with this item
        - security_vendor_access_group:
          The value associated with this item
        - global_development_center:
          The boolean value associated with this item
        - responsible_nike_liaison_office_identifier_reference:
          The reference key associated with this item
        - supplier_location_state_identifier:
          The value associated with this item
        - supplier_location_state_identifier_reference:
          The reference key associated with this item
        - supplier_location_status_indicator:
          The value associated with this item
        - supplier_location_status_indicator_boolean:
          The boolean value associated with this item
        - supplier_location_address_type:
          The value associated with this item
        - state_province:
          The value associated with this item
        - geographic_area:
          The value associated with this item
        - country:
          The reference key associated with this item
        - supplier_location_contact_role:
          The value associated with this item
        - supplier_location_country:
          The reference key associated with this item
        - port_of_origin_country:
          The reference key associated with this item
        """
        response: sob.abc.Readable = self.request(
            "/search/materialSupplierLocations",
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
                "supplierIdentifier": oapi.client.format_argument_value(
                    "supplierIdentifier",
                    supplier_identifier,
                    style="form",
                    explode=False,
                ),
                "legacySupplierLocationCode": oapi.client.format_argument_value(  # noqa
                    "legacySupplierLocationCode",
                    legacy_supplier_location_code,
                    style="form",
                    explode=False,
                ),
                "responsibleNikeLiaisonOfficeIdentifier": oapi.client.format_argument_value(  # noqa
                    "responsibleNikeLiaisonOfficeIdentifier",
                    responsible_nike_liaison_office_identifier,
                    style="form",
                    explode=False,
                ),
                "supplierReasonRetiredIdentifier": oapi.client.format_argument_value(  # noqa
                    "supplierReasonRetiredIdentifier",
                    supplier_reason_retired_identifier,
                    style="form",
                    explode=False,
                ),
                "supplierLocationFoundedYearNumber": oapi.client.format_argument_value(  # noqa
                    "supplierLocationFoundedYearNumber",
                    supplier_location_founded_year_number,
                    style="form",
                    explode=False,
                ),
                "accreditedTestFacility": oapi.client.format_argument_value(
                    "accreditedTestFacility",
                    accredited_test_facility,
                    style="form",
                    explode=False,
                ),
                "securityVendorAccessGroup": oapi.client.format_argument_value(
                    "securityVendorAccessGroup",
                    security_vendor_access_group,
                    style="form",
                    explode=False,
                ),
                "globalDevelopmentCenter": oapi.client.format_argument_value(
                    "globalDevelopmentCenter",
                    global_development_center,
                    style="form",
                    explode=False,
                ),
                "responsibleNikeLiaisonOfficeIdentifierReference": oapi.client.format_argument_value(  # noqa
                    "responsibleNikeLiaisonOfficeIdentifierReference",
                    responsible_nike_liaison_office_identifier_reference,
                    style="form",
                    explode=False,
                ),
                "supplierLocationStateIdentifier": oapi.client.format_argument_value(  # noqa
                    "supplierLocationStateIdentifier",
                    supplier_location_state_identifier,
                    style="form",
                    explode=False,
                ),
                "supplierLocationStateIdentifierReference": oapi.client.format_argument_value(  # noqa
                    "supplierLocationStateIdentifierReference",
                    supplier_location_state_identifier_reference,
                    style="form",
                    explode=False,
                ),
                "supplierLocationStatusIndicator": oapi.client.format_argument_value(  # noqa
                    "supplierLocationStatusIndicator",
                    supplier_location_status_indicator,
                    style="form",
                    explode=False,
                ),
                "supplierLocationStatusIndicatorBoolean": oapi.client.format_argument_value(  # noqa
                    "supplierLocationStatusIndicatorBoolean",
                    supplier_location_status_indicator_boolean,
                    style="form",
                    explode=False,
                ),
                "supplierLocationAddressType": oapi.client.format_argument_value(  # noqa
                    "supplierLocationAddressType",
                    supplier_location_address_type,
                    style="form",
                    explode=False,
                ),
                "stateProvince": oapi.client.format_argument_value(
                    "stateProvince",
                    state_province,
                    style="form",
                    explode=False,
                ),
                "geographicArea": oapi.client.format_argument_value(
                    "geographicArea",
                    geographic_area,
                    style="form",
                    explode=False,
                ),
                "country": oapi.client.format_argument_value(
                    "country",
                    country,
                    style="form",
                    explode=False,
                ),
                "supplierLocationContactRole": oapi.client.format_argument_value(  # noqa
                    "supplierLocationContactRole",
                    supplier_location_contact_role,
                    style="form",
                    explode=False,
                ),
                "supplierLocationCountry": oapi.client.format_argument_value(
                    "supplierLocationCountry",
                    supplier_location_country,
                    style="form",
                    explode=False,
                ),
                "portOfOriginCountry": oapi.client.format_argument_value(
                    "portOfOriginCountry",
                    port_of_origin_country,
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

    def get_data_material_performance_test_labs_object_id(
        self,
        object_id: int,
        *,
        dataunits: typing.Optional[
            model.DataMaterialPerformanceTestLabsObjectIdGetDataunits
        ] = None,
        x_b_3_trace_id: typing.Optional[
            str
        ] = None,
    ) -> model.MaterialPerformanceTestLabResponse:
        """
        How you get a single record of Material Performance Test Lab.

        Parameters:

        - object_id:
          A single Id of the object (in this case Testing Lab Identifier)
        - dataunits:
          The data units that would be desired, default returns just core data
        - x_b_3_trace_id:
          A UUID that will uniquely identify a reqest for tracking purposes, if
          not passed one will be assigned
        """
        response: sob.abc.Readable = self.request(
            "/data/materialPerformanceTestLabs/{objectId}".format(**{
                "objectId": str(oapi.client.format_argument_value(
                    "objectId",
                    object_id,
                    style="form",
                    explode=False,
                )),
            }),
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
                model.MaterialPerformanceTestLabResponse,
            )
        )
