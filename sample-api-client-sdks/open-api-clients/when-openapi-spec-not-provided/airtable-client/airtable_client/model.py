import datetime
import typing
import sob


class Base(sob.model.Object):

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
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        permission_level: typing.Optional[
            str
        ] = None
    ) -> None:
        self.id_ = id_
        self.name = name
        self.permission_level = permission_level
        super().__init__(_data)


class Bases(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Base"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MetaBasesGetResponse(sob.model.Object):

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
        bases: typing.Optional[
            "Bases"
        ] = None
    ) -> None:
        self.bases = bases
        super().__init__(_data)


class TableFieldOptionsChoice(sob.model.Object):

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
        color: typing.Optional[
            str
        ] = None,
        id_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.color = color
        self.id_ = id_
        self.name = name
        super().__init__(_data)


class TableFieldOptionsChoices(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TableFieldOptionsChoice"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TableFieldOptionsReferencedFieldIds(sob.model.Array):

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


class TableFieldOptionsResultOptionsDateFormat(sob.model.Object):

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
        format_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.format_ = format_
        self.name = name
        super().__init__(_data)


class TableFieldOptionsResultOptionsTimeFormat(sob.model.Object):

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
        format_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.format_ = format_
        self.name = name
        super().__init__(_data)


class TableFieldOptionsResultOptionsChoice(sob.model.Object):

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
        color: typing.Optional[
            str
        ] = None,
        id_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.color = color
        self.id_ = id_
        self.name = name
        super().__init__(_data)


class TableFieldOptionsResultOptionsChoices(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TableFieldOptionsResultOptionsChoice"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TableFieldOptionsResultOptions(sob.model.Object):

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
        precision: typing.Optional[
            int
        ] = None,
        symbol: typing.Optional[
            str
        ] = None,
        date_format: typing.Optional[
            "TableFieldOptionsResultOptionsDateFormat"
        ] = None,
        time_format: typing.Optional[
            "TableFieldOptionsResultOptionsTimeFormat"
        ] = None,
        time_zone: typing.Optional[
            str
        ] = None,
        choices: typing.Optional[
            "TableFieldOptionsResultOptionsChoices"
        ] = None,
        is_reversed: typing.Optional[
            bool
        ] = None,
        prefers_single_record_link: typing.Optional[
            bool
        ] = None
    ) -> None:
        self.precision = precision
        self.symbol = symbol
        self.date_format = date_format
        self.time_format = time_format
        self.time_zone = time_zone
        self.choices = choices
        self.is_reversed = is_reversed
        self.prefers_single_record_link = prefers_single_record_link
        super().__init__(_data)


class TableFieldOptionsResult(sob.model.Object):

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
        options: typing.Optional[
            "TableFieldOptionsResultOptions"
        ] = None
    ) -> None:
        self.type_ = type_
        self.options = options
        super().__init__(_data)


class TableFieldOptionsDateFormat(sob.model.Object):

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
        format_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.format_ = format_
        self.name = name
        super().__init__(_data)


class TableFieldOptionsTimeFormat(sob.model.Object):

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
        format_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None
    ) -> None:
        self.format_ = format_
        self.name = name
        super().__init__(_data)


