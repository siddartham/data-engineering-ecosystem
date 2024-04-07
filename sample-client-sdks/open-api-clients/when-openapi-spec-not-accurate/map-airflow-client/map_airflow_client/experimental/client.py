import typing
from datetime import datetime
from logging import Logger

import oapi
import sob
from cerberus_assistant.decorate import apply_cerberus_path_arguments

from . import model


class Client(oapi.client.Client):
    """
    Initialization Parameters:

    - url (str): The base URL for API requests.
    - oauth2_token_url (str) = "": The token URL to use for OAuth2
      authentication.
      Can be relative to `url`.
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
      they occur
    """

    __slots__: typing.Tuple[str, ...] = oapi.client.CLIENT_SLOTS

    @apply_cerberus_path_arguments(
        cerberus_url_parameter_name="cerberus_url",
        oauth2_client_secret="oauth2_client_secret_cerberus_path",
    )
    def __init__(
        self,
        url: str = "",
        oauth2_client_id: str = "",
        oauth2_client_secret: str = "",
        oauth2_token_url: str = "",
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
        cerberus_url: str = "https://prod.cerberus.mycloud.com",
        oauth2_client_secret_cerberus_path: str = "",
    ) -> None:
        super().__init__(
            url=url,
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

    def get_latest_runs(self) -> model.LatestRunsResponse:
        return model.LatestRunsResponse(
            self.request("/latest_runs", method="GET"),
        )

    def get_dag_runs(self, dag_id: str) -> model.DagRuns:
        return model.DagRuns(
            self.request(f"/dags/{dag_id}/dag_runs", method="GET")
        )

    def get_dag_run(
        self, dag_id: str, execution_date: typing.Union[str, datetime]
    ) -> model.DagRun:
        if isinstance(execution_date, datetime):
            execution_date = execution_date.isoformat()
        else:
            assert isinstance(execution_date, str)
        return model.DagRun(
            self.request(
                f"/dags/{dag_id}/dag_runs/{execution_date}", method="GET"
            )
        )

    def get_dag_task(self, dag_id: str, task_id: str) -> sob.model.Dictionary:
        return sob.model.Dictionary(
            self.request(f"/dags/{dag_id}/tasks/{task_id}", method="GET")
        )

    def get_dag_run_task(
        self,
        dag_id: str,
        execution_date: typing.Union[str, datetime],
        task_id: str,
    ) -> model.DagRun:
        if isinstance(execution_date, datetime):
            execution_date = execution_date.isoformat()
        else:
            assert isinstance(execution_date, str)
        return model.DagRun(
            self.request(
                f"/dags/{dag_id}/dag_runs/{execution_date}/tasks/{task_id}",
                method="GET",
            )
        )

    def get_dag_paused(
        self, dag_id: str, paused: typing.Optional[bool] = None
    ) -> model.DagPaused:
        """
        This method returns the paused state of the DAG if no value
        is passed for `paused`. If a boolean value is passed to the `paused`
        parameter, the DAG will be paused or un-paused.

        Parameters:

        - dag_id (str)
        - paused (bool|None) = None: `True`, `False`, or `None`
        """
        if paused is not None:
            assert isinstance(paused, bool)
        return model.DagPaused(
            self.request(
                "/dags/{}/paused{}".format(
                    dag_id,
                    (
                        ""
                        if paused is None
                        else "/true"
                        if paused
                        else "/false"
                    ),
                ),
                method="GET",
            )
        )

    def get_pools(self) -> model.Pools:
        return model.Pools(self.request("/pools", method="GET"))

    def get_pool(self, name: str) -> model.Pool:
        return model.Pool(self.request(f"/pools/{name}", method="GET"))

    def delete_pool(self, name: str) -> sob.abc.Readable:
        return self.request(f"/pools/{name}", method="DELETE")

    def post_pool(self, pool: model.Pool) -> sob.abc.Readable:
        return self.request("/pools", data=pool, method="POST")

    def post_dag_run(
        self, dag_id: str, conf: str = ""
    ) -> model.PostDagRunResponse:
        return model.PostDagRunResponse(
            self.request(
                f"/dags/{dag_id}/dag_runs",
                data=sob.model.Dictionary({"conf": conf}),
                method="POST",
            )
        )
