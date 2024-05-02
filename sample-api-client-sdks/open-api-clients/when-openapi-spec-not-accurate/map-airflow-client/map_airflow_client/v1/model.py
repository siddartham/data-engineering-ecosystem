import datetime
import decimal
import typing
import sob


class FilterPool(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class FilterQueue(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class FilterState(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class FilterTags(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class UpdateMask(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Action(sob.model.Object):
    """
    An action Item.

    *New in version 2.1.0*

    Properties:

    - name:
      The name of the permission "action"
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.name = name
        super().__init__(_data)


class ActionCollection(sob.model.Object):
    """
    A collection of actions.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        actions: typing.Optional[
            "ActionCollectionActions"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.actions = actions
        self.total_entries = total_entries
        super().__init__(_data)


class ActionCollectionActions(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Action"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ActionResource(sob.model.Object):
    """
    The Action-Resource item.

    *New in version 2.1.0*

    Properties:

    - action:
      An action Item.
      *New in version 2.1.0*
    - resource:
      A resource on which permissions are granted.
      *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        action: typing.Optional[
            "Action"
        ] = None,
        resource: typing.Optional[
            "Resource"
        ] = None
    ) -> None:
        self.action = action
        self.resource = resource
        super().__init__(_data)


class BasicDAGRun(sob.model.Object):
    """
    Properties:

    - run_id:
      Run ID.
    - dag_id
    - logical_date:
      The logical date (previously called execution date). This is the time or
      interval covered by
      this DAG run, according to the DAG definition.
      The value of this field can be set only when creating the object. If you
      try to modify the
      field of an existing object, the request fails with an BAD_REQUEST error.
      This together with DAG_ID are a unique key.
      *New in version 2.2.0*
    - start_date:
      The start time. The time when DAG run was actually created.
      *Changed in version 2.1.3*&#58; Field becomes nullable.
    - end_date
    - data_interval_start
    - data_interval_end
    - state:
      DAG State.
      *Changed in version 2.1.3*&#58; 'queued' is added as a possible value.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        run_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        logical_date: typing.Optional[
            datetime.datetime
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        data_interval_start: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        data_interval_end: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        state: typing.Optional[
            str
        ] = None
    ) -> None:
        self.run_id = run_id
        self.dag_id = dag_id
        self.logical_date = logical_date
        self.start_date = start_date
        self.end_date = end_date
        self.data_interval_start = data_interval_start
        self.data_interval_end = data_interval_end
        self.state = state
        super().__init__(_data)


class ClassReference(sob.model.Object):
    """
    Class reference

    Properties:

    - module_path
    - class_name
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        module_path: typing.Optional[
            str
        ] = None,
        class_name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.module_path = module_path
        self.class_name = class_name
        super().__init__(_data)


class ClearDagRun(sob.model.Object):
    """
    Properties:

    - dry_run:
      If set, don't actually run this operation. The response will contain a
      list of task instances
      planned to be cleaned, but not modified in any way.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dry_run: typing.Optional[
            bool
        ] = None
    ) -> None:
        self.dry_run = dry_run
        super().__init__(_data)


class ClearTaskInstances(sob.model.Object):
    """
    Properties:

    - dry_run:
      If set, don't actually run this operation. The response will contain a
      list of task instances
      planned to be cleaned, but not modified in any way.
    - task_ids:
      A list of task ids to clear.
      *New in version 2.1.0*
    - start_date:
      The minimum execution date to clear.
    - end_date:
      The maximum execution date to clear.
    - only_failed:
      Only clear failed tasks.
    - only_running:
      Only clear running tasks.
    - include_subdags:
      Clear tasks in subdags and clear external tasks indicated by
      ExternalTaskMarker.
    - include_parentdag:
      Clear tasks in the parent dag of the subdag.
    - reset_dag_runs:
      Set state of DAG runs to RUNNING.
    - dag_run_id:
      The DagRun ID for this task instance
    - include_upstream:
      If set to true, upstream tasks are also affected.
    - include_downstream:
      If set to true, downstream tasks are also affected.
    - include_future:
      If set to True, also tasks from future DAG Runs are affected.
    - include_past:
      If set to True, also tasks from past DAG Runs are affected.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dry_run: typing.Optional[
            bool
        ] = None,
        task_ids: typing.Optional[
            "ClearTaskInstancesTaskIds"
        ] = None,
        start_date: typing.Optional[
            str
        ] = None,
        end_date: typing.Optional[
            str
        ] = None,
        only_failed: typing.Optional[
            bool
        ] = None,
        only_running: typing.Optional[
            bool
        ] = None,
        include_subdags: typing.Optional[
            bool
        ] = None,
        include_parentdag: typing.Optional[
            bool
        ] = None,
        reset_dag_runs: typing.Optional[
            bool
        ] = None,
        dag_run_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        include_upstream: typing.Optional[
            bool
        ] = None,
        include_downstream: typing.Optional[
            bool
        ] = None,
        include_future: typing.Optional[
            bool
        ] = None,
        include_past: typing.Optional[
            bool
        ] = None
    ) -> None:
        self.dry_run = dry_run
        self.task_ids = task_ids
        self.start_date = start_date
        self.end_date = end_date
        self.only_failed = only_failed
        self.only_running = only_running
        self.include_subdags = include_subdags
        self.include_parentdag = include_parentdag
        self.reset_dag_runs = reset_dag_runs
        self.dag_run_id = dag_run_id
        self.include_upstream = include_upstream
        self.include_downstream = include_downstream
        self.include_future = include_future
        self.include_past = include_past
        super().__init__(_data)


class ClearTaskInstancesTaskIds(sob.model.Array):
    """
    A list of task ids to clear.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class CollectionInfo(sob.model.Object):
    """
    Metadata about collection.

    Properties:

    - total_entries:
      Count of total objects in the current result set before pagination
      parameters
      (limit, offset) are applied.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.total_entries = total_entries
        super().__init__(_data)


class Config(sob.model.Object):
    """
    The configuration.

    Properties:

    - sections
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sections: typing.Optional[
            "ConfigSections"
        ] = None
    ) -> None:
        self.sections = sections
        super().__init__(_data)


class ConfigSections(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ConfigSection"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ConfigOption(sob.model.Object):
    """
    The option of configuration.

    Properties:

    - key
    - value
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        key: typing.Optional[
            str
        ] = None,
        value: typing.Optional[
            str
        ] = None
    ) -> None:
        self.key = key
        self.value = value
        super().__init__(_data)


class ConfigSection(sob.model.Object):
    """
    The section of configuration.

    Properties:

    - name
    - options
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        options: typing.Optional[
            "ConfigOptions"
        ] = None
    ) -> None:
        self.name = name
        self.options = options
        super().__init__(_data)


class ConfigOptions(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ConfigOption"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Connection(sob.model.Object):
    """
    Full representation of the connection.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        connection_id: typing.Optional[
            str
        ] = None,
        conn_type: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        host: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        login: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        schema: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        port: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        password: typing.Optional[
            str
        ] = None,
        extra: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.connection_id = connection_id
        self.conn_type = conn_type
        self.description = description
        self.host = host
        self.login = login
        self.schema = schema
        self.port = port
        self.password = password
        self.extra = extra
        super().__init__(_data)


class ConnectionCollection(sob.model.Object):
    """
    Collection of connections.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        connections: typing.Optional[
            "ConnectionCollectionConnections"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.connections = connections
        self.total_entries = total_entries
        super().__init__(_data)


class ConnectionCollectionConnections(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ConnectionCollectionItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ConnectionCollectionItem(sob.model.Object):
    """
    Connection collection item.
    The password and extra fields are only available when retrieving a single
    object due to the sensitivity of this data.

    Properties:

    - connection_id:
      The connection ID.
    - conn_type:
      The connection type.
    - description:
      The description of the connection.
    - host:
      Host of the connection.
    - login:
      Login of the connection.
    - schema:
      Schema of the connection.
    - port:
      Port of the connection.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        connection_id: typing.Optional[
            str
        ] = None,
        conn_type: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        host: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        login: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        schema: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        port: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.connection_id = connection_id
        self.conn_type = conn_type
        self.description = description
        self.host = host
        self.login = login
        self.schema = schema
        self.port = port
        super().__init__(_data)


class ConnectionTest(sob.model.Object):
    """
    Connection test results.

    *New in version 2.2.0*

    Properties:

    - status:
      The status of the request.
    - message:
      The success or failure message of the request.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        status: typing.Optional[
            bool
        ] = None,
        message: typing.Optional[
            str
        ] = None
    ) -> None:
        self.status = status
        self.message = message
        super().__init__(_data)


class CronExpression(sob.model.Object):
    """
    Cron expression

    Properties:

    - type
    - value
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        type: typing.Optional[
            str
        ] = None,
        value: typing.Optional[
            str
        ] = None
    ) -> None:
        self.type = type
        self.value = value
        super().__init__(_data)


class DAG(sob.model.Object):
    """
    DAG

    Properties:

    - dag_id:
      The ID of the DAG.
    - root_dag_id:
      If the DAG is SubDAG then it is the top level DAG identifier. Otherwise,
      null.
    - is_paused:
      Whether the DAG is paused.
    - is_active:
      Whether the DAG is currently seen by the scheduler(s).
      *New in version 2.1.1*
      *Changed in version 2.2.0*&#58; Field is read-only.
    - is_subdag:
      Whether the DAG is SubDAG.
    - last_parsed_time:
      The last time the DAG was parsed.
      *New in version 2.3.0*
    - last_pickled:
      The last time the DAG was pickled.
      *New in version 2.3.0*
    - last_expired:
      Time when the DAG last received a refresh signal
      (e.g. the DAG's "refresh" button was clicked in the web UI)
      *New in version 2.3.0*
    - scheduler_lock:
      Whether (one of) the scheduler is scheduling this DAG at the moment
      *New in version 2.3.0*
    - pickle_id:
      Foreign key to the latest pickle_id
      *New in version 2.3.0*
    - default_view:
      Default view of the DAG inside the webserver
      *New in version 2.3.0*
    - fileloc:
      The absolute path to the file.
    - file_token:
      The key containing the encrypted path to the file. Encryption and
      decryption take place only on the server. This prevents the client from
      reading an non-DAG file. This also ensures API extensibility, because the
      format of encrypted data may change.
    - owners
    - description:
      User-provided DAG description, which can consist of several sentences or
      paragraphs that describe DAG contents.
    - schedule_interval:
      Schedule interval. Defines how often DAG runs, this object gets added to
      your latest task instance's
      execution_date to figure out the next schedule.
    - timetable_description:
      Timetable/Schedule Interval description.
      *New in version 2.3.0*
    - tags:
      List of tags.
    - max_active_tasks:
      Maximum number of active tasks that can be run on the DAG
      *New in version 2.3.0*
    - max_active_runs:
      Maximum number of active DAG runs for the DAG
      *New in version 2.3.0*
    - has_task_concurrency_limits:
      Whether the DAG has task concurrency limits
      *New in version 2.3.0*
    - has_import_errors:
      Whether the DAG has import errors
      *New in version 2.3.0*
    - next_dagrun:
      The logical date of the next dag run.
      *New in version 2.3.0*
    - next_dagrun_data_interval_start:
      The start of the interval of the next dag run.
      *New in version 2.3.0*
    - next_dagrun_data_interval_end:
      The end of the interval of the next dag run.
      *New in version 2.3.0*
    - next_dagrun_create_after:
      Earliest time at which this ``next_dagrun`` can be created.
      *New in version 2.3.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        root_dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        is_paused: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        is_active: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        is_subdag: typing.Optional[
            bool
        ] = None,
        last_parsed_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        last_pickled: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        last_expired: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        scheduler_lock: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        pickle_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        default_view: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        fileloc: typing.Optional[
            str
        ] = None,
        file_token: typing.Optional[
            str
        ] = None,
        owners: typing.Optional[
            "Owners"
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        schedule_interval: typing.Optional[
            typing.Union[
                "TimeDelta",
                sob.utilities.types.Null,
                "RelativeDelta",
                "CronExpression"
            ]
        ] = None,
        timetable_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        tags: typing.Optional[
            typing.Union[
                "Tags",
                sob.utilities.types.Null
            ]
        ] = None,
        max_active_tasks: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        max_active_runs: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        has_task_concurrency_limits: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        has_import_errors: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_data_interval_start: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_data_interval_end: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_create_after: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.root_dag_id = root_dag_id
        self.is_paused = is_paused
        self.is_active = is_active
        self.is_subdag = is_subdag
        self.last_parsed_time = last_parsed_time
        self.last_pickled = last_pickled
        self.last_expired = last_expired
        self.scheduler_lock = scheduler_lock
        self.pickle_id = pickle_id
        self.default_view = default_view
        self.fileloc = fileloc
        self.file_token = file_token
        self.owners = owners
        self.description = description
        self.schedule_interval = schedule_interval
        self.timetable_description = timetable_description
        self.tags = tags
        self.max_active_tasks = max_active_tasks
        self.max_active_runs = max_active_runs
        self.has_task_concurrency_limits = has_task_concurrency_limits
        self.has_import_errors = has_import_errors
        self.next_dagrun = next_dagrun
        self.next_dagrun_data_interval_start = next_dagrun_data_interval_start
        self.next_dagrun_data_interval_end = next_dagrun_data_interval_end
        self.next_dagrun_create_after = next_dagrun_create_after
        super().__init__(_data)


class Owners(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Tags(sob.model.Array):
    """
    List of tags.
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Tag"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DAGCollection(sob.model.Object):
    """
    Collection of DAGs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dags: typing.Optional[
            "DAGCollectionDags"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.dags = dags
        self.total_entries = total_entries
        super().__init__(_data)


class DAGCollectionDags(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DAG"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DAGDetail(sob.model.Object):
    """
    DAG details.

    For details see:
    [airflow.models.dag.DAG](https://airflow.apache.org/docs/apache-airflow/
    stable/_api/airflow/models/dag/index.html#airflow.models.dag.DAG)
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        root_dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        is_paused: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        is_active: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        is_subdag: typing.Optional[
            bool
        ] = None,
        last_parsed_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        last_pickled: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        last_expired: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        scheduler_lock: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        pickle_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        default_view: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null,
                str
            ]
        ] = None,
        fileloc: typing.Optional[
            str
        ] = None,
        file_token: typing.Optional[
            str
        ] = None,
        owners: typing.Optional[
            "Owners"
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        schedule_interval: typing.Optional[
            typing.Union[
                "TimeDelta",
                sob.utilities.types.Null,
                "RelativeDelta",
                "CronExpression"
            ]
        ] = None,
        timetable_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        tags: typing.Optional[
            typing.Union[
                "Tags",
                sob.utilities.types.Null
            ]
        ] = None,
        max_active_tasks: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        max_active_runs: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        has_task_concurrency_limits: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        has_import_errors: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_data_interval_start: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_data_interval_end: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        next_dagrun_create_after: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        timezone: typing.Optional[
            str
        ] = None,
        catchup: typing.Optional[
            bool
        ] = None,
        orientation: typing.Optional[
            str
        ] = None,
        concurrency: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        dag_run_timeout: typing.Optional[
            typing.Union[
                "TimeDelta",
                sob.utilities.types.Null
            ]
        ] = None,
        doc_md: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        params: typing.Optional[
            sob.model.Dictionary
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        is_paused_upon_creation: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        last_parsed: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        template_search_path: typing.Optional[
            typing.Union[
                "DAGDetailTemplateSearchPath",
                sob.utilities.types.Null
            ]
        ] = None,
        render_template_as_native_obj: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.root_dag_id = root_dag_id
        self.is_paused = is_paused
        self.is_active = is_active
        self.is_subdag = is_subdag
        self.last_parsed_time = last_parsed_time
        self.last_pickled = last_pickled
        self.last_expired = last_expired
        self.scheduler_lock = scheduler_lock
        self.pickle_id = pickle_id
        self.default_view = default_view
        self.fileloc = fileloc
        self.file_token = file_token
        self.owners = owners
        self.description = description
        self.schedule_interval = schedule_interval
        self.timetable_description = timetable_description
        self.tags = tags
        self.max_active_tasks = max_active_tasks
        self.max_active_runs = max_active_runs
        self.has_task_concurrency_limits = has_task_concurrency_limits
        self.has_import_errors = has_import_errors
        self.next_dagrun = next_dagrun
        self.next_dagrun_data_interval_start = next_dagrun_data_interval_start
        self.next_dagrun_data_interval_end = next_dagrun_data_interval_end
        self.next_dagrun_create_after = next_dagrun_create_after
        self.timezone = timezone
        self.catchup = catchup
        self.orientation = orientation
        self.concurrency = concurrency
        self.start_date = start_date
        self.dag_run_timeout = dag_run_timeout
        self.doc_md = doc_md
        self.params = params
        self.end_date = end_date
        self.is_paused_upon_creation = is_paused_upon_creation
        self.last_parsed = last_parsed
        self.template_search_path = template_search_path
        self.render_template_as_native_obj = render_template_as_native_obj
        super().__init__(_data)


class DAGDetailTemplateSearchPath(sob.model.Array):
    """
    The template search path.

    *New in version 2.3.0*
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DAGRun(sob.model.Object):
    """
    Properties:

    - dag_run_id:
      Run ID.
      The value of this field can be set only when creating the object. If you
      try to modify the
      field of an existing object, the request fails with an BAD_REQUEST error.
      If not provided, a value will be generated based on execution_date.
      If the specified dag_run_id is in use, the creation request fails with an
      ALREADY_EXISTS error.
      This together with DAG_ID are a unique key.
    - dag_id
    - logical_date:
      The logical date (previously called execution date). This is the time or
      interval covered by
      this DAG run, according to the DAG definition.
      The value of this field can be set only when creating the object. If you
      try to modify the
      field of an existing object, the request fails with an BAD_REQUEST error.
      This together with DAG_ID are a unique key.
      *New in version 2.2.0*
    - execution_date:
      The execution date. This is the same as logical_date, kept for backwards
      compatibility.
      If both this field and logical_date are provided but with different
      values, the request
      will fail with an BAD_REQUEST error.
      *Changed in version 2.2.0*&#58; Field becomes nullable.
      *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.
    - start_date:
      The start time. The time when DAG run was actually created.
      *Changed in version 2.1.3*&#58; Field becomes nullable.
    - end_date
    - data_interval_start
    - data_interval_end
    - last_scheduling_decision
    - run_type
    - state:
      DAG State.
      *Changed in version 2.1.3*&#58; 'queued' is added as a possible value.
    - external_trigger
    - conf:
      JSON object describing additional configuration parameters.
      The value of this field can be set only when creating the object. If you
      try to modify the
      field of an existing object, the request fails with an BAD_REQUEST error.
    - note:
      Contains manually entered notes by the user about the DagRun.
      *New in version 2.5.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_run_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        logical_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        execution_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        data_interval_start: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        data_interval_end: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        last_scheduling_decision: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        run_type: typing.Optional[
            str
        ] = None,
        state: typing.Optional[
            str
        ] = None,
        external_trigger: typing.Optional[
            bool
        ] = None,
        conf: typing.Optional[
            sob.model.Dictionary
        ] = None,
        note: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.dag_run_id = dag_run_id
        self.dag_id = dag_id
        self.logical_date = logical_date
        self.execution_date = execution_date
        self.start_date = start_date
        self.end_date = end_date
        self.data_interval_start = data_interval_start
        self.data_interval_end = data_interval_end
        self.last_scheduling_decision = last_scheduling_decision
        self.run_type = run_type
        self.state = state
        self.external_trigger = external_trigger
        self.conf = conf
        self.note = note
        super().__init__(_data)


class DAGRunCollection(sob.model.Object):
    """
    Collection of DAG runs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_runs: typing.Optional[
            "DAGRunCollectionDagRuns"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.dag_runs = dag_runs
        self.total_entries = total_entries
        super().__init__(_data)


class DAGRunCollectionDagRuns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DAGRun"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DagProcessorStatus(sob.model.Object):
    """
    The status and the latest dag processor heartbeat.

    *New in version 2.6.3*

    Properties:

    - status:
      Health status
    - latest_dag_processor_heartbeat:
      The time the dag processor last did a heartbeat.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        latest_dag_processor_heartbeat: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.status = status
        self.latest_dag_processor_heartbeat = latest_dag_processor_heartbeat
        super().__init__(_data)


class DagScheduleDatasetReference(sob.model.Object):
    """
    A datasets reference to a downstream DAG.

    *New in version 2.4.0*

    Properties:

    - dag_id:
      The DAG ID that depends on the dataset.
    - created_at:
      The dataset reference creation time
    - updated_at:
      The dataset reference update time
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        created_at: typing.Optional[
            str
        ] = None,
        updated_at: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__(_data)


class DagWarning(sob.model.Object):
    """
    Properties:

    - dag_id:
      The dag_id.
    - warning_type:
      The warning type for the dag warning.
    - message:
      The message for the dag warning.
    - timestamp:
      The time when this warning was logged.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        warning_type: typing.Optional[
            str
        ] = None,
        message: typing.Optional[
            str
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.warning_type = warning_type
        self.message = message
        self.timestamp = timestamp
        super().__init__(_data)


class DagWarningCollection(sob.model.Object):
    """
    Collection of DAG warnings.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        import_errors: typing.Optional[
            "DagWarningCollectionImportErrors"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.import_errors = import_errors
        self.total_entries = total_entries
        super().__init__(_data)


class DagWarningCollectionImportErrors(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DagWarning"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Dataset(sob.model.Object):
    """
    A dataset item.

    *New in version 2.4.0*

    Properties:

    - id_:
      The dataset id
    - uri:
      The dataset uri
    - extra:
      The dataset extra
    - created_at:
      The dataset creation time
    - updated_at:
      The dataset update time
    - consuming_dags
    - producing_tasks
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        id_: typing.Optional[
            int
        ] = None,
        uri: typing.Optional[
            str
        ] = None,
        extra: typing.Optional[
            typing.Union[
                sob.model.Dictionary,
                sob.utilities.types.Null
            ]
        ] = None,
        created_at: typing.Optional[
            str
        ] = None,
        updated_at: typing.Optional[
            str
        ] = None,
        consuming_dags: typing.Optional[
            "DatasetConsumingDags"
        ] = None,
        producing_tasks: typing.Optional[
            "DatasetProducingTasks"
        ] = None
    ) -> None:
        self.id_ = id_
        self.uri = uri
        self.extra = extra
        self.created_at = created_at
        self.updated_at = updated_at
        self.consuming_dags = consuming_dags
        self.producing_tasks = producing_tasks
        super().__init__(_data)


class DatasetConsumingDags(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DagScheduleDatasetReference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DatasetProducingTasks(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TaskOutletDatasetReference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DatasetCollection(sob.model.Object):
    """
    A collection of datasets.

    *New in version 2.4.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        datasets: typing.Optional[
            "DatasetCollectionDatasets"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.datasets = datasets
        self.total_entries = total_entries
        super().__init__(_data)


class DatasetCollectionDatasets(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Dataset"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DatasetEvent(sob.model.Object):
    """
    A dataset event.

    *New in version 2.4.0*

    Properties:

    - dataset_id:
      The dataset id
    - dataset_uri:
      The URI of the dataset
    - extra:
      The dataset event extra
    - source_dag_id:
      The DAG ID that updated the dataset.
    - source_task_id:
      The task ID that updated the dataset.
    - source_run_id:
      The DAG run ID that updated the dataset.
    - source_map_index:
      The task map index that updated the dataset.
    - created_dagruns
    - timestamp:
      The dataset event creation time
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dataset_id: typing.Optional[
            int
        ] = None,
        dataset_uri: typing.Optional[
            str
        ] = None,
        extra: typing.Optional[
            typing.Union[
                sob.model.Dictionary,
                sob.utilities.types.Null
            ]
        ] = None,
        source_dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        source_task_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        source_run_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        source_map_index: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        created_dagruns: typing.Optional[
            "DatasetEventCreatedDagruns"
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dataset_id = dataset_id
        self.dataset_uri = dataset_uri
        self.extra = extra
        self.source_dag_id = source_dag_id
        self.source_task_id = source_task_id
        self.source_run_id = source_run_id
        self.source_map_index = source_map_index
        self.created_dagruns = created_dagruns
        self.timestamp = timestamp
        super().__init__(_data)


class DatasetEventCreatedDagruns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BasicDAGRun"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DatasetEventCollection(sob.model.Object):
    """
    A collection of dataset events.

    *New in version 2.4.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dataset_events: typing.Optional[
            "DatasetEventCollectionDatasetEvents"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.dataset_events = dataset_events
        self.total_entries = total_entries
        super().__init__(_data)


class DatasetEventCollectionDatasetEvents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DatasetEvent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Error(sob.model.Object):
    """
    [RFC7807](https://tools.ietf.org/html/rfc7807) compliant response.

    Properties:

    - type_:
      A URI reference [RFC3986] that identifies the problem type. This
      specification
      encourages that, when dereferenced, it provide human-readable
      documentation for
      the problem type.
    - title:
      A short, human-readable summary of the problem type.
    - status:
      The HTTP status code generated by the API server for this occurrence of
      the problem.
    - detail:
      A human-readable explanation specific to this occurrence of the problem.
    - instance:
      A URI reference that identifies the specific occurrence of the problem.
      It may or may
      not yield further information if dereferenced.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        type_: typing.Optional[
            str
        ] = None,
        title: typing.Optional[
            str
        ] = None,
        status: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        detail: typing.Optional[
            str
        ] = None,
        instance: typing.Optional[
            str
        ] = None
    ) -> None:
        self.type_ = type_
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance
        super().__init__(_data)


class EventLog(sob.model.Object):
    """
    Log of user operations via CLI or Web UI.

    Properties:

    - event_log_id:
      The event log ID
    - when:
      The time when these events happened.
    - dag_id:
      The DAG ID
    - task_id:
      The DAG ID
    - event:
      A key describing the type of event.
    - execution_date:
      When the event was dispatched for an object having execution_date, the
      value of this field.
    - owner:
      Name of the user who triggered these events a.
    - extra:
      Other information that was not included in the other fields, e.g. the
      complete CLI command.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        event_log_id: typing.Optional[
            int
        ] = None,
        when: typing.Optional[
            datetime.datetime
        ] = None,
        dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        task_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        event: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        owner: typing.Optional[
            str
        ] = None,
        extra: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.event_log_id = event_log_id
        self.when = when
        self.dag_id = dag_id
        self.task_id = task_id
        self.event = event
        self.execution_date = execution_date
        self.owner = owner
        self.extra = extra
        super().__init__(_data)


class EventLogCollection(sob.model.Object):
    """
    Collection of event logs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        event_logs: typing.Optional[
            "EventLogCollectionEventLogs_"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.event_logs = event_logs
        self.total_entries = total_entries
        super().__init__(_data)


class EventLogCollectionEventLogs_(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "EventLog"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ExtraLink(sob.model.Object):
    """
    Additional links containing additional information about the task.

    Properties:

    - class_ref:
      Class reference
    - name
    - href
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        class_ref: typing.Optional[
            "ClassReference"
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        href: typing.Optional[
            str
        ] = None
    ) -> None:
        self.class_ref = class_ref
        self.name = name
        self.href = href
        super().__init__(_data)


class ExtraLinkCollection(sob.model.Object):
    """
    The collection of extra links.

    Properties:

    - extra_links
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        extra_links: typing.Optional[
            "ExtraLinks"
        ] = None
    ) -> None:
        self.extra_links = extra_links
        super().__init__(_data)


class ExtraLinks(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ExtraLink"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class HealthInfo(sob.model.Object):
    """
    Instance status information.

    Properties:

    - metadatabase:
      The status of the metadatabase.
    - scheduler:
      The status and the latest scheduler heartbeat.
    - triggerer:
      The status and the latest triggerer heartbeat.
      *New in version 2.6.2*
    - dag_processor:
      The status and the latest dag processor heartbeat.
      *New in version 2.6.3*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        metadatabase: typing.Optional[
            "MetadatabaseStatus"
        ] = None,
        scheduler: typing.Optional[
            "SchedulerStatus"
        ] = None,
        triggerer: typing.Optional[
            "TriggererStatus"
        ] = None,
        dag_processor: typing.Optional[
            "DagProcessorStatus"
        ] = None
    ) -> None:
        self.metadatabase = metadatabase
        self.scheduler = scheduler
        self.triggerer = triggerer
        self.dag_processor = dag_processor
        super().__init__(_data)


class ImportError(sob.model.Object):
    """
    Properties:

    - import_error_id:
      The import error ID.
    - timestamp:
      The time when this error was created.
    - filename:
      The filename
    - stack_trace:
      The full stackstrace..
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        import_error_id: typing.Optional[
            int
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None,
        filename: typing.Optional[
            str
        ] = None,
        stack_trace: typing.Optional[
            str
        ] = None
    ) -> None:
        self.import_error_id = import_error_id
        self.timestamp = timestamp
        self.filename = filename
        self.stack_trace = stack_trace
        super().__init__(_data)


class ImportErrorCollection(sob.model.Object):
    """
    Collection of import errors.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        import_errors: typing.Optional[
            "ImportErrorCollectionImportErrors_"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.import_errors = import_errors
        self.total_entries = total_entries
        super().__init__(_data)


class ImportErrorCollectionImportErrors_(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ImportError"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Job(sob.model.Object):
    """
    Properties:

    - id_
    - dag_id
    - state
    - job_type
    - start_date
    - end_date
    - latest_heartbeat
    - executor_class
    - hostname
    - unixname
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        id_: typing.Optional[
            int
        ] = None,
        dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        state: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        job_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        latest_heartbeat: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        executor_class: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        hostname: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        unixname: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.id_ = id_
        self.dag_id = dag_id
        self.state = state
        self.job_type = job_type
        self.start_date = start_date
        self.end_date = end_date
        self.latest_heartbeat = latest_heartbeat
        self.executor_class = executor_class
        self.hostname = hostname
        self.unixname = unixname
        super().__init__(_data)


class ListDagRunsForm(sob.model.Object):
    """
    Properties:

    - order_by:
      The name of the field to order the results by. Prefix a field name
      with `-` to reverse the sort order.
      *New in version 2.1.0*
    - page_offset:
      The number of items to skip before starting to collect the result set.
    - page_limit:
      The numbers of items to return.
    - dag_ids:
      Return objects with specific DAG IDs.
      The value can be repeated to retrieve multiple matching values (OR
      condition).
    - states:
      Return objects with specific states.
      The value can be repeated to retrieve multiple matching values (OR
      condition).
    - execution_date_gte:
      Returns objects greater or equal to the specified date.
      This can be combined with execution_date_lte key to receive only the
      selected period.
    - execution_date_lte:
      Returns objects less than or equal to the specified date.
      This can be combined with execution_date_gte key to receive only the
      selected period.
    - start_date_gte:
      Returns objects greater or equal the specified date.
      This can be combined with start_date_lte key to receive only the selected
      period.
    - start_date_lte:
      Returns objects less or equal the specified date.
      This can be combined with start_date_gte parameter to receive only the
      selected period
    - end_date_gte:
      Returns objects greater or equal the specified date.
      This can be combined with end_date_lte parameter to receive only the
      selected period.
    - end_date_lte:
      Returns objects less than or equal to the specified date.
      This can be combined with end_date_gte parameter to receive only the
      selected period.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        order_by: typing.Optional[
            str
        ] = None,
        page_offset: typing.Optional[
            int
        ] = None,
        page_limit: typing.Optional[
            int
        ] = None,
        dag_ids: typing.Optional[
            "ListDagRunsFormDagIds"
        ] = None,
        states: typing.Optional[
            "ListDagRunsFormStates"
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
        ] = None
    ) -> None:
        self.order_by = order_by
        self.page_offset = page_offset
        self.page_limit = page_limit
        self.dag_ids = dag_ids
        self.states = states
        self.execution_date_gte = execution_date_gte
        self.execution_date_lte = execution_date_lte
        self.start_date_gte = start_date_gte
        self.start_date_lte = start_date_lte
        self.end_date_gte = end_date_gte
        self.end_date_lte = end_date_lte
        super().__init__(_data)


class ListDagRunsFormDagIds(sob.model.Array):
    """
    Return objects with specific DAG IDs.
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListDagRunsFormStates(sob.model.Array):
    """
    Return objects with specific states.
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceForm(sob.model.Object):
    """
    Properties:

    - dag_ids:
      Return objects with specific DAG IDs.
      The value can be repeated to retrieve multiple matching values (OR
      condition).
    - dag_run_ids:
      Return objects with specific DAG Run IDs.
      The value can be repeated to retrieve multiple matching values (OR
      condition).
      *New in version 2.7.1*
    - task_ids:
      Return objects with specific task IDs.
      The value can be repeated to retrieve multiple matching values (OR
      condition).
      *New in version 2.7.1*
    - execution_date_gte:
      Returns objects greater or equal to the specified date.
      This can be combined with execution_date_lte parameter to receive only
      the selected period.
    - execution_date_lte:
      Returns objects less than or equal to the specified date.
      This can be combined with execution_date_gte parameter to receive only
      the selected period.
    - start_date_gte:
      Returns objects greater or equal the specified date.
      This can be combined with start_date_lte parameter to receive only the
      selected period.
    - start_date_lte:
      Returns objects less or equal the specified date.
      This can be combined with start_date_gte parameter to receive only the
      selected period.
    - end_date_gte:
      Returns objects greater or equal the specified date.
      This can be combined with start_date_lte parameter to receive only the
      selected period.
    - end_date_lte:
      Returns objects less than or equal to the specified date.
      This can be combined with start_date_gte parameter to receive only the
      selected period.
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

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_ids: typing.Optional[
            "ListTaskInstanceFormDagIds"
        ] = None,
        dag_run_ids: typing.Optional[
            "ListTaskInstanceFormDagRunIds"
        ] = None,
        task_ids: typing.Optional[
            "ListTaskInstanceFormTaskIds"
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
        duration_gte: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        duration_lte: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        state: typing.Optional[
            "ListTaskInstanceFormState"
        ] = None,
        pool: typing.Optional[
            "ListTaskInstanceFormPool"
        ] = None,
        queue: typing.Optional[
            "ListTaskInstanceFormQueue"
        ] = None
    ) -> None:
        self.dag_ids = dag_ids
        self.dag_run_ids = dag_run_ids
        self.task_ids = task_ids
        self.execution_date_gte = execution_date_gte
        self.execution_date_lte = execution_date_lte
        self.start_date_gte = start_date_gte
        self.start_date_lte = start_date_lte
        self.end_date_gte = end_date_gte
        self.end_date_lte = end_date_lte
        self.duration_gte = duration_gte
        self.duration_lte = duration_lte
        self.state = state
        self.pool = pool
        self.queue = queue
        super().__init__(_data)


class ListTaskInstanceFormDagIds(sob.model.Array):
    """
    Return objects with specific DAG IDs.
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceFormDagRunIds(sob.model.Array):
    """
    Return objects with specific DAG Run IDs.
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    *New in version 2.7.1*
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceFormPool(sob.model.Array):
    """
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceFormQueue(sob.model.Array):
    """
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceFormState(sob.model.Array):
    """
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ListTaskInstanceFormTaskIds(sob.model.Array):
    """
    Return objects with specific task IDs.
    The value can be repeated to retrieve multiple matching values (OR
    condition).
    *New in version 2.7.1*
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MetadatabaseStatus(sob.model.Object):
    """
    The status of the metadatabase.

    Properties:

    - status:
      Health status
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.status = status
        super().__init__(_data)


class PluginCollection(sob.model.Object):
    """
    A collection of plugin.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        plugins: typing.Optional[
            "PluginCollectionPlugins"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.plugins = plugins
        self.total_entries = total_entries
        super().__init__(_data)


class PluginCollectionPlugins(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PluginCollectionItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItem(sob.model.Object):
    """
    A plugin Item.

    *New in version 2.1.0*

    Properties:

    - name:
      The name of the plugin
    - hooks:
      The plugin hooks
    - executors:
      The plugin executors
    - macros:
      The plugin macros
    - flask_blueprints:
      The flask blueprints
    - appbuilder_views:
      The appuilder views
    - appbuilder_menu_items:
      The Flask Appbuilder menu items
    - global_operator_extra_links:
      The global operator extra links
    - operator_extra_links:
      Operator extra links
    - source:
      The plugin source
    - ti_deps:
      The plugin task instance dependencies
    - listeners:
      The plugin listeners
    - timetables:
      The plugin timetables
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        hooks: typing.Optional[
            "PluginCollectionItemHooks"
        ] = None,
        executors: typing.Optional[
            "PluginCollectionItemExecutors"
        ] = None,
        macros: typing.Optional[
            "PluginCollectionItemMacros"
        ] = None,
        flask_blueprints: typing.Optional[
            "PluginCollectionItemFlaskBlueprints"
        ] = None,
        appbuilder_views: typing.Optional[
            "PluginCollectionItemAppbuilderViews"
        ] = None,
        appbuilder_menu_items: typing.Optional[
            "PluginCollectionItemAppbuilderMenuItems"
        ] = None,
        global_operator_extra_links: typing.Optional[
            "PluginCollectionItemGlobalOperatorExtraLinks"
        ] = None,
        operator_extra_links: typing.Optional[
            "PluginCollectionItemOperatorExtraLinks"
        ] = None,
        source: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        ti_deps: typing.Optional[
            "PluginCollectionItemTiDeps"
        ] = None,
        listeners: typing.Optional[
            "PluginCollectionItemListeners"
        ] = None,
        timetables: typing.Optional[
            "PluginCollectionItemTimetables"
        ] = None
    ) -> None:
        self.name = name
        self.hooks = hooks
        self.executors = executors
        self.macros = macros
        self.flask_blueprints = flask_blueprints
        self.appbuilder_views = appbuilder_views
        self.appbuilder_menu_items = appbuilder_menu_items
        self.global_operator_extra_links = global_operator_extra_links
        self.operator_extra_links = operator_extra_links
        self.source = source
        self.ti_deps = ti_deps
        self.listeners = listeners
        self.timetables = timetables
        super().__init__(_data)


class PluginCollectionItemAppbuilderMenuItems(sob.model.Array):
    """
    The Flask Appbuilder menu items
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                sob.model.Dictionary
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemAppbuilderViews(sob.model.Array):
    """
    The appuilder views
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                sob.model.Dictionary
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemExecutors(sob.model.Array):
    """
    The plugin executors
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemFlaskBlueprints(sob.model.Array):
    """
    The flask blueprints
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemGlobalOperatorExtraLinks(sob.model.Array):
    """
    The global operator extra links
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemHooks(sob.model.Array):
    """
    The plugin hooks
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemListeners(sob.model.Array):
    """
    The plugin listeners
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemMacros(sob.model.Array):
    """
    The plugin macros
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemOperatorExtraLinks(sob.model.Array):
    """
    Operator extra links
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    str,
                    sob.utilities.types.Null
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemTiDeps(sob.model.Array):
    """
    The plugin task instance dependencies
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PluginCollectionItemTimetables(sob.model.Array):
    """
    The plugin timetables
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Pool(sob.model.Object):
    """
    The pool

    Properties:

    - name:
      The name of pool.
    - slots:
      The maximum number of slots that can be assigned to tasks. One job may
      occupy one or more slots.
    - occupied_slots:
      The number of slots used by running/queued tasks at the moment. May
      include deferred tasks if 'include_deferred' is set to true.
    - running_slots:
      The number of slots used by running tasks at the moment.
    - queued_slots:
      The number of slots used by queued tasks at the moment.
    - open_slots:
      The number of free slots at the moment.
    - scheduled_slots:
      The number of slots used by scheduled tasks at the moment.
    - deferred_slots:
      The number of slots used by deferred tasks at the moment. Relevant if '
      include_deferred' is set to true.
      *New in version 2.7.0*
    - description:
      The description of the pool.
      *New in version 2.3.0*
    - include_deferred:
      If set to true, deferred tasks are considered when calculating open pool
      slots.
      *New in version 2.7.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        slots: typing.Optional[
            int
        ] = None,
        occupied_slots: typing.Optional[
            int
        ] = None,
        running_slots: typing.Optional[
            int
        ] = None,
        queued_slots: typing.Optional[
            int
        ] = None,
        open_slots: typing.Optional[
            int
        ] = None,
        scheduled_slots: typing.Optional[
            int
        ] = None,
        deferred_slots: typing.Optional[
            int
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        include_deferred: typing.Optional[
            bool
        ] = None
    ) -> None:
        self.name = name
        self.slots = slots
        self.occupied_slots = occupied_slots
        self.running_slots = running_slots
        self.queued_slots = queued_slots
        self.open_slots = open_slots
        self.scheduled_slots = scheduled_slots
        self.deferred_slots = deferred_slots
        self.description = description
        self.include_deferred = include_deferred
        super().__init__(_data)


class PoolCollection(sob.model.Object):
    """
    Collection of pools.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        pools: typing.Optional[
            "PoolCollectionPools_"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.pools = pools
        self.total_entries = total_entries
        super().__init__(_data)


class PoolCollectionPools_(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Pool"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Provider(sob.model.Object):
    """
    The provider

    *New in version 2.1.0*

    Properties:

    - package_name:
      The package name of the provider.
    - description:
      The description of the provider.
    - version:
      The version of the provider.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        package_name: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            str
        ] = None,
        version: typing.Optional[
            str
        ] = None
    ) -> None:
        self.package_name = package_name
        self.description = description
        self.version = version
        super().__init__(_data)


class ProviderCollection(sob.model.Object):
    """
    Collection of providers.

    *New in version 2.1.0*

    Properties:

    - providers
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        providers: typing.Optional[
            "ProviderCollectionProviders"
        ] = None
    ) -> None:
        self.providers = providers
        super().__init__(_data)


class ProviderCollectionProviders(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Provider"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class RelativeDelta(sob.model.Object):
    """
    Relative delta

    Properties:

    - type
    - years
    - months
    - days
    - leapdays
    - hours
    - minutes
    - seconds
    - microseconds
    - year
    - month
    - day
    - hour
    - minute
    - second
    - microsecond
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        type: typing.Optional[
            str
        ] = None,
        years: typing.Optional[
            int
        ] = None,
        months: typing.Optional[
            int
        ] = None,
        days: typing.Optional[
            int
        ] = None,
        leapdays: typing.Optional[
            int
        ] = None,
        hours: typing.Optional[
            int
        ] = None,
        minutes: typing.Optional[
            int
        ] = None,
        seconds: typing.Optional[
            int
        ] = None,
        microseconds: typing.Optional[
            int
        ] = None,
        year: typing.Optional[
            int
        ] = None,
        month: typing.Optional[
            int
        ] = None,
        day: typing.Optional[
            int
        ] = None,
        hour: typing.Optional[
            int
        ] = None,
        minute: typing.Optional[
            int
        ] = None,
        second: typing.Optional[
            int
        ] = None,
        microsecond: typing.Optional[
            int
        ] = None
    ) -> None:
        self.type = type
        self.years = years
        self.months = months
        self.days = days
        self.leapdays = leapdays
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        super().__init__(_data)


class Resource(sob.model.Object):
    """
    A resource on which permissions are granted.

    *New in version 2.1.0*

    Properties:

    - name:
      The name of the resource
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.name = name
        super().__init__(_data)


class Role(sob.model.Object):
    """
    a role item.

    *New in version 2.1.0*

    Properties:

    - name:
      The name of the role
      *Changed in version 2.3.0*&#58; A minimum character length requirement ('
      minLength') is added.
    - actions
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        actions: typing.Optional[
            "RoleActions"
        ] = None
    ) -> None:
        self.name = name
        self.actions = actions
        super().__init__(_data)


class RoleActions(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ActionResource"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class RoleCollection(sob.model.Object):
    """
    A collection of roles.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        roles: typing.Optional[
            "RoleCollectionRoles"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.roles = roles
        self.total_entries = total_entries
        super().__init__(_data)


class RoleCollectionRoles(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Role"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SLAMiss(sob.model.Object):
    """
    Properties:

    - task_id:
      The task ID.
    - dag_id:
      The DAG ID.
    - execution_date
    - email_sent
    - timestamp
    - description
    - notification_sent
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        email_sent: typing.Optional[
            bool
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        notification_sent: typing.Optional[
            bool
        ] = None
    ) -> None:
        self.task_id = task_id
        self.dag_id = dag_id
        self.execution_date = execution_date
        self.email_sent = email_sent
        self.timestamp = timestamp
        self.description = description
        self.notification_sent = notification_sent
        super().__init__(_data)


class SchedulerStatus(sob.model.Object):
    """
    The status and the latest scheduler heartbeat.

    Properties:

    - status:
      Health status
    - latest_scheduler_heartbeat:
      The time the scheduler last did a heartbeat.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        latest_scheduler_heartbeat: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.status = status
        self.latest_scheduler_heartbeat = latest_scheduler_heartbeat
        super().__init__(_data)


class SetDagRunNote(sob.model.Object):
    """
    Properties:

    - note:
      Custom notes left by users for this Dag Run.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        note: typing.Optional[
            str
        ] = None
    ) -> None:
        self.note = note
        super().__init__(_data)


class SetTaskInstanceNote(sob.model.Object):
    """
    Properties:

    - note:
      The custom note to set for this Task Instance.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        note: typing.Optional[
            str
        ] = None
    ) -> None:
        self.note = note
        super().__init__(_data)


class Tag(sob.model.Object):
    """
    Tag

    Properties:

    - name
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.name = name
        super().__init__(_data)


class Task(sob.model.Object):
    """
    For details see:
    [airflow.models.baseoperator.BaseOperator](https://airflow.apache.org/docs/
    apache-airflow/stable/_api/airflow/models/baseoperator/index.html#airflow.
    models.baseoperator.BaseOperator)

    Properties:

    - class_ref:
      Class reference
    - task_id
    - owner
    - start_date
    - end_date
    - trigger_rule:
      Trigger rule.
      *Changed in version 2.2.0*&#58; 'none_failed_min_one_success' is added as
      a possible value. Deprecated 'dummy' and 'always' is added as a possible
      value
      *Changed in version 2.3.0*&#58; 'all_skipped' is added as a possible
      value.
      *Changed in version 2.5.0*&#58; 'one_done' is added as a possible value.
      *Changed in version 2.7.0*&#58; 'all_done_setup_success' is added as a
      possible value.
    - extra_links
    - depends_on_past
    - is_mapped
    - wait_for_downstream
    - retries
    - queue
    - pool
    - pool_slots
    - execution_timeout:
      Time delta
    - retry_delay:
      Time delta
    - retry_exponential_backoff
    - priority_weight
    - weight_rule:
      Weight rule.
    - ui_color:
      Color in hexadecimal notation.
    - ui_fgcolor:
      Color in hexadecimal notation.
    - template_fields
    - sub_dag:
      DAG
    - downstream_task_ids
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        class_ref: typing.Optional[
            "ClassReference"
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        owner: typing.Optional[
            str
        ] = None,
        start_date: typing.Optional[
            datetime.datetime
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        trigger_rule: typing.Optional[
            str
        ] = None,
        extra_links: typing.Optional[
            "TaskExtraLinks"
        ] = None,
        depends_on_past: typing.Optional[
            bool
        ] = None,
        is_mapped: typing.Optional[
            bool
        ] = None,
        wait_for_downstream: typing.Optional[
            bool
        ] = None,
        retries: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        queue: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pool: typing.Optional[
            str
        ] = None,
        pool_slots: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        execution_timeout: typing.Optional[
            typing.Union[
                "TimeDelta",
                sob.utilities.types.Null
            ]
        ] = None,
        retry_delay: typing.Optional[
            typing.Union[
                "TimeDelta",
                sob.utilities.types.Null
            ]
        ] = None,
        retry_exponential_backoff: typing.Optional[
            bool
        ] = None,
        priority_weight: typing.Optional[
            typing.Union[
                float,
                int,
                decimal.Decimal
            ]
        ] = None,
        weight_rule: typing.Optional[
            str
        ] = None,
        ui_color: typing.Optional[
            str
        ] = None,
        ui_fgcolor: typing.Optional[
            str
        ] = None,
        template_fields: typing.Optional[
            "TemplateField"
        ] = None,
        sub_dag: typing.Optional[
            "DAG"
        ] = None,
        downstream_task_ids: typing.Optional[
            "DownstreamTaskIds"
        ] = None
    ) -> None:
        self.class_ref = class_ref
        self.task_id = task_id
        self.owner = owner
        self.start_date = start_date
        self.end_date = end_date
        self.trigger_rule = trigger_rule
        self.extra_links = extra_links
        self.depends_on_past = depends_on_past
        self.is_mapped = is_mapped
        self.wait_for_downstream = wait_for_downstream
        self.retries = retries
        self.queue = queue
        self.pool = pool
        self.pool_slots = pool_slots
        self.execution_timeout = execution_timeout
        self.retry_delay = retry_delay
        self.retry_exponential_backoff = retry_exponential_backoff
        self.priority_weight = priority_weight
        self.weight_rule = weight_rule
        self.ui_color = ui_color
        self.ui_fgcolor = ui_fgcolor
        self.template_fields = template_fields
        self.sub_dag = sub_dag
        self.downstream_task_ids = downstream_task_ids
        super().__init__(_data)


class DownstreamTaskIds(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskExtraLinks(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TaskExtraLinksItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskExtraLinksItem(sob.model.Object):
    """
    Properties:

    - class_ref:
      Class reference
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        class_ref: typing.Optional[
            "ClassReference"
        ] = None
    ) -> None:
        self.class_ref = class_ref
        super().__init__(_data)


class TemplateField(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                str
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskCollection(sob.model.Object):
    """
    Collection of tasks.

    Properties:

    - tasks
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        tasks: typing.Optional[
            "Tasks"
        ] = None
    ) -> None:
        self.tasks = tasks
        super().__init__(_data)


class Tasks(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Task"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskInstance(sob.model.Object):
    """
    Properties:

    - task_id
    - dag_id
    - dag_run_id:
      The DagRun ID for this task instance
      *New in version 2.3.0*
    - execution_date
    - start_date
    - end_date
    - duration
    - state:
      Task state.
      *Changed in version 2.0.2*&#58; 'removed' is added as a possible value.
      *Changed in version 2.2.0*&#58; 'deferred' is added as a possible value.
      *Changed in version 2.4.0*&#58; 'sensing' state has been removed.
      *Changed in version 2.4.2*&#58; 'restarting' is added as a possible value
      *Changed in version 2.7.0*&#58; Field becomes nullable and null primitive
      is added as a possible value.
      *Changed in version 2.7.0*&#58; 'none' state is deprecated in favor of
      null.
    - try_number
    - map_index
    - max_tries
    - hostname
    - unixname
    - pool
    - pool_slots
    - queue
    - priority_weight
    - operator:
      *Changed in version 2.1.1*&#58; Field becomes nullable.
    - queued_when
    - pid
    - executor_config
    - sla_miss
    - rendered_fields:
      JSON object describing rendered fields.
      *New in version 2.3.0*
    - trigger
    - triggerer_job
    - note:
      Contains manually entered notes by the user about the TaskInstance.
      *New in version 2.5.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        dag_run_id: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        end_date: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        duration: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        state: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        try_number: typing.Optional[
            int
        ] = None,
        map_index: typing.Optional[
            int
        ] = None,
        max_tries: typing.Optional[
            int
        ] = None,
        hostname: typing.Optional[
            str
        ] = None,
        unixname: typing.Optional[
            str
        ] = None,
        pool: typing.Optional[
            str
        ] = None,
        pool_slots: typing.Optional[
            int
        ] = None,
        queue: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        priority_weight: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        operator: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        queued_when: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pid: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        executor_config: typing.Optional[
            str
        ] = None,
        sla_miss: typing.Optional[
            typing.Union[
                "SLAMiss",
                sob.utilities.types.Null
            ]
        ] = None,
        rendered_fields: typing.Optional[
            sob.model.Dictionary
        ] = None,
        trigger: typing.Optional[
            typing.Union[
                "Trigger",
                sob.utilities.types.Null
            ]
        ] = None,
        triggerer_job: typing.Optional[
            typing.Union[
                "Job",
                sob.utilities.types.Null
            ]
        ] = None,
        note: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.task_id = task_id
        self.dag_id = dag_id
        self.dag_run_id = dag_run_id
        self.execution_date = execution_date
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
        self.state = state
        self.try_number = try_number
        self.map_index = map_index
        self.max_tries = max_tries
        self.hostname = hostname
        self.unixname = unixname
        self.pool = pool
        self.pool_slots = pool_slots
        self.queue = queue
        self.priority_weight = priority_weight
        self.operator = operator
        self.queued_when = queued_when
        self.pid = pid
        self.executor_config = executor_config
        self.sla_miss = sla_miss
        self.rendered_fields = rendered_fields
        self.trigger = trigger
        self.triggerer_job = triggerer_job
        self.note = note
        super().__init__(_data)


class TaskInstanceCollection(sob.model.Object):
    """
    Collection of task instances.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        task_instances: typing.Optional[
            "TaskInstanceCollectionTaskInstances"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.task_instances = task_instances
        self.total_entries = total_entries
        super().__init__(_data)


class TaskInstanceCollectionTaskInstances(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TaskInstance"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskInstanceReference(sob.model.Object):
    """
    Properties:

    - task_id:
      The task ID.
    - dag_id:
      The DAG ID.
    - execution_date
    - dag_run_id:
      The DAG run ID.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        dag_run_id: typing.Optional[
            str
        ] = None
    ) -> None:
        self.task_id = task_id
        self.dag_id = dag_id
        self.execution_date = execution_date
        self.dag_run_id = dag_run_id
        super().__init__(_data)


class TaskInstanceReferenceCollection(sob.model.Object):
    """
    Properties:

    - task_instances
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        task_instances: typing.Optional[
            "TaskInstances_"
        ] = None
    ) -> None:
        self.task_instances = task_instances
        super().__init__(_data)


class TaskInstances_(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TaskInstanceReference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TaskOutletDatasetReference(sob.model.Object):
    """
    A datasets reference to an upstream task.

    *New in version 2.4.0*

    Properties:

    - dag_id:
      The DAG ID that updates the dataset.
    - task_id:
      The task ID that updates the dataset.
    - created_at:
      The dataset creation time
    - updated_at:
      The dataset update time
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dag_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        task_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        created_at: typing.Optional[
            str
        ] = None,
        updated_at: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.task_id = task_id
        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__(_data)


class TimeDelta(sob.model.Object):
    """
    Time delta

    Properties:

    - type
    - days
    - seconds
    - microseconds
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        type: typing.Optional[
            str
        ] = None,
        days: typing.Optional[
            int
        ] = None,
        seconds: typing.Optional[
            int
        ] = None,
        microseconds: typing.Optional[
            int
        ] = None
    ) -> None:
        self.type = type
        self.days = days
        self.seconds = seconds
        self.microseconds = microseconds
        super().__init__(_data)


class Trigger(sob.model.Object):
    """
    Properties:

    - id_
    - classpath
    - kwargs
    - created_date
    - triggerer_id
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        id_: typing.Optional[
            int
        ] = None,
        classpath: typing.Optional[
            str
        ] = None,
        kwargs: typing.Optional[
            str
        ] = None,
        created_date: typing.Optional[
            str
        ] = None,
        triggerer_id: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.id_ = id_
        self.classpath = classpath
        self.kwargs = kwargs
        self.created_date = created_date
        self.triggerer_id = triggerer_id
        super().__init__(_data)


class TriggererStatus(sob.model.Object):
    """
    The status and the latest triggerer heartbeat.

    *New in version 2.6.2*

    Properties:

    - status:
      Health status
    - latest_triggerer_heartbeat:
      The time the triggerer last did a heartbeat.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        latest_triggerer_heartbeat: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.status = status
        self.latest_triggerer_heartbeat = latest_triggerer_heartbeat
        super().__init__(_data)


class UpdateDagRunState(sob.model.Object):
    """
    Modify the state of a DAG run.

    *New in version 2.2.0*

    Properties:

    - state:
      The state to set this DagRun
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        state: typing.Optional[
            str
        ] = None
    ) -> None:
        self.state = state
        super().__init__(_data)


class UpdateTaskInstance(sob.model.Object):
    """
    Properties:

    - dry_run:
      If set, don't actually run this operation. The response will contain the
      task instance
      planned to be affected, but won't be modified in any way.
    - new_state:
      Expected new state. Only a subset of TaskState are available.
      Other states are managed directly by the scheduler or the workers and
      cannot be updated manually through the REST API.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dry_run: typing.Optional[
            bool
        ] = None,
        new_state: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dry_run = dry_run
        self.new_state = new_state
        super().__init__(_data)


class UpdateTaskInstancesState(sob.model.Object):
    """
    Properties:

    - dry_run:
      If set, don't actually run this operation. The response will contain a
      list of task instances
      planned to be affected, but won't be modified in any way.
    - task_id:
      The task ID.
    - execution_date:
      The execution date. Either set this or dag_run_id but not both.
    - dag_run_id:
      The task instance's DAG run ID. Either set this or execution_date but not
      both.
      *New in version 2.3.0*
    - include_upstream:
      If set to true, upstream tasks are also affected.
    - include_downstream:
      If set to true, downstream tasks are also affected.
    - include_future:
      If set to True, also tasks from future DAG Runs are affected.
    - include_past:
      If set to True, also tasks from past DAG Runs are affected.
    - new_state:
      Expected new state. Only a subset of TaskState are available.
      Other states are managed directly by the scheduler or the workers and
      cannot be updated manually through the REST API.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dry_run: typing.Optional[
            bool
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        dag_run_id: typing.Optional[
            str
        ] = None,
        include_upstream: typing.Optional[
            bool
        ] = None,
        include_downstream: typing.Optional[
            bool
        ] = None,
        include_future: typing.Optional[
            bool
        ] = None,
        include_past: typing.Optional[
            bool
        ] = None,
        new_state: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dry_run = dry_run
        self.task_id = task_id
        self.execution_date = execution_date
        self.dag_run_id = dag_run_id
        self.include_upstream = include_upstream
        self.include_downstream = include_downstream
        self.include_future = include_future
        self.include_past = include_past
        self.new_state = new_state
        super().__init__(_data)


class User(sob.model.Object):
    """
    A user object with sensitive data.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        first_name: typing.Optional[
            str
        ] = None,
        last_name: typing.Optional[
            str
        ] = None,
        username: typing.Optional[
            str
        ] = None,
        email: typing.Optional[
            str
        ] = None,
        active: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        last_login: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        login_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        failed_login_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        roles: typing.Optional[
            "UserCollectionItemRoles"
        ] = None,
        created_on: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        changed_on: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        password: typing.Optional[
            str
        ] = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.active = active
        self.last_login = last_login
        self.login_count = login_count
        self.failed_login_count = failed_login_count
        self.roles = roles
        self.created_on = created_on
        self.changed_on = changed_on
        self.password = password
        super().__init__(_data)


class UserCollection(sob.model.Object):
    """
    Collection of users.

    *New in version 2.1.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        users: typing.Optional[
            "UserCollectionUsers"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.users = users
        self.total_entries = total_entries
        super().__init__(_data)


class UserCollectionUsers(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "UserCollectionItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class UserCollectionItem(sob.model.Object):
    """
    A user object.

    *New in version 2.1.0*

    Properties:

    - first_name:
      The user's first name.
      *Changed in version 2.4.0*&#58; The requirement for this to be non-empty
      was removed.
    - last_name:
      The user's last name.
      *Changed in version 2.4.0*&#58; The requirement for this to be non-empty
      was removed.
    - username:
      The username.
      *Changed in version 2.2.0*&#58; A minimum character length requirement ('
      minLength') is added.
    - email:
      The user's email.
      *Changed in version 2.2.0*&#58; A minimum character length requirement ('
      minLength') is added.
    - active:
      Whether the user is active
    - last_login:
      The last user login
    - login_count:
      The login count
    - failed_login_count:
      The number of times the login failed
    - roles:
      User roles.
      *Changed in version 2.2.0*&#58; Field is no longer read-only.
    - created_on:
      The date user was created
    - changed_on:
      The date user was changed
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        first_name: typing.Optional[
            str
        ] = None,
        last_name: typing.Optional[
            str
        ] = None,
        username: typing.Optional[
            str
        ] = None,
        email: typing.Optional[
            str
        ] = None,
        active: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        last_login: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        login_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        failed_login_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        roles: typing.Optional[
            "UserCollectionItemRoles"
        ] = None,
        created_on: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        changed_on: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.active = active
        self.last_login = last_login
        self.login_count = login_count
        self.failed_login_count = failed_login_count
        self.roles = roles
        self.created_on = created_on
        self.changed_on = changed_on
        super().__init__(_data)


class UserCollectionItemRoles(sob.model.Array):
    """
    User roles.

    *Changed in version 2.2.0*&#58; Field is no longer read-only.
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "UserCollectionItemRolesItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class UserCollectionItemRolesItem(sob.model.Object):
    """
    Properties:

    - name
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.name = name
        super().__init__(_data)


class Variable(sob.model.Object):
    """
    Full representation of Variable
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        key: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        value: typing.Optional[
            str
        ] = None
    ) -> None:
        self.key = key
        self.description = description
        self.value = value
        super().__init__(_data)


class VariableCollection(sob.model.Object):
    """
    Collection of variables.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        variables: typing.Optional[
            "VariableCollectionVariables"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.variables = variables
        self.total_entries = total_entries
        super().__init__(_data)


class VariableCollectionVariables(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "VariableCollectionItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class VariableCollectionItem(sob.model.Object):
    """
    XCom entry collection item.
    The value field are only available when retrieving a single object due to
    the sensitivity of this data.

    Properties:

    - key
    - description:
      The description of the variable.
      *New in version 2.4.0*
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        key: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.key = key
        self.description = description
        super().__init__(_data)


class VersionInfo(sob.model.Object):
    """
    Version information.

    Properties:

    - version:
      The version of Airflow
    - git_version:
      The git version (including git commit hash)
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        version: typing.Optional[
            str
        ] = None,
        git_version: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.version = version
        self.git_version = git_version
        super().__init__(_data)


class XCom(sob.model.Object):
    """
    Full representations of XCom entry.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        key: typing.Optional[
            str
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        map_index: typing.Optional[
            int
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None,
        value: typing.Optional[
            str
        ] = None
    ) -> None:
        self.key = key
        self.timestamp = timestamp
        self.execution_date = execution_date
        self.map_index = map_index
        self.task_id = task_id
        self.dag_id = dag_id
        self.value = value
        super().__init__(_data)


class XComCollection(sob.model.Object):
    """
    Collection of XCom entries.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        xcom_entries: typing.Optional[
            "XComCollectionXcomEntries"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.xcom_entries = xcom_entries
        self.total_entries = total_entries
        super().__init__(_data)


class XComCollectionXcomEntries(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "XComCollectionItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class XComCollectionItem(sob.model.Object):
    """
    XCom entry collection item.

    The value field is only available when reading a single object due to the
    size of the value.

    Properties:

    - key
    - timestamp
    - execution_date
    - map_index
    - task_id
    - dag_id
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        key: typing.Optional[
            str
        ] = None,
        timestamp: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            str
        ] = None,
        map_index: typing.Optional[
            int
        ] = None,
        task_id: typing.Optional[
            str
        ] = None,
        dag_id: typing.Optional[
            str
        ] = None
    ) -> None:
        self.key = key
        self.timestamp = timestamp
        self.execution_date = execution_date
        self.map_index = map_index
        self.task_id = task_id
        self.dag_id = dag_id
        super().__init__(_data)


class DagSourcesFileTokenGetResponse(sob.model.Object):
    """
    Properties:

    - content
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        content: typing.Optional[
            str
        ] = None
    ) -> None:
        self.content = content
        super().__init__(_data)


class DagsDagIdDagRunsDagRunIdTaskInstancesTaskIdLogsTaskTryNumberGetResponse(
    sob.model.Object
):
    """
    Properties:

    - continuation_token
    - content
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        continuation_token: typing.Optional[
            str
        ] = None,
        content: typing.Optional[
            str
        ] = None
    ) -> None:
        self.continuation_token = continuation_token
        self.content = content
        super().__init__(_data)


class ProvidersGetResponse(sob.model.Object):

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        providers: typing.Optional[
            "ProviderCollectionProviders"
        ] = None,
        total_entries: typing.Optional[
            int
        ] = None
    ) -> None:
        self.providers = providers
        self.total_entries = total_entries
        super().__init__(_data)


sob.meta.array_writable(  # type: ignore
    FilterPool
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    FilterQueue
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    FilterState
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    FilterTags
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    UpdateMask
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    Action
).properties = sob.meta.Properties([
    ('name', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ActionCollection
).properties = sob.meta.Properties([
    (
        'actions',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ActionCollectionActions
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    ActionCollectionActions
).item_types = sob.types.MutableTypes([
    Action
])
sob.meta.object_writable(  # type: ignore
    ActionResource
).properties = sob.meta.Properties([
    (
        'action',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Action
            ])
        )
    ),
    (
        'resource',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Resource
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BasicDAGRun
).properties = sob.meta.Properties([
    ('run_id', sob.properties.String()),
    ('dag_id', sob.properties.String()),
    ('logical_date', sob.properties.DateTime()),
    (
        'start_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data_interval_start',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data_interval_end',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'state',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "failed",
                "queued",
                "running",
                "success"
            }
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ClassReference
).properties = sob.meta.Properties([
    ('module_path', sob.properties.String()),
    ('class_name', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ClearDagRun
).properties = sob.meta.Properties([
    ('dry_run', sob.properties.Boolean())
])
sob.meta.object_writable(  # type: ignore
    ClearTaskInstances
).properties = sob.meta.Properties([
    ('dry_run', sob.properties.Boolean()),
    (
        'task_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ClearTaskInstancesTaskIds
            ])
        )
    ),
    ('start_date', sob.properties.String()),
    ('end_date', sob.properties.String()),
    ('only_failed', sob.properties.Boolean()),
    ('only_running', sob.properties.Boolean()),
    ('include_subdags', sob.properties.Boolean()),
    ('include_parentdag', sob.properties.Boolean()),
    ('reset_dag_runs', sob.properties.Boolean()),
    (
        'dag_run_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('include_upstream', sob.properties.Boolean()),
    ('include_downstream', sob.properties.Boolean()),
    ('include_future', sob.properties.Boolean()),
    ('include_past', sob.properties.Boolean())
])
sob.meta.array_writable(  # type: ignore
    ClearTaskInstancesTaskIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    CollectionInfo
).properties = sob.meta.Properties([
    ('total_entries', sob.properties.Integer())
])
sob.meta.object_writable(  # type: ignore
    Config
).properties = sob.meta.Properties([
    (
        'sections',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ConfigSections
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ConfigSections
).item_types = sob.types.MutableTypes([
    ConfigSection
])
sob.meta.object_writable(  # type: ignore
    ConfigOption
).properties = sob.meta.Properties([
    ('key', sob.properties.String()),
    ('value', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ConfigSection
).properties = sob.meta.Properties([
    ('name', sob.properties.String()),
    (
        'options',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ConfigOptions
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ConfigOptions
).item_types = sob.types.MutableTypes([
    ConfigOption
])
sob.meta.object_writable(  # type: ignore
    Connection
).properties = sob.meta.Properties([
    ('connection_id', sob.properties.String()),
    ('conn_type', sob.properties.String()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'host',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'login',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'schema',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'port',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('password', sob.properties.String()),
    (
        'extra',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ConnectionCollection
).properties = sob.meta.Properties([
    (
        'connections',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ConnectionCollectionConnections
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    ConnectionCollectionConnections
).item_types = sob.types.MutableTypes([
    ConnectionCollectionItem
])
sob.meta.object_writable(  # type: ignore
    ConnectionCollectionItem
).properties = sob.meta.Properties([
    ('connection_id', sob.properties.String()),
    ('conn_type', sob.properties.String()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'host',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'login',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'schema',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'port',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ConnectionTest
).properties = sob.meta.Properties([
    ('status', sob.properties.Boolean()),
    ('message', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    CronExpression
).properties = sob.meta.Properties([
    (
        'type',
        sob.properties.String(
            name="__type",
            required=True
        )
    ),
    (
        'value',
        sob.properties.String(
            required=True
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DAG
).properties = sob.meta.Properties([
    ('dag_id', sob.properties.String()),
    (
        'root_dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_paused',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_active',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('is_subdag', sob.properties.Boolean()),
    (
        'last_parsed_time',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_pickled',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_expired',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'scheduler_lock',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pickle_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'default_view',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('fileloc', sob.properties.String()),
    ('file_token', sob.properties.String()),
    (
        'owners',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Owners
            ])
        )
    ),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'schedule_interval',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TimeDelta,
                sob.utilities.types.Null,
                RelativeDelta,
                CronExpression
            ])
        )
    ),
    (
        'timetable_description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tags',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Tags,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'max_active_tasks',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'max_active_runs',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'has_task_concurrency_limits',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'has_import_errors',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_data_interval_start',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_data_interval_end',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_create_after',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Owners
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    Tags
).item_types = sob.types.MutableTypes([
    Tag
])
sob.meta.object_writable(  # type: ignore
    DAGCollection
).properties = sob.meta.Properties([
    (
        'dags',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DAGCollectionDags
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    DAGCollectionDags
).item_types = sob.types.MutableTypes([
    DAG
])
sob.meta.object_writable(  # type: ignore
    DAGDetail
).properties = sob.meta.Properties([
    ('dag_id', sob.properties.String()),
    (
        'root_dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_paused',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_active',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('is_subdag', sob.properties.Boolean()),
    (
        'last_parsed_time',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_pickled',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_expired',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'scheduler_lock',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pickle_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'default_view',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null,
                str
            ])
        )
    ),
    ('fileloc', sob.properties.String()),
    ('file_token', sob.properties.String()),
    (
        'owners',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Owners
            ])
        )
    ),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'schedule_interval',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TimeDelta,
                sob.utilities.types.Null,
                RelativeDelta,
                CronExpression
            ])
        )
    ),
    (
        'timetable_description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tags',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Tags,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'max_active_tasks',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'max_active_runs',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'has_task_concurrency_limits',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'has_import_errors',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_data_interval_start',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_data_interval_end',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'next_dagrun_create_after',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('timezone', sob.properties.String()),
    ('catchup', sob.properties.Boolean()),
    ('orientation', sob.properties.String()),
    ('concurrency', sob.properties.Number()),
    (
        'start_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dag_run_timeout',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TimeDelta,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'doc_md',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'params',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.model.Dictionary
            ])
        )
    ),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_paused_upon_creation',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_parsed',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'template_search_path',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DAGDetailTemplateSearchPath,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'render_template_as_native_obj',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DAGDetailTemplateSearchPath
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    DAGRun
).properties = sob.meta.Properties([
    (
        'dag_run_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('dag_id', sob.properties.String()),
    (
        'logical_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'execution_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'start_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data_interval_start',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data_interval_end',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_scheduling_decision',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'run_type',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "backfill",
                "dataset_triggered",
                "manual",
                "scheduled"
            }
        )
    ),
    (
        'state',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "failed",
                "queued",
                "running",
                "success"
            }
        )
    ),
    ('external_trigger', sob.properties.Boolean()),
    (
        'conf',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.model.Dictionary
            ])
        )
    ),
    (
        'note',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DAGRunCollection
).properties = sob.meta.Properties([
    (
        'dag_runs',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DAGRunCollectionDagRuns
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    DAGRunCollectionDagRuns
).item_types = sob.types.MutableTypes([
    DAGRun
])
sob.meta.object_writable(  # type: ignore
    DagProcessorStatus
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Enumerated(
                    types=sob.types.Types([
                        str
                    ]),
                    values={
                        "healthy",
                        "unhealthy"
                    }
                ),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'latest_dag_processor_heartbeat',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DagScheduleDatasetReference
).properties = sob.meta.Properties([
    (
        'dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('created_at', sob.properties.String()),
    ('updated_at', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    DagWarning
).properties = sob.meta.Properties([
    ('dag_id', sob.properties.String()),
    ('warning_type', sob.properties.String()),
    ('message', sob.properties.String()),
    ('timestamp', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    DagWarningCollection
).properties = sob.meta.Properties([
    (
        'import_errors',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DagWarningCollectionImportErrors
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    DagWarningCollectionImportErrors
).item_types = sob.types.MutableTypes([
    DagWarning
])
sob.meta.object_writable(  # type: ignore
    Dataset
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.Integer(
            name="id"
        )
    ),
    ('uri', sob.properties.String()),
    (
        'extra',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.model.Dictionary,
                sob.utilities.types.Null
            ])
        )
    ),
    ('created_at', sob.properties.String()),
    ('updated_at', sob.properties.String()),
    (
        'consuming_dags',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DatasetConsumingDags
            ])
        )
    ),
    (
        'producing_tasks',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DatasetProducingTasks
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DatasetConsumingDags
).item_types = sob.types.MutableTypes([
    DagScheduleDatasetReference
])
sob.meta.array_writable(  # type: ignore
    DatasetProducingTasks
).item_types = sob.types.MutableTypes([
    TaskOutletDatasetReference
])
sob.meta.object_writable(  # type: ignore
    DatasetCollection
).properties = sob.meta.Properties([
    (
        'datasets',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DatasetCollectionDatasets
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    DatasetCollectionDatasets
).item_types = sob.types.MutableTypes([
    Dataset
])
sob.meta.object_writable(  # type: ignore
    DatasetEvent
).properties = sob.meta.Properties([
    ('dataset_id', sob.properties.Integer()),
    ('dataset_uri', sob.properties.String()),
    (
        'extra',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.model.Dictionary,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'source_dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'source_task_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'source_run_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'source_map_index',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_dagruns',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DatasetEventCreatedDagruns
            ])
        )
    ),
    ('timestamp', sob.properties.String())
])
sob.meta.array_writable(  # type: ignore
    DatasetEventCreatedDagruns
).item_types = sob.types.MutableTypes([
    BasicDAGRun
])
sob.meta.object_writable(  # type: ignore
    DatasetEventCollection
).properties = sob.meta.Properties([
    (
        'dataset_events',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DatasetEventCollectionDatasetEvents
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    DatasetEventCollectionDatasetEvents
).item_types = sob.types.MutableTypes([
    DatasetEvent
])
sob.meta.object_writable(  # type: ignore
    Error
).properties = sob.meta.Properties([
    (
        'type_',
        sob.properties.String(
            name="type",
            required=True
        )
    ),
    (
        'title',
        sob.properties.String(
            required=True
        )
    ),
    (
        'status',
        sob.properties.Number(
            required=True
        )
    ),
    ('detail', sob.properties.String()),
    ('instance', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    EventLog
).properties = sob.meta.Properties([
    ('event_log_id', sob.properties.Integer()),
    ('when', sob.properties.DateTime()),
    (
        'dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'task_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('event', sob.properties.String()),
    (
        'execution_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('owner', sob.properties.String()),
    (
        'extra',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    EventLogCollection
).properties = sob.meta.Properties([
    (
        'event_logs',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                EventLogCollectionEventLogs_
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    EventLogCollectionEventLogs_
).item_types = sob.types.MutableTypes([
    EventLog
])
sob.meta.object_writable(  # type: ignore
    ExtraLink
).properties = sob.meta.Properties([
    (
        'class_ref',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ClassReference
            ])
        )
    ),
    ('name', sob.properties.String()),
    ('href', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ExtraLinkCollection
).properties = sob.meta.Properties([
    (
        'extra_links',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ExtraLinks
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ExtraLinks
).item_types = sob.types.MutableTypes([
    ExtraLink
])
sob.meta.object_writable(  # type: ignore
    HealthInfo
).properties = sob.meta.Properties([
    (
        'metadatabase',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MetadatabaseStatus
            ])
        )
    ),
    (
        'scheduler',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SchedulerStatus
            ])
        )
    ),
    (
        'triggerer',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TriggererStatus
            ])
        )
    ),
    (
        'dag_processor',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DagProcessorStatus
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ImportError
).properties = sob.meta.Properties([
    ('import_error_id', sob.properties.Integer()),
    ('timestamp', sob.properties.String()),
    ('filename', sob.properties.String()),
    ('stack_trace', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ImportErrorCollection
).properties = sob.meta.Properties([
    (
        'import_errors',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ImportErrorCollectionImportErrors_
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    ImportErrorCollectionImportErrors_
).item_types = sob.types.MutableTypes([
    ImportError
])
sob.meta.object_writable(  # type: ignore
    Job
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.Integer(
            name="id"
        )
    ),
    (
        'dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'state',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'job_type',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'start_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'latest_heartbeat',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'executor_class',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'hostname',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'unixname',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ListDagRunsForm
).properties = sob.meta.Properties([
    ('order_by', sob.properties.String()),
    ('page_offset', sob.properties.Integer()),
    ('page_limit', sob.properties.Integer()),
    (
        'dag_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListDagRunsFormDagIds
            ])
        )
    ),
    (
        'states',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListDagRunsFormStates
            ])
        )
    ),
    ('execution_date_gte', sob.properties.DateTime()),
    ('execution_date_lte', sob.properties.DateTime()),
    ('start_date_gte', sob.properties.DateTime()),
    ('start_date_lte', sob.properties.DateTime()),
    ('end_date_gte', sob.properties.DateTime()),
    ('end_date_lte', sob.properties.DateTime())
])
sob.meta.array_writable(  # type: ignore
    ListDagRunsFormDagIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ListDagRunsFormStates
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    ListTaskInstanceForm
).properties = sob.meta.Properties([
    (
        'dag_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormDagIds
            ])
        )
    ),
    (
        'dag_run_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormDagRunIds
            ])
        )
    ),
    (
        'task_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormTaskIds
            ])
        )
    ),
    ('execution_date_gte', sob.properties.DateTime()),
    ('execution_date_lte', sob.properties.DateTime()),
    ('start_date_gte', sob.properties.DateTime()),
    ('start_date_lte', sob.properties.DateTime()),
    ('end_date_gte', sob.properties.DateTime()),
    ('end_date_lte', sob.properties.DateTime()),
    ('duration_gte', sob.properties.Number()),
    ('duration_lte', sob.properties.Number()),
    (
        'state',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormState
            ])
        )
    ),
    (
        'pool',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormPool
            ])
        )
    ),
    (
        'queue',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ListTaskInstanceFormQueue
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormDagIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormDagRunIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormPool
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormQueue
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormState
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Enumerated(
                types=sob.types.Types([
                    str
                ]),
                values={
                    "deferred",
                    "failed",
                    "none",
                    "queued",
                    "removed",
                    "restarting",
                    "running",
                    "scheduled",
                    "skipped",
                    "success",
                    "up_for_reschedule",
                    "up_for_retry",
                    "upstream_failed",
                    sob.utilities.types.NULL
                }
            ),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    ListTaskInstanceFormTaskIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    MetadatabaseStatus
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Enumerated(
                    types=sob.types.Types([
                        str
                    ]),
                    values={
                        "healthy",
                        "unhealthy"
                    }
                ),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PluginCollection
).properties = sob.meta.Properties([
    (
        'plugins',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionPlugins
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionPlugins
).item_types = sob.types.MutableTypes([
    PluginCollectionItem
])
sob.meta.object_writable(  # type: ignore
    PluginCollectionItem
).properties = sob.meta.Properties([
    ('name', sob.properties.String()),
    (
        'hooks',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemHooks
            ])
        )
    ),
    (
        'executors',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemExecutors
            ])
        )
    ),
    (
        'macros',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemMacros
            ])
        )
    ),
    (
        'flask_blueprints',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemFlaskBlueprints
            ])
        )
    ),
    (
        'appbuilder_views',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemAppbuilderViews
            ])
        )
    ),
    (
        'appbuilder_menu_items',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemAppbuilderMenuItems
            ])
        )
    ),
    (
        'global_operator_extra_links',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemGlobalOperatorExtraLinks
            ])
        )
    ),
    (
        'operator_extra_links',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemOperatorExtraLinks
            ])
        )
    ),
    (
        'source',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ti_deps',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemTiDeps
            ])
        )
    ),
    (
        'listeners',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemListeners
            ])
        )
    ),
    (
        'timetables',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PluginCollectionItemTimetables
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemAppbuilderMenuItems
).item_types = sob.types.MutableTypes([
    sob.model.Dictionary
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemAppbuilderViews
).item_types = sob.types.MutableTypes([
    sob.model.Dictionary
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemExecutors
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemFlaskBlueprints
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemGlobalOperatorExtraLinks
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemHooks
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemListeners
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemMacros
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemOperatorExtraLinks
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemTiDeps
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    PluginCollectionItemTimetables
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    Pool
).properties = sob.meta.Properties([
    ('name', sob.properties.String()),
    ('slots', sob.properties.Integer()),
    ('occupied_slots', sob.properties.Integer()),
    ('running_slots', sob.properties.Integer()),
    ('queued_slots', sob.properties.Integer()),
    ('open_slots', sob.properties.Integer()),
    ('scheduled_slots', sob.properties.Integer()),
    ('deferred_slots', sob.properties.Integer()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('include_deferred', sob.properties.Boolean())
])
sob.meta.object_writable(  # type: ignore
    PoolCollection
).properties = sob.meta.Properties([
    (
        'pools',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PoolCollectionPools_
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    PoolCollectionPools_
).item_types = sob.types.MutableTypes([
    Pool
])
sob.meta.object_writable(  # type: ignore
    Provider
).properties = sob.meta.Properties([
    ('package_name', sob.properties.String()),
    ('description', sob.properties.String()),
    ('version', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ProviderCollection
).properties = sob.meta.Properties([
    (
        'providers',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProviderCollectionProviders
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ProviderCollectionProviders
).item_types = sob.types.MutableTypes([
    Provider
])
sob.meta.object_writable(  # type: ignore
    RelativeDelta
).properties = sob.meta.Properties([
    (
        'type',
        sob.properties.String(
            name="__type",
            required=True
        )
    ),
    (
        'years',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'months',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'days',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'leapdays',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'hours',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'minutes',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'seconds',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'microseconds',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'year',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'month',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'day',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'hour',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'minute',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'second',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'microsecond',
        sob.properties.Integer(
            required=True
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Resource
).properties = sob.meta.Properties([
    ('name', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    Role
).properties = sob.meta.Properties([
    ('name', sob.properties.String()),
    (
        'actions',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                RoleActions
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    RoleActions
).item_types = sob.types.MutableTypes([
    ActionResource
])
sob.meta.object_writable(  # type: ignore
    RoleCollection
).properties = sob.meta.Properties([
    (
        'roles',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                RoleCollectionRoles
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    RoleCollectionRoles
).item_types = sob.types.MutableTypes([
    Role
])
sob.meta.object_writable(  # type: ignore
    SLAMiss
).properties = sob.meta.Properties([
    ('task_id', sob.properties.String()),
    ('dag_id', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    ('email_sent', sob.properties.Boolean()),
    ('timestamp', sob.properties.String()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('notification_sent', sob.properties.Boolean())
])
sob.meta.object_writable(  # type: ignore
    SchedulerStatus
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Enumerated(
                    types=sob.types.Types([
                        str
                    ]),
                    values={
                        "healthy",
                        "unhealthy"
                    }
                ),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'latest_scheduler_heartbeat',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SetDagRunNote
).properties = sob.meta.Properties([
    ('note', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    SetTaskInstanceNote
).properties = sob.meta.Properties([
    (
        'note',
        sob.properties.String(
            required=True
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Tag
).properties = sob.meta.Properties([
    ('name', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    Task
).properties = sob.meta.Properties([
    (
        'class_ref',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ClassReference
            ])
        )
    ),
    ('task_id', sob.properties.String()),
    ('owner', sob.properties.String()),
    ('start_date', sob.properties.DateTime()),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'trigger_rule',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "all_done",
                "all_done_setup_success",
                "all_failed",
                "all_skipped",
                "all_success",
                "always",
                "dummy",
                "none_failed",
                "none_failed_min_one_success",
                "none_failed_or_skipped",
                "none_skipped",
                "one_done",
                "one_failed",
                "one_success"
            }
        )
    ),
    (
        'extra_links',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TaskExtraLinks
            ])
        )
    ),
    ('depends_on_past', sob.properties.Boolean()),
    ('is_mapped', sob.properties.Boolean()),
    ('wait_for_downstream', sob.properties.Boolean()),
    ('retries', sob.properties.Number()),
    (
        'queue',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('pool', sob.properties.String()),
    ('pool_slots', sob.properties.Number()),
    (
        'execution_timeout',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TimeDelta,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'retry_delay',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TimeDelta,
                sob.utilities.types.Null
            ])
        )
    ),
    ('retry_exponential_backoff', sob.properties.Boolean()),
    ('priority_weight', sob.properties.Number()),
    (
        'weight_rule',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "absolute",
                "downstream",
                "upstream"
            }
        )
    ),
    ('ui_color', sob.properties.String()),
    ('ui_fgcolor', sob.properties.String()),
    (
        'template_fields',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TemplateField
            ])
        )
    ),
    (
        'sub_dag',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DAG
            ])
        )
    ),
    (
        'downstream_task_ids',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DownstreamTaskIds
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DownstreamTaskIds
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    TaskExtraLinks
).item_types = sob.types.MutableTypes([
    TaskExtraLinksItem
])
sob.meta.object_writable(  # type: ignore
    TaskExtraLinksItem
).properties = sob.meta.Properties([
    (
        'class_ref',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ClassReference
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TemplateField
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    TaskCollection
).properties = sob.meta.Properties([
    (
        'tasks',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Tasks
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Tasks
).item_types = sob.types.MutableTypes([
    Task
])
sob.meta.object_writable(  # type: ignore
    TaskInstance
).properties = sob.meta.Properties([
    ('task_id', sob.properties.String()),
    ('dag_id', sob.properties.String()),
    ('dag_run_id', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    (
        'start_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'end_date',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'duration',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'state',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Enumerated(
                    types=sob.types.Types([
                        str
                    ]),
                    values={
                        "deferred",
                        "failed",
                        "none",
                        "queued",
                        "removed",
                        "restarting",
                        "running",
                        "scheduled",
                        "skipped",
                        "success",
                        "up_for_reschedule",
                        "up_for_retry",
                        "upstream_failed",
                        sob.utilities.types.NULL
                    }
                ),
                sob.utilities.types.Null
            ])
        )
    ),
    ('try_number', sob.properties.Integer()),
    ('map_index', sob.properties.Integer()),
    ('max_tries', sob.properties.Integer()),
    ('hostname', sob.properties.String()),
    ('unixname', sob.properties.String()),
    ('pool', sob.properties.String()),
    ('pool_slots', sob.properties.Integer()),
    (
        'queue',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'priority_weight',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'operator',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'queued_when',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pid',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('executor_config', sob.properties.String()),
    (
        'sla_miss',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SLAMiss,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'rendered_fields',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.model.Dictionary
            ])
        )
    ),
    (
        'trigger',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Trigger,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'triggerer_job',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Job,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'note',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TaskInstanceCollection
).properties = sob.meta.Properties([
    (
        'task_instances',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TaskInstanceCollectionTaskInstances
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    TaskInstanceCollectionTaskInstances
).item_types = sob.types.MutableTypes([
    TaskInstance
])
sob.meta.object_writable(  # type: ignore
    TaskInstanceReference
).properties = sob.meta.Properties([
    ('task_id', sob.properties.String()),
    ('dag_id', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    ('dag_run_id', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    TaskInstanceReferenceCollection
).properties = sob.meta.Properties([
    (
        'task_instances',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TaskInstances_
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TaskInstances_
).item_types = sob.types.MutableTypes([
    TaskInstanceReference
])
sob.meta.object_writable(  # type: ignore
    TaskOutletDatasetReference
).properties = sob.meta.Properties([
    (
        'dag_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'task_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('created_at', sob.properties.String()),
    ('updated_at', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    TimeDelta
).properties = sob.meta.Properties([
    (
        'type',
        sob.properties.String(
            name="__type",
            required=True
        )
    ),
    (
        'days',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'seconds',
        sob.properties.Integer(
            required=True
        )
    ),
    (
        'microseconds',
        sob.properties.Integer(
            required=True
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Trigger
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.Integer(
            name="id"
        )
    ),
    ('classpath', sob.properties.String()),
    ('kwargs', sob.properties.String()),
    ('created_date', sob.properties.String()),
    (
        'triggerer_id',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TriggererStatus
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Enumerated(
                    types=sob.types.Types([
                        str
                    ]),
                    values={
                        "healthy",
                        "unhealthy"
                    }
                ),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'latest_triggerer_heartbeat',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    UpdateDagRunState
).properties = sob.meta.Properties([
    (
        'state',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "failed",
                "queued",
                "success"
            }
        )
    )
])
sob.meta.object_writable(  # type: ignore
    UpdateTaskInstance
).properties = sob.meta.Properties([
    ('dry_run', sob.properties.Boolean()),
    (
        'new_state',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "failed",
                "skipped",
                "success"
            }
        )
    )
])
sob.meta.object_writable(  # type: ignore
    UpdateTaskInstancesState
).properties = sob.meta.Properties([
    ('dry_run', sob.properties.Boolean()),
    ('task_id', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    ('dag_run_id', sob.properties.String()),
    ('include_upstream', sob.properties.Boolean()),
    ('include_downstream', sob.properties.Boolean()),
    ('include_future', sob.properties.Boolean()),
    ('include_past', sob.properties.Boolean()),
    (
        'new_state',
        sob.properties.Enumerated(
            types=sob.types.Types([
                str
            ]),
            values={
                "failed",
                "skipped",
                "success"
            }
        )
    )
])
sob.meta.object_writable(  # type: ignore
    User
).properties = sob.meta.Properties([
    ('first_name', sob.properties.String()),
    ('last_name', sob.properties.String()),
    ('username', sob.properties.String()),
    ('email', sob.properties.String()),
    (
        'active',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_login',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'login_count',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'failed_login_count',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'roles',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                UserCollectionItemRoles
            ])
        )
    ),
    (
        'created_on',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'changed_on',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('password', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    UserCollection
).properties = sob.meta.Properties([
    (
        'users',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                UserCollectionUsers
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    UserCollectionUsers
).item_types = sob.types.MutableTypes([
    UserCollectionItem
])
sob.meta.object_writable(  # type: ignore
    UserCollectionItem
).properties = sob.meta.Properties([
    ('first_name', sob.properties.String()),
    ('last_name', sob.properties.String()),
    ('username', sob.properties.String()),
    ('email', sob.properties.String()),
    (
        'active',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'last_login',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'login_count',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'failed_login_count',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'roles',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                UserCollectionItemRoles
            ])
        )
    ),
    (
        'created_on',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'changed_on',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    UserCollectionItemRoles
).item_types = sob.types.MutableTypes([
    UserCollectionItemRolesItem
])
sob.meta.object_writable(  # type: ignore
    UserCollectionItemRolesItem
).properties = sob.meta.Properties([
    ('name', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    Variable
).properties = sob.meta.Properties([
    ('key', sob.properties.String()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    ('value', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    VariableCollection
).properties = sob.meta.Properties([
    (
        'variables',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                VariableCollectionVariables
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    VariableCollectionVariables
).item_types = sob.types.MutableTypes([
    VariableCollectionItem
])
sob.meta.object_writable(  # type: ignore
    VariableCollectionItem
).properties = sob.meta.Properties([
    ('key', sob.properties.String()),
    (
        'description',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    VersionInfo
).properties = sob.meta.Properties([
    ('version', sob.properties.String()),
    (
        'git_version',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    XCom
).properties = sob.meta.Properties([
    ('key', sob.properties.String()),
    ('timestamp', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    ('map_index', sob.properties.Integer()),
    ('task_id', sob.properties.String()),
    ('dag_id', sob.properties.String()),
    ('value', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    XComCollection
).properties = sob.meta.Properties([
    (
        'xcom_entries',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                XComCollectionXcomEntries
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
sob.meta.array_writable(  # type: ignore
    XComCollectionXcomEntries
).item_types = sob.types.MutableTypes([
    XComCollectionItem
])
sob.meta.object_writable(  # type: ignore
    XComCollectionItem
).properties = sob.meta.Properties([
    ('key', sob.properties.String()),
    ('timestamp', sob.properties.String()),
    ('execution_date', sob.properties.String()),
    ('map_index', sob.properties.Integer()),
    ('task_id', sob.properties.String()),
    ('dag_id', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    DagSourcesFileTokenGetResponse
).properties = sob.meta.Properties([
    ('content', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    DagsDagIdDagRunsDagRunIdTaskInstancesTaskIdLogsTaskTryNumberGetResponse
).properties = sob.meta.Properties([
    ('continuation_token', sob.properties.String()),
    ('content', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    ProvidersGetResponse
).properties = sob.meta.Properties([
    (
        'providers',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProviderCollectionProviders
            ])
        )
    ),
    ('total_entries', sob.properties.Integer())
])
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/components/parameters/FilterPool/schema": FilterPool,
    "#/components/parameters/FilterQueue/schema": FilterQueue,
    "#/components/parameters/FilterState/schema": FilterState,
    "#/components/parameters/FilterTags/schema": FilterTags,
    "#/components/parameters/UpdateMask/schema": UpdateMask,
    "#/components/schemas/Action": Action,
    "#/components/schemas/ActionCollection": ActionCollection,
    "#/components/schemas/ActionCollection/allOf/0/properties/actions":
    ActionCollectionActions,
    "#/components/schemas/ActionResource": ActionResource,
    "#/components/schemas/BasicDAGRun": BasicDAGRun,
    "#/components/schemas/ClassReference": ClassReference,
    "#/components/schemas/ClearDagRun": ClearDagRun,
    "#/components/schemas/ClearTaskInstances": ClearTaskInstances,
    "#/components/schemas/ClearTaskInstances/properties/task_ids":
    ClearTaskInstancesTaskIds,
    "#/components/schemas/CollectionInfo": CollectionInfo,
    "#/components/schemas/Config": Config,
    "#/components/schemas/Config/properties/sections": ConfigSections,
    "#/components/schemas/ConfigOption": ConfigOption,
    "#/components/schemas/ConfigSection": ConfigSection,
    "#/components/schemas/ConfigSection/properties/options": ConfigOptions,
    "#/components/schemas/Connection": Connection,
    "#/components/schemas/ConnectionCollection": ConnectionCollection,
    "#/components/schemas/ConnectionCollection/allOf/0/properties/connections":
    ConnectionCollectionConnections,
    "#/components/schemas/ConnectionCollectionItem": ConnectionCollectionItem,
    "#/components/schemas/ConnectionTest": ConnectionTest,
    "#/components/schemas/CronExpression": CronExpression,
    "#/components/schemas/DAG": DAG,
    "#/components/schemas/DAG/properties/owners": Owners,
    "#/components/schemas/DAG/properties/tags": Tags,
    "#/components/schemas/DAGCollection": DAGCollection,
    "#/components/schemas/DAGCollection/allOf/0/properties/dags":
    DAGCollectionDags,
    "#/components/schemas/DAGDetail": DAGDetail,
    "#/components/schemas/DAGDetail/allOf/1/properties/template_search_path":
    DAGDetailTemplateSearchPath,
    "#/components/schemas/DAGRun": DAGRun,
    "#/components/schemas/DAGRunCollection": DAGRunCollection,
    "#/components/schemas/DAGRunCollection/allOf/0/properties/dag_runs":
    DAGRunCollectionDagRuns,
    "#/components/schemas/DagProcessorStatus": DagProcessorStatus,
    "#/components/schemas/DagScheduleDatasetReference":
    DagScheduleDatasetReference,
    "#/components/schemas/DagWarning": DagWarning,
    "#/components/schemas/DagWarningCollection": DagWarningCollection,
    "#/components/schemas/DagWarningCollection/allOf/0/properties/import_errors":  # noqa
    DagWarningCollectionImportErrors,
    "#/components/schemas/Dataset": Dataset,
    "#/components/schemas/Dataset/properties/consuming_dags":
    DatasetConsumingDags,
    "#/components/schemas/Dataset/properties/producing_tasks":
    DatasetProducingTasks,
    "#/components/schemas/DatasetCollection": DatasetCollection,
    "#/components/schemas/DatasetCollection/allOf/0/properties/datasets":
    DatasetCollectionDatasets,
    "#/components/schemas/DatasetEvent": DatasetEvent,
    "#/components/schemas/DatasetEvent/properties/created_dagruns":
    DatasetEventCreatedDagruns,
    "#/components/schemas/DatasetEventCollection": DatasetEventCollection,
    "#/components/schemas/DatasetEventCollection/allOf/0/properties/dataset_events":  # noqa
    DatasetEventCollectionDatasetEvents,
    "#/components/schemas/Error": Error,
    "#/components/schemas/EventLog": EventLog,
    "#/components/schemas/EventLogCollection": EventLogCollection,
    "#/components/schemas/EventLogCollection/allOf/0/properties/event_logs":
    EventLogCollectionEventLogs_,
    "#/components/schemas/ExtraLink": ExtraLink,
    "#/components/schemas/ExtraLinkCollection": ExtraLinkCollection,
    "#/components/schemas/ExtraLinkCollection/properties/extra_links":
    ExtraLinks,
    "#/components/schemas/HealthInfo": HealthInfo,
    "#/components/schemas/ImportError": ImportError,
    "#/components/schemas/ImportErrorCollection": ImportErrorCollection,
    "#/components/schemas/ImportErrorCollection/allOf/0/properties/import_errors":  # noqa
    ImportErrorCollectionImportErrors_,
    "#/components/schemas/Job": Job,
    "#/components/schemas/ListDagRunsForm": ListDagRunsForm,
    "#/components/schemas/ListDagRunsForm/properties/dag_ids":
    ListDagRunsFormDagIds,
    "#/components/schemas/ListDagRunsForm/properties/states":
    ListDagRunsFormStates,
    "#/components/schemas/ListTaskInstanceForm": ListTaskInstanceForm,
    "#/components/schemas/ListTaskInstanceForm/properties/dag_ids":
    ListTaskInstanceFormDagIds,
    "#/components/schemas/ListTaskInstanceForm/properties/dag_run_ids":
    ListTaskInstanceFormDagRunIds,
    "#/components/schemas/ListTaskInstanceForm/properties/pool":
    ListTaskInstanceFormPool,
    "#/components/schemas/ListTaskInstanceForm/properties/queue":
    ListTaskInstanceFormQueue,
    "#/components/schemas/ListTaskInstanceForm/properties/state":
    ListTaskInstanceFormState,
    "#/components/schemas/ListTaskInstanceForm/properties/task_ids":
    ListTaskInstanceFormTaskIds,
    "#/components/schemas/MetadatabaseStatus": MetadatabaseStatus,
    "#/components/schemas/PluginCollection": PluginCollection,
    "#/components/schemas/PluginCollection/allOf/0/properties/plugins":
    PluginCollectionPlugins,
    "#/components/schemas/PluginCollectionItem": PluginCollectionItem,
    "#/components/schemas/PluginCollectionItem/properties/appbuilder_menu_items":  # noqa
    PluginCollectionItemAppbuilderMenuItems,
    "#/components/schemas/PluginCollectionItem/properties/appbuilder_views":
    PluginCollectionItemAppbuilderViews,
    "#/components/schemas/PluginCollectionItem/properties/executors":
    PluginCollectionItemExecutors,
    "#/components/schemas/PluginCollectionItem/properties/flask_blueprints":
    PluginCollectionItemFlaskBlueprints,
    "#/components/schemas/PluginCollectionItem/properties/global_operator_extra_links":  # noqa
    PluginCollectionItemGlobalOperatorExtraLinks,
    "#/components/schemas/PluginCollectionItem/properties/hooks":
    PluginCollectionItemHooks,
    "#/components/schemas/PluginCollectionItem/properties/listeners":
    PluginCollectionItemListeners,
    "#/components/schemas/PluginCollectionItem/properties/macros":
    PluginCollectionItemMacros,
    "#/components/schemas/PluginCollectionItem/properties/operator_extra_links":  # noqa
    PluginCollectionItemOperatorExtraLinks,
    "#/components/schemas/PluginCollectionItem/properties/ti_deps":
    PluginCollectionItemTiDeps,
    "#/components/schemas/PluginCollectionItem/properties/timetables":
    PluginCollectionItemTimetables,
    "#/components/schemas/Pool": Pool,
    "#/components/schemas/PoolCollection": PoolCollection,
    "#/components/schemas/PoolCollection/allOf/0/properties/pools":
    PoolCollectionPools_,
    "#/components/schemas/Provider": Provider,
    "#/components/schemas/ProviderCollection": ProviderCollection,
    "#/components/schemas/ProviderCollection/properties/providers":
    ProviderCollectionProviders,
    "#/components/schemas/RelativeDelta": RelativeDelta,
    "#/components/schemas/Resource": Resource,
    "#/components/schemas/Role": Role,
    "#/components/schemas/Role/properties/actions": RoleActions,
    "#/components/schemas/RoleCollection": RoleCollection,
    "#/components/schemas/RoleCollection/allOf/0/properties/roles":
    RoleCollectionRoles,
    "#/components/schemas/SLAMiss": SLAMiss,
    "#/components/schemas/SchedulerStatus": SchedulerStatus,
    "#/components/schemas/SetDagRunNote": SetDagRunNote,
    "#/components/schemas/SetTaskInstanceNote": SetTaskInstanceNote,
    "#/components/schemas/Tag": Tag,
    "#/components/schemas/Task": Task,
    "#/components/schemas/Task/properties/downstream_task_ids":
    DownstreamTaskIds,
    "#/components/schemas/Task/properties/extra_links": TaskExtraLinks,
    "#/components/schemas/Task/properties/extra_links/items":
    TaskExtraLinksItem,
    "#/components/schemas/Task/properties/template_fields": TemplateField,
    "#/components/schemas/TaskCollection": TaskCollection,
    "#/components/schemas/TaskCollection/properties/tasks": Tasks,
    "#/components/schemas/TaskInstance": TaskInstance,
    "#/components/schemas/TaskInstanceCollection": TaskInstanceCollection,
    "#/components/schemas/TaskInstanceCollection/allOf/0/properties/task_instances":  # noqa
    TaskInstanceCollectionTaskInstances,
    "#/components/schemas/TaskInstanceReference": TaskInstanceReference,
    "#/components/schemas/TaskInstanceReferenceCollection":
    TaskInstanceReferenceCollection,
    "#/components/schemas/TaskInstanceReferenceCollection/properties/task_instances":  # noqa
    TaskInstances_,
    "#/components/schemas/TaskOutletDatasetReference":
    TaskOutletDatasetReference,
    "#/components/schemas/TimeDelta": TimeDelta,
    "#/components/schemas/Trigger": Trigger,
    "#/components/schemas/TriggererStatus": TriggererStatus,
    "#/components/schemas/UpdateDagRunState": UpdateDagRunState,
    "#/components/schemas/UpdateTaskInstance": UpdateTaskInstance,
    "#/components/schemas/UpdateTaskInstancesState": UpdateTaskInstancesState,
    "#/components/schemas/User": User,
    "#/components/schemas/UserCollection": UserCollection,
    "#/components/schemas/UserCollection/allOf/0/properties/users":
    UserCollectionUsers,
    "#/components/schemas/UserCollectionItem": UserCollectionItem,
    "#/components/schemas/UserCollectionItem/properties/roles":
    UserCollectionItemRoles,
    "#/components/schemas/UserCollectionItem/properties/roles/items":
    UserCollectionItemRolesItem,
    "#/components/schemas/Variable": Variable,
    "#/components/schemas/VariableCollection": VariableCollection,
    "#/components/schemas/VariableCollection/allOf/0/properties/variables":
    VariableCollectionVariables,
    "#/components/schemas/VariableCollectionItem": VariableCollectionItem,
    "#/components/schemas/VersionInfo": VersionInfo,
    "#/components/schemas/XCom": XCom,
    "#/components/schemas/XComCollection": XComCollection,
    "#/components/schemas/XComCollection/allOf/0/properties/xcom_entries":
    XComCollectionXcomEntries,
    "#/components/schemas/XComCollectionItem": XComCollectionItem,
    "#/paths/~1dagSources~1{file_token}/get/responses/200/content/application~1json/schema":  # noqa
    DagSourcesFileTokenGetResponse,
    "#/paths/~1dags~1{dag_id}~1dagRuns~1{dag_run_id}~1taskInstances~1{task_id}~1logs~1{task_try_number}/get/responses/200/content/application~1json/schema":  # noqa
    DagsDagIdDagRunsDagRunIdTaskInstancesTaskIdLogsTaskTryNumberGetResponse,
    "#/paths/~1providers/get/responses/200/content/application~1json/schema":
    ProvidersGetResponse,
}