class TableFieldOptions(sob.model.Object):

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
        precision: typing.Optional[
            int
        ] = None,
        choices: typing.Optional[
            "TableFieldOptionsChoices"
        ] = None,
        inverse_link_field_id: typing.Optional[
            str
        ] = None,
        is_reversed: typing.Optional[
            bool
        ] = None,
        linked_table_id: typing.Optional[
            str
        ] = None,
        prefers_single_record_link: typing.Optional[
            bool
        ] = None,
        field_id_in_linked_table: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        is_valid: typing.Optional[
            bool
        ] = None,
        record_link_field_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        referenced_field_ids: typing.Optional[
            "TableFieldOptionsReferencedFieldIds"
        ] = None,
        result: typing.Optional[
            typing.Union[
                "TableFieldOptionsResult",
                sob.utilities.types.Null
            ]
        ] = None,
        date_format: typing.Optional[
            "TableFieldOptionsDateFormat"
        ] = None,
        symbol: typing.Optional[
            str
        ] = None,
        color: typing.Optional[
            str
        ] = None,
        icon: typing.Optional[
            str
        ] = None,
        formula: typing.Optional[
            str
        ] = None,
        time_format: typing.Optional[
            "TableFieldOptionsTimeFormat"
        ] = None,
        time_zone: typing.Optional[
            str
        ] = None
    ) -> None:
        self.precision = precision
        self.choices = choices
        self.inverse_link_field_id = inverse_link_field_id
        self.is_reversed = is_reversed
        self.linked_table_id = linked_table_id
        self.prefers_single_record_link = prefers_single_record_link
        self.field_id_in_linked_table = field_id_in_linked_table
        self.is_valid = is_valid
        self.record_link_field_id = record_link_field_id
        self.referenced_field_ids = referenced_field_ids
        self.result = result
        self.date_format = date_format
        self.symbol = symbol
        self.color = color
        self.icon = icon
        self.formula = formula
        self.time_format = time_format
        self.time_zone = time_zone
        super().__init__(_data)


class TableField(sob.model.Object):

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
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        options: typing.Optional[
            "TableFieldOptions"
        ] = None,
        type_: typing.Optional[
            str
        ] = None,
        description: typing.Optional[
            str
        ] = None
    ) -> None:
        self.id_ = id_
        self.name = name
        self.options = options
        self.type_ = type_
        self.description = description
        super().__init__(_data)


class TableFields(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TableField"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TableView(sob.model.Object):

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
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        type_: typing.Optional[
            str
        ] = None
    ) -> None:
        self.id_ = id_
        self.name = name
        self.type_ = type_
        super().__init__(_data)


class TableViews(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TableView"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class Table(sob.model.Object):

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
        fields: typing.Optional[
            "TableFields"
        ] = None,
        id_: typing.Optional[
            str
        ] = None,
        name: typing.Optional[
            str
        ] = None,
        primary_field_id: typing.Optional[
            str
        ] = None,
        views: typing.Optional[
            "TableViews"
        ] = None
    ) -> None:
        self.description = description
        self.fields = fields
        self.id_ = id_
        self.name = name
        self.primary_field_id = primary_field_id
        self.views = views
        super().__init__(_data)


class Tables(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Table"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MetaBasesBaseIdTablesGetResponse(sob.model.Object):

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
        tables: typing.Optional[
            "Tables"
        ] = None
    ) -> None:
        self.tables = tables
        super().__init__(_data)


class RecordFields(sob.model.Dictionary):

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                typing.Optional[sob.abc.MarshallableTypes]
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    typing.Optional[sob.abc.MarshallableTypes]
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class Record(sob.model.Object):

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
        created_time: typing.Optional[
            datetime.datetime
        ] = None,
        fields: typing.Optional[
            "RecordFields"
        ] = None,
        id_: typing.Optional[
            str
        ] = None
    ) -> None:
        self.created_time = created_time
        self.fields = fields
        self.id_ = id_
        super().__init__(_data)


class Records(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Record"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BaseIdTableGetResponse(sob.model.Object):

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
        records: typing.Optional[
            "Records"
        ] = None,
        offset: typing.Optional[
            str
        ] = None
    ) -> None:
        self.records = records
        self.offset = offset
        super().__init__(_data)


class Fields(sob.model.Dictionary):

    def __init__(
        self,
        items: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                typing.Optional[sob.abc.MarshallableTypes]
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    typing.Optional[sob.abc.MarshallableTypes]
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
    ) -> None:
        super().__init__(items)


class BaseIdTableRecordIdGetResponse(sob.model.Object):

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
        created_time: typing.Optional[
            datetime.datetime
        ] = None,
        fields: typing.Optional[
            "Fields"
        ] = None,
        id_: typing.Optional[
            str
        ] = None
    ) -> None:
        self.created_time = created_time
        self.fields = fields
        self.id_ = id_
        super().__init__(_data)


