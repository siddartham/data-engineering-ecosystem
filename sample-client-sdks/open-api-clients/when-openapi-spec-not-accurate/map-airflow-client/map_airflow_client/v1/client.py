
import datetime
import decimal
import oapi
import sob
import typing
from . import model
from logging import Logger
from cerberus_assistant.config import CERBERUS_URL
from cerberus_assistant.decorate import apply_cerberus_path_arguments


class Client(oapi.client.Client):
    """
    Initialization Parameters:

    - url (str): The base URL for API requests.
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
    - oauth2_client_secret_cerberus_path (str) = "": A Cerberus secure data
      path (including /key) wherein a username with which to authenticate can
      be found.
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
        oauth2_token_url: str = (
            "https://api.aegis.mycloud.com/v1/prod/token"
        ),
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

    def get_connections(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.ConnectionCollection:
        """
        List connections

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/connections",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ConnectionCollection,
            )
        )

    def post_connections(
        self,
        connection: model.Connection,
    ) -> model.Connection:
        """
        Create a connection

        Parameters:

        - connection:
          Full representation of the connection.
        """
        response: sob.abc.Readable = self.request(
            "/connections",
            method="POST",
            json=connection,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Connection,
            )
        )

    def get_connections_connection_id(
        self,
        connection_id: str,
    ) -> model.Connection:
        """
        Get a connection

        Parameters:

        - connection_id:
          The connection ID.
        """
        response: sob.abc.Readable = self.request(
            "/connections/{connection_id}".format(**{
                "connection_id": str(oapi.client.format_argument_value(
                    "connection_id",
                    connection_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Connection,
            )
        )

    def delete_connections_connection_id(
        self,
        connection_id: str,
    ) -> None:
        """
        Delete a connection

        Parameters:

        - connection_id:
          The connection ID.
        """
        self.request(
            "/connections/{connection_id}".format(**{
                "connection_id": str(oapi.client.format_argument_value(
                    "connection_id",
                    connection_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_connections_connection_id(
        self,
        connection: model.Connection,
        connection_id: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.Connection:
        """
        Update a connection

        Parameters:

        - connection:
          Full representation of the connection.
        - connection_id:
          The connection ID.
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/connections/{connection_id}".format(**{
                "connection_id": str(oapi.client.format_argument_value(
                    "connection_id",
                    connection_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=connection,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Connection,
            )
        )

    def post_connections_test(
        self,
        connection: model.Connection,
    ) -> model.ConnectionTest:
        """
        Test a connection.

        For security reasons, the test connection functionality is disabled by
        default across Airflow UI, API and CLI.
        For more information on capabilities of users, see the documentation:
        https://airflow.apache.org/docs/apache-airflow/stable/security/
        security_model.html#capabilities-of-authenticated-ui-users.
        It is strongly advised to not enable the feature until you make sure
        that only
        highly trusted UI/API users have "edit connection" permissions.

        Set the "test_connection" flag to "Enabled" in the "core" section of
        Airflow configuration (airflow.cfg) to enable testing of collections.
        It can also be controlled by the environment variable `
        AIRFLOW__CORE__TEST_CONNECTION`.

        *New in version 2.2.0*

        Parameters:

        - connection:
          Full representation of the connection.
        """
        response: sob.abc.Readable = self.request(
            "/connections/test",
            method="POST",
            json=connection,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ConnectionTest,
            )
        )

    def get_dags(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
        tags: typing.Optional[
            model.FilterTags
        ] = None,
        only_active: typing.Optional[
            bool
        ] = None,
        paused: typing.Optional[
            bool
        ] = None,
        dag_id_pattern: typing.Optional[
            str
        ] = None,
    ) -> model.DAGCollection:
        """
        List DAGs in the database.
        `dag_id_pattern` can be set to match dags of a specific pattern

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        - tags:
          List of tags to filter results.
          *New in version 2.2.0*
        - only_active:
          Only filter active DAGs.
          *New in version 2.1.1*
        - paused:
          Only filter paused/unpaused DAGs. If absent or null, it returns
          paused and unpaused DAGs.
          *New in version 2.6.0*
        - dag_id_pattern:
          If set, only return DAGs with dag_ids matching this pattern.
        """
        response: sob.abc.Readable = self.request(
            "/dags",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
                "tags": oapi.client.format_argument_value(
                    "tags",
                    tags,
                    style="form",
                    explode=True,
                ),
                "only_active": oapi.client.format_argument_value(
                    "only_active",
                    only_active,
                    style="form",
                    explode=True,
                ),
                "paused": oapi.client.format_argument_value(
                    "paused",
                    paused,
                    style="form",
                    explode=True,
                ),
                "dag_id_pattern": oapi.client.format_argument_value(
                    "dag_id_pattern",
                    dag_id_pattern,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGCollection,
            )
        )

    def patch_dags(
        self,
        dag: model.DAG,
        dag_id_pattern: str,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        tags: typing.Optional[
            model.FilterTags
        ] = None,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
        only_active: typing.Optional[
            bool
        ] = None,
    ) -> model.DAGCollection:
        """
        Update DAGs of a given dag_id_pattern using UpdateMask.
        This endpoint allows specifying `~` as the dag_id_pattern to update all
        DAGs.
        *New in version 2.3.0*

        Parameters:

        - dag:
          DAG
        - dag_id_pattern:
          If set, only update DAGs with dag_ids matching this pattern.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - tags:
          List of tags to filter results.
          *New in version 2.2.0*
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        - only_active:
          Only filter active DAGs.
          *New in version 2.1.1*
        """
        response: sob.abc.Readable = self.request(
            "/dags",
            method="PATCH",
            query={
                "dag_id_pattern": oapi.client.format_argument_value(
                    "dag_id_pattern",
                    dag_id_pattern,
                    style="form",
                    explode=True,
                ),
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "tags": oapi.client.format_argument_value(
                    "tags",
                    tags,
                    style="form",
                    explode=True,
                ),
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
                "only_active": oapi.client.format_argument_value(
                    "only_active",
                    only_active,
                    style="form",
                    explode=True,
                ),
            },
            json=dag,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGCollection,
            )
        )

    def get_dags_dag_id(
        self,
        dag_id: str,
    ) -> model.DAG:
        """
        Presents only information available in database (DAGModel).
        If you need detailed information, consider using GET /dags/{dag_id}/
        details.

        Parameters:

        - dag_id:
          The DAG ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAG,
            )
        )

    def delete_dags_dag_id(
        self,
        dag_id: str,
    ) -> None:
        """
        Deletes all metadata related to the DAG, including finished DAG Runs
        and Tasks.
        Logs are not deleted. This action cannot be undone.

        *New in version 2.2.0*

        Parameters:

        - dag_id:
          The DAG ID.
        """
        self.request(
            "/dags/{dag_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_dags_dag_id(
        self,
        dag: model.DAG,
        dag_id: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.DAG:
        """
        Update a DAG

        Parameters:

        - dag:
          DAG
        - dag_id:
          The DAG ID.
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=dag,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAG,
            )
        )

    def post_dags_dag_id_clear_task_instances(
        self,
        clear_task_instances: model.ClearTaskInstances,
        dag_id: str,
    ) -> model.TaskInstanceReferenceCollection:
        """
        Clears a set of task instances associated with the DAG for a specified
        date range.

        Parameters:

        - clear_task_instances
        - dag_id:
          The DAG ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/clearTaskInstances".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="POST",
            json=clear_task_instances,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceReferenceCollection,
            )
        )

    def patch_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_set_note(
        self,
        set_task_instance_note: model.SetTaskInstanceNote,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
    ) -> model.TaskInstance:
        """
        Update the manual user note of a non-mapped Task Instance.

        *New in version 2.5.0*

        Parameters:

        - set_task_instance_note
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=set_task_instance_note,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstance,
            )
        )

    def patch_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_map_index_set_note(  # noqa
        self,
        set_task_instance_note: model.SetTaskInstanceNote,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
    ) -> model.TaskInstance:
        """
        Update the manual user note of a mapped Task Instance.

        *New in version 2.5.0*

        Parameters:

        - set_task_instance_note
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - map_index:
          The map index.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
                "map_index": str(oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=set_task_instance_note,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstance,
            )
        )

    def post_dags_dag_id_update_task_instances_state(
        self,
        update_task_instances_state: model.UpdateTaskInstancesState,
        dag_id: str,
    ) -> model.TaskInstanceReferenceCollection:
        """
        Updates the state for multiple task instances simultaneously.

        Parameters:

        - update_task_instances_state
        - dag_id:
          The DAG ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/updateTaskInstancesState".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="POST",
            json=update_task_instances_state,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceReferenceCollection,
            )
        )

    def get_dags_dag_id_dag_runs(
        self,
        dag_id: str,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        execution_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        execution_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_gte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_lte: typing.Optional[
            datetime.datetime
        ] = None,
        state: typing.Optional[
            model.FilterState
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.DAGRunCollection:
        """
        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs
        for all DAGs.

        Parameters:

        - dag_id:
          The DAG ID.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - execution_date_gte:
          Returns objects greater or equal to the specified date.
          This can be combined with execution_date_lte parameter to receive
          only the selected period.
        - execution_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with execution_date_gte parameter to receive
          only the selected period.
        - start_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - start_date_lte:
          Returns objects less or equal the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - end_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - end_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - updated_at_gte:
          Returns objects greater or equal the specified date.
          This can be combined with updated_at_lte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - updated_at_lte:
          Returns objects less or equal the specified date.
          This can be combined with updated_at_gte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - state:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "execution_date_gte": oapi.client.format_argument_value(
                    "execution_date_gte",
                    execution_date_gte,
                    style="form",
                    explode=True,
                ),
                "execution_date_lte": oapi.client.format_argument_value(
                    "execution_date_lte",
                    execution_date_lte,
                    style="form",
                    explode=True,
                ),
                "start_date_gte": oapi.client.format_argument_value(
                    "start_date_gte",
                    start_date_gte,
                    style="form",
                    explode=True,
                ),
                "start_date_lte": oapi.client.format_argument_value(
                    "start_date_lte",
                    start_date_lte,
                    style="form",
                    explode=True,
                ),
                "end_date_gte": oapi.client.format_argument_value(
                    "end_date_gte",
                    end_date_gte,
                    style="form",
                    explode=True,
                ),
                "end_date_lte": oapi.client.format_argument_value(
                    "end_date_lte",
                    end_date_lte,
                    style="form",
                    explode=True,
                ),
                "updated_at_gte": oapi.client.format_argument_value(
                    "updated_at_gte",
                    updated_at_gte,
                    style="form",
                    explode=True,
                ),
                "updated_at_lte": oapi.client.format_argument_value(
                    "updated_at_lte",
                    updated_at_lte,
                    style="form",
                    explode=True,
                ),
                "state": oapi.client.format_argument_value(
                    "state",
                    state,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRunCollection,
            )
        )

    def post_dags_dag_id_dag_runs(
        self,
        dag_run: model.DAGRun,
        dag_id: str,
    ) -> model.DAGRun:
        """
        This will initiate a dagrun. If DAG is paused then dagrun state will
        remain queued, and the task won't run.

        Parameters:

        - dag_run
        - dag_id:
          The DAG ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="POST",
            json=dag_run,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRun,
            )
        )

    def post_dags_dag_runs_list(
        self,
        list_dag_runs_form: model.ListDagRunsForm,
    ) -> model.DAGRunCollection:
        """
        This endpoint is a POST to allow filtering across a large number of DAG
        IDs, where as a GET it would run in to maximum HTTP request URL length
        limit.

        Parameters:

        - list_dag_runs_form
        """
        response: sob.abc.Readable = self.request(
            "/dags/~/dagRuns/list",
            method="POST",
            json=list_dag_runs_form,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRunCollection,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id(
        self,
        dag_id: str,
        dag_run_id: str,
    ) -> model.DAGRun:
        """
        Get a DAG run

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRun,
            )
        )

    def delete_dags_dag_id_dag_runs_dag_run_id(
        self,
        dag_id: str,
        dag_run_id: str,
    ) -> None:
        """
        Delete a DAG run

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_dags_dag_id_dag_runs_dag_run_id(
        self,
        update_dag_run_state: model.UpdateDagRunState,
        dag_id: str,
        dag_run_id: str,
    ) -> model.DAGRun:
        """
        Modify a DAG run.

        *New in version 2.2.0*

        Parameters:

        - update_dag_run_state:
          Modify the state of a DAG run.
          *New in version 2.2.0*
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=update_dag_run_state,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRun,
            )
        )

    def post_dags_dag_id_dag_runs_dag_run_id_clear(
        self,
        clear_dag_run: model.ClearDagRun,
        dag_id: str,
        dag_run_id: str,
    ) -> typing.Union[
        model.DAGRun,
        model.TaskInstanceCollection
    ]:
        """
        Clear a DAG run.

        *New in version 2.4.0*

        Parameters:

        - clear_dag_run
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/clear".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="POST",
            json=clear_dag_run,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRun,
                model.TaskInstanceCollection,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_upstream_dataset_events(
        self,
        dag_id: str,
        dag_run_id: str,
    ) -> model.DatasetEventCollection:
        """
        Get datasets for a dag run.

        *New in version 2.4.0*

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DatasetEventCollection,
            )
        )

    def patch_dags_dag_id_dag_runs_dag_run_id_set_note(
        self,
        set_dag_run_note: model.SetDagRunNote,
        dag_id: str,
        dag_run_id: str,
    ) -> model.DAGRun:
        """
        Update the manual user note of a DagRun.

        *New in version 2.5.0*

        Parameters:

        - set_dag_run_note
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/setNote".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=set_dag_run_note,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGRun,
            )
        )

    def get_event_logs(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        event: typing.Optional[
            str
        ] = None,
        owner: typing.Optional[
            str
        ] = None,
        before: typing.Optional[
            datetime.datetime
        ] = None,
        after: typing.Optional[
            datetime.datetime
        ] = None,
    ) -> model.EventLogCollection:
        """
        List log entries from event log.

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        - dag_id:
          Returns objects matched by the DAG ID.
        - task_id:
          Returns objects matched by the Task ID.
        - event:
          The name of event log.
        - owner:
          The owner's name of event log.
        - before:
          Timestamp to select event logs occurring before.
        - after:
          Timestamp to select event logs occurring after.
        """
        response: sob.abc.Readable = self.request(
            "/eventLogs",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
                "dag_id": oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="form",
                    explode=True,
                ),
                "task_id": oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="form",
                    explode=True,
                ),
                "event": oapi.client.format_argument_value(
                    "event",
                    event,
                    style="form",
                    explode=True,
                ),
                "owner": oapi.client.format_argument_value(
                    "owner",
                    owner,
                    style="form",
                    explode=True,
                ),
                "before": oapi.client.format_argument_value(
                    "before",
                    before,
                    style="form",
                    explode=True,
                ),
                "after": oapi.client.format_argument_value(
                    "after",
                    after,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.EventLogCollection,
            )
        )

    def get_event_logs_event_log_id(
        self,
        event_log_id: int,
    ) -> model.EventLog:
        """
        Get a log entry

        Parameters:

        - event_log_id:
          The event log ID.
        """
        response: sob.abc.Readable = self.request(
            "/eventLogs/{event_log_id}".format(**{
                "event_log_id": str(oapi.client.format_argument_value(
                    "event_log_id",
                    event_log_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.EventLog,
            )
        )

    def get_import_errors(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.ImportErrorCollection:
        """
        List import errors

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/importErrors",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ImportErrorCollection,
            )
        )

    def get_import_errors_import_error_id(
        self,
        import_error_id: int,
    ) -> model.ImportError:
        """
        Get an import error

        Parameters:

        - import_error_id:
          The import error ID.
        """
        response: sob.abc.Readable = self.request(
            "/importErrors/{import_error_id}".format(**{
                "import_error_id": str(oapi.client.format_argument_value(
                    "import_error_id",
                    import_error_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ImportError,
            )
        )

    def get_pools(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.PoolCollection:
        """
        List pools

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/pools",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.PoolCollection,
            )
        )

    def post_pools(
        self,
        pool: model.Pool,
    ) -> model.Pool:
        """
        Create a pool

        Parameters:

        - pool:
          The pool
        """
        response: sob.abc.Readable = self.request(
            "/pools",
            method="POST",
            json=pool,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Pool,
            )
        )

    def get_pools_pool_name(
        self,
        pool_name: str,
    ) -> model.Pool:
        """
        Get a pool

        Parameters:

        - pool_name:
          The pool name.
        """
        response: sob.abc.Readable = self.request(
            "/pools/{pool_name}".format(**{
                "pool_name": str(oapi.client.format_argument_value(
                    "pool_name",
                    pool_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Pool,
            )
        )

    def delete_pools_pool_name(
        self,
        pool_name: str,
    ) -> None:
        """
        Delete a pool

        Parameters:

        - pool_name:
          The pool name.
        """
        self.request(
            "/pools/{pool_name}".format(**{
                "pool_name": str(oapi.client.format_argument_value(
                    "pool_name",
                    pool_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_pools_pool_name(
        self,
        pool: model.Pool,
        pool_name: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.Pool:
        """
        Update a pool

        Parameters:

        - pool:
          The pool
        - pool_name:
          The pool name.
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/pools/{pool_name}".format(**{
                "pool_name": str(oapi.client.format_argument_value(
                    "pool_name",
                    pool_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=pool,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Pool,
            )
        )

    def get_providers(
        self,
    ) -> model.ProvidersGetResponse:
        """
        Get a list of providers.

        *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/providers",
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ProvidersGetResponse,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        execution_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        execution_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_gte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_lte: typing.Optional[
            datetime.datetime
        ] = None,
        duration_gte: typing.Union[
            int,
            float,
            decimal.Decimal,
            None
        ] = None,
        duration_lte: typing.Union[
            int,
            float,
            decimal.Decimal,
            None
        ] = None,
        state: typing.Optional[
            model.FilterState
        ] = None,
        pool: typing.Optional[
            model.FilterPool
        ] = None,
        queue: typing.Optional[
            model.FilterQueue
        ] = None,
    ) -> model.TaskInstanceCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id to
        retrieve DAG runs for all DAGs and DAG runs.

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - execution_date_gte:
          Returns objects greater or equal to the specified date.
          This can be combined with execution_date_lte parameter to receive
          only the selected period.
        - execution_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with execution_date_gte parameter to receive
          only the selected period.
        - start_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - start_date_lte:
          Returns objects less or equal the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - end_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - end_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - updated_at_gte:
          Returns objects greater or equal the specified date.
          This can be combined with updated_at_lte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - updated_at_lte:
          Returns objects less or equal the specified date.
          This can be combined with updated_at_gte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - duration_gte:
          Returns objects greater than or equal to the specified values.
          This can be combined with duration_lte parameter to receive only the
          selected period.
        - duration_lte:
          Returns objects less than or equal to the specified values.
          This can be combined with duration_gte parameter to receive only the
          selected range.
        - state:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - pool:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - queue:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "execution_date_gte": oapi.client.format_argument_value(
                    "execution_date_gte",
                    execution_date_gte,
                    style="form",
                    explode=True,
                ),
                "execution_date_lte": oapi.client.format_argument_value(
                    "execution_date_lte",
                    execution_date_lte,
                    style="form",
                    explode=True,
                ),
                "start_date_gte": oapi.client.format_argument_value(
                    "start_date_gte",
                    start_date_gte,
                    style="form",
                    explode=True,
                ),
                "start_date_lte": oapi.client.format_argument_value(
                    "start_date_lte",
                    start_date_lte,
                    style="form",
                    explode=True,
                ),
                "end_date_gte": oapi.client.format_argument_value(
                    "end_date_gte",
                    end_date_gte,
                    style="form",
                    explode=True,
                ),
                "end_date_lte": oapi.client.format_argument_value(
                    "end_date_lte",
                    end_date_lte,
                    style="form",
                    explode=True,
                ),
                "updated_at_gte": oapi.client.format_argument_value(
                    "updated_at_gte",
                    updated_at_gte,
                    style="form",
                    explode=True,
                ),
                "updated_at_lte": oapi.client.format_argument_value(
                    "updated_at_lte",
                    updated_at_lte,
                    style="form",
                    explode=True,
                ),
                "duration_gte": oapi.client.format_argument_value(
                    "duration_gte",
                    duration_gte,
                    style="form",
                    explode=True,
                ),
                "duration_lte": oapi.client.format_argument_value(
                    "duration_lte",
                    duration_lte,
                    style="form",
                    explode=True,
                ),
                "state": oapi.client.format_argument_value(
                    "state",
                    state,
                    style="form",
                    explode=True,
                ),
                "pool": oapi.client.format_argument_value(
                    "pool",
                    pool,
                    style="form",
                    explode=True,
                ),
                "queue": oapi.client.format_argument_value(
                    "queue",
                    queue,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceCollection,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
    ) -> model.TaskInstance:
        """
        Get a task instance

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstance,
            )
        )

    def patch_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id(
        self,
        update_task_instance: model.UpdateTaskInstance,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
    ) -> model.TaskInstanceReference:
        """
        Updates the state for single task instance.
        *New in version 2.5.0*

        Parameters:

        - update_task_instance
        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=update_task_instance,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceReference,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_map_index(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
    ) -> model.TaskInstance:
        """
        Get details of a mapped task instance.

        *New in version 2.3.0*

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - map_index:
          The map index.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
                "map_index": str(oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstance,
            )
        )

    def patch_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_map_index(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        update_task_instance: typing.Optional[
            model.UpdateTaskInstance
        ] = None,
    ) -> model.TaskInstanceReference:
        """
        Updates the state for single mapped task instance.
        *New in version 2.5.0*

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - map_index:
          The map index.
        - update_task_instance
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
                "map_index": str(oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            json=update_task_instance,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceReference,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_list_mapped(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        execution_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        execution_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        start_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_gte: typing.Optional[
            datetime.datetime
        ] = None,
        end_date_lte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_gte: typing.Optional[
            datetime.datetime
        ] = None,
        updated_at_lte: typing.Optional[
            datetime.datetime
        ] = None,
        duration_gte: typing.Union[
            int,
            float,
            decimal.Decimal,
            None
        ] = None,
        duration_lte: typing.Union[
            int,
            float,
            decimal.Decimal,
            None
        ] = None,
        state: typing.Optional[
            model.FilterState
        ] = None,
        pool: typing.Optional[
            model.FilterPool
        ] = None,
        queue: typing.Optional[
            model.FilterQueue
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.TaskInstanceCollection:
        """
        Get details of all mapped task instances.

        *New in version 2.3.0*

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - execution_date_gte:
          Returns objects greater or equal to the specified date.
          This can be combined with execution_date_lte parameter to receive
          only the selected period.
        - execution_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with execution_date_gte parameter to receive
          only the selected period.
        - start_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - start_date_lte:
          Returns objects less or equal the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - end_date_gte:
          Returns objects greater or equal the specified date.
          This can be combined with start_date_lte parameter to receive only
          the selected period.
        - end_date_lte:
          Returns objects less than or equal to the specified date.
          This can be combined with start_date_gte parameter to receive only
          the selected period.
        - updated_at_gte:
          Returns objects greater or equal the specified date.
          This can be combined with updated_at_lte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - updated_at_lte:
          Returns objects less or equal the specified date.
          This can be combined with updated_at_gte parameter to receive only
          the selected period.
          *New in version 2.6.0*
        - duration_gte:
          Returns objects greater than or equal to the specified values.
          This can be combined with duration_lte parameter to receive only the
          selected period.
        - duration_lte:
          Returns objects less than or equal to the specified values.
          This can be combined with duration_gte parameter to receive only the
          selected range.
        - state:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - pool:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - queue:
          The value can be repeated to retrieve multiple matching values (OR
          condition).
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "execution_date_gte": oapi.client.format_argument_value(
                    "execution_date_gte",
                    execution_date_gte,
                    style="form",
                    explode=True,
                ),
                "execution_date_lte": oapi.client.format_argument_value(
                    "execution_date_lte",
                    execution_date_lte,
                    style="form",
                    explode=True,
                ),
                "start_date_gte": oapi.client.format_argument_value(
                    "start_date_gte",
                    start_date_gte,
                    style="form",
                    explode=True,
                ),
                "start_date_lte": oapi.client.format_argument_value(
                    "start_date_lte",
                    start_date_lte,
                    style="form",
                    explode=True,
                ),
                "end_date_gte": oapi.client.format_argument_value(
                    "end_date_gte",
                    end_date_gte,
                    style="form",
                    explode=True,
                ),
                "end_date_lte": oapi.client.format_argument_value(
                    "end_date_lte",
                    end_date_lte,
                    style="form",
                    explode=True,
                ),
                "updated_at_gte": oapi.client.format_argument_value(
                    "updated_at_gte",
                    updated_at_gte,
                    style="form",
                    explode=True,
                ),
                "updated_at_lte": oapi.client.format_argument_value(
                    "updated_at_lte",
                    updated_at_lte,
                    style="form",
                    explode=True,
                ),
                "duration_gte": oapi.client.format_argument_value(
                    "duration_gte",
                    duration_gte,
                    style="form",
                    explode=True,
                ),
                "duration_lte": oapi.client.format_argument_value(
                    "duration_lte",
                    duration_lte,
                    style="form",
                    explode=True,
                ),
                "state": oapi.client.format_argument_value(
                    "state",
                    state,
                    style="form",
                    explode=True,
                ),
                "pool": oapi.client.format_argument_value(
                    "pool",
                    pool,
                    style="form",
                    explode=True,
                ),
                "queue": oapi.client.format_argument_value(
                    "queue",
                    queue,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceCollection,
            )
        )

    def post_dags_dag_runs_task_instances_list(
        self,
        list_task_instance_form: model.ListTaskInstanceForm,
    ) -> model.TaskInstanceCollection:
        """
        List task instances from all DAGs and DAG runs.
        This endpoint is a POST to allow filtering across a large number of DAG
        IDs, where as a GET it would run in to maximum HTTP request URL length
        limits.

        Parameters:

        - list_task_instance_form
        """
        response: sob.abc.Readable = self.request(
            "/dags/~/dagRuns/~/taskInstances/list",
            method="POST",
            json=list_task_instance_form,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskInstanceCollection,
            )
        )

    def get_variables(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.VariableCollection:
        """
        The collection does not contain data. To get data, you must get a
        single entity.

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/variables",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.VariableCollection,
            )
        )

    def post_variables(
        self,
        variable: model.Variable,
    ) -> model.Variable:
        """
        Create a variable

        Parameters:

        - variable:
          Full representation of Variable
        """
        response: sob.abc.Readable = self.request(
            "/variables",
            method="POST",
            json=variable,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Variable,
            )
        )

    def get_variables_variable_key(
        self,
        variable_key: str,
    ) -> model.Variable:
        """
        Get a variable by key.

        Parameters:

        - variable_key:
          The variable Key.
        """
        response: sob.abc.Readable = self.request(
            "/variables/{variable_key}".format(**{
                "variable_key": str(oapi.client.format_argument_value(
                    "variable_key",
                    variable_key,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Variable,
            )
        )

    def delete_variables_variable_key(
        self,
        variable_key: str,
    ) -> None:
        """
        Delete a variable

        Parameters:

        - variable_key:
          The variable Key.
        """
        self.request(
            "/variables/{variable_key}".format(**{
                "variable_key": str(oapi.client.format_argument_value(
                    "variable_key",
                    variable_key,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_variables_variable_key(
        self,
        variable: model.Variable,
        variable_key: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.Variable:
        """
        Update a variable by key.

        Parameters:

        - variable:
          Full representation of Variable
        - variable_key:
          The variable Key.
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/variables/{variable_key}".format(**{
                "variable_key": str(oapi.client.format_argument_value(
                    "variable_key",
                    variable_key,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=variable,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Variable,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_xcom_entries(  # noqa
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        map_index: typing.Optional[
            int
        ] = None,
        xcom_key: typing.Optional[
            str
        ] = None,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
    ) -> model.XComCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id
        to retrieve XCOM entries for for all DAGs, DAG runs and task instances.
        XCom values won't be returned as they can be large. Use this endpoint
        to get a list of XCom entries and then fetch individual entry to get
        value.

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - map_index:
          Filter on map index for mapped task.
        - xcom_key:
          Only filter the XCom records which have the provided key.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "map_index": oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="form",
                    explode=True,
                ),
                "xcom_key": oapi.client.format_argument_value(
                    "xcom_key",
                    xcom_key,
                    style="form",
                    explode=True,
                ),
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.XComCollection,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_xcom_entries_xcom_key(  # noqa
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        xcom_key: str,
        *,
        map_index: typing.Optional[
            int
        ] = None,
        deserialize: typing.Optional[
            bool
        ] = None,
    ) -> model.XCom:
        """
        Get an XCom entry

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - xcom_key:
          The XCom key.
        - map_index:
          Filter on map index for mapped task.
        - deserialize:
          Whether to deserialize an XCom value when using a custom XCom
          backend.
          The XCom API endpoint calls `orm_deserialize_value` by default since
          an XCom may contain value
          that is potentially expensive to deserialize in the web server.
          Setting this to true overrides
          the consideration, and calls `deserialize_value` instead.
          This parameter is not meaningful when using the default XCom backend.
          *New in version 2.4.0*
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
                "xcom_key": str(oapi.client.format_argument_value(
                    "xcom_key",
                    xcom_key,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "map_index": oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="form",
                    explode=True,
                ),
                "deserialize": oapi.client.format_argument_value(
                    "deserialize",
                    deserialize,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.XCom,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_links(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
    ) -> model.ExtraLinkCollection:
        """
        List extra links for task instance.

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ExtraLinkCollection,
            )
        )

    def get_dags_dag_id_dag_runs_dag_run_id_task_instances_task_id_logs_task_try_number(  # noqa
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        task_try_number: int,
        *,
        full_content: typing.Optional[
            bool
        ] = None,
        map_index: typing.Optional[
            int
        ] = None,
        token: typing.Optional[
            str
        ] = None,
    ) -> typing.Union[
        model.DagsDagIdDagRunsDagRunIdTaskInstancesTaskIdLogsTaskTryNumberGetResponse,  # noqa
        str
    ]:
        """
        Get logs for a specific task instance and its try number.
        To get log from specific character position, following way of using
        URLSafeSerializer can be used.

        Example:
        ```
        from itsdangerous.url_safe import URLSafeSerializer

        request_url = f"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{
        TASK_ID}/logs/1"
        key = app.config["SECRET_KEY"]
        serializer = URLSafeSerializer(key)
        token = serializer.dumps({"log_pos": 10000})

        response = self.client.get(
            request_url,
            query_string={"token": token},
            headers={"Accept": "text/plain"},
            environ_overrides={"REMOTE_USER": "test"},
        )
        continuation_token = response.json["continuation_token"]
            metadata = URLSafeSerializer(key).loads(continuation_token)
            log_pos = metadata["log_pos"]
            end_of_log = metadata["end_of_log"]
        ```
        If log_pos is passed as 10000 like the above example, it renders the
        logs starting
        from char position 10000 to last (not the end as the logs may be
        tailing behind in
        running state). This way pagination can be done with metadata as part
        of the token.

        Parameters:

        - dag_id:
          The DAG ID.
        - dag_run_id:
          The DAG run ID.
        - task_id:
          The task ID.
        - task_try_number:
          The task try number.
        - full_content:
          A full content will be returned.
          By default, only the first fragment will be returned.
        - map_index:
          Filter on map index for mapped task.
        - token:
          A token that allows you to continue fetching logs.
          If passed, it will specify the location from which the download
          should be continued.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number}".format(**{  # noqa
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "dag_run_id": str(oapi.client.format_argument_value(
                    "dag_run_id",
                    dag_run_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
                "task_try_number": str(oapi.client.format_argument_value(
                    "task_try_number",
                    task_try_number,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "full_content": oapi.client.format_argument_value(
                    "full_content",
                    full_content,
                    style="form",
                    explode=True,
                ),
                "map_index": oapi.client.format_argument_value(
                    "map_index",
                    map_index,
                    style="form",
                    explode=True,
                ),
                "token": oapi.client.format_argument_value(
                    "token",
                    token,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DagsDagIdDagRunsDagRunIdTaskInstancesTaskIdLogsTaskTryNumberGetResponse,  # noqa
                sob.properties.String(),
            )
        )

    def get_dags_dag_id_details(
        self,
        dag_id: str,
    ) -> model.DAGDetail:
        """
        The response contains many DAG attributes, so the response can be
        large. If possible, consider using GET /dags/{dag_id}.

        Parameters:

        - dag_id:
          The DAG ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/details".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DAGDetail,
            )
        )

    def get_dags_dag_id_tasks(
        self,
        dag_id: str,
        *,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.TaskCollection:
        """
        Get tasks for DAG

        Parameters:

        - dag_id:
          The DAG ID.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/tasks".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
            query={
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.TaskCollection,
            )
        )

    def get_dags_dag_id_tasks_task_id(
        self,
        dag_id: str,
        task_id: str,
    ) -> model.Task:
        """
        Get simplified representation of a task

        Parameters:

        - dag_id:
          The DAG ID.
        - task_id:
          The task ID.
        """
        response: sob.abc.Readable = self.request(
            "/dags/{dag_id}/tasks/{task_id}".format(**{
                "dag_id": str(oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="simple",
                    explode=False,
                )),
                "task_id": str(oapi.client.format_argument_value(
                    "task_id",
                    task_id,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Task,
            )
        )

    def get_dag_sources_file_token(
        self,
        file_token: str,
    ) -> typing.Union[
        model.DagSourcesFileTokenGetResponse,
        str
    ]:
        """
        Get a source code using file token.

        Parameters:

        - file_token:
          The key containing the encrypted path to the file. Encryption and
          decryption take place only on
          the server. This prevents the client from reading an non-DAG file.
          This also ensures API
          extensibility, because the format of encrypted data may change.
        """
        response: sob.abc.Readable = self.request(
            "/dagSources/{file_token}".format(**{
                "file_token": str(oapi.client.format_argument_value(
                    "file_token",
                    file_token,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DagSourcesFileTokenGetResponse,
                sob.properties.String(),
            )
        )

    def get_dag_warnings(
        self,
        *,
        dag_id: typing.Optional[
            str
        ] = None,
        warning_type: typing.Optional[
            str
        ] = None,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.DagWarningCollection:
        """
        List dag warnings

        Parameters:

        - dag_id:
          If set, only return DAG warnings with this dag_id.
        - warning_type:
          If set, only return DAG warnings with this type.
        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/dagWarnings",
            method="GET",
            query={
                "dag_id": oapi.client.format_argument_value(
                    "dag_id",
                    dag_id,
                    style="form",
                    explode=True,
                ),
                "warning_type": oapi.client.format_argument_value(
                    "warning_type",
                    warning_type,
                    style="form",
                    explode=True,
                ),
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DagWarningCollection,
            )
        )

    def get_datasets(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
        uri_pattern: typing.Optional[
            str
        ] = None,
    ) -> model.DatasetCollection:
        """
        List datasets

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        - uri_pattern:
          If set, only return datasets with uris matching this pattern.
        """
        response: sob.abc.Readable = self.request(
            "/datasets",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
                "uri_pattern": oapi.client.format_argument_value(
                    "uri_pattern",
                    uri_pattern,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DatasetCollection,
            )
        )

    def get_datasets_uri(
        self,
        uri: str,
    ) -> model.Dataset:
        """
        Get a dataset by uri.

        Parameters:

        - uri:
          The encoded Dataset URI
        """
        response: sob.abc.Readable = self.request(
            "/datasets/{uri}".format(**{
                "uri": str(oapi.client.format_argument_value(
                    "uri",
                    uri,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Dataset,
            )
        )

    def get_datasets_events(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
        dataset_id: typing.Optional[
            int
        ] = None,
        source_dag_id: typing.Optional[
            str
        ] = None,
        source_task_id: typing.Optional[
            str
        ] = None,
        source_run_id: typing.Optional[
            str
        ] = None,
        source_map_index: typing.Optional[
            int
        ] = None,
    ) -> model.DatasetEventCollection:
        """
        Get dataset events

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        - dataset_id:
          The Dataset ID that updated the dataset.
        - source_dag_id:
          The DAG ID that updated the dataset.
        - source_task_id:
          The task ID that updated the dataset.
        - source_run_id:
          The DAG run ID that updated the dataset.
        - source_map_index:
          The map index that updated the dataset.
        """
        response: sob.abc.Readable = self.request(
            "/datasets/events",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
                "dataset_id": oapi.client.format_argument_value(
                    "dataset_id",
                    dataset_id,
                    style="form",
                    explode=True,
                ),
                "source_dag_id": oapi.client.format_argument_value(
                    "source_dag_id",
                    source_dag_id,
                    style="form",
                    explode=True,
                ),
                "source_task_id": oapi.client.format_argument_value(
                    "source_task_id",
                    source_task_id,
                    style="form",
                    explode=True,
                ),
                "source_run_id": oapi.client.format_argument_value(
                    "source_run_id",
                    source_run_id,
                    style="form",
                    explode=True,
                ),
                "source_map_index": oapi.client.format_argument_value(
                    "source_map_index",
                    source_map_index,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.DatasetEventCollection,
            )
        )

    def get_config(
        self,
        *,
        section: typing.Optional[
            str
        ] = None,
    ) -> typing.Union[
        model.Config,
        str
    ]:
        """
        Get current configuration

        Parameters:

        - section:
          If given, only return config of this section.
        """
        response: sob.abc.Readable = self.request(
            "/config",
            method="GET",
            query={
                "section": oapi.client.format_argument_value(
                    "section",
                    section,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Config,
                sob.properties.String(),
            )
        )

    def get_config_section_section_option_option(
        self,
        section: str,
        option: str,
    ) -> typing.Union[
        model.Config,
        str
    ]:
        """
        Get a option from configuration

        Parameters:

        - section
        - option
        """
        response: sob.abc.Readable = self.request(
            "/config/section/{section}/option/{option}".format(**{
                "section": str(oapi.client.format_argument_value(
                    "section",
                    section,
                    style="simple",
                    explode=False,
                )),
                "option": str(oapi.client.format_argument_value(
                    "option",
                    option,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Config,
                sob.properties.String(),
            )
        )

    def get_health(
        self,
    ) -> model.HealthInfo:
        """
        Get the status of Airflow's metadatabase, triggerer and scheduler. It
        includes info about
        metadatabase and last heartbeat of scheduler and triggerer.
        """
        response: sob.abc.Readable = self.request(
            "/health",
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.HealthInfo,
            )
        )

    def get_version(
        self,
    ) -> model.VersionInfo:
        """
        Get version information
        """
        response: sob.abc.Readable = self.request(
            "/version",
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.VersionInfo,
            )
        )

    def get_plugins(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
    ) -> model.PluginCollection:
        """
        Get a list of loaded plugins.

        *New in version 2.1.0*

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        """
        response: sob.abc.Readable = self.request(
            "/plugins",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.PluginCollection,
            )
        )

    def get_roles(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.RoleCollection:
        """
        Get a list of roles.

        *New in version 2.1.0*

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/roles",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.RoleCollection,
            )
        )

    def post_roles(
        self,
        role: model.Role,
    ) -> model.Role:
        """
        Create a new role.

        *New in version 2.1.0*

        Parameters:

        - role:
          a role item.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/roles",
            method="POST",
            json=role,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Role,
            )
        )

    def get_roles_role_name(
        self,
        role_name: str,
    ) -> model.Role:
        """
        Get a role.

        *New in version 2.1.0*

        Parameters:

        - role_name:
          The role name
        """
        response: sob.abc.Readable = self.request(
            "/roles/{role_name}".format(**{
                "role_name": str(oapi.client.format_argument_value(
                    "role_name",
                    role_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Role,
            )
        )

    def delete_roles_role_name(
        self,
        role_name: str,
    ) -> None:
        """
        Delete a role.

        *New in version 2.1.0*

        Parameters:

        - role_name:
          The role name
        """
        self.request(
            "/roles/{role_name}".format(**{
                "role_name": str(oapi.client.format_argument_value(
                    "role_name",
                    role_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_roles_role_name(
        self,
        role: model.Role,
        role_name: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.Role:
        """
        Update a role.

        *New in version 2.1.0*

        Parameters:

        - role:
          a role item.
          *New in version 2.1.0*
        - role_name:
          The role name
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/roles/{role_name}".format(**{
                "role_name": str(oapi.client.format_argument_value(
                    "role_name",
                    role_name,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=role,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.Role,
            )
        )

    def get_permissions(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
    ) -> model.ActionCollection:
        """
        Get a list of permissions.

        *New in version 2.1.0*

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        """
        response: sob.abc.Readable = self.request(
            "/permissions",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.ActionCollection,
            )
        )

    def get_users(
        self,
        *,
        limit: typing.Optional[
            int
        ] = None,
        offset: typing.Optional[
            int
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
    ) -> model.UserCollection:
        """
        Get a list of users.

        *New in version 2.1.0*

        Parameters:

        - limit:
          The numbers of items to return.
        - offset:
          The number of items to skip before starting to collect the result
          set.
        - order_by:
          The name of the field to order the results by.
          Prefix a field name with `-` to reverse the sort order.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/users",
            method="GET",
            query={
                "limit": oapi.client.format_argument_value(
                    "limit",
                    limit,
                    style="form",
                    explode=True,
                ),
                "offset": oapi.client.format_argument_value(
                    "offset",
                    offset,
                    style="form",
                    explode=True,
                ),
                "order_by": oapi.client.format_argument_value(
                    "order_by",
                    order_by,
                    style="form",
                    explode=True,
                ),
            },
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.UserCollection,
            )
        )

    def post_users(
        self,
        user: model.User,
    ) -> model.User:
        """
        Create a new user with unique username and email.

        *New in version 2.2.0*

        Parameters:

        - user:
          A user object with sensitive data.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/users",
            method="POST",
            json=user,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.User,
            )
        )

    def get_users_username(
        self,
        username: str,
    ) -> model.UserCollectionItem:
        """
        Get a user with a specific username.

        *New in version 2.1.0*

        Parameters:

        - username:
          The username of the user.
          *New in version 2.1.0*
        """
        response: sob.abc.Readable = self.request(
            "/users/{username}".format(**{
                "username": str(oapi.client.format_argument_value(
                    "username",
                    username,
                    style="simple",
                    explode=False,
                )),
            }),
            method="GET",
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.UserCollectionItem,
            )
        )

    def delete_users_username(
        self,
        username: str,
    ) -> None:
        """
        Delete a user with a specific username.

        *New in version 2.2.0*

        Parameters:

        - username:
          The username of the user.
          *New in version 2.1.0*
        """
        self.request(
            "/users/{username}".format(**{
                "username": str(oapi.client.format_argument_value(
                    "username",
                    username,
                    style="simple",
                    explode=False,
                )),
            }),
            method="DELETE",
        )

    def patch_users_username(
        self,
        user: model.User,
        username: str,
        *,
        update_mask: typing.Optional[
            model.UpdateMask
        ] = None,
    ) -> model.UserCollectionItem:
        """
        Update fields for a user.

        *New in version 2.2.0*

        Parameters:

        - user:
          A user object with sensitive data.
          *New in version 2.1.0*
        - username:
          The username of the user.
          *New in version 2.1.0*
        - update_mask:
          The fields to update on the resource. If absent or empty, all
          modifiable fields are updated.
          A comma-separated list of fully qualified names of fields.
        """
        response: sob.abc.Readable = self.request(
            "/users/{username}".format(**{
                "username": str(oapi.client.format_argument_value(
                    "username",
                    username,
                    style="simple",
                    explode=False,
                )),
            }),
            method="PATCH",
            query={
                "update_mask": oapi.client.format_argument_value(
                    "update_mask",
                    update_mask,
                    style="form",
                    explode=False,
                ),
            },
            json=user,
        )
        return sob.model.unmarshal(  # type: ignore
            sob.model.deserialize(response),
            types=(
                model.UserCollectionItem,
            )
        )
