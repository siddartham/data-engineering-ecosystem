import functools
from urllib.error import HTTPError
import sob
from oapi.client import (
    DEFAULT_RETRY_FOR_ERRORS,
    CLIENT_SLOTS,
    Client as _Client,
)
from logging import Logger, getLogger
from typing import (
    Any,
    Callable,
    Optional,
    Tuple,
    Type,
    Iterable,
)
from urllib.parse import quote
from xml.dom import minidom
from nike.cerberus_assistant.decorate import apply_cerberus_path_arguments
from . import model

lru_cache: Callable[..., Any] = functools.lru_cache
log: Logger = getLogger(__name__)

_service_root_response_lru_cache: Callable[
    [], Callable[..., Callable[..., model.ServiceRootResponse]]
] = functools.lru_cache  # type: ignore
_readable_lru_cache: Callable[
    [], Callable[..., Callable[..., sob.abc.Readable]]
] = functools.lru_cache  # type: ignore


def default_retry_hook(error: Exception) -> bool:
    if isinstance(error, HTTPError) and error.code == 404:
        # This error won't be overcome with additional attempts
        return False
    return True


class Client(_Client):
    """
    Instances of this class act as client for retrieving
    records from the Enablon "Blink" OData API.

    Initialization Parameters:

    - url (str): The base URL for API requests.
    - user (str) = "": A user name for use with HTTP basic authentication.
    - password (str) = "":  A password for use with HTTP basic authentication.
    - timeout (int): The number of seconds before a request will timeout
      and throw an error. If this is 0 (the default), the system default
      timeout will be used.
    - retry_number_of_attempts (int) = 1: The number of times to retry
      a request which results in an error.
    - retry_for_errors: A tuple of one or more exception types
      on which to retry a request. To retry for *all* errors,
      pass `(Exception,)` for this argument.
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
        url: str = "https://www51.enablon.com/Nike/odata/v4",
        user: str = "",
        password: str = "",
        timeout: int = 0,
        retry_number_of_attempts: int = 3,
        retry_for_errors: Tuple[
            Type[Exception], ...
        ] = DEFAULT_RETRY_FOR_ERRORS,
        retry_hook: Callable[  # Force line-break retention
            [Exception], bool
        ] = default_retry_hook,
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
            retry_number_of_attempts=retry_number_of_attempts,
            retry_for_errors=retry_for_errors,
            retry_hook=retry_hook,
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
            # Not Initialization Parameters
            self._cookie_jar,
            self._oauth2_authorization_expires,
        )

    @property  # type: ignore
    @_readable_lru_cache()
    def metadata(self) -> sob.abc.Readable:
        """
        Return an XML document with information about the OData structures
        and endpoints in this API.
        """
        service_root_response: model.ServiceRootResponse = self.get()
        assert service_root_response.odata_context
        response: sob.abc.Readable = self.request(
            service_root_response.odata_context, method="GET"
        )
        # Cause the HTTPResponse to return *pretty-printed* XML
        response_body: str = minidom.parse(
            response  # type: ignore
        ).toprettyxml(indent="  ")

        def read(amt: Optional[int] = None) -> str:
            return response_body[:amt]

        response.read = read  # type: ignore
        return response

    @_service_root_response_lru_cache()
    def get(self) -> model.ServiceRootResponse:
        """
        Request the service root, which contains table/asset information.
        """
        return model.ServiceRootResponse(self.request("/", method="GET"))

    def csr_impact_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRImpactTypesResponse]:
        response_instance: model.CSRImpactTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ImpactTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRImpactTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_target_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesTargetTypesResponse]:
        response_instance: model.CSRObjectivesTargetTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesTargetTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesTargetTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_strategy_hierarchy_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRStrategyHierarchyLevelsResponse]:
        response_instance: model.CSRStrategyHierarchyLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_StrategyHierarchyLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRStrategyHierarchyLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_sources(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesSourcesResponse]:
        response_instance: model.CSRObjectivesSourcesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesSources?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesSourcesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_achievement_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesAchievementStatusResponse]:
        response_instance: model.CSRObjectivesAchievementStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesAchievementStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesAchievementStatusResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_priority(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesPriorityResponse]:
        response_instance: model.CSRObjectivesPriorityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesPriority?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesPriorityResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesAuditTrailResponse]:
        response_instance: model.CSRObjectivesAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_strategy_hierarchy_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRStrategyHierarchyAuditTrailResponse]:
        response_instance: model.CSRStrategyHierarchyAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_StrategyHierarchyAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRStrategyHierarchyAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesResponse]:
        response_instance: model.CSRObjectivesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_Objectives?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_strategy_hierarchy(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRStrategyHierarchyResponse]:
        response_instance: model.CSRStrategyHierarchyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_StrategyHierarchy?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRStrategyHierarchyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_visibility(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKVisibilityResponse]:
        response_instance: model.TCKVisibilityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_Visibility?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKVisibilityResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_items_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemsAuditTrailResponse]:
        response_instance: model.TCKActionItemsAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemsAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemsAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_resolution(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemResolutionResponse]:
        response_instance: model.TCKActionItemResolutionResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemResolution?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemResolutionResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_priority(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemPriorityResponse]:
        response_instance: model.TCKActionItemPriorityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemPriority?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemPriorityResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemStatusResponse]:
        response_instance: model.TCKActionItemStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemStatusResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_impacted_layers(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemImpactedLayersResponse]:
        response_instance: model.TCKActionItemImpactedLayersResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemImpactedLayers?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemImpactedLayersResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemTypeResponse]:
        response_instance: model.TCKActionItemTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_cs_status_for_nike_team(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKCsStatusForNikeTeamResponse]:
        response_instance: model.TCKCsStatusForNikeTeamResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_CS_StatusForNikeTeam?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKCsStatusForNikeTeamResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_cs_type_of_change(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKCsTypeOfChangeResponse]:
        response_instance: model.TCKCsTypeOfChangeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_CS_TypeOfChange?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKCsTypeOfChangeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_cs_action_item_project(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKCsActionItemProjectResponse]:
        response_instance: model.TCKCsActionItemProjectResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_CS_ActionItemProject?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKCsActionItemProjectResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_cs_teams_responsible(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKCsTeamsResponsibleResponse]:
        response_instance: model.TCKCsTeamsResponsibleResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_CS_TeamsResponsible?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKCsTeamsResponsibleResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_modules_pages(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKModulesPagesResponse]:
        response_instance: model.TCKModulesPagesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ModulesPages?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKModulesPagesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_screen_captures(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKScreenCapturesResponse]:
        response_instance: model.TCKScreenCapturesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ScreenCaptures?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKScreenCapturesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemResponse]:
        response_instance: model.TCKActionItemResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItem?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKActionItemResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_resources(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKResourcesResponse]:
        response_instance: model.TCKResourcesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_Resources?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKResourcesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_record_gender(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoRecordGenderResponse]:
        response_instance: model.HoRecordGenderResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_RecordGender?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoRecordGenderResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_sub_applications(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSubApplicationsResponse]:
        response_instance: model.HoSubApplicationsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SubApplications?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoSubApplicationsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_applications(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoApplicationsResponse]:
        response_instance: model.HoApplicationsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Applications?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoApplicationsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_deletions_table(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDeletionsTableResponse]:
        response_instance: model.HoDeletionsTableResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_DeletionsTable?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoDeletionsTableResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_unit_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoUnitLevelsResponse]:
        response_instance: model.HoUnitLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_UnitLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoUnitLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_entity_unit_management(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoEntityUnitManagementResponse]:
        response_instance: model.HoEntityUnitManagementResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_EntityUnitManagement?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoEntityUnitManagementResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_unit_conversions(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoUnitConversionsResponse]:
        response_instance: model.HoUnitConversionsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_UnitConversions?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoUnitConversionsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_units(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoUnitsResponse]:
        response_instance: model.HoUnitsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Units?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoUnitsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_calendar_configuration(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoCalendarConfigurationResponse]:
        response_instance: model.HoCalendarConfigurationResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_CalendarConfiguration?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoCalendarConfigurationResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_languages(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsLanguagesResponse]:
        response_instance: model.HoNewsLanguagesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsLanguages?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoNewsLanguagesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_audit_trail_user(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoAuditTrailUserResponse]:
        response_instance: model.HoAuditTrailUserResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_AuditTrailUser?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoAuditTrailUserResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_directory_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDirectoryAuditTrailResponse]:
        response_instance: model.HoDirectoryAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_DirectoryAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoDirectoryAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_directory(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDirectoryResponse]:
        response_instance: model.HoDirectoryResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Directory?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoDirectoryResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_geography_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoGeographyLevelsResponse]:
        response_instance: model.HoGeographyLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_GeographyLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoGeographyLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_third_axis_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoThirdAxisLevelsResponse]:
        response_instance: model.HoThirdAxisLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_ThirdAxisLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoThirdAxisLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_second_axis_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSecondAxisLevelsResponse]:
        response_instance: model.HoSecondAxisLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SecondAxisLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoSecondAxisLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_first_axis_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoFirstAxisLevelsResponse]:
        response_instance: model.HoFirstAxisLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_FirstAxisLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoFirstAxisLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_key_words_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoKeyWordsEntitiesResponse]:
        response_instance: model.HoKeyWordsEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_KeyWordsEntities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoKeyWordsEntitiesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_business(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoBusinessResponse]:
        response_instance: model.HoBusinessResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Business?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoBusinessResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_third_axis_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoThirdAxisAuditTrailResponse]:
        response_instance: model.HoThirdAxisAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_ThirdAxisAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoThirdAxisAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_second_axis_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSecondAxisAuditTrailResponse]:
        response_instance: model.HoSecondAxisAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SecondAxisAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoSecondAxisAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_entities_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoEntitiesAuditTrailResponse]:
        response_instance: model.HoEntitiesAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_EntitiesAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoEntitiesAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_third_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHThirdAxisResponse]:
        response_instance: model.HoHThirdAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HThirdAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoHThirdAxisResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_second_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHSecondAxisResponse]:
        response_instance: model.HoHSecondAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HSecondAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoHSecondAxisResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_first_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHFirstAxisResponse]:
        response_instance: model.HoHFirstAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HFirstAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoHFirstAxisResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_snapshots_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSnapshotsAxisResponse]:
        response_instance: model.HoSnapshotsAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SnapshotsAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoSnapshotsAxisResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_geography(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoGeographyResponse]:
        response_instance: model.HoGeographyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Geography?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoGeographyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_second_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSecondAxisResponse]:
        response_instance: model.HoSecondAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SecondAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoSecondAxisResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoEntitiesResponse]:
        response_instance: model.HoEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Entities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoEntitiesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_new_glossary(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewGlossaryResponse]:
        response_instance: model.HoNewGlossaryResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewGlossary?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoNewGlossaryResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_documents(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDocumentsResponse]:
        response_instance: model.HoDocumentsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Documents?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoDocumentsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesResponse]:
        response_instance: model.HoNewsArticlesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoNewsArticlesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_consistency_check_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConsistencyCheckTypesResponse]:
        response_instance: model.SDConsistencyCheckTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConsistencyCheckTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDConsistencyCheckTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_consistency_check_justification_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConsistencyCheckJustificationTypesResponse]:
        response_instance: model.SDConsistencyCheckJustificationTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConsistencyCheckJustificationTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDConsistencyCheckJustificationTypesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_updater_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDUpdaterTypeResponse]:
        response_instance: model.SDUpdaterTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_UpdaterType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDUpdaterTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_consolidation_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConsolidationTypeResponse]:
        response_instance: model.SDConsolidationTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConsolidationType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDConsolidationTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_questionnaire_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDQuestionnaireTypeResponse]:
        response_instance: model.SDQuestionnaireTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_QuestionnaireType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDQuestionnaireTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_input_subtypes(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDInputSubtypesResponse]:
        response_instance: model.SDInputSubtypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_InputSubtypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDInputSubtypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_input_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDInputTypesResponse]:
        response_instance: model.SDInputTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_InputTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDInputTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_emission_factor_source(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEmissionFactorSourceResponse]:
        response_instance: model.SDEmissionFactorSourceResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EmissionFactorSource?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEmissionFactorSourceResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_fuel_type_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDFuelTypeLevelsResponse]:
        response_instance: model.SDFuelTypeLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_FuelTypeLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDFuelTypeLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_source_type_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDSourceTypeLevelsResponse]:
        response_instance: model.SDSourceTypeLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_SourceTypeLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDSourceTypeLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_ef_distribution_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEfDistributionLevelsResponse]:
        response_instance: model.SDEfDistributionLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EFDistributionLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEfDistributionLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_material_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDMaterialTypesResponse]:
        response_instance: model.SDMaterialTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_MaterialTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDMaterialTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_conversion_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConversionTypesResponse]:
        response_instance: model.SDConversionTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConversionTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDConversionTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_fuel_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDFuelTypeResponse]:
        response_instance: model.SDFuelTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_FuelType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDFuelTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_source_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDSourceTypeResponse]:
        response_instance: model.SDSourceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_SourceType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDSourceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_source_scope(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDSourceScopeResponse]:
        response_instance: model.SDSourceScopeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_SourceScope?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDSourceScopeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_green_house_gas(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDGreenHouseGasResponse]:
        response_instance: model.SDGreenHouseGasResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_GreenHouseGas?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDGreenHouseGasResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_material_types_at(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDMaterialTypesATResponse]:
        response_instance: model.SDMaterialTypesATResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_MaterialTypesAT?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDMaterialTypesATResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_conversion_types_at(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConversionTypesATResponse]:
        response_instance: model.SDConversionTypesATResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConversionTypesAT?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDConversionTypesATResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cross_units_conversions_at(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCrossUnitsConversionsATResponse]:
        response_instance: model.SDCrossUnitsConversionsATResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CrossUnitsConversionsAT?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCrossUnitsConversionsATResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_emission_factor_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEmissionFactorAuditTrailResponse]:
        response_instance: model.SDEmissionFactorAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EmissionFactorAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEmissionFactorAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_ghg_protocols_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDGhgProtocolsAuditTrailResponse]:
        response_instance: model.SDGhgProtocolsAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_GHGProtocolsAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDGhgProtocolsAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cross_units_conversions(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCrossUnitsConversionsResponse]:
        response_instance: model.SDCrossUnitsConversionsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CrossUnitsConversions?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCrossUnitsConversionsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_related_geography(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRelatedGeographyResponse]:
        response_instance: model.SDRelatedGeographyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_RelatedGeography?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDRelatedGeographyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_emission_factor(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEmissionFactorResponse]:
        response_instance: model.SDEmissionFactorResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EmissionFactor?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEmissionFactorResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_t_component(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsTComponentResponse]:
        response_instance: model.SDCsTComponentResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_TComponent?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsTComponentResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_prod_gender(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProdGenderResponse]:
        response_instance: model.SDCsProdGenderResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ProdGender?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProdGenderResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_prod_size_group(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProdSizeGroupResponse]:
        response_instance: model.SDCsProdSizeGroupResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ProdSizeGroup?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProdSizeGroupResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_mold_country(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMoldCountryResponse]:
        response_instance: model.SDCsMoldCountryResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MoldCountry?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMoldCountryResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_mold_manuf(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMoldManufResponse]:
        response_instance: model.SDCsMoldManufResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MoldManuf?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMoldManufResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_mold_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMoldStatusResponse]:
        response_instance: model.SDCsMoldStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MoldStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMoldStatusResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_mold_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMoldTypeResponse]:
        response_instance: model.SDCsMoldTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MoldType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMoldTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_mcs_code(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMCSCodeResponse]:
        response_instance: model.SDCsMCSCodeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MCSCode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMCSCodeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_tooling_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsToolingAuditTrailResponse]:
        response_instance: model.SDCsToolingAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ToolingAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsToolingAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_tooling(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsToolingResponse]:
        response_instance: model.SDCsToolingResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Tooling?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsToolingResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_crossbrand_rollup_frequency(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsCrossbrandRollupFrequencyResponse]:
        response_instance: model.SDCsCrossbrandRollupFrequencyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_CrossbrandRollupFrequency?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsCrossbrandRollupFrequencyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_rolled_up_data(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsRolledUpDataResponse]:
        response_instance: model.SDCsRolledUpDataResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_RolledUpData?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsRolledUpDataResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_crossbrand_indicator_mapping(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsCrossbrandIndicatorMappingResponse]:
        response_instance: model.SDCsCrossbrandIndicatorMappingResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_CrossbrandIndicatorMapping?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsCrossbrandIndicatorMappingResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_data_rollup_configuration_table(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsDataRollupConfigurationTableResponse]:
        response_instance: model.SDCsDataRollupConfigurationTableResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_DataRollupConfigurationTable?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsDataRollupConfigurationTableResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_reporting_axis_mapping_table(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsReportingAxisMappingTableResponse]:
        response_instance: model.SDCsReportingAxisMappingTableResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ReportingAxisMappingTable?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsReportingAxisMappingTableResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_columns_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableColumnsLevelsResponse]:
        response_instance: model.SDTableColumnsLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableColumnsLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableColumnsLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_lines_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableLinesLevelsResponse]:
        response_instance: model.SDTableLinesLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableLinesLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableLinesLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorLevelsResponse]:
        response_instance: model.SDIndicatorLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_custom_lists(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCustomListsResponse]:
        response_instance: model.SDCustomListsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CustomLists?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCustomListsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_custom_list_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCustomListTypesResponse]:
        response_instance: model.SDCustomListTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CustomListTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCustomListTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsAuditTrailResponse]:
        response_instance: model.SDIndicatorsAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorsAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorsAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDVersionedConsistencyChecksResponse]:
        response_instance: model.SDVersionedConsistencyChecksResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsResponse]:
        response_instance: model.SDHistorizedIndicatorsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_snapshots(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDSnapshotsResponse]:
        response_instance: model.SDSnapshotsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Snapshots?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDSnapshotsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_referentials(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDReferentialsResponse]:
        response_instance: model.SDReferentialsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Referentials?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDReferentialsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_column(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableColumnResponse]:
        response_instance: model.SDTableColumnResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableColumn?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableColumnResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_line(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableLineResponse]:
        response_instance: model.SDTableLineResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableLine?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableLineResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorConsistencyChecksResponse]:
        response_instance: model.SDIndicatorConsistencyChecksResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsResponse]:
        response_instance: model.SDIndicatorsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_frequency(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDFrequencyResponse]:
        response_instance: model.SDFrequencyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Frequency?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDFrequencyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_chemistry_upload(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsChemistryUploadResponse]:
        response_instance: model.SDCsChemistryUploadResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ChemistryUpload?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsChemistryUploadResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_unit_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsUnitTypesResponse]:
        response_instance: model.SDCsUnitTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_UnitTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsUnitTypesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_defect_bottom(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsDefectBottomResponse]:
        response_instance: model.SDCsDefectBottomResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_DefectBottom?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsDefectBottomResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_defect_settings(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsDefectSettingsResponse]:
        response_instance: model.SDCsDefectSettingsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_DefectSettings?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsDefectSettingsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_component_color(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsComponentColorResponse]:
        response_instance: model.SDCsComponentColorResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ComponentColor?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsComponentColorResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_defect_process(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsDefectProcessResponse]:
        response_instance: model.SDCsDefectProcessResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_DefectProcess?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsDefectProcessResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_component_size(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsComponentSizeResponse]:
        response_instance: model.SDCsComponentSizeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ComponentSize?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsComponentSizeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_material(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMaterialResponse]:
        response_instance: model.SDCsMaterialResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_material?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMaterialResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_shift(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsShiftResponse]:
        response_instance: model.SDCsShiftResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Shift?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsShiftResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_actual_extrapolated(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsActualExtrapolatedResponse]:
        response_instance: model.SDCsActualExtrapolatedResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ActualExtrapolated?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsActualExtrapolatedResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_function(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsFunctionResponse]:
        response_instance: model.SDCsFunctionResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Function?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsFunctionResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_emissions_source(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsEmissionsSourceResponse]:
        response_instance: model.SDCsEmissionsSourceResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_EmissionsSource?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsEmissionsSourceResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_energy_emissions(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsEnergyEmissionsResponse]:
        response_instance: model.SDCsEnergyEmissionsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_EnergyEmissions?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsEnergyEmissionsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_ghg(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsGHGResponse]:
        response_instance: model.SDCsGHGResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_GHG?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsGHGResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_scope(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsScopeResponse]:
        response_instance: model.SDCsScopeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Scope?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsScopeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_product_cas(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProductCASResponse]:
        response_instance: model.SDCsProductCASResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ProductCAS?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProductCASResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_cas_numbers(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsCASNumbersResponse]:
        response_instance: model.SDCsCASNumbersResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_CASNumbers?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsCASNumbersResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_product_group(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProductGroupResponse]:
        response_instance: model.SDCsProductGroupResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ProductGroup?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProductGroupResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_product(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProductResponse]:
        response_instance: model.SDCsProductResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Product?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProductResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_vendor(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsVendorResponse]:
        response_instance: model.SDCsVendorResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Vendor?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsVendorResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_source(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsSourceResponse]:
        response_instance: model.SDCsSourceResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Source?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsSourceResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_waste_vendor(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsWasteVendorResponse]:
        response_instance: model.SDCsWasteVendorResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_WasteVendor?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsWasteVendorResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_management_method(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsManagementMethodResponse]:
        response_instance: model.SDCsManagementMethodResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ManagementMethod?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsManagementMethodResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_component(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsComponentResponse]:
        response_instance: model.SDCsComponentResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_Component?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsComponentResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_waste_item(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsWasteItemResponse]:
        response_instance: model.SDCsWasteItemResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_WasteItem?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsWasteItemResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_material_group(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsMaterialGroupResponse]:
        response_instance: model.SDCsMaterialGroupResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_MaterialGroup?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsMaterialGroupResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_waste_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsWasteTypeResponse]:
        response_instance: model.SDCsWasteTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_WasteType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsWasteTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_product_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsProductTypeResponse]:
        response_instance: model.SDCsProductTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ProductType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsProductTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_input_wf_levels(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsInputWFLevelsResponse]:
        response_instance: model.SDCsInputWFLevelsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_InputWFLevels?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCsInputWFLevelsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_standard_alerts(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDStandardAlertsResponse]:
        response_instance: model.SDStandardAlertsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_StandardAlerts?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDStandardAlertsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_alerts_templates(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDAlertsTemplatesResponse]:
        response_instance: model.SDAlertsTemplatesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_AlertsTemplates?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDAlertsTemplatesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_recalculations(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRecalculationsResponse]:
        response_instance: model.SDRecalculationsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Recalculations?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDRecalculationsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_recalculations_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRecalculationsAuditTrailResponse]:
        response_instance: model.SDRecalculationsAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_RecalculationsAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDRecalculationsAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_campaigns_audit_trail(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCampaignsAuditTrailResponse]:
        response_instance: model.SDCampaignsAuditTrailResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CampaignsAuditTrail?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCampaignsAuditTrailResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_tracking_alerts(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTrackingAlertsResponse]:
        response_instance: model.SDTrackingAlertsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TrackingAlerts?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTrackingAlertsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_alerts(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDAlertsResponse]:
        response_instance: model.SDAlertsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Alerts?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDAlertsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_updater(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDUpdaterResponse]:
        response_instance: model.SDUpdaterResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Updater?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDUpdaterResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_campaigns(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCampaignsResponse]:
        response_instance: model.SDCampaignsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Campaigns?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCampaignsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesResponse]:
        response_instance: model.SDEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_cs_defect_entries(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesCSDefectEntriesResponse]:
        response_instance: model.SDEntitiesCSDefectEntriesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_CS_DefectEntries?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesCSDefectEntriesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_cs_chemistry(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesCSChemistryResponse]:
        response_instance: model.SDEntitiesCSChemistryResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_CS_Chemistry?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesCSChemistryResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_cs_waste_entries(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesCSWasteEntriesResponse]:
        response_instance: model.SDEntitiesCSWasteEntriesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_CS_WasteEntries?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesCSWasteEntriesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_consistency_checks(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesConsistencyChecksResponse]:
        response_instance: model.SDEntitiesConsistencyChecksResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_ConsistencyChecks?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesConsistencyChecksResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_input_at(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesInputATResponse]:
        response_instance: model.SDEntitiesInputATResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_InputAT?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesInputATResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_tracking(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesTrackingResponse]:
        response_instance: model.SDEntitiesTrackingResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_Tracking?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesTrackingResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_data_consistency_checks(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesDataConsistencyChecksResponse]:
        response_instance: model.SDEntitiesDataConsistencyChecksResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_DataConsistencyChecks?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesDataConsistencyChecksResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_data(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesDataResponse]:
        response_instance: model.SDEntitiesDataResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_Data?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesDataResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_input(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesInputResponse]:
        response_instance: model.SDEntitiesInputResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_Input?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesInputResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_csr_objectives_first_axis(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksCSRObjectivesFirstAxisResponse]:
        response_instance: model.SysMultiLinksCSRObjectivesFirstAxisResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_CSR_Objectives_FirstAxis?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksCSRObjectivesFirstAxisResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_tck_action_item_captures(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksTCKActionItemCapturesResponse]:
        response_instance: model.SysMultiLinksTCKActionItemCapturesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_TCK_ActionItem_Captures?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksTCKActionItemCapturesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_tck_action_item_followers(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksTCKActionItemFollowersResponse]:
        response_instance: model.SysMultiLinksTCKActionItemFollowersResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_TCK_ActionItem_Followers?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksTCKActionItemFollowersResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_tck_action_item_linked_items(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksTCKActionItemLinkedItemsResponse]:
        response_instance: model.SysMultiLinksTCKActionItemLinkedItemsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_TCK_ActionItem_LinkedItems?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksTCKActionItemLinkedItemsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_units_first_part_filter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoUnitsFirstPartFilterResponse]:
        response_instance: model.SysMultiLinksHoUnitsFirstPartFilterResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Units_FirstPartFilter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoUnitsFirstPartFilterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_units_second_part_filter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoUnitsSecondPartFilterResponse]:
        response_instance: model.SysMultiLinksHoUnitsSecondPartFilterResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Units_SecondPartFilter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoUnitsSecondPartFilterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_directory_working_perimeter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoDirectoryWorkingPerimeterResponse]:
        response_instance: (
            model.SysMultiLinksHoDirectoryWorkingPerimeterResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Directory_WorkingPerimeter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoDirectoryWorkingPerimeterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_directory_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoDirectoryEntitiesResponse]:
        response_instance: model.SysMultiLinksHoDirectoryEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Directory_Entities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksHoDirectoryEntitiesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_h_first_axis_second_axes(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoHFirstAxisSecondAxesResponse]:
        response_instance: model.SysMultiLinksHoHFirstAxisSecondAxesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_HFirstAxis_SecondAxes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoHFirstAxisSecondAxesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_h_first_axis_keywords(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoHFirstAxisKeywordsResponse]:
        response_instance: model.SysMultiLinksHoHFirstAxisKeywordsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_HFirstAxis_Keywords?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoHFirstAxisKeywordsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_entities_keywords(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoEntitiesKeywordsResponse]:
        response_instance: model.SysMultiLinksHoEntitiesKeywordsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Entities_Keywords?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksHoEntitiesKeywordsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_entities_second_axes(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoEntitiesSecondAxesResponse]:
        response_instance: model.SysMultiLinksHoEntitiesSecondAxesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_Entities_SecondAxes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoEntitiesSecondAxesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_news_articles_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoNewsArticlesEntitiesResponse]:
        response_instance: model.SysMultiLinksHoNewsArticlesEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_NewsArticles_Entities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoNewsArticlesEntitiesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_ho_news_articles_applications(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksHoNewsArticlesApplicationsResponse]:
        response_instance: (
            model.SysMultiLinksHoNewsArticlesApplicationsResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_ho_NewsArticles_Applications?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksHoNewsArticlesApplicationsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_data_rollup_configuration_table_cs_source_entities(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCsDataRollupConfigurationTableCSSourceEntitiesResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDCsDataRollupConfigurationTableCSSourceEntitiesResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_DataRollupConfigurationTable_CS_SourceEntities?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCsDataRollupConfigurationTableCSSourceEntitiesResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_data_rollup_configuration_table_source_indicators(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCsDataRollupConfigurationTableSourceIndicatorsResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDCsDataRollupConfigurationTableSourceIndicatorsResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_DataRollupConfigurationTable_SourceIndicators?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCsDataRollupConfigurationTableSourceIndicatorsResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_data_rollup_configuration_table_frequencies(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCsDataRollupConfigurationTableFrequenciesResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDCsDataRollupConfigurationTableFrequenciesResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_DataRollupConfigurationTable_Frequencies?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCsDataRollupConfigurationTableFrequenciesResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_reporting_axis_mapping_table_cs_source_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCsReportingAxisMappingTableCSSourceEntitiesResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDCsReportingAxisMappingTableCSSourceEntitiesResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_ReportingAxisMappingTable_CS_SourceEntities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCsReportingAxisMappingTableCSSourceEntitiesResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_versioned_consistency_checks_expected_value_list(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDVersionedConsistencyChecksExpectedValueListResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDVersionedConsistencyChecksExpectedValueListResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_VersionedConsistencyChecks_ExpectedValueList?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDVersionedConsistencyChecksExpectedValueListResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_versioned_consistency_checks_justification_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDVersionedConsistencyChecksJustificationTypeResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDVersionedConsistencyChecksJustificationTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_VersionedConsistencyChecks_JustificationType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDVersionedConsistencyChecksJustificationTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_historized_indicators_dependency_answers(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDHistorizedIndicatorsDependencyAnswersResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDHistorizedIndicatorsDependencyAnswersResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_HistorizedIndicators_DependencyAnswers?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDHistorizedIndicatorsDependencyAnswersResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_historized_indicators_line_composition(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDHistorizedIndicatorsLineCompositionResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDHistorizedIndicatorsLineCompositionResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_HistorizedIndicators_LineComposition?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDHistorizedIndicatorsLineCompositionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_historized_indicators_column_composition(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDHistorizedIndicatorsColumnCompositionResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDHistorizedIndicatorsColumnCompositionResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_HistorizedIndicators_ColumnComposition?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDHistorizedIndicatorsColumnCompositionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_historized_indicators_referentials(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDHistorizedIndicatorsReferentialsResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDHistorizedIndicatorsReferentialsResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_HistorizedIndicators_Referentials?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDHistorizedIndicatorsReferentialsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_snapshots_indicator_perimeter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDSnapshotsIndicatorPerimeterResponse]:
        response_instance: (
            model.SysMultiLinksSDSnapshotsIndicatorPerimeterResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Snapshots_IndicatorPerimeter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDSnapshotsIndicatorPerimeterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicator_consistency_checks_expected_value_list(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDIndicatorConsistencyChecksExpectedValueListResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDIndicatorConsistencyChecksExpectedValueListResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_IndicatorConsistencyChecks_ExpectedValueList?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDIndicatorConsistencyChecksExpectedValueListResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicator_consistency_checks_justification_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDIndicatorConsistencyChecksJustificationTypeResponse  # noqa
    ]:
        response_instance: (
            model.SysMultiLinksSDIndicatorConsistencyChecksJustificationTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_IndicatorConsistencyChecks_JustificationType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDIndicatorConsistencyChecksJustificationTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_dependency_answers(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsDependencyAnswersResponse]:
        response_instance: (
            model.SysMultiLinksSDIndicatorsDependencyAnswersResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_DependencyAnswers?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsDependencyAnswersResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_table_lines(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsTableLinesResponse]:
        response_instance: model.SysMultiLinksSDIndicatorsTableLinesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_TableLines?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsTableLinesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_all_line_composition(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsAllLineCompositionResponse]:
        response_instance: (
            model.SysMultiLinksSDIndicatorsAllLineCompositionResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_AllLineComposition?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsAllLineCompositionResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_table_columns(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsTableColumnsResponse]:
        response_instance: model.SysMultiLinksSDIndicatorsTableColumnsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_TableColumns?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsTableColumnsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_all_column_composition(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsAllColumnCompositionResponse]:
        response_instance: (
            model.SysMultiLinksSDIndicatorsAllColumnCompositionResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_AllColumnComposition?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsAllColumnCompositionResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_indicators_referentials(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDIndicatorsReferentialsResponse]:
        response_instance: model.SysMultiLinksSDIndicatorsReferentialsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Indicators_Referentials?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDIndicatorsReferentialsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_product_cs_brand(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCsProductCSBrandResponse]:
        response_instance: model.SysMultiLinksSDCsProductCSBrandResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_Product_CS_Brand?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCsProductCSBrandResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_waste_vendor_cs_product_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCsWasteVendorCSProductTypeResponse]:
        response_instance: (
            model.SysMultiLinksSDCsWasteVendorCSProductTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_WasteVendor_CS_ProductType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCsWasteVendorCSProductTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_management_method_cs_product_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCsManagementMethodCSProductTypeResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDCsManagementMethodCSProductTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_ManagementMethod_CS_ProductType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCsManagementMethodCSProductTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_component_cs_waste_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCsComponentCSWasteTypesResponse]:
        response_instance: model.SysMultiLinksSDCsComponentCSWasteTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_Component_CS_WasteTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCsComponentCSWasteTypesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_waste_item_cs_waste_types(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCsWasteItemCSWasteTypesResponse]:
        response_instance: model.SysMultiLinksSDCsWasteItemCSWasteTypesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_WasteItem_CS_WasteTypes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCsWasteItemCSWasteTypesResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_cs_waste_type_cs_product_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCsWasteTypeCSProductTypeResponse]:
        response_instance: (
            model.SysMultiLinksSDCsWasteTypeCSProductTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_CS_WasteType_CS_ProductType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCsWasteTypeCSProductTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_recalculations_campaigns(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDRecalculationsCampaignsResponse]:
        response_instance: model.SysMultiLinksSDRecalculationsCampaignsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Recalculations_Campaigns?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDRecalculationsCampaignsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_campaigns(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterCampaignsResponse]:
        response_instance: model.SysMultiLinksSDUpdaterCampaignsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_Campaigns?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDUpdaterCampaignsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_historized_indicators(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterHistorizedIndicatorsResponse]:
        response_instance: (
            model.SysMultiLinksSDUpdaterHistorizedIndicatorsResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_HistorizedIndicators?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDUpdaterHistorizedIndicatorsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_indicators(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterIndicatorsResponse]:
        response_instance: model.SysMultiLinksSDUpdaterIndicatorsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_Indicators?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDUpdaterIndicatorsResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_table_lines(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterTableLinesResponse]:
        response_instance: model.SysMultiLinksSDUpdaterTableLinesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_TableLines?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDUpdaterTableLinesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_table_columns(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterTableColumnsResponse]:
        response_instance: model.SysMultiLinksSDUpdaterTableColumnsResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_TableColumns?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDUpdaterTableColumnsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_updater_entities(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDUpdaterEntitiesResponse]:
        response_instance: model.SysMultiLinksSDUpdaterEntitiesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Updater_Entities?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDUpdaterEntitiesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_campaigns_archive_indicator_perimeter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SysMultiLinksSDCampaignsArchiveIndicatorPerimeterResponse
    ]:
        response_instance: (
            model.SysMultiLinksSDCampaignsArchiveIndicatorPerimeterResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Campaigns_ArchiveIndicatorPerimeter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SysMultiLinksSDCampaignsArchiveIndicatorPerimeterResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_campaigns_indicator_perimeter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCampaignsIndicatorPerimeterResponse]:
        response_instance: (
            model.SysMultiLinksSDCampaignsIndicatorPerimeterResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Campaigns_IndicatorPerimeter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCampaignsIndicatorPerimeterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_campaigns_reporting_perimeter(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDCampaignsReportingPerimeterResponse]:
        response_instance: (
            model.SysMultiLinksSDCampaignsReportingPerimeterResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Campaigns_ReportingPerimeter?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDCampaignsReportingPerimeterResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_entities_data_referentials(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDEntitiesDataReferentialsResponse]:
        response_instance: (
            model.SysMultiLinksSDEntitiesDataReferentialsResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Entities_Data_Referentials?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDEntitiesDataReferentialsResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sys_multi_links_sd_entities_data_value_list_multiple(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SysMultiLinksSDEntitiesDataValueListMultipleResponse]:
        response_instance: (
            model.SysMultiLinksSDEntitiesDataValueListMultipleResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SysMultiLinks_SD_Entities_Data_ValueListMultiple?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SysMultiLinksSDEntitiesDataValueListMultipleResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def shared_no_yes(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SharedNoYesResponse]:
        response_instance: model.SharedNoYesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/Shared_No_Yes?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SharedNoYesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def shared_timezones(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SharedTimezonesResponse]:
        response_instance: model.SharedTimezonesResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/Shared_Timezones?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SharedTimezonesResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.CSRObjectivesAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_ObjectivesAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.CSRObjectivesAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_strategy_hierarchy_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.CSRStrategyHierarchyAuditTrailCustomChoiceModeResponse
    ]:
        response_instance: (
            model.CSRStrategyHierarchyAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_StrategyHierarchyAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.CSRStrategyHierarchyAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesCustomChoiceTypeResponse]:
        response_instance: model.CSRObjectivesCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_Objectives_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.CSRObjectivesCustomChoiceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_custom_choice_threshold_symbol(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesCustomChoiceThresholdSymbolResponse]:
        response_instance: (
            model.CSRObjectivesCustomChoiceThresholdSymbolResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_Objectives_CustomChoice_ThresholdSymbol?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.CSRObjectivesCustomChoiceThresholdSymbolResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_custom_choice_sd_spatial_conso(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesCustomChoiceSDSpatialConsoResponse]:
        response_instance: (
            model.CSRObjectivesCustomChoiceSDSpatialConsoResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_Objectives_CustomChoice_SDSpatialConso?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.CSRObjectivesCustomChoiceSDSpatialConsoResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def csr_objectives_custom_choice_sd_time_conso(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.CSRObjectivesCustomChoiceSDTimeConsoResponse]:
        response_instance: model.CSRObjectivesCustomChoiceSDTimeConsoResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/CSR_Objectives_CustomChoice_SDTimeConso?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.CSRObjectivesCustomChoiceSDTimeConsoResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_items_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemsAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.TCKActionItemsAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItemsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.TCKActionItemsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_custom_choice_severity(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemCustomChoiceSeverityResponse]:
        response_instance: model.TCKActionItemCustomChoiceSeverityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItem_CustomChoice_Severity?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.TCKActionItemCustomChoiceSeverityResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_custom_choice_cs_quality_check_complete(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.TCKActionItemCustomChoiceCSQualityCheckCompleteResponse
    ]:
        response_instance: (
            model.TCKActionItemCustomChoiceCSQualityCheckCompleteResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItem_CustomChoice_CS_QualityCheckComplete?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.TCKActionItemCustomChoiceCSQualityCheckCompleteResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_custom_choice_sw_ticket_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemCustomChoiceSWTicketStatusResponse]:
        response_instance: (
            model.TCKActionItemCustomChoiceSWTicketStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItem_CustomChoice_SWTicketStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.TCKActionItemCustomChoiceSWTicketStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_action_item_custom_choice_sw_ticket_build_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKActionItemCustomChoiceSWTicketBuildStatusResponse]:
        response_instance: (
            model.TCKActionItemCustomChoiceSWTicketBuildStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_ActionItem_CustomChoice_SWTicketBuildStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.TCKActionItemCustomChoiceSWTicketBuildStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def tck_resources_custom_choice_company(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.TCKResourcesCustomChoiceCompanyResponse]:
        response_instance: model.TCKResourcesCustomChoiceCompanyResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/TCK_Resources_CustomChoice_Company?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.TCKResourcesCustomChoiceCompanyResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_import_files_dpc_custom_choice_import_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoImportFilesDPCCustomChoiceImportTypeResponse]:
        response_instance: model.HoImportFilesDPCCustomChoiceImportTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_ImportFilesDPC_CustomChoice_ImportType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoImportFilesDPCCustomChoiceImportTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_applications_custom_choice_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoApplicationsCustomChoiceStatusResponse]:
        response_instance: model.HoApplicationsCustomChoiceStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Applications_CustomChoice_Status?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoApplicationsCustomChoiceStatusResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_units_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoUnitsCustomChoiceTypeResponse]:
        response_instance: model.HoUnitsCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Units_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoUnitsCustomChoiceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_units_custom_choice_relation(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoUnitsCustomChoiceRelationResponse]:
        response_instance: model.HoUnitsCustomChoiceRelationResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Units_CustomChoice_Relation?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoUnitsCustomChoiceRelationResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_calendar_configuration_custom_choice_display(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoCalendarConfigurationCustomChoiceDisplayResponse]:
        response_instance: (
            model.HoCalendarConfigurationCustomChoiceDisplayResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_CalendarConfiguration_CustomChoice_Display?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoCalendarConfigurationCustomChoiceDisplayResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_calendar_configuration_custom_choice_end_date_based_on(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.HoCalendarConfigurationCustomChoiceEndDateBasedOnResponse
    ]:
        response_instance: (
            model.HoCalendarConfigurationCustomChoiceEndDateBasedOnResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_CalendarConfiguration_CustomChoice_EndDateBasedOn?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoCalendarConfigurationCustomChoiceEndDateBasedOnResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_audit_trail_user_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoAuditTrailUserCustomChoiceModeResponse]:
        response_instance: model.HoAuditTrailUserCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_AuditTrailUser_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoAuditTrailUserCustomChoiceModeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_business_directory_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoBusinessDirectoryATCustomChoiceModeResponse]:
        response_instance: model.HoBusinessDirectoryATCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_BusinessDirectoryAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoBusinessDirectoryATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_directory_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDirectoryAuditTrailCustomChoiceModeResponse]:
        response_instance: model.HoDirectoryAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_DirectoryAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoDirectoryAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_directory_custom_choice_account_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoDirectoryCustomChoiceAccountStatusResponse]:
        response_instance: model.HoDirectoryCustomChoiceAccountStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Directory_CustomChoice_AccountStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoDirectoryCustomChoiceAccountStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_geography_levels_custom_choice_system_level(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoGeographyLevelsCustomChoiceSystemLevelResponse]:
        response_instance: (
            model.HoGeographyLevelsCustomChoiceSystemLevelResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_GeographyLevels_CustomChoice_SystemLevel?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoGeographyLevelsCustomChoiceSystemLevelResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_third_axis_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoThirdAxisAuditTrailCustomChoiceModeResponse]:
        response_instance: model.HoThirdAxisAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_ThirdAxisAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoThirdAxisAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_second_axis_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSecondAxisAuditTrailCustomChoiceModeResponse]:
        response_instance: model.HoSecondAxisAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SecondAxisAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoSecondAxisAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_entities_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoEntitiesAuditTrailCustomChoiceModeResponse]:
        response_instance: model.HoEntitiesAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_EntitiesAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoEntitiesAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_third_axis_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHThirdAxisCustomChoiceEntityStatusResponse]:
        response_instance: model.HoHThirdAxisCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HThirdAxis_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoHThirdAxisCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_second_axis_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHSecondAxisCustomChoiceEntityStatusResponse]:
        response_instance: model.HoHSecondAxisCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HSecondAxis_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoHSecondAxisCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_h_first_axis_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoHFirstAxisCustomChoiceEntityStatusResponse]:
        response_instance: model.HoHFirstAxisCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_HFirstAxis_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoHFirstAxisCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_snapshots_axis_custom_choice_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSnapshotsAxisCustomChoiceStatusResponse]:
        response_instance: model.HoSnapshotsAxisCustomChoiceStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SnapshotsAxis_CustomChoice_Status?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoSnapshotsAxisCustomChoiceStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_third_axis_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoThirdAxisCustomChoiceEntityStatusResponse]:
        response_instance: model.HoThirdAxisCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_ThirdAxis_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoThirdAxisCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_second_axis_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoSecondAxisCustomChoiceEntityStatusResponse]:
        response_instance: model.HoSecondAxisCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_SecondAxis_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoSecondAxisCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_entities_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoEntitiesCustomChoiceEntityStatusResponse]:
        response_instance: model.HoEntitiesCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_Entities_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoEntitiesCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_new_glossary_custom_choice_type_of_constant(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewGlossaryCustomChoiceTypeOfConstantResponse]:
        response_instance: (
            model.HoNewGlossaryCustomChoiceTypeOfConstantResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewGlossary_CustomChoice_TypeOfConstant?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoNewGlossaryCustomChoiceTypeOfConstantResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles_custom_choice_priority(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesCustomChoicePriorityResponse]:
        response_instance: model.HoNewsArticlesCustomChoicePriorityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles_CustomChoice_Priority?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoNewsArticlesCustomChoicePriorityResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles_custom_choice_links_number(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesCustomChoiceLinksNumberResponse]:
        response_instance: model.HoNewsArticlesCustomChoiceLinksNumberResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles_CustomChoice_LinksNumber?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoNewsArticlesCustomChoiceLinksNumberResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles_custom_choice_files_number(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesCustomChoiceFilesNumberResponse]:
        response_instance: model.HoNewsArticlesCustomChoiceFilesNumberResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles_CustomChoice_FilesNumber?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoNewsArticlesCustomChoiceFilesNumberResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles_custom_choice_axe(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesCustomChoiceAxeResponse]:
        response_instance: model.HoNewsArticlesCustomChoiceAxeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles_CustomChoice_Axe?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.HoNewsArticlesCustomChoiceAxeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def ho_news_articles_custom_choice_visibility(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.HoNewsArticlesCustomChoiceVisibilityResponse]:
        response_instance: model.HoNewsArticlesCustomChoiceVisibilityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/ho_NewsArticles_CustomChoice_Visibility?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.HoNewsArticlesCustomChoiceVisibilityResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_supplier_energy_coverage_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDSupplierEnergyCoverageATCustomChoiceModeResponse]:
        response_instance: (
            model.SDSupplierEnergyCoverageATCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_SupplierEnergyCoverageAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDSupplierEnergyCoverageATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_energy_supplier_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEnergySupplierATCustomChoiceModeResponse]:
        response_instance: model.SDEnergySupplierATCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EnergySupplierAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEnergySupplierATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_eac_energy_allocation_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEacEnergyAllocationATCustomChoiceModeResponse]:
        response_instance: (
            model.SDEacEnergyAllocationATCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EACEnergyAllocationAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEacEnergyAllocationATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_energy_attributes_certificate_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDEnergyAttributesCertificateATCustomChoiceModeResponse
    ]:
        response_instance: (
            model.SDEnergyAttributesCertificateATCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EnergyAttributesCertificateAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEnergyAttributesCertificateATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_material_types_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDMaterialTypesATCustomChoiceModeResponse]:
        response_instance: model.SDMaterialTypesATCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_MaterialTypesAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDMaterialTypesATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_conversion_types_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDConversionTypesATCustomChoiceModeResponse]:
        response_instance: model.SDConversionTypesATCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_ConversionTypesAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDConversionTypesATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_local_cross_units_conversions_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDLocalCrossUnitsConversionsATCustomChoiceModeResponse
    ]:
        response_instance: (
            model.SDLocalCrossUnitsConversionsATCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_LocalCrossUnitsConversionsAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDLocalCrossUnitsConversionsATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cross_units_conversions_at_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCrossUnitsConversionsATCustomChoiceModeResponse]:
        response_instance: (
            model.SDCrossUnitsConversionsATCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CrossUnitsConversionsAT_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCrossUnitsConversionsATCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_emission_factor_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEmissionFactorAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.SDEmissionFactorAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EmissionFactorAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEmissionFactorAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_emission_factors_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEmissionFactorsAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.SDEmissionFactorsAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_EmissionFactorsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEmissionFactorsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_ghg_protocols_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDGhgProtocolsAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.SDGhgProtocolsAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_GHGProtocolsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDGhgProtocolsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_tooling_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsToolingAuditTrailCustomChoiceModeResponse]:
        response_instance: model.SDCsToolingAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ToolingAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCsToolingAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsAuditTrailCustomChoiceModeResponse]:
        response_instance: model.SDIndicatorsAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_trend_method(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceTrendMethodResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceTrendMethodResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_TrendMethod?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceTrendMethodResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_trend_operator(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceTrendOperatorResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceTrendOperatorResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_TrendOperator?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceTrendOperatorResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_trend_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceTrendInclusionResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceTrendInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_TrendInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceTrendInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_trend_min_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceTrendMinInclusionResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceTrendMinInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_TrendMinInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceTrendMinInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_trend_max_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceTrendMaxInclusionResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceTrendMaxInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_TrendMaxInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceTrendMaxInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_expected_value_list_comparison_type(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse  # noqa
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_ExpectedValueListComparisonType?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_expected_value_comparison_type(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse  # noqa
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_ExpectedValueComparisonType?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_expected_value_min_inclusion(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse  # noqa
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_ExpectedValueMinInclusion?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_expected_value_max_inclusion(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse  # noqa
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_ExpectedValueMaxInclusion?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_failure_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceFailureTypeResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceFailureTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_FailureType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceFailureTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_versioned_consistency_checks_custom_choice_justification_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDVersionedConsistencyChecksCustomChoiceJustificationModeResponse
    ]:
        response_instance: (
            model.SDVersionedConsistencyChecksCustomChoiceJustificationModeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_VersionedConsistencyChecks_CustomChoice_JustificationMode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDVersionedConsistencyChecksCustomChoiceJustificationModeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_previous_value_based_on(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoicePreviousValueBasedOnResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoicePreviousValueBasedOnResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_PreviousValueBasedOn?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoicePreviousValueBasedOnResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsCustomChoiceTypeResponse]:
        response_instance: model.SDHistorizedIndicatorsCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_line_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsCustomChoiceLineTypeResponse]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceLineTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_LineType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceLineTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_column_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsCustomChoiceColumnTypeResponse]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceColumnTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_ColumnType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceColumnTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_consolidation_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceConsolidationTypeResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceConsolidationTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_ConsolidationType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceConsolidationTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_conso_order(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsCustomChoiceConsoOrderResponse]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceConsoOrderResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_ConsoOrder?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceConsoOrderResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_wished_trend(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDHistorizedIndicatorsCustomChoiceWishedTrendResponse]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceWishedTrendResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_WishedTrend?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceWishedTrendResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_comments_active(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcCommentsActiveResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcCommentsActiveResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcCommentsActive?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceCcCommentsActiveResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_range_active(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcRangeActiveResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcRangeActiveResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcRangeActive?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceCcRangeActiveResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_min_value_behavior(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceMinValueBehaviorResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceMinValueBehaviorResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_MinValueBehavior?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceMinValueBehaviorResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_max_value_behavior(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceMaxValueBehaviorResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceMaxValueBehaviorResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_MaxValueBehavior?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceMaxValueBehaviorResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_previous_period_active(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodActiveResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodActiveResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcPreviousPeriodActive?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodActiveResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_previous_period_appreciation(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodAppreciationResponse  # noqa
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodAppreciationResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcPreviousPeriodAppreciation?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceCcPreviousPeriodAppreciationResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_rule_active(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcRuleActiveResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcRuleActiveResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcRuleActive?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceCcRuleActiveResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cc_filled_active(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCcFilledActiveResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCcFilledActiveResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CcFilledActive?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDHistorizedIndicatorsCustomChoiceCcFilledActiveResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_historized_indicators_custom_choice_cs_questionnaire_form(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDHistorizedIndicatorsCustomChoiceCSQuestionnaireFormResponse
    ]:
        response_instance: (
            model.SDHistorizedIndicatorsCustomChoiceCSQuestionnaireFormResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_HistorizedIndicators_CustomChoice_CS_QuestionnaireForm?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDHistorizedIndicatorsCustomChoiceCSQuestionnaireFormResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_column_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableColumnCustomChoiceTypeResponse]:
        response_instance: model.SDTableColumnCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableColumn_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableColumnCustomChoiceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_column_custom_choice_conso_order(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableColumnCustomChoiceConsoOrderResponse]:
        response_instance: model.SDTableColumnCustomChoiceConsoOrderResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableColumn_CustomChoice_ConsoOrder?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDTableColumnCustomChoiceConsoOrderResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_table_line_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDTableLineCustomChoiceTypeResponse]:
        response_instance: model.SDTableLineCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_TableLine_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDTableLineCustomChoiceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_trend_method(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceTrendMethodResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceTrendMethodResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_TrendMethod?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceTrendMethodResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_trend_operator(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceTrendOperatorResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceTrendOperatorResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_TrendOperator?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceTrendOperatorResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_trend_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceTrendInclusionResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceTrendInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_TrendInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceTrendInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_trend_min_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceTrendMinInclusionResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceTrendMinInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_TrendMinInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceTrendMinInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_trend_max_inclusion(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceTrendMaxInclusionResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceTrendMaxInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_TrendMaxInclusion?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceTrendMaxInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_expected_value_list_comparison_type(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse  # noqa
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_ExpectedValueListComparisonType?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueListComparisonTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_expected_value_comparison_type(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse  # noqa
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_ExpectedValueComparisonType?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueComparisonTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_expected_value_min_inclusion(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse  # noqa
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_ExpectedValueMinInclusion?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMinInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_expected_value_max_inclusion(  # noqa
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse  # noqa
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_ExpectedValueMaxInclusion?"  # noqa
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceExpectedValueMaxInclusionResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_failure_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceFailureTypeResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceFailureTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_FailureType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceFailureTypeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicator_consistency_checks_custom_choice_justification_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDIndicatorConsistencyChecksCustomChoiceJustificationModeResponse
    ]:
        response_instance: (
            model.SDIndicatorConsistencyChecksCustomChoiceJustificationModeResponse  # noqa
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_IndicatorConsistencyChecks_CustomChoice_JustificationMode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorConsistencyChecksCustomChoiceJustificationModeResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_previous_value_based_on(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoicePreviousValueBasedOnResponse]:
        response_instance: (
            model.SDIndicatorsCustomChoicePreviousValueBasedOnResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_PreviousValueBasedOn?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsCustomChoicePreviousValueBasedOnResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_cs_questionnaire_form(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceCSQuestionnaireFormResponse]:
        response_instance: (
            model.SDIndicatorsCustomChoiceCSQuestionnaireFormResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_CS_QuestionnaireForm?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsCustomChoiceCSQuestionnaireFormResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceTypeResponse]:
        response_instance: model.SDIndicatorsCustomChoiceTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_Type?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorsCustomChoiceTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_line_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceLineTypeResponse]:
        response_instance: model.SDIndicatorsCustomChoiceLineTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_LineType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDIndicatorsCustomChoiceLineTypeResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_column_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceColumnTypeResponse]:
        response_instance: model.SDIndicatorsCustomChoiceColumnTypeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_ColumnType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsCustomChoiceColumnTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_conso_order(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceConsoOrderResponse]:
        response_instance: model.SDIndicatorsCustomChoiceConsoOrderResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_ConsoOrder?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsCustomChoiceConsoOrderResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_indicators_custom_choice_wished_trend(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDIndicatorsCustomChoiceWishedTrendResponse]:
        response_instance: model.SDIndicatorsCustomChoiceWishedTrendResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Indicators_CustomChoice_WishedTrend?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDIndicatorsCustomChoiceWishedTrendResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_defect_import_custom_choice_cs_upload_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsDefectImportCustomChoiceCSUploadStatusResponse]:
        response_instance: (
            model.SDCsDefectImportCustomChoiceCSUploadStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_DefectImport_CustomChoice_CS_UploadStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCsDefectImportCustomChoiceCSUploadStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_chemistry_upload_custom_choice_cs_upload_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCsChemistryUploadCustomChoiceCSUploadStatusResponse]:
        response_instance: (
            model.SDCsChemistryUploadCustomChoiceCSUploadStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ChemistryUpload_CustomChoice_CS_UploadStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCsChemistryUploadCustomChoiceCSUploadStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_cs_import_waste_entries_custom_choice_cs_upload_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDCsImportWasteEntriesCustomChoiceCSUploadStatusResponse
    ]:
        response_instance: (
            model.SDCsImportWasteEntriesCustomChoiceCSUploadStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CS_ImportWasteEntries_CustomChoice_CS_UploadStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCsImportWasteEntriesCustomChoiceCSUploadStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_standard_alerts_custom_choice_tg_xml_start_date(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDStandardAlertsCustomChoiceTgXmlStartDateResponse]:
        response_instance: (
            model.SDStandardAlertsCustomChoiceTgXmlStartDateResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_StandardAlerts_CustomChoice_TgXmlStartDate?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDStandardAlertsCustomChoiceTgXmlStartDateResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_standard_alerts_custom_choice_delay(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDStandardAlertsCustomChoiceDelayResponse]:
        response_instance: model.SDStandardAlertsCustomChoiceDelayResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_StandardAlerts_CustomChoice_Delay?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDStandardAlertsCustomChoiceDelayResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_standard_alerts_custom_choice_periodicity(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDStandardAlertsCustomChoicePeriodicityResponse]:
        response_instance: (
            model.SDStandardAlertsCustomChoicePeriodicityResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_StandardAlerts_CustomChoice_Periodicity?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDStandardAlertsCustomChoicePeriodicityResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_standard_alerts_custom_choice_tg_xml_end_date(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDStandardAlertsCustomChoiceTgXmlEndDateResponse]:
        response_instance: (
            model.SDStandardAlertsCustomChoiceTgXmlEndDateResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_StandardAlerts_CustomChoice_TgXmlEndDate?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDStandardAlertsCustomChoiceTgXmlEndDateResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_recalculations_custom_choice_definition_level(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRecalculationsCustomChoiceDefinitionLevelResponse]:
        response_instance: (
            model.SDRecalculationsCustomChoiceDefinitionLevelResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Recalculations_CustomChoice_DefinitionLevel?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDRecalculationsCustomChoiceDefinitionLevelResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_recalculations_custom_choice_recurrence(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRecalculationsCustomChoiceRecurrenceResponse]:
        response_instance: model.SDRecalculationsCustomChoiceRecurrenceResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Recalculations_CustomChoice_Recurrence?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDRecalculationsCustomChoiceRecurrenceResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_recalculations_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDRecalculationsAuditTrailCustomChoiceModeResponse]:
        response_instance: (
            model.SDRecalculationsAuditTrailCustomChoiceModeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_RecalculationsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDRecalculationsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_campaigns_audit_trail_custom_choice_mode(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCampaignsAuditTrailCustomChoiceModeResponse]:
        response_instance: model.SDCampaignsAuditTrailCustomChoiceModeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_CampaignsAuditTrail_CustomChoice_Mode?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDCampaignsAuditTrailCustomChoiceModeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_alerts_custom_choice_periodicity(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDAlertsCustomChoicePeriodicityResponse]:
        response_instance: model.SDAlertsCustomChoicePeriodicityResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Alerts_CustomChoice_Periodicity?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDAlertsCustomChoicePeriodicityResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_updater_custom_choice_fractal_scope(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDUpdaterCustomChoiceFractalScopeResponse]:
        response_instance: model.SDUpdaterCustomChoiceFractalScopeResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Updater_CustomChoice_FractalScope?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDUpdaterCustomChoiceFractalScopeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_campaigns_custom_choice_level_no(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDCampaignsCustomChoiceLevelNoResponse]:
        response_instance: model.SDCampaignsCustomChoiceLevelNoResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Campaigns_CustomChoice_LevelNo?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDCampaignsCustomChoiceLevelNoResponse(
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_custom_choice_entity_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesCustomChoiceEntityStatusResponse]:
        response_instance: model.SDEntitiesCustomChoiceEntityStatusResponse
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_CustomChoice_EntityStatus?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEntitiesCustomChoiceEntityStatusResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_consistency_checks_custom_choice_cc_type(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[model.SDEntitiesConsistencyChecksCustomChoiceCcTypeResponse]:
        response_instance: (
            model.SDEntitiesConsistencyChecksCustomChoiceCcTypeResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_ConsistencyChecks_CustomChoice_CcType?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = (
                model.SDEntitiesConsistencyChecksCustomChoiceCcTypeResponse(
                    self.request(url, method="GET")
                )
            )
            yield response_instance
            url = response_instance.odata_next_link

    def sd_entities_data_consistency_checks_custom_choice_status(
        self, filter: str = "", orderby: str = "", top: int = 0, skip: int = 0
    ) -> Iterable[
        model.SDEntitiesDataConsistencyChecksCustomChoiceStatusResponse
    ]:
        response_instance: (
            model.SDEntitiesDataConsistencyChecksCustomChoiceStatusResponse
        )
        filter_query_argument: str = (
            f"&$filter={quote(filter)}" if filter else ""
        )
        orderby_query_argument: str = (
            f"&$orderby={quote(orderby)}" if orderby else ""
        )
        top_query_argument: str = f"&$top={top}" if top else ""
        skip_query_argument: str = f"&skip={skip}" if skip else ""
        url: Optional[str] = (
            "/SD_Entities_DataConsistencyChecks_CustomChoice_Status?"
            "$count=true"
            f"{filter_query_argument}"
            f"{orderby_query_argument}"
            f"{top_query_argument}"
            f"{skip_query_argument}"
        )
        while url:
            response_instance = model.SDEntitiesDataConsistencyChecksCustomChoiceStatusResponse(  # noqa
                self.request(url, method="GET")
            )
            yield response_instance
            url = response_instance.odata_next_link