sob.meta.object_writable(  # type: ignore
    Base
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    ),
    (
        'permission_level',
        sob.properties.String(
            name="permissionLevel"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Bases
).item_types = sob.types.MutableTypes([
    Base
])
sob.meta.object_writable(  # type: ignore
    MetaBasesGetResponse
).properties = sob.meta.Properties([
    (
        'bases',
        sob.properties.Property(
            name="bases",
            types=sob.types.MutableTypes([
                Bases
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsChoice
).properties = sob.meta.Properties([
    (
        'color',
        sob.properties.String(
            name="color"
        )
    ),
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TableFieldOptionsChoices
).item_types = sob.types.MutableTypes([
    TableFieldOptionsChoice
])
sob.meta.array_writable(  # type: ignore
    TableFieldOptionsReferencedFieldIds
).item_types = sob.types.MutableTypes([
    str
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsResultOptionsDateFormat
).properties = sob.meta.Properties([
    (
        'format_',
        sob.properties.String(
            name="format"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsResultOptionsTimeFormat
).properties = sob.meta.Properties([
    (
        'format_',
        sob.properties.String(
            name="format"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsResultOptionsChoice
).properties = sob.meta.Properties([
    (
        'color',
        sob.properties.String(
            name="color"
        )
    ),
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TableFieldOptionsResultOptionsChoices
).item_types = sob.types.MutableTypes([
    TableFieldOptionsResultOptionsChoice
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsResultOptions
).properties = sob.meta.Properties([
    (
        'precision',
        sob.properties.Integer(
            name="precision"
        )
    ),
    (
        'symbol',
        sob.properties.String(
            name="symbol"
        )
    ),
    (
        'date_format',
        sob.properties.Property(
            name="dateFormat",
            types=sob.types.MutableTypes([
                TableFieldOptionsResultOptionsDateFormat
            ])
        )
    ),
    (
        'time_format',
        sob.properties.Property(
            name="timeFormat",
            types=sob.types.MutableTypes([
                TableFieldOptionsResultOptionsTimeFormat
            ])
        )
    ),
    (
        'time_zone',
        sob.properties.String(
            name="timeZone"
        )
    ),
    (
        'choices',
        sob.properties.Property(
            name="choices",
            types=sob.types.MutableTypes([
                TableFieldOptionsResultOptionsChoices
            ])
        )
    ),
    (
        'is_reversed',
        sob.properties.Boolean(
            name="isReversed"
        )
    ),
    (
        'prefers_single_record_link',
        sob.properties.Boolean(
            name="prefersSingleRecordLink"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsResult
).properties = sob.meta.Properties([
    (
        'type_',
        sob.properties.String(
            name="type"
        )
    ),
    (
        'options',
        sob.properties.Property(
            name="options",
            types=sob.types.MutableTypes([
                TableFieldOptionsResultOptions
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsDateFormat
).properties = sob.meta.Properties([
    (
        'format_',
        sob.properties.String(
            name="format"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptionsTimeFormat
).properties = sob.meta.Properties([
    (
        'format_',
        sob.properties.String(
            name="format"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableFieldOptions
).properties = sob.meta.Properties([
    (
        'precision',
        sob.properties.Integer(
            name="precision"
        )
    ),
    (
        'choices',
        sob.properties.Property(
            name="choices",
            types=sob.types.MutableTypes([
                TableFieldOptionsChoices
            ])
        )
    ),
    (
        'inverse_link_field_id',
        sob.properties.String(
            name="inverseLinkFieldId"
        )
    ),
    (
        'is_reversed',
        sob.properties.Boolean(
            name="isReversed"
        )
    ),
    (
        'linked_table_id',
        sob.properties.String(
            name="linkedTableId"
        )
    ),
    (
        'prefers_single_record_link',
        sob.properties.Boolean(
            name="prefersSingleRecordLink"
        )
    ),
    (
        'field_id_in_linked_table',
        sob.properties.Property(
            name="fieldIdInLinkedTable",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_valid',
        sob.properties.Boolean(
            name="isValid"
        )
    ),
    (
        'record_link_field_id',
        sob.properties.Property(
            name="recordLinkFieldId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'referenced_field_ids',
        sob.properties.Property(
            name="referencedFieldIds",
            types=sob.types.MutableTypes([
                TableFieldOptionsReferencedFieldIds
            ])
        )
    ),
    (
        'result',
        sob.properties.Property(
            name="result",
            types=sob.types.MutableTypes([
                TableFieldOptionsResult,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'date_format',
        sob.properties.Property(
            name="dateFormat",
            types=sob.types.MutableTypes([
                TableFieldOptionsDateFormat
            ])
        )
    ),
    (
        'symbol',
        sob.properties.String(
            name="symbol"
        )
    ),
    (
        'color',
        sob.properties.String(
            name="color"
        )
    ),
    (
        'icon',
        sob.properties.String(
            name="icon"
        )
    ),
    (
        'formula',
        sob.properties.String(
            name="formula"
        )
    ),
    (
        'time_format',
        sob.properties.Property(
            name="timeFormat",
            types=sob.types.MutableTypes([
                TableFieldOptionsTimeFormat
            ])
        )
    ),
    (
        'time_zone',
        sob.properties.String(
            name="timeZone"
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TableField
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    ),
    (
        'options',
        sob.properties.Property(
            name="options",
            types=sob.types.MutableTypes([
                TableFieldOptions
            ])
        )
    ),
    (
        'type_',
        sob.properties.String(
            name="type"
        )
    ),
    (
        'description',
        sob.properties.String(
            name="description"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TableFields
).item_types = sob.types.MutableTypes([
    TableField
])
sob.meta.object_writable(  # type: ignore
    TableView
).properties = sob.meta.Properties([
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    ),
    (
        'type_',
        sob.properties.String(
            name="type"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TableViews
).item_types = sob.types.MutableTypes([
    TableView
])
sob.meta.object_writable(  # type: ignore
    Table
).properties = sob.meta.Properties([
    (
        'description',
        sob.properties.String(
            name="description"
        )
    ),
    (
        'fields',
        sob.properties.Property(
            name="fields",
            types=sob.types.MutableTypes([
                TableFields
            ])
        )
    ),
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    ),
    (
        'name',
        sob.properties.String(
            name="name"
        )
    ),
    (
        'primary_field_id',
        sob.properties.String(
            name="primaryFieldId"
        )
    ),
    (
        'views',
        sob.properties.Property(
            name="views",
            types=sob.types.MutableTypes([
                TableViews
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Tables
).item_types = sob.types.MutableTypes([
    Table
])
sob.meta.object_writable(  # type: ignore
    MetaBasesBaseIdTablesGetResponse
).properties = sob.meta.Properties([
    (
        'tables',
        sob.properties.Property(
            name="tables",
            types=sob.types.MutableTypes([
                Tables
            ])
        )
    )
])
sob.meta.dictionary_writable(  # type: ignore
    RecordFields
).value_types = None
sob.meta.object_writable(  # type: ignore
    Record
).properties = sob.meta.Properties([
    (
        'created_time',
        sob.properties.DateTime(
            name="createdTime"
        )
    ),
    (
        'fields',
        sob.properties.Property(
            name="fields",
            types=sob.types.MutableTypes([
                RecordFields
            ])
        )
    ),
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    )
])
sob.meta.array_writable(  # type: ignore
    Records
).item_types = sob.types.MutableTypes([
    Record
])
sob.meta.object_writable(  # type: ignore
    BaseIdTableGetResponse
).properties = sob.meta.Properties([
    (
        'records',
        sob.properties.Property(
            name="records",
            types=sob.types.MutableTypes([
                Records
            ])
        )
    ),
    (
        'offset',
        sob.properties.String(
            name="offset"
        )
    )
])
sob.meta.dictionary_writable(  # type: ignore
    Fields
).value_types = None
sob.meta.object_writable(  # type: ignore
    BaseIdTableRecordIdGetResponse
).properties = sob.meta.Properties([
    (
        'created_time',
        sob.properties.DateTime(
            name="createdTime"
        )
    ),
    (
        'fields',
        sob.properties.Property(
            name="fields",
            types=sob.types.MutableTypes([
                Fields
            ])
        )
    ),
    (
        'id_',
        sob.properties.String(
            name="id"
        )
    )
])
