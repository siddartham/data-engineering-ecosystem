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


class ResponsibleNikeLiaisonOffice(sob.model.Object):
    """
    Properties:

    - responsible_nike_liaison_office_identifier
    - responsible_nike_liaison_office_name
    - created_by
    - create_timestamp
    - modified_by
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
        responsible_nike_liaison_office_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        responsible_nike_liaison_office_name: typing.Optional[
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
        self.responsible_nike_liaison_office_identifier = (
            responsible_nike_liaison_office_identifier
        )
        self.responsible_nike_liaison_office_name = (
            responsible_nike_liaison_office_name
        )
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class ResponsibleNikeLiaisonOfficeBulkResponse(sob.model.Object):
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
                "ResponsibleNikeLiaisonOfficeBulkResponseContents",
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


class ResponsibleNikeLiaisonOfficeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "ResponsibleNikeLiaisonOfficeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class ResponsibleNikeLiaisonOfficeBulkResponseContent(sob.model.Object):
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
                "ResponsibleNikeLiaisonOffice",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class ResponsibleNikeLiaisonOfficeResponse(sob.model.Object):
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
                "ResponsibleNikeLiaisonOfficeResponseContent",
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


class ResponsibleNikeLiaisonOfficeResponseContent(sob.model.Object):
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
                "ResponsibleNikeLiaisonOffice",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class SupplierState(sob.model.Object):
    """
    Properties:

    - supplier_state_identifier
    - supplier_state_name
    - created_by
    - create_timestamp
    - modified_by
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
        supplier_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_state_name: typing.Optional[
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
        self.supplier_state_identifier = supplier_state_identifier
        self.supplier_state_name = supplier_state_name
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class SupplierStateBulkResponse(sob.model.Object):
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
                "SupplierStateBulkResponseContents",
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


class SupplierStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SupplierStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SupplierStateBulkResponseContent(sob.model.Object):
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
                "SupplierState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class SupplierStateResponse(sob.model.Object):
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
                "SupplierStateResponseContent",
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


class SupplierStateResponseContent(sob.model.Object):
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
                "SupplierState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TestLabLiaisonOffice(sob.model.Object):
    """
    Properties:

    - test_lab_liaison_office_identifier
    - test_lab_liaison_office_name
    - created_by
    - create_timestamp
    - modified_by
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
        test_lab_liaison_office_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        test_lab_liaison_office_name: typing.Optional[
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
        self.test_lab_liaison_office_identifier = (
            test_lab_liaison_office_identifier
        )
        self.test_lab_liaison_office_name = test_lab_liaison_office_name
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class TestLabLiaisonOfficeBulkResponse(sob.model.Object):
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
                "TestLabLiaisonOfficeBulkResponseContents",
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


class TestLabLiaisonOfficeBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TestLabLiaisonOfficeBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TestLabLiaisonOfficeBulkResponseContent(sob.model.Object):
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
                "TestLabLiaisonOffice",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TestLabLiaisonOfficeResponse(sob.model.Object):
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
                "TestLabLiaisonOfficeResponseContent",
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


class TestLabLiaisonOfficeResponseContent(sob.model.Object):
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
                "TestLabLiaisonOffice",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TestLabState(sob.model.Object):
    """
    Properties:

    - test_lab_state_identifier
    - test_lab_state_name
    - created_by
    - create_timestamp
    - modified_by
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
        test_lab_state_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        test_lab_state_name: typing.Optional[
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
        self.test_lab_state_identifier = test_lab_state_identifier
        self.test_lab_state_name = test_lab_state_name
        self.created_by = created_by
        self.create_timestamp = create_timestamp
        self.modified_by = modified_by
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class TestLabStateBulkResponse(sob.model.Object):
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
                "TestLabStateBulkResponseContents",
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


class TestLabStateBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "TestLabStateBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class TestLabStateBulkResponseContent(sob.model.Object):
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
                "TestLabState",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class TestLabStateResponse(sob.model.Object):
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
                "TestLabStateResponseContent",
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


class TestLabStateResponseContent(sob.model.Object):
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
                "TestLabState",
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
    ResponsibleNikeLiaisonOffice
).properties = sob.meta.Properties([
    (
        'responsible_nike_liaison_office_identifier',
        sob.properties.Property(
            name="responsibleNikeLiaisonOfficeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'responsible_nike_liaison_office_name',
        sob.properties.Property(
            name="responsibleNikeLiaisonOfficeName",
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
    ResponsibleNikeLiaisonOfficeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ResponsibleNikeLiaisonOfficeBulkResponseContents,
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
    ResponsibleNikeLiaisonOfficeBulkResponseContents
).item_types = sob.types.MutableTypes([
    ResponsibleNikeLiaisonOfficeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    ResponsibleNikeLiaisonOfficeBulkResponseContent
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
                ResponsibleNikeLiaisonOffice,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ResponsibleNikeLiaisonOfficeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                ResponsibleNikeLiaisonOfficeResponseContent,
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
    ResponsibleNikeLiaisonOfficeResponseContent
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
                ResponsibleNikeLiaisonOffice,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierState
).properties = sob.meta.Properties([
    (
        'supplier_state_identifier',
        sob.properties.Property(
            name="supplierStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_state_name',
        sob.properties.Property(
            name="supplierStateName",
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
    SupplierStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierStateBulkResponseContents,
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
    SupplierStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    SupplierStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    SupplierStateBulkResponseContent
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
                SupplierState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierStateResponseContent,
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
    SupplierStateResponseContent
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
                SupplierState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TestLabLiaisonOffice
).properties = sob.meta.Properties([
    (
        'test_lab_liaison_office_identifier',
        sob.properties.Property(
            name="testLabLiaisonOfficeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'test_lab_liaison_office_name',
        sob.properties.Property(
            name="testLabLiaisonOfficeName",
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
    TestLabLiaisonOfficeBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TestLabLiaisonOfficeBulkResponseContents,
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
    TestLabLiaisonOfficeBulkResponseContents
).item_types = sob.types.MutableTypes([
    TestLabLiaisonOfficeBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    TestLabLiaisonOfficeBulkResponseContent
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
                TestLabLiaisonOffice,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TestLabLiaisonOfficeResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TestLabLiaisonOfficeResponseContent,
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
    TestLabLiaisonOfficeResponseContent
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
                TestLabLiaisonOffice,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TestLabState
).properties = sob.meta.Properties([
    (
        'test_lab_state_identifier',
        sob.properties.Property(
            name="testLabStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'test_lab_state_name',
        sob.properties.Property(
            name="testLabStateName",
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
    TestLabStateBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TestLabStateBulkResponseContents,
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
    TestLabStateBulkResponseContents
).item_types = sob.types.MutableTypes([
    TestLabStateBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    TestLabStateBulkResponseContent
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
                TestLabState,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TestLabStateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                TestLabStateResponseContent,
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
    TestLabStateResponseContent
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
                TestLabState,
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
    "#/definitions/responsibleNikeLiaisonOffice": ResponsibleNikeLiaisonOffice,
    "#/definitions/responsibleNikeLiaisonOfficeBulkResponse":
    ResponsibleNikeLiaisonOfficeBulkResponse,
    "#/definitions/responsibleNikeLiaisonOfficeBulkResponse/properties/content":  # noqa
    ResponsibleNikeLiaisonOfficeBulkResponseContents,
    "#/definitions/responsibleNikeLiaisonOfficeBulkResponse/properties/content/items":  # noqa
    ResponsibleNikeLiaisonOfficeBulkResponseContent,
    "#/definitions/responsibleNikeLiaisonOfficeResponse":
    ResponsibleNikeLiaisonOfficeResponse,
    "#/definitions/responsibleNikeLiaisonOfficeResponse/properties/content":
    ResponsibleNikeLiaisonOfficeResponseContent,
    "#/definitions/supplierState": SupplierState,
    "#/definitions/supplierStateBulkResponse": SupplierStateBulkResponse,
    "#/definitions/supplierStateBulkResponse/properties/content":
    SupplierStateBulkResponseContents,
    "#/definitions/supplierStateBulkResponse/properties/content/items":
    SupplierStateBulkResponseContent,
    "#/definitions/supplierStateResponse": SupplierStateResponse,
    "#/definitions/supplierStateResponse/properties/content":
    SupplierStateResponseContent,
    "#/definitions/testLabLiaisonOffice": TestLabLiaisonOffice,
    "#/definitions/testLabLiaisonOfficeBulkResponse":
    TestLabLiaisonOfficeBulkResponse,
    "#/definitions/testLabLiaisonOfficeBulkResponse/properties/content":
    TestLabLiaisonOfficeBulkResponseContents,
    "#/definitions/testLabLiaisonOfficeBulkResponse/properties/content/items":
    TestLabLiaisonOfficeBulkResponseContent,
    "#/definitions/testLabLiaisonOfficeResponse": TestLabLiaisonOfficeResponse,
    "#/definitions/testLabLiaisonOfficeResponse/properties/content":
    TestLabLiaisonOfficeResponseContent,
    "#/definitions/testLabState": TestLabState,
    "#/definitions/testLabStateBulkResponse": TestLabStateBulkResponse,
    "#/definitions/testLabStateBulkResponse/properties/content":
    TestLabStateBulkResponseContents,
    "#/definitions/testLabStateBulkResponse/properties/content/items":
    TestLabStateBulkResponseContent,
    "#/definitions/testLabStateResponse": TestLabStateResponse,
    "#/definitions/testLabStateResponse/properties/content":
    TestLabStateResponseContent,
}
