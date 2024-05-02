import oapi
import typing
from numbers import Number
from urllib.parse import quote, urlencode
from . import model
from logging import Logger
from cerberus_assistant.config import CERBERUS_URL
from cerberus_assistant.decorate import apply_cerberus_path_arguments


def _is_dict_item_true_or_number(item: typing.Tuple[str, typing.Any]) -> bool:
    value: typing.Any = item[1]
    return isinstance(value, Number) or bool(value)


class Client(oapi.client.Client):
    """
    Initialization Parameters:

    - url (str): The base URL for API requests.
    - bearer_token (str) = "": A token for use with HTTP bearer authentication.
    - timeout (int): The number of seconds before a request will timeout
      and throw an error. If this is 0 (the default), the system default
      timeout will be used.
    - retry_number_of_attempts (int) = 1: The number of times to retry
      a request which results in an error.
    - retry_for_errors: A tuple of one or more exception types
      on which to retry a request. To retry for *all* errors,
      pass `(Exception,)` for this argument.
    - retry_hook: A function, accepting one argument (an Exception),
      and returning a boolean value indicating whether to retry the
      request (if retries have not been exhausted). This hook applies
      *only* for exceptions which are a sub-class of an exception
      included in `retry_for_errors`.
    - logger (logging.Logger|None) = None:
      A `logging.Logger` to which requests should be logged.
    - echo (bool) = False: If `True`, requests/responses are printed as
      they occur.
    - cerberus_url (str): The root URL for the Cerberus API where
      your secrets are stored.
    - bearer_token_cerberus_path (str) = "": A Cerberus secure data path
      (including /key) wherein a bearer token with which to authenticate can be
      found.
    - url_cerberus_path (str) = "": A Cerberus secure data path (including /key
      ) wherein the API base URL can be found.
    """

    __slots__: typing.Tuple[str, ...] = oapi.client.CLIENT_SLOTS

    @apply_cerberus_path_arguments(
        cerberus_url_parameter_name="cerberus_url",
        bearer_token="bearer_token_cerberus_path",
        url="url_cerberus_path",
    )
    def __init__(
        self,
        url: str = "https://api.airtable.com/v0",
        bearer_token: str = "",
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
        bearer_token_cerberus_path: str = "",
        url_cerberus_path: str = "",
    ) -> None:
        super().__init__(
            url=url,
            bearer_token=bearer_token,
            timeout=timeout,
            retry_number_of_attempts=retry_number_of_attempts,
            retry_for_errors=retry_for_errors,
            retry_hook=retry_hook,
            logger=logger,
            echo=echo,
        )

    def __reduce__(
        self,
    ) -> typing.Tuple[
        typing.Callable[..., oapi.client.Client], typing.Tuple[typing.Any, ...]
    ]:
        return self._resurrect_client, (
            # Initialization Parameters
            self.url,
            self.bearer_token,
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

    def get_meta_bases(self) -> model.MetaBasesGetResponse:
        """
        This function returns information about all bases you have access to.
        """
        return model.MetaBasesGetResponse(
            self.request("/meta/bases", method="GET")
        )

    def get_meta_bases_base_id_tables(
        self, base_id: str
    ) -> model.MetaBasesBaseIdTablesGetResponse:
        """
        This function returns information about all tables
        in the specified `base_id`.

        Parameters:

        - base_id (str)
        """
        return model.MetaBasesBaseIdTablesGetResponse(
            self.request(f"/meta/bases/{base_id}/tables", method="GET")
        )

    def get_base_id_table(
        self,
        base_id: typing.Optional[str],
        table: str,
        page_size: typing.Optional[int] = None,
        offset: str = "",
        filter_by_formula: str = "",
        view: str = "",
        max_records: typing.Optional[int] = None,
        fields: typing.Sequence[str] = (),
    ) -> model.BaseIdTableGetResponse:
        """
        This function gets data from a table, optionally filtering
        according to the provided argument values.

        Parameters:
        - base_id (str)
        - table (str)
        - page_size (int) = None: The number of records to return. If this is
          `None`, no page size will be explicitly passed, causing the API to
          default to 100 (a default which is subject to change).
        - offset (str) = "": An `offset` identifier returned by a previously
          returned `model.GetResponse` instance.
        - filter_by_formula (str) = "": See AirTable's
          [formula field reference](https://bit.ly/34mzPer).
        - view (str) = "": The name of a view from which to return records.
        - max_records (int) = 0: The maximum number of records to return
          *total* (including all pages).
        - fields ([str]) = (): A list/tuple of field names to include.
        """
        # Assemble the URL
        path: str = f"/{base_id}/{quote(table)}"
        # Assemble the query string
        query_string_arguments: typing.Dict[
            str, typing.Union[str, int, typing.Sequence[str], None]
        ] = {
            "pageSize": page_size,
            "offset": offset,
            "filterByFormula": filter_by_formula,
            "view": view,
            "maxRecords": max_records,
            "fields": fields,
        }
        # Append any non-empty query string arguments to the path
        if any(query_string_arguments.values()):
            # Filter out empty arguments and encode the query string
            query_string: str = urlencode(
                tuple(
                    filter(  # type: ignore
                        _is_dict_item_true_or_number,
                        query_string_arguments.items(),
                    )
                )
            )
            path = f"{path}?{query_string}"
        return model.BaseIdTableGetResponse(self.request(path, method="GET"))

    def get_base_id_table_record_id(
        self, base_id: typing.Optional[str], table: str, record_id: str
    ) -> model.BaseIdTableRecordIdGetResponse:
        """
        This function gets a single record from a table.

        Parameters:
        - base_id (str)
        - table (str)
        - record_id (str)
        """
        return model.BaseIdTableRecordIdGetResponse(
            self.request(
                f"/{base_id}/{quote(table)}/{record_id}", method="GET"
            )
        )
