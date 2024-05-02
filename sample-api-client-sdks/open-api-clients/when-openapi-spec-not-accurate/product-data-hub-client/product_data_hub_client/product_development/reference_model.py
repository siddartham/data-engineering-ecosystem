import datetime
import typing
import sob


class Error(sob.model.Object):
    """
    Properties:

    - code
    - detail_type
    - message
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
        code: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        detail_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        message: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.code = code
        self.detail_type = detail_type
        self.message = message
        super().__init__(_data)


class Links(sob.model.Object):
    """
    Properties:

    - rel:
      The type of relationship
    - href:
      The reference link
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
        rel: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        href: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.rel = rel
        self.href = href
        super().__init__(_data)


class Reference(sob.model.Object):
    """
    Properties:

    - reference_key:
      The key for the described field
    - link
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
        reference_key: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        link: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.reference_key = reference_key
        self.link = link
        super().__init__(_data)


class BillOfMaterialsSection(sob.model.Object):
    """
    Properties:

    - bom_section_identifier:
      None
    - bom_section_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
    - availablefor_use_indicator
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
        bom_section_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_section_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        availablefor_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_section_identifier = bom_section_identifier
        self.bom_section_name = bom_section_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        self.availablefor_use_indicator = availablefor_use_indicator
        super().__init__(_data)


class BillOfMaterialsSectionBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
    - self_
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
            typing.Union[
                "BillOfMaterialsSectionBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        self.self_ = self_
        super().__init__(_data)


class BillOfMaterialsSectionBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BillOfMaterialsSectionBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BillOfMaterialsSectionBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "BillOfMaterialsSection",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class BillOfMaterialsSectionResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
    - self_
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
            typing.Union[
                "BillOfMaterialsSectionResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        self.self_ = self_
        super().__init__(_data)


class BillOfMaterialsSectionResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "BillOfMaterialsSection",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class BillOfMaterialsUnitOfMeasurement(sob.model.Object):
    """
    Properties:

    - bom_unit_of_measurement_identifier:
      None
    - bom_unit_of_measurement_description:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        bom_unit_of_measurement_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_unit_of_measurement_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_unit_of_measurement_identifier = (
            bom_unit_of_measurement_identifier
        )
        self.bom_unit_of_measurement_description = (
            bom_unit_of_measurement_description
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class BillOfMaterialsUnitOfMeasurementBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "BillOfMaterialsUnitOfMeasurementBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class BillOfMaterialsUnitOfMeasurementBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BillOfMaterialsUnitOfMeasurementBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BillOfMaterialsUnitOfMeasurementBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "BillOfMaterialsUnitOfMeasurement",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class BillOfMaterialsUnitOfMeasurementResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
    - self_
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
            typing.Union[
                "BillOfMaterialsUnitOfMeasurementResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        self.self_ = self_
        super().__init__(_data)


class BillOfMaterialsUnitOfMeasurementResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "BillOfMaterialsUnitOfMeasurement",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayGate(sob.model.Object):
    """
    Properties:

    - development_colorway_gate_identifier:
      None
    - development_colorway_gate_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_colorway_gate_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_gate_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_gate_identifier = (
            development_colorway_gate_identifier
        )
        self.development_colorway_gate_name = development_colorway_gate_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentColorwayGateBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayGateBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayGateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentColorwayGateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentColorwayGateBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayGate",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayGateResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayGateResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayGateResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayGate",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayState(sob.model.Object):
    """
    Properties:

    - development_colorway_state_identifier:
      None
    - development_colorway_state_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_colorway_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_state_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_state_identifier = (
            development_colorway_state_identifier
        )
        self.development_colorway_state_name = development_colorway_state_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentColorwayStateBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayStateBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentColorwayStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentColorwayStateBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayStateResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayStateResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayStateResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayType(sob.model.Object):
    """
    Properties:

    - development_colorway_type_identifier:
      None
    - development_colorway_type_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_colorway_type_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_type_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_type_identifier = (
            development_colorway_type_identifier
        )
        self.development_colorway_type_name = development_colorway_type_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentColorwayTypeBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayTypeBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayTypeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentColorwayTypeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentColorwayTypeBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentColorwayTypeResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentColorwayTypeResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentColorwayTypeResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentColorwayType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleChangeRequestReason(sob.model.Object):
    """
    Properties:

    - development_sample_change_request_reason_identifier:
      None
    - development_sample_change_request_reason_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_change_request_reason_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_change_request_reason_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_change_request_reason_identifier = (
            development_sample_change_request_reason_identifier
        )
        self.development_sample_change_request_reason_name = (
            development_sample_change_request_reason_name
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleChangeRequestReasonBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleChangeRequestReasonBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleChangeRequestReasonBulkResponseContents(
    sob.model.Array
):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleChangeRequestReasonBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleChangeRequestReasonBulkResponseContent(
    sob.model.Object
):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleChangeRequestReason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleChangeRequestReasonResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleChangeRequestReasonResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleChangeRequestReasonResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleChangeRequestReason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleEvaluationState(sob.model.Object):
    """
    Properties:

    - development_sample_evaluation_state_identifier:
      None
    - development_sample_evaluation_state_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_evaluation_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_evaluation_state_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_evaluation_state_identifier = (
            development_sample_evaluation_state_identifier
        )
        self.development_sample_evaluation_state_name = (
            development_sample_evaluation_state_name
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleEvaluationStateBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleEvaluationStateBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleEvaluationStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleEvaluationStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleEvaluationStateBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleEvaluationState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleEvaluationStateResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleEvaluationStateResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleEvaluationStateResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleEvaluationState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleFabricInstruction(sob.model.Object):
    """
    Properties:

    - development_sample_fabric_instruction_identifier:
      None
    - development_sample_fabric_instruction_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_fabric_instruction_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_fabric_instruction_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_fabric_instruction_identifier = (
            development_sample_fabric_instruction_identifier
        )
        self.development_sample_fabric_instruction_name = (
            development_sample_fabric_instruction_name
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleFabricInstructionBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleFabricInstructionBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleFabricInstructionBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleFabricInstructionBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleFabricInstructionBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleFabricInstruction",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleFabricInstructionResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleFabricInstructionResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleFabricInstructionResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleFabricInstruction",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleFormat(sob.model.Object):
    """
    Properties:

    - development_sample_format_identifier:
      None
    - development_sample_format_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_format_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_format_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_format_identifier = (
            development_sample_format_identifier
        )
        self.development_sample_format_name = development_sample_format_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleFormatBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleFormatBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleFormatBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleFormatBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleFormatBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleFormat",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleFormatResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleFormatResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleFormatResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleFormat",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSamplePurpose(sob.model.Object):
    """
    Properties:

    - development_sample_purpose_identifier:
      None
    - development_sample_purpose_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_purpose_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_purpose_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_purpose_identifier = (
            development_sample_purpose_identifier
        )
        self.development_sample_purpose_name = development_sample_purpose_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSamplePurposeBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSamplePurposeBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSamplePurposeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSamplePurposeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSamplePurposeBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSamplePurpose",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSamplePurposeResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSamplePurposeResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSamplePurposeResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSamplePurpose",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleQuoteRequirement(sob.model.Object):
    """
    Properties:

    - development_sample_quote_requirement_identifier:
      None
    - development_sample_quote_requirement_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_quote_requirement_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_quote_requirement_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_quote_requirement_identifier = (
            development_sample_quote_requirement_identifier
        )
        self.development_sample_quote_requirement_name = (
            development_sample_quote_requirement_name
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleQuoteRequirementBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleQuoteRequirementBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleQuoteRequirementBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleQuoteRequirementBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleQuoteRequirementBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleQuoteRequirement",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleQuoteRequirementResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleQuoteRequirementResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleQuoteRequirementResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleQuoteRequirement",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleState(sob.model.Object):
    """
    Properties:

    - development_sample_state_identifier:
      None
    - development_sample_state_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_state_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_state_identifier = (
            development_sample_state_identifier
        )
        self.development_sample_state_name = development_sample_state_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleStateBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleStateBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleStateBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleStateResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleStateResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleStateResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleType(sob.model.Object):
    """
    Properties:

    - development_sample_type_identifier:
      None
    - development_sample_type_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_sample_type_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_type_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_type_identifier = (
            development_sample_type_identifier
        )
        self.development_sample_type_name = development_sample_type_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentSampleTypeBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleTypeBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleTypeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentSampleTypeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentSampleTypeBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentSampleTypeResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentSampleTypeResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentSampleTypeResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentSampleType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentStyleType(sob.model.Object):
    """
    Properties:

    - development_style_type_identifier:
      None
    - development_style_type_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_style_type_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_type_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_type_identifier = (
            development_style_type_identifier
        )
        self.development_style_type_name = development_style_type_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentStyleTypeBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentStyleTypeBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentStyleTypeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentStyleTypeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentStyleTypeBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentStyleType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentStyleTypeResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentStyleTypeResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentStyleTypeResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentStyleType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTeam(sob.model.Object):
    """
    Properties:

    - development_team_identifier:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FDevelopment%2520Team%2520Identifier">Definition</a>
    - development_team_name:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FDevelopment%2520Team%2520Name">Definition</a>
    - development_team_description
    - development_team_abbreviation:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FConsumer%2520Use%2520Abbreviation">Definition</a>
    - available_for_use_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FAvailable%2520For%2520Use%2520Indicator">Definition</a>
    - status_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FStatus%2520Indicator">Definition</a>
    - by_division
    - created_by:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FCreated%2520By%2520Name">Definition</a>
    - create_timestamp:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FCreate%2520Timestamp">Definition</a>
    - modified_by:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FModified%2520By%2520Name">Definition</a>
    - change_timestamp:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FChange%2520Timestamp">Definition</a>
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
        development_team_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_team_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_team_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_team_abbreviation: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        by_division: typing.Optional[
            typing.Union[
                "DevelopmentTeamByDivisions",
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_team_identifier = development_team_identifier
        self.development_team_name = development_team_name
        self.development_team_description = development_team_description
        self.development_team_abbreviation = development_team_abbreviation
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.by_division = by_division
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentTeamByDivisions(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentTeamByDivision"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentTeamByDivision(sob.model.Object):
    """
    Properties:

    - division
    - available_for_use_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FAvailable%2520For%2520Use%2520Indicator">Definition</a>
    - status_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FStatus%2520Indicator">Definition</a>
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FChange%2520Timestamp">Definition</a>
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
        division: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.division = division
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentTeamBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - self_
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTeamBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.self_ = self_
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTeamBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentTeamBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentTeamBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTeam",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTeamGroup(sob.model.Object):
    """
    Properties:

    - development_team_group_identifier:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FDevelopment%2520Team%2520Identifier">Definition</a>
    - development_team_group_name:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FDevelopment%2520Team%2520Name">Definition</a>
    - available_for_use_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FAvailable%2520For%2520Use%2520Indicator">Definition</a>
    - status_indicator:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FStatus%2520Indicator">Definition</a>
    - created_by:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FCreated%2520By%2520Name">Definition</a>
    - create_timestamp:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FCreate%2520Timestamp">Definition</a>
    - modified_by:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FModified%2520By%2520Name">Definition</a>
    - change_timestamp:
      <a target="_blank" href ="http://nke-lnx-int-q013:10250/mm/#
      browse___glossary___MM%252FNike%2520Approved%2520Terms%252FBusiness%
      2520Term%252FChange%2520Timestamp">Definition</a>
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
        development_team_group_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_team_group_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_team_group_identifier = (
            development_team_group_identifier
        )
        self.development_team_group_name = development_team_group_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentTeamGroupBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - self_
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTeamGroupBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.self_ = self_
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTeamGroupBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentTeamGroupBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentTeamGroupBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTeamGroup",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTeamGroupResponse(sob.model.Object):
    """
    Properties:

    - content
    - self_
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTeamGroupResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTeamGroupResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTeamGroup",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTeamResponse(sob.model.Object):
    """
    Properties:

    - content
    - self_
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTeamResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTeamResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTeam",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTrack(sob.model.Object):
    """
    Properties:

    - development_track_identifier:
      None
    - development_track_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        development_track_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_track_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_track_identifier = development_track_identifier
        self.development_track_name = development_track_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class DevelopmentTrackBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTrackBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTrackBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentTrackBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentTrackBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTrack",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentTrackResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "DevelopmentTrackResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class DevelopmentTrackResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "DevelopmentTrack",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class GoodsAtConsolidatorReason(sob.model.Object):
    """
    Properties:

    - goods_at_consolidator_reason_code:
      None
    - goods_at_consolidator_reason_description:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        goods_at_consolidator_reason_code: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        goods_at_consolidator_reason_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.goods_at_consolidator_reason_code = (
            goods_at_consolidator_reason_code
        )
        self.goods_at_consolidator_reason_description = (
            goods_at_consolidator_reason_description
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class GoodsAtConsolidatorReasonBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "GoodsAtConsolidatorReasonBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class GoodsAtConsolidatorReasonBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "GoodsAtConsolidatorReasonBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class GoodsAtConsolidatorReasonBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "GoodsAtConsolidatorReason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class GoodsAtConsolidatorReasonResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "GoodsAtConsolidatorReasonResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class GoodsAtConsolidatorReasonResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "GoodsAtConsolidatorReason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class MeasurementSetState(sob.model.Object):
    """
    Properties:

    - measurement_set_state_identifier:
      None
    - measurement_set_state_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        measurement_set_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_set_state_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_set_state_identifier = (
            measurement_set_state_identifier
        )
        self.measurement_set_state_name = measurement_set_state_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class MeasurementSetStateBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "MeasurementSetStateBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class MeasurementSetStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "MeasurementSetStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MeasurementSetStateBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "MeasurementSetState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class MeasurementSetStateResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "MeasurementSetStateResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class MeasurementSetStateResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "MeasurementSetState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class MeasurementTemplateType(sob.model.Object):
    """
    Properties:

    - measurement_template_type_identifier:
      None
    - measurement_template_type_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        measurement_template_type_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_template_type_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_template_type_identifier = (
            measurement_template_type_identifier
        )
        self.measurement_template_type_name = measurement_template_type_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class MeasurementTemplateTypeBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "MeasurementTemplateTypeBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class MeasurementTemplateTypeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "MeasurementTemplateTypeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MeasurementTemplateTypeBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "MeasurementTemplateType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class MeasurementTemplateTypeResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "MeasurementTemplateTypeResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class MeasurementTemplateTypeResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "MeasurementTemplateType",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class NikeProductionTrial(sob.model.Object):
    """
    Properties:

    - nike_production_trial_identifier:
      None
    - nike_production_trial_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        nike_production_trial_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_production_trial_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.nike_production_trial_identifier = (
            nike_production_trial_identifier
        )
        self.nike_production_trial_name = nike_production_trial_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class NikeProductionTrialBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "NikeProductionTrialBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class NikeProductionTrialBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "NikeProductionTrialBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class NikeProductionTrialBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "NikeProductionTrial",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class NikeProductionTrialResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "NikeProductionTrialResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class NikeProductionTrialResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "NikeProductionTrial",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartModifier(sob.model.Object):
    """
    Properties:

    - part_modifier_identifier:
      None
    - part_modifier_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        part_modifier_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_modifier_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_modifier_identifier = part_modifier_identifier
        self.part_modifier_name = part_modifier_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PartModifierBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartModifierBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartModifierBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartModifierBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartModifierBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartModifier",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartModifierResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartModifierResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartModifierResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartModifier",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartName(sob.model.Object):
    """
    Properties:

    - part_name_identifier:
      None
    - part_name:
      None
    - part_short_name:
      None
    - is_aggregate_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
    - division
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
        part_name_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        part_short_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        is_aggregate_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        division: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_name_identifier = part_name_identifier
        self.part_name = part_name
        self.part_short_name = part_short_name
        self.is_aggregate_indicator = is_aggregate_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        self.division = division
        super().__init__(_data)


class PartNameBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartNameBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartNameBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartNameBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartNameBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartName",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartNameResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
    - self_
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
            typing.Union[
                "PartNameResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        self_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        self.self_ = self_
        super().__init__(_data)


class PartNameResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartName",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartPrefix(sob.model.Object):
    """
    Properties:

    - part_prefix_identifier:
      None
    - part_prefix_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        part_prefix_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_prefix_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_prefix_identifier = part_prefix_identifier
        self.part_prefix_name = part_prefix_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PartPrefixBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartPrefixBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartPrefixBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartPrefixBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartPrefixBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartPrefix",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartPrefixResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartPrefixResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartPrefixResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartPrefix",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartPrimary(sob.model.Object):
    """
    Properties:

    - part_primary_identifier:
      None
    - part_primary_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        part_primary_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_primary_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_primary_identifier = part_primary_identifier
        self.part_primary_name = part_primary_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PartPrimaryBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartPrimaryBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartPrimaryBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartPrimaryBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartPrimaryBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartPrimary",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartPrimaryResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartPrimaryResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartPrimaryResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartPrimary",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartSecondary(sob.model.Object):
    """
    Properties:

    - part_secondary_identifier:
      None
    - part_secondary_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        part_secondary_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_secondary_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_secondary_identifier = part_secondary_identifier
        self.part_secondary_name = part_secondary_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PartSecondaryBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartSecondaryBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartSecondaryBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartSecondaryBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartSecondaryBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartSecondary",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartSecondaryResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartSecondaryResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartSecondaryResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartSecondary",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartSuffix(sob.model.Object):
    """
    Properties:

    - part_suffix_identifier:
      None
    - part_suffix_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        part_suffix_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        part_suffix_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.part_suffix_identifier = part_suffix_identifier
        self.part_suffix_name = part_suffix_name
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PartSuffixBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartSuffixBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartSuffixBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PartSuffixBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PartSuffixBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartSuffix",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PartSuffixResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PartSuffixResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PartSuffixResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PartSuffix",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PointOfMeasurementCriticality(sob.model.Object):
    """
    Properties:

    - point_of_measurement_criticality_identifier:
      None
    - point_of_measurement_criticality_name:
      None
    - division_code:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        point_of_measurement_criticality_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_criticality_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.point_of_measurement_criticality_identifier = (
            point_of_measurement_criticality_identifier
        )
        self.point_of_measurement_criticality_name = (
            point_of_measurement_criticality_name
        )
        self.division_code = division_code
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PointOfMeasurementCriticalityBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PointOfMeasurementCriticalityBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PointOfMeasurementCriticalityBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PointOfMeasurementCriticalityBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PointOfMeasurementCriticalityBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PointOfMeasurementCriticality",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class PointOfMeasurementCriticalityResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "PointOfMeasurementCriticalityResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class PointOfMeasurementCriticalityResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "PointOfMeasurementCriticality",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class ProductTrack(sob.model.Object):
    """
    Properties:

    - product_track_identifier:
      None
    - product_track_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        product_track_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        product_track_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.product_track_identifier = product_track_identifier
        self.product_track_name = product_track_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class ProductTrackBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "ProductTrackBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class ProductTrackBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ProductTrackBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ProductTrackBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "ProductTrack",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class ProductTrackResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "ProductTrackResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class ProductTrackResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "ProductTrack",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class ShippingService(sob.model.Object):
    """
    Properties:

    - shipping_service_identifier:
      None
    - shipping_service_name:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        shipping_service_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        shipping_service_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.shipping_service_identifier = shipping_service_identifier
        self.shipping_service_name = shipping_service_name
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class ShippingServiceBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "ShippingServiceBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class ShippingServiceBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ShippingServiceBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ShippingServiceBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "ShippingService",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class ShippingServiceResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "ShippingServiceResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class ShippingServiceResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "ShippingService",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TechnicalDifficulty(sob.model.Object):
    """
    Properties:

    - technical_difficulty_identifier:
      None
    - technical_difficulty_code:
      None
    - technical_difficulty_description:
      None
    - available_for_use_indicator:
      None
    - status_indicator:
      None
    - nike_new_upper:
      None
    - nike_new_midsole:
      None
    - nike_new_outsole:
      None
    - created_by:
      None
    - create_timestamp:
      None
    - modified_by:
      None
    - change_timestamp:
      None
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
        technical_difficulty_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        technical_difficulty_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        technical_difficulty_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        available_for_use_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_new_upper: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_new_midsole: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_new_outsole: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.technical_difficulty_identifier = technical_difficulty_identifier
        self.technical_difficulty_code = technical_difficulty_code
        self.technical_difficulty_description = (
            technical_difficulty_description
        )
        self.available_for_use_indicator = available_for_use_indicator
        self.status_indicator = status_indicator
        self.nike_new_upper = nike_new_upper
        self.nike_new_midsole = nike_new_midsole
        self.nike_new_outsole = nike_new_outsole
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class TechnicalDifficultyBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - total_count:
      The number of entries returned in this responses
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "TechnicalDifficultyBulkResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.total_count = total_count
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class TechnicalDifficultyBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TechnicalDifficultyBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TechnicalDifficultyBulkResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "TechnicalDifficulty",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TechnicalDifficultyResponse(sob.model.Object):
    """
    Properties:

    - content
    - request_time:
      A UTC timestamp for when the response was given, also for tracking
      purposes
    - request_status:
      This is a status code that will list out the status of the request, e.g.
      success, partial or something to tell the user what has happened
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
            typing.Union[
                "TechnicalDifficultyResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        request_time: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        request_status: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.content = content
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class TechnicalDifficultyResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
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
        object_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        object_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        data: typing.Optional[
            typing.Union[
                "TechnicalDifficulty",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


sob.meta.object_writable(  # type: ignore
    Error
).properties = sob.meta.Properties([
    (
        'code',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'detail_type',
        sob.properties.Property(
            name="detailType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'message',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Links
).properties = sob.meta.Properties([
    (
        'rel',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'href',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    Reference
).properties = sob.meta.Properties([
    (
        'reference_key',
        sob.properties.Property(
            name="referenceKey",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'link',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSection
).properties = sob.meta.Properties([
    (
        'bom_section_identifier',
        sob.properties.Property(
            name="bomSectionIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_section_name',
        sob.properties.Property(
            name="bomSectionName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'availablefor_use_indicator',
        sob.properties.Property(
            name="availableforUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSectionBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSectionBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BillOfMaterialsSectionBulkResponseContents
).item_types = sob.types.MutableTypes([
    BillOfMaterialsSectionBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSectionBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSection,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSectionResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSectionResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSectionResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSection,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurement
).properties = sob.meta.Properties([
    (
        'bom_unit_of_measurement_identifier',
        sob.properties.Property(
            name="bomUnitOfMeasurementIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_unit_of_measurement_description',
        sob.properties.Property(
            name="bomUnitOfMeasurementDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurementBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsUnitOfMeasurementBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurementBulkResponseContents
).item_types = sob.types.MutableTypes([
    BillOfMaterialsUnitOfMeasurementBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurementBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsUnitOfMeasurement,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurementResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsUnitOfMeasurementResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsUnitOfMeasurementResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsUnitOfMeasurement,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayGate
).properties = sob.meta.Properties([
    (
        'development_colorway_gate_identifier',
        sob.properties.Property(
            name="developmentColorwayGateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_gate_name',
        sob.properties.Property(
            name="developmentColorwayGateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayGateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayGateBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentColorwayGateBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentColorwayGateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayGateBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayGate,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayGateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayGateResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayGateResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayGate,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayState
).properties = sob.meta.Properties([
    (
        'development_colorway_state_identifier',
        sob.properties.Property(
            name="developmentColorwayStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_state_name',
        sob.properties.Property(
            name="developmentColorwayStateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayStateBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentColorwayStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentColorwayStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayStateBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayStateResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayStateResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayType
).properties = sob.meta.Properties([
    (
        'development_colorway_type_identifier',
        sob.properties.Property(
            name="developmentColorwayTypeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_type_name',
        sob.properties.Property(
            name="developmentColorwayTypeName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayTypeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayTypeBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentColorwayTypeBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentColorwayTypeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayTypeBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayTypeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayTypeResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayTypeResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleChangeRequestReason
).properties = sob.meta.Properties([
    (
        'development_sample_change_request_reason_identifier',
        sob.properties.Property(
            name="developmentSampleChangeRequestReasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_change_request_reason_name',
        sob.properties.Property(
            name="developmentSampleChangeRequestReasonName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleChangeRequestReasonBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleChangeRequestReasonBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleChangeRequestReasonBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleChangeRequestReasonBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleChangeRequestReasonBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleChangeRequestReason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleChangeRequestReasonResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleChangeRequestReasonResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleChangeRequestReasonResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleChangeRequestReason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleEvaluationState
).properties = sob.meta.Properties([
    (
        'development_sample_evaluation_state_identifier',
        sob.properties.Property(
            name="developmentSampleEvaluationStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_evaluation_state_name',
        sob.properties.Property(
            name="developmentSampleEvaluationStateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleEvaluationStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleEvaluationStateBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleEvaluationStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleEvaluationStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleEvaluationStateBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleEvaluationState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleEvaluationStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleEvaluationStateResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleEvaluationStateResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleEvaluationState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFabricInstruction
).properties = sob.meta.Properties([
    (
        'development_sample_fabric_instruction_identifier',
        sob.properties.Property(
            name="developmentSampleFabricInstructionIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_fabric_instruction_name',
        sob.properties.Property(
            name="developmentSampleFabricInstructionName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFabricInstructionBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFabricInstructionBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleFabricInstructionBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleFabricInstructionBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFabricInstructionBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFabricInstruction,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFabricInstructionResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFabricInstructionResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFabricInstructionResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFabricInstruction,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFormat
).properties = sob.meta.Properties([
    (
        'development_sample_format_identifier',
        sob.properties.Property(
            name="developmentSampleFormatIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_format_name',
        sob.properties.Property(
            name="developmentSampleFormatName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFormatBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFormatBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleFormatBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleFormatBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFormatBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFormat,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFormatResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFormatResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleFormatResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleFormat,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSamplePurpose
).properties = sob.meta.Properties([
    (
        'development_sample_purpose_identifier',
        sob.properties.Property(
            name="developmentSamplePurposeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_purpose_name',
        sob.properties.Property(
            name="developmentSamplePurposeName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSamplePurposeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSamplePurposeBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSamplePurposeBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSamplePurposeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSamplePurposeBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSamplePurpose,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSamplePurposeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSamplePurposeResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSamplePurposeResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSamplePurpose,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleQuoteRequirement
).properties = sob.meta.Properties([
    (
        'development_sample_quote_requirement_identifier',
        sob.properties.Property(
            name="developmentSampleQuoteRequirementIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_quote_requirement_name',
        sob.properties.Property(
            name="developmentSampleQuoteRequirementName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleQuoteRequirementBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleQuoteRequirementBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleQuoteRequirementBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleQuoteRequirementBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleQuoteRequirementBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleQuoteRequirement,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleQuoteRequirementResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleQuoteRequirementResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleQuoteRequirementResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleQuoteRequirement,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleState
).properties = sob.meta.Properties([
    (
        'development_sample_state_identifier',
        sob.properties.Property(
            name="developmentSampleStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_state_name',
        sob.properties.Property(
            name="developmentSampleStateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleStateBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleStateBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleStateResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleStateResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleType
).properties = sob.meta.Properties([
    (
        'development_sample_type_identifier',
        sob.properties.Property(
            name="developmentSampleTypeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_type_name',
        sob.properties.Property(
            name="developmentSampleTypeName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleTypeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleTypeBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentSampleTypeBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentSampleTypeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleTypeBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleTypeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleTypeResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleTypeResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleType
).properties = sob.meta.Properties([
    (
        'development_style_type_identifier',
        sob.properties.Property(
            name="developmentStyleTypeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_type_name',
        sob.properties.Property(
            name="developmentStyleTypeName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleTypeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentStyleTypeBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentStyleTypeBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentStyleTypeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleTypeBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentStyleType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleTypeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentStyleTypeResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleTypeResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentStyleType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeam
).properties = sob.meta.Properties([
    (
        'development_team_identifier',
        sob.properties.Property(
            name="developmentTeamIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_team_name',
        sob.properties.Property(
            name="developmentTeamName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_team_description',
        sob.properties.Property(
            name="developmentTeamDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_team_abbreviation',
        sob.properties.Property(
            name="developmentTeamAbbreviation",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'by_division',
        sob.properties.Property(
            name="byDivision",
            types=sob.types.MutableTypes([
                DevelopmentTeamByDivisions,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentTeamByDivisions
).item_types = sob.types.MutableTypes([
    DevelopmentTeamByDivision
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamByDivision
).properties = sob.meta.Properties([
    (
        'division',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentTeamBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentTeamBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeam,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamGroup
).properties = sob.meta.Properties([
    (
        'development_team_group_identifier',
        sob.properties.Property(
            name="developmentTeamGroupIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_team_group_name',
        sob.properties.Property(
            name="developmentTeamGroupName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamGroupBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamGroupBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentTeamGroupBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentTeamGroupBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamGroupBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamGroup,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamGroupResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamGroupResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamGroupResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamGroup,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeamResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTeamResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTeam,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTrack
).properties = sob.meta.Properties([
    (
        'development_track_identifier',
        sob.properties.Property(
            name="developmentTrackIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_track_name',
        sob.properties.Property(
            name="developmentTrackName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTrackBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTrackBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DevelopmentTrackBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentTrackBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTrackBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTrack,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTrackResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTrackResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentTrackResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentTrack,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    GoodsAtConsolidatorReason
).properties = sob.meta.Properties([
    (
        'goods_at_consolidator_reason_code',
        sob.properties.Property(
            name="goodsAtConsolidatorReasonCode",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'goods_at_consolidator_reason_description',
        sob.properties.Property(
            name="goodsAtConsolidatorReasonDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    GoodsAtConsolidatorReasonBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                GoodsAtConsolidatorReasonBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    GoodsAtConsolidatorReasonBulkResponseContents
).item_types = sob.types.MutableTypes([
    GoodsAtConsolidatorReasonBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    GoodsAtConsolidatorReasonBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                GoodsAtConsolidatorReason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    GoodsAtConsolidatorReasonResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                GoodsAtConsolidatorReasonResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    GoodsAtConsolidatorReasonResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                GoodsAtConsolidatorReason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementSetState
).properties = sob.meta.Properties([
    (
        'measurement_set_state_identifier',
        sob.properties.Property(
            name="measurementSetStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_set_state_name',
        sob.properties.Property(
            name="measurementSetStateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementSetStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementSetStateBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    MeasurementSetStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    MeasurementSetStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    MeasurementSetStateBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementSetState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementSetStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementSetStateResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementSetStateResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementSetState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementTemplateType
).properties = sob.meta.Properties([
    (
        'measurement_template_type_identifier',
        sob.properties.Property(
            name="measurementTemplateTypeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_template_type_name',
        sob.properties.Property(
            name="measurementTemplateTypeName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementTemplateTypeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementTemplateTypeBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    MeasurementTemplateTypeBulkResponseContents
).item_types = sob.types.MutableTypes([
    MeasurementTemplateTypeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    MeasurementTemplateTypeBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementTemplateType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementTemplateTypeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementTemplateTypeResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MeasurementTemplateTypeResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MeasurementTemplateType,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    NikeProductionTrial
).properties = sob.meta.Properties([
    (
        'nike_production_trial_identifier',
        sob.properties.Property(
            name="nikeProductionTrialIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_production_trial_name',
        sob.properties.Property(
            name="nikeProductionTrialName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    NikeProductionTrialBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                NikeProductionTrialBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    NikeProductionTrialBulkResponseContents
).item_types = sob.types.MutableTypes([
    NikeProductionTrialBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    NikeProductionTrialBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                NikeProductionTrial,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    NikeProductionTrialResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                NikeProductionTrialResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    NikeProductionTrialResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                NikeProductionTrial,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartModifier
).properties = sob.meta.Properties([
    (
        'part_modifier_identifier',
        sob.properties.Property(
            name="partModifierIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_modifier_name',
        sob.properties.Property(
            name="partModifierName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartModifierBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartModifierBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartModifierBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartModifierBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartModifierBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartModifier,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartModifierResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartModifierResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartModifierResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartModifier,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartName
).properties = sob.meta.Properties([
    (
        'part_name_identifier',
        sob.properties.Property(
            name="partNameIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_name',
        sob.properties.Property(
            name="partName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_short_name',
        sob.properties.Property(
            name="partShortName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'is_aggregate_indicator',
        sob.properties.Property(
            name="isAggregateIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartNameBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartNameBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartNameBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartNameBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartNameBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartName,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartNameResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartNameResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'self_',
        sob.properties.Property(
            name="self",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartNameResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartName,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrefix
).properties = sob.meta.Properties([
    (
        'part_prefix_identifier',
        sob.properties.Property(
            name="partPrefixIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_prefix_name',
        sob.properties.Property(
            name="partPrefixName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrefixBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrefixBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartPrefixBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartPrefixBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartPrefixBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrefix,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrefixResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrefixResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrefixResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrefix,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrimary
).properties = sob.meta.Properties([
    (
        'part_primary_identifier',
        sob.properties.Property(
            name="partPrimaryIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_primary_name',
        sob.properties.Property(
            name="partPrimaryName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrimaryBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrimaryBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartPrimaryBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartPrimaryBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartPrimaryBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrimary,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrimaryResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrimaryResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartPrimaryResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartPrimary,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSecondary
).properties = sob.meta.Properties([
    (
        'part_secondary_identifier',
        sob.properties.Property(
            name="partSecondaryIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_secondary_name',
        sob.properties.Property(
            name="partSecondaryName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSecondaryBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSecondaryBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartSecondaryBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartSecondaryBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartSecondaryBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSecondary,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSecondaryResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSecondaryResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSecondaryResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSecondary,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSuffix
).properties = sob.meta.Properties([
    (
        'part_suffix_identifier',
        sob.properties.Property(
            name="partSuffixIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_suffix_name',
        sob.properties.Property(
            name="partSuffixName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSuffixBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSuffixBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PartSuffixBulkResponseContents
).item_types = sob.types.MutableTypes([
    PartSuffixBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PartSuffixBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSuffix,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSuffixResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSuffixResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PartSuffixResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PartSuffix,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PointOfMeasurementCriticality
).properties = sob.meta.Properties([
    (
        'point_of_measurement_criticality_identifier',
        sob.properties.Property(
            name="pointOfMeasurementCriticalityIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_criticality_name',
        sob.properties.Property(
            name="pointOfMeasurementCriticalityName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'division_code',
        sob.properties.Property(
            name="divisionCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PointOfMeasurementCriticalityBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PointOfMeasurementCriticalityBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PointOfMeasurementCriticalityBulkResponseContents
).item_types = sob.types.MutableTypes([
    PointOfMeasurementCriticalityBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    PointOfMeasurementCriticalityBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PointOfMeasurementCriticality,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PointOfMeasurementCriticalityResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PointOfMeasurementCriticalityResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PointOfMeasurementCriticalityResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PointOfMeasurementCriticality,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ProductTrack
).properties = sob.meta.Properties([
    (
        'product_track_identifier',
        sob.properties.Property(
            name="productTrackIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_track_name',
        sob.properties.Property(
            name="productTrackName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ProductTrackBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProductTrackBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ProductTrackBulkResponseContents
).item_types = sob.types.MutableTypes([
    ProductTrackBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    ProductTrackBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProductTrack,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ProductTrackResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProductTrackResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ProductTrackResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ProductTrack,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ShippingService
).properties = sob.meta.Properties([
    (
        'shipping_service_identifier',
        sob.properties.Property(
            name="shippingServiceIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'shipping_service_name',
        sob.properties.Property(
            name="shippingServiceName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ShippingServiceBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ShippingServiceBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ShippingServiceBulkResponseContents
).item_types = sob.types.MutableTypes([
    ShippingServiceBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    ShippingServiceBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ShippingService,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ShippingServiceResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ShippingServiceResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ShippingServiceResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ShippingService,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TechnicalDifficulty
).properties = sob.meta.Properties([
    (
        'technical_difficulty_identifier',
        sob.properties.Property(
            name="technicalDifficultyIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'technical_difficulty_code',
        sob.properties.Property(
            name="technicalDifficultyCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'technical_difficulty_description',
        sob.properties.Property(
            name="technicalDifficultyDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'available_for_use_indicator',
        sob.properties.Property(
            name="availableForUseIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'status_indicator',
        sob.properties.Property(
            name="statusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_new_upper',
        sob.properties.Property(
            name="nikeNewUpper",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_new_midsole',
        sob.properties.Property(
            name="nikeNewMidsole",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_new_outsole',
        sob.properties.Property(
            name="nikeNewOutsole",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'created_by',
        sob.properties.Property(
            name="createdBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'create_timestamp',
        sob.properties.Property(
            name="createTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_timestamp',
        sob.properties.Property(
            name="changeTimestamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TechnicalDifficultyBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TechnicalDifficultyBulkResponseContents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'total_count',
        sob.properties.Property(
            name="totalCount",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    TechnicalDifficultyBulkResponseContents
).item_types = sob.types.MutableTypes([
    TechnicalDifficultyBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    TechnicalDifficultyBulkResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TechnicalDifficulty,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TechnicalDifficultyResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TechnicalDifficultyResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_time',
        sob.properties.Property(
            name="requestTime",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'request_status',
        sob.properties.Property(
            name="requestStatus",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TechnicalDifficultyResponseContent
).properties = sob.meta.Properties([
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_type',
        sob.properties.Property(
            name="objectType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'data',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TechnicalDifficulty,
                sob.utilities.types.Null
            ])
        )
    )
])
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/definitions/_error": Error,
    "#/definitions/_links": Links,
    "#/definitions/_reference": Reference,
    "#/definitions/billOfMaterialsSection": BillOfMaterialsSection,
    "#/definitions/billOfMaterialsSectionBulkResponse":
    BillOfMaterialsSectionBulkResponse,
    "#/definitions/billOfMaterialsSectionBulkResponse/properties/content":
    BillOfMaterialsSectionBulkResponseContents,
    "#/definitions/billOfMaterialsSectionBulkResponse/properties/content/items":  # noqa
    BillOfMaterialsSectionBulkResponseContent,
    "#/definitions/billOfMaterialsSectionResponse":
    BillOfMaterialsSectionResponse,
    "#/definitions/billOfMaterialsSectionResponse/properties/content":
    BillOfMaterialsSectionResponseContent,
    "#/definitions/billOfMaterialsUnitOfMeasurement":
    BillOfMaterialsUnitOfMeasurement,
    "#/definitions/billOfMaterialsUnitOfMeasurementBulkResponse":
    BillOfMaterialsUnitOfMeasurementBulkResponse,
    "#/definitions/billOfMaterialsUnitOfMeasurementBulkResponse/properties/content":  # noqa
    BillOfMaterialsUnitOfMeasurementBulkResponseContents,
    "#/definitions/billOfMaterialsUnitOfMeasurementBulkResponse/properties/content/items":  # noqa
    BillOfMaterialsUnitOfMeasurementBulkResponseContent,
    "#/definitions/billOfMaterialsUnitOfMeasurementResponse":
    BillOfMaterialsUnitOfMeasurementResponse,
    "#/definitions/billOfMaterialsUnitOfMeasurementResponse/properties/content":  # noqa
    BillOfMaterialsUnitOfMeasurementResponseContent,
    "#/definitions/developmentColorwayGate": DevelopmentColorwayGate,
    "#/definitions/developmentColorwayGateBulkResponse":
    DevelopmentColorwayGateBulkResponse,
    "#/definitions/developmentColorwayGateBulkResponse/properties/content":
    DevelopmentColorwayGateBulkResponseContents,
    "#/definitions/developmentColorwayGateBulkResponse/properties/content/items":  # noqa
    DevelopmentColorwayGateBulkResponseContent,
    "#/definitions/developmentColorwayGateResponse":
    DevelopmentColorwayGateResponse,
    "#/definitions/developmentColorwayGateResponse/properties/content":
    DevelopmentColorwayGateResponseContent,
    "#/definitions/developmentColorwayState": DevelopmentColorwayState,
    "#/definitions/developmentColorwayStateBulkResponse":
    DevelopmentColorwayStateBulkResponse,
    "#/definitions/developmentColorwayStateBulkResponse/properties/content":
    DevelopmentColorwayStateBulkResponseContents,
    "#/definitions/developmentColorwayStateBulkResponse/properties/content/items":  # noqa
    DevelopmentColorwayStateBulkResponseContent,
    "#/definitions/developmentColorwayStateResponse":
    DevelopmentColorwayStateResponse,
    "#/definitions/developmentColorwayStateResponse/properties/content":
    DevelopmentColorwayStateResponseContent,
    "#/definitions/developmentColorwayType": DevelopmentColorwayType,
    "#/definitions/developmentColorwayTypeBulkResponse":
    DevelopmentColorwayTypeBulkResponse,
    "#/definitions/developmentColorwayTypeBulkResponse/properties/content":
    DevelopmentColorwayTypeBulkResponseContents,
    "#/definitions/developmentColorwayTypeBulkResponse/properties/content/items":  # noqa
    DevelopmentColorwayTypeBulkResponseContent,
    "#/definitions/developmentColorwayTypeResponse":
    DevelopmentColorwayTypeResponse,
    "#/definitions/developmentColorwayTypeResponse/properties/content":
    DevelopmentColorwayTypeResponseContent,
    "#/definitions/developmentSampleChangeRequestReason":
    DevelopmentSampleChangeRequestReason,
    "#/definitions/developmentSampleChangeRequestReasonBulkResponse":
    DevelopmentSampleChangeRequestReasonBulkResponse,
    "#/definitions/developmentSampleChangeRequestReasonBulkResponse/properties/content":  # noqa
    DevelopmentSampleChangeRequestReasonBulkResponseContents,
    "#/definitions/developmentSampleChangeRequestReasonBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleChangeRequestReasonBulkResponseContent,
    "#/definitions/developmentSampleChangeRequestReasonResponse":
    DevelopmentSampleChangeRequestReasonResponse,
    "#/definitions/developmentSampleChangeRequestReasonResponse/properties/content":  # noqa
    DevelopmentSampleChangeRequestReasonResponseContent,
    "#/definitions/developmentSampleEvaluationState":
    DevelopmentSampleEvaluationState,
    "#/definitions/developmentSampleEvaluationStateBulkResponse":
    DevelopmentSampleEvaluationStateBulkResponse,
    "#/definitions/developmentSampleEvaluationStateBulkResponse/properties/content":  # noqa
    DevelopmentSampleEvaluationStateBulkResponseContents,
    "#/definitions/developmentSampleEvaluationStateBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleEvaluationStateBulkResponseContent,
    "#/definitions/developmentSampleEvaluationStateResponse":
    DevelopmentSampleEvaluationStateResponse,
    "#/definitions/developmentSampleEvaluationStateResponse/properties/content":  # noqa
    DevelopmentSampleEvaluationStateResponseContent,
    "#/definitions/developmentSampleFabricInstruction":
    DevelopmentSampleFabricInstruction,
    "#/definitions/developmentSampleFabricInstructionBulkResponse":
    DevelopmentSampleFabricInstructionBulkResponse,
    "#/definitions/developmentSampleFabricInstructionBulkResponse/properties/content":  # noqa
    DevelopmentSampleFabricInstructionBulkResponseContents,
    "#/definitions/developmentSampleFabricInstructionBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleFabricInstructionBulkResponseContent,
    "#/definitions/developmentSampleFabricInstructionResponse":
    DevelopmentSampleFabricInstructionResponse,
    "#/definitions/developmentSampleFabricInstructionResponse/properties/content":  # noqa
    DevelopmentSampleFabricInstructionResponseContent,
    "#/definitions/developmentSampleFormat": DevelopmentSampleFormat,
    "#/definitions/developmentSampleFormatBulkResponse":
    DevelopmentSampleFormatBulkResponse,
    "#/definitions/developmentSampleFormatBulkResponse/properties/content":
    DevelopmentSampleFormatBulkResponseContents,
    "#/definitions/developmentSampleFormatBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleFormatBulkResponseContent,
    "#/definitions/developmentSampleFormatResponse":
    DevelopmentSampleFormatResponse,
    "#/definitions/developmentSampleFormatResponse/properties/content":
    DevelopmentSampleFormatResponseContent,
    "#/definitions/developmentSamplePurpose": DevelopmentSamplePurpose,
    "#/definitions/developmentSamplePurposeBulkResponse":
    DevelopmentSamplePurposeBulkResponse,
    "#/definitions/developmentSamplePurposeBulkResponse/properties/content":
    DevelopmentSamplePurposeBulkResponseContents,
    "#/definitions/developmentSamplePurposeBulkResponse/properties/content/items":  # noqa
    DevelopmentSamplePurposeBulkResponseContent,
    "#/definitions/developmentSamplePurposeResponse":
    DevelopmentSamplePurposeResponse,
    "#/definitions/developmentSamplePurposeResponse/properties/content":
    DevelopmentSamplePurposeResponseContent,
    "#/definitions/developmentSampleQuoteRequirement":
    DevelopmentSampleQuoteRequirement,
    "#/definitions/developmentSampleQuoteRequirementBulkResponse":
    DevelopmentSampleQuoteRequirementBulkResponse,
    "#/definitions/developmentSampleQuoteRequirementBulkResponse/properties/content":  # noqa
    DevelopmentSampleQuoteRequirementBulkResponseContents,
    "#/definitions/developmentSampleQuoteRequirementBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleQuoteRequirementBulkResponseContent,
    "#/definitions/developmentSampleQuoteRequirementResponse":
    DevelopmentSampleQuoteRequirementResponse,
    "#/definitions/developmentSampleQuoteRequirementResponse/properties/content":  # noqa
    DevelopmentSampleQuoteRequirementResponseContent,
    "#/definitions/developmentSampleState": DevelopmentSampleState,
    "#/definitions/developmentSampleStateBulkResponse":
    DevelopmentSampleStateBulkResponse,
    "#/definitions/developmentSampleStateBulkResponse/properties/content":
    DevelopmentSampleStateBulkResponseContents,
    "#/definitions/developmentSampleStateBulkResponse/properties/content/items":  # noqa
    DevelopmentSampleStateBulkResponseContent,
    "#/definitions/developmentSampleStateResponse":
    DevelopmentSampleStateResponse,
    "#/definitions/developmentSampleStateResponse/properties/content":
    DevelopmentSampleStateResponseContent,
    "#/definitions/developmentSampleType": DevelopmentSampleType,
    "#/definitions/developmentSampleTypeBulkResponse":
    DevelopmentSampleTypeBulkResponse,
    "#/definitions/developmentSampleTypeBulkResponse/properties/content":
    DevelopmentSampleTypeBulkResponseContents,
    "#/definitions/developmentSampleTypeBulkResponse/properties/content/items":
    DevelopmentSampleTypeBulkResponseContent,
    "#/definitions/developmentSampleTypeResponse":
    DevelopmentSampleTypeResponse,
    "#/definitions/developmentSampleTypeResponse/properties/content":
    DevelopmentSampleTypeResponseContent,
    "#/definitions/developmentStyleType": DevelopmentStyleType,
    "#/definitions/developmentStyleTypeBulkResponse":
    DevelopmentStyleTypeBulkResponse,
    "#/definitions/developmentStyleTypeBulkResponse/properties/content":
    DevelopmentStyleTypeBulkResponseContents,
    "#/definitions/developmentStyleTypeBulkResponse/properties/content/items":
    DevelopmentStyleTypeBulkResponseContent,
    "#/definitions/developmentStyleTypeResponse": DevelopmentStyleTypeResponse,
    "#/definitions/developmentStyleTypeResponse/properties/content":
    DevelopmentStyleTypeResponseContent,
    "#/definitions/developmentTeam": DevelopmentTeam,
    "#/definitions/developmentTeam/properties/byDivision":
    DevelopmentTeamByDivisions,
    "#/definitions/developmentTeam/properties/byDivision/items":
    DevelopmentTeamByDivision,
    "#/definitions/developmentTeamBulkResponse": DevelopmentTeamBulkResponse,
    "#/definitions/developmentTeamBulkResponse/properties/content":
    DevelopmentTeamBulkResponseContents,
    "#/definitions/developmentTeamBulkResponse/properties/content/items":
    DevelopmentTeamBulkResponseContent,
    "#/definitions/developmentTeamGroup": DevelopmentTeamGroup,
    "#/definitions/developmentTeamGroupBulkResponse":
    DevelopmentTeamGroupBulkResponse,
    "#/definitions/developmentTeamGroupBulkResponse/properties/content":
    DevelopmentTeamGroupBulkResponseContents,
    "#/definitions/developmentTeamGroupBulkResponse/properties/content/items":
    DevelopmentTeamGroupBulkResponseContent,
    "#/definitions/developmentTeamGroupResponse": DevelopmentTeamGroupResponse,
    "#/definitions/developmentTeamGroupResponse/properties/content":
    DevelopmentTeamGroupResponseContent,
    "#/definitions/developmentTeamResponse": DevelopmentTeamResponse,
    "#/definitions/developmentTeamResponse/properties/content":
    DevelopmentTeamResponseContent,
    "#/definitions/developmentTrack": DevelopmentTrack,
    "#/definitions/developmentTrackBulkResponse": DevelopmentTrackBulkResponse,
    "#/definitions/developmentTrackBulkResponse/properties/content":
    DevelopmentTrackBulkResponseContents,
    "#/definitions/developmentTrackBulkResponse/properties/content/items":
    DevelopmentTrackBulkResponseContent,
    "#/definitions/developmentTrackResponse": DevelopmentTrackResponse,
    "#/definitions/developmentTrackResponse/properties/content":
    DevelopmentTrackResponseContent,
    "#/definitions/goodsAtConsolidatorReason": GoodsAtConsolidatorReason,
    "#/definitions/goodsAtConsolidatorReasonBulkResponse":
    GoodsAtConsolidatorReasonBulkResponse,
    "#/definitions/goodsAtConsolidatorReasonBulkResponse/properties/content":
    GoodsAtConsolidatorReasonBulkResponseContents,
    "#/definitions/goodsAtConsolidatorReasonBulkResponse/properties/content/items":  # noqa
    GoodsAtConsolidatorReasonBulkResponseContent,
    "#/definitions/goodsAtConsolidatorReasonResponse":
    GoodsAtConsolidatorReasonResponse,
    "#/definitions/goodsAtConsolidatorReasonResponse/properties/content":
    GoodsAtConsolidatorReasonResponseContent,
    "#/definitions/measurementSetState": MeasurementSetState,
    "#/definitions/measurementSetStateBulkResponse":
    MeasurementSetStateBulkResponse,
    "#/definitions/measurementSetStateBulkResponse/properties/content":
    MeasurementSetStateBulkResponseContents,
    "#/definitions/measurementSetStateBulkResponse/properties/content/items":
    MeasurementSetStateBulkResponseContent,
    "#/definitions/measurementSetStateResponse": MeasurementSetStateResponse,
    "#/definitions/measurementSetStateResponse/properties/content":
    MeasurementSetStateResponseContent,
    "#/definitions/measurementTemplateType": MeasurementTemplateType,
    "#/definitions/measurementTemplateTypeBulkResponse":
    MeasurementTemplateTypeBulkResponse,
    "#/definitions/measurementTemplateTypeBulkResponse/properties/content":
    MeasurementTemplateTypeBulkResponseContents,
    "#/definitions/measurementTemplateTypeBulkResponse/properties/content/items":  # noqa
    MeasurementTemplateTypeBulkResponseContent,
    "#/definitions/measurementTemplateTypeResponse":
    MeasurementTemplateTypeResponse,
    "#/definitions/measurementTemplateTypeResponse/properties/content":
    MeasurementTemplateTypeResponseContent,
    "#/definitions/nikeProductionTrial": NikeProductionTrial,
    "#/definitions/nikeProductionTrialBulkResponse":
    NikeProductionTrialBulkResponse,
    "#/definitions/nikeProductionTrialBulkResponse/properties/content":
    NikeProductionTrialBulkResponseContents,
    "#/definitions/nikeProductionTrialBulkResponse/properties/content/items":
    NikeProductionTrialBulkResponseContent,
    "#/definitions/nikeProductionTrialResponse": NikeProductionTrialResponse,
    "#/definitions/nikeProductionTrialResponse/properties/content":
    NikeProductionTrialResponseContent,
    "#/definitions/partModifier": PartModifier,
    "#/definitions/partModifierBulkResponse": PartModifierBulkResponse,
    "#/definitions/partModifierBulkResponse/properties/content":
    PartModifierBulkResponseContents,
    "#/definitions/partModifierBulkResponse/properties/content/items":
    PartModifierBulkResponseContent,
    "#/definitions/partModifierResponse": PartModifierResponse,
    "#/definitions/partModifierResponse/properties/content":
    PartModifierResponseContent,
    "#/definitions/partName": PartName,
    "#/definitions/partNameBulkResponse": PartNameBulkResponse,
    "#/definitions/partNameBulkResponse/properties/content":
    PartNameBulkResponseContents,
    "#/definitions/partNameBulkResponse/properties/content/items":
    PartNameBulkResponseContent,
    "#/definitions/partNameResponse": PartNameResponse,
    "#/definitions/partNameResponse/properties/content":
    PartNameResponseContent,
    "#/definitions/partPrefix": PartPrefix,
    "#/definitions/partPrefixBulkResponse": PartPrefixBulkResponse,
    "#/definitions/partPrefixBulkResponse/properties/content":
    PartPrefixBulkResponseContents,
    "#/definitions/partPrefixBulkResponse/properties/content/items":
    PartPrefixBulkResponseContent,
    "#/definitions/partPrefixResponse": PartPrefixResponse,
    "#/definitions/partPrefixResponse/properties/content":
    PartPrefixResponseContent,
    "#/definitions/partPrimary": PartPrimary,
    "#/definitions/partPrimaryBulkResponse": PartPrimaryBulkResponse,
    "#/definitions/partPrimaryBulkResponse/properties/content":
    PartPrimaryBulkResponseContents,
    "#/definitions/partPrimaryBulkResponse/properties/content/items":
    PartPrimaryBulkResponseContent,
    "#/definitions/partPrimaryResponse": PartPrimaryResponse,
    "#/definitions/partPrimaryResponse/properties/content":
    PartPrimaryResponseContent,
    "#/definitions/partSecondary": PartSecondary,
    "#/definitions/partSecondaryBulkResponse": PartSecondaryBulkResponse,
    "#/definitions/partSecondaryBulkResponse/properties/content":
    PartSecondaryBulkResponseContents,
    "#/definitions/partSecondaryBulkResponse/properties/content/items":
    PartSecondaryBulkResponseContent,
    "#/definitions/partSecondaryResponse": PartSecondaryResponse,
    "#/definitions/partSecondaryResponse/properties/content":
    PartSecondaryResponseContent,
    "#/definitions/partSuffix": PartSuffix,
    "#/definitions/partSuffixBulkResponse": PartSuffixBulkResponse,
    "#/definitions/partSuffixBulkResponse/properties/content":
    PartSuffixBulkResponseContents,
    "#/definitions/partSuffixBulkResponse/properties/content/items":
    PartSuffixBulkResponseContent,
    "#/definitions/partSuffixResponse": PartSuffixResponse,
    "#/definitions/partSuffixResponse/properties/content":
    PartSuffixResponseContent,
    "#/definitions/pointOfMeasurementCriticality":
    PointOfMeasurementCriticality,
    "#/definitions/pointOfMeasurementCriticalityBulkResponse":
    PointOfMeasurementCriticalityBulkResponse,
    "#/definitions/pointOfMeasurementCriticalityBulkResponse/properties/content":  # noqa
    PointOfMeasurementCriticalityBulkResponseContents,
    "#/definitions/pointOfMeasurementCriticalityBulkResponse/properties/content/items":  # noqa
    PointOfMeasurementCriticalityBulkResponseContent,
    "#/definitions/pointOfMeasurementCriticalityResponse":
    PointOfMeasurementCriticalityResponse,
    "#/definitions/pointOfMeasurementCriticalityResponse/properties/content":
    PointOfMeasurementCriticalityResponseContent,
    "#/definitions/productTrack": ProductTrack,
    "#/definitions/productTrackBulkResponse": ProductTrackBulkResponse,
    "#/definitions/productTrackBulkResponse/properties/content":
    ProductTrackBulkResponseContents,
    "#/definitions/productTrackBulkResponse/properties/content/items":
    ProductTrackBulkResponseContent,
    "#/definitions/productTrackResponse": ProductTrackResponse,
    "#/definitions/productTrackResponse/properties/content":
    ProductTrackResponseContent,
    "#/definitions/shippingService": ShippingService,
    "#/definitions/shippingServiceBulkResponse": ShippingServiceBulkResponse,
    "#/definitions/shippingServiceBulkResponse/properties/content":
    ShippingServiceBulkResponseContents,
    "#/definitions/shippingServiceBulkResponse/properties/content/items":
    ShippingServiceBulkResponseContent,
    "#/definitions/shippingServiceResponse": ShippingServiceResponse,
    "#/definitions/shippingServiceResponse/properties/content":
    ShippingServiceResponseContent,
    "#/definitions/technicalDifficulty": TechnicalDifficulty,
    "#/definitions/technicalDifficultyBulkResponse":
    TechnicalDifficultyBulkResponse,
    "#/definitions/technicalDifficultyBulkResponse/properties/content":
    TechnicalDifficultyBulkResponseContents,
    "#/definitions/technicalDifficultyBulkResponse/properties/content/items":
    TechnicalDifficultyBulkResponseContent,
    "#/definitions/technicalDifficultyResponse": TechnicalDifficultyResponse,
    "#/definitions/technicalDifficultyResponse/properties/content":
    TechnicalDifficultyResponseContent,
}
