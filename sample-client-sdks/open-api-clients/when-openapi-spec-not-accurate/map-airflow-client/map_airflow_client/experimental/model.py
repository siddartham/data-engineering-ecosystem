import typing
import datetime
import sob


class LatestRun(sob.model.Object):

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
        dag_run_url: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            datetime.datetime
        ] = None,
        start_date: typing.Optional[
            datetime.datetime
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.dag_run_url = dag_run_url
        self.execution_date = execution_date
        self.start_date = start_date
        super().__init__(_data)


class LatestRuns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                'LatestRun'
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class LatestRunsResponse(sob.model.Object):

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
        items: typing.Optional[
            'LatestRuns'
        ] = None
    ) -> None:
        self.items = items
        super().__init__(_data)


class Pool(sob.model.Object):

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
        description: typing.Optional[
            str
        ] = None,
        id_: typing.Optional[
            int
        ] = None,
        pool: typing.Optional[
            str
        ] = None,
        slots: typing.Optional[
            int
        ] = None
    ) -> None:
        self.description = description
        self.id_ = id_
        self.pool = pool
        self.slots = slots
        super().__init__(_data)


class Pools(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                'Pool'
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Test(sob.model.Object):

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
            str
        ] = None
    ) -> None:
        self.status = status
        super().__init__(_data)


class DagRun(sob.model.Object):

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
        dag_run_url: typing.Optional[
            str
        ] = None,
        execution_date: typing.Optional[
            datetime.datetime
        ] = None,
        id_: typing.Optional[
            int
        ] = None,
        run_id: typing.Optional[
            str
        ] = None,
        start_date: typing.Optional[
            datetime.datetime
        ] = None,
        state: typing.Optional[
            str
        ] = None
    ) -> None:
        self.dag_id = dag_id
        self.dag_run_url = dag_run_url
        self.execution_date = execution_date
        self.id_ = id_
        self.run_id = run_id
        self.start_date = start_date
        self.state = state
        super().__init__(_data)


class DagRuns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                'DagRun'
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PostDagRunResponse(sob.model.Object):

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
        execution_date: typing.Optional[
            datetime.datetime
        ] = None,
        message: typing.Optional[
            str
        ] = None,
        run_id: typing.Optional[
            str
        ] = None
    ) -> None:
        self.execution_date = execution_date
        self.message = message
        self.run_id = run_id
        super().__init__(_data)


class DagPaused(sob.model.Object):

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
        is_paused: typing.Optional[
            bool
        ] = None,
        response: typing.Optional[
            str
        ] = None
    ) -> None:
        self.is_paused = is_paused
        self.response = response
        super().__init__(_data)


sob.meta.object_writable(  # type: ignore
    LatestRun
).properties = sob.meta.Properties([
    (
        'dag_id',
        sob.properties.String(
            name='dag_id'
        )
    ),
    (
        'dag_run_url',
        sob.properties.String(
            name='dag_run_url'
        )
    ),
    (
        'execution_date',
        sob.properties.DateTime(
            name='execution_date'
        )
    ),
    (
        'start_date',
        sob.properties.DateTime(
            name='start_date'
        )
    )
])
sob.meta.array_writable(  # type: ignore
    LatestRuns
).item_types = sob.types.MutableTypes([
    LatestRun
])
sob.meta.object_writable(  # type: ignore
    LatestRunsResponse
).properties = sob.meta.Properties([
    (
        'items',
        sob.properties.Property(
            name='items',
            types=sob.types.MutableTypes([
                LatestRuns
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Pool
).properties = sob.meta.Properties([
    (
        'description',
        sob.properties.String(
            name='description'
        )
    ),
    (
        'id_',
        sob.properties.Integer(
            name='id'
        )
    ),
    (
        'pool',
        sob.properties.String(
            name='pool'
        )
    ),
    (
        'slots',
        sob.properties.Integer(
            name='slots'
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Pools
).item_types = sob.types.MutableTypes([
    Pool
])
sob.meta.object_writable(  # type: ignore
    Test
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.String(
            name='status'
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DagRun
).properties = sob.meta.Properties([
    (
        'dag_id',
        sob.properties.String(
            name='dag_id'
        )
    ),
    (
        'dag_run_url',
        sob.properties.String(
            name='dag_run_url'
        )
    ),
    (
        'execution_date',
        sob.properties.DateTime(
            name='execution_date'
        )
    ),
    (
        'id_',
        sob.properties.Integer(
            name='id'
        )
    ),
    (
        'run_id',
        sob.properties.String(
            name='run_id'
        )
    ),
    (
        'start_date',
        sob.properties.DateTime(
            name='start_date'
        )
    ),
    (
        'state',
        sob.properties.String(
            name='state'
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DagRuns
).item_types = sob.types.MutableTypes([
    DagRun
])
sob.meta.object_writable(  # type: ignore
    PostDagRunResponse
).properties = sob.meta.Properties([
    (
        'execution_date',
        sob.properties.DateTime(
            name='execution_date'
        )
    ),
    (
        'message',
        sob.properties.String(
            name='message'
        )
    ),
    (
        'run_id',
        sob.properties.String(
            name='run_id'
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DagPaused
).properties = sob.meta.Properties([
    (
        'is_paused',
        sob.properties.Boolean(
            name='is_paused'
        )
    ),
    (
        'response',
        sob.properties.String(
            name='response'
        )
    )
])
