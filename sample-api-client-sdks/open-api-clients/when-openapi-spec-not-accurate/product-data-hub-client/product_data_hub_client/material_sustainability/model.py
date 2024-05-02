import datetime
import decimal
import typing
import sob


class PDHStreamAdaptorItems(sob.model.Object):
    """
    Properties:

    - domain:
      Specifies the domain related to the data
    - event_type:
      Type of events responsible for the message e.g. CREATE, UPDATE
    - source_system:
      Specifies the system from there the data is sourced from
    - object_id:
      Unique identifier for the data
    - object_type:
      Type of the data
    - object_version:
      Version of object data resultant to change. This information will be used
      to expose the latest data to a consumer. The older versions will be saved
      in the cold and warm storage areas.
    - api_version:
      Version of the splitting required for aligning to the exposed canonical
      form of data. the expectation if this will help us to version changes to
      data as defined by the source system / integration services
    - correlation_id:
      id for tracking the data produced by source system, logging, monitoring
      and alerts - UUID is recommended for this field
    - entitlements:
      Who can see this data or confidential group information
    - changes:
      What are the changes to data in case there is a field level event is
      required, but encrypted using AES 256
    - full_object:
      The data itself in JSON format encrypted
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        domain: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        event_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        source_system: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
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
        object_version: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        api_version: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        correlation_id: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        entitlements: typing.Optional[
            typing.Union[
                "PDHStreamAdaptorItemsEntitlements",
                sob.utilities.types.Null
            ]
        ] = None,
        changes: typing.Optional[
            typing.Union[
                "PDHStreamAdaptorItemsChanges",
                sob.utilities.types.Null
            ]
        ] = None,
        full_object: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.domain = domain
        self.event_type = event_type
        self.source_system = source_system
        self.object_id = object_id
        self.object_type = object_type
        self.object_version = object_version
        self.api_version = api_version
        self.correlation_id = correlation_id
        self.entitlements = entitlements
        self.changes = changes
        self.full_object = full_object
        super().__init__(_data)


class PDHStreamAdaptorItemsChanges(sob.model.Array):
    """
    What are the changes to data in case there is a field level event is
    required, but encrypted using AES 256
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PDHStreamAdaptorItemsChangesItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PDHStreamAdaptorItemsChangesItem(sob.model.Object):
    """
    Properties:

    - field_name
    - from_value
    - to_value
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        field_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        from_value: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        to_value: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.field_name = field_name
        self.from_value = from_value
        self.to_value = to_value
        super().__init__(_data)


class PDHStreamAdaptorItemsEntitlements(sob.model.Array):
    """
    Who can see this data or confidential group information
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


class MaterialSustainabilityIndexDataunits(sob.model.Object):
    """
    Properties:

    - sustnblty_supplied_material_score_core
    - sustnblty_supplied_material_score_components
    - sustnblty_supplier_location_score_components
    - sustnblty_supplied_material_score_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sustnblty_supplied_material_score_core: typing.Optional[
            typing.Union[
                "SustnbltySuppliedMaterialScoreCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sustnblty_supplied_material_score_components: typing.Optional[
            typing.Union[
                "SustnbltySuppliedMaterialScoreComponents",
                sob.utilities.types.Null
            ]
        ] = None,
        sustnblty_supplier_location_score_components: typing.Optional[
            typing.Union[
                "SustnbltySupplierLocationScoreComponents",
                sob.utilities.types.Null
            ]
        ] = None,
        sustnblty_supplied_material_score_audit: typing.Optional[
            typing.Union[
                "SustnbltySuppliedMaterialScoreAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sustnblty_supplied_material_score_core = (
            sustnblty_supplied_material_score_core
        )
        self.sustnblty_supplied_material_score_components = (
            sustnblty_supplied_material_score_components
        )
        self.sustnblty_supplier_location_score_components = (
            sustnblty_supplier_location_score_components
        )
        self.sustnblty_supplied_material_score_audit = (
            sustnblty_supplied_material_score_audit
        )
        super().__init__(_data)


class SuppliedMaterialIndexBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - count:
      The number of entries returned in this responses
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
                "SuppliedMaterialIndexBulkResponseContent",
                sob.utilities.types.Null
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[
                int,
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
        self.count = count
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class SuppliedMaterialIndexBulkResponseContent(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SuppliedMaterialIndexBulkResponseContentItem"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SuppliedMaterialIndexBulkResponseContentItem(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
    - relationships
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "MaterialSustainabilityIndexDataunits",
                sob.utilities.types.Null
            ]
        ] = None,
        relationships: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        self.relationships = relationships
        super().__init__(_data)


class SuppliedMaterialIndexResponse(sob.model.Object):
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
    - object_id
    - object_type
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "SuppliedMaterialIndexResponseContent",
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
        ] = None
    ) -> None:
        self.content = content
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        self.object_id = object_id
        self.object_type = object_type
        super().__init__(_data)


class SuppliedMaterialIndexResponseContent(sob.model.Object):
    """
    Properties:

    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    - data
    - relationships
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "MaterialSustainabilityIndexDataunits",
                sob.utilities.types.Null
            ]
        ] = None,
        relationships: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        self.relationships = relationships
        super().__init__(_data)


class SustainabilityDateResponse(sob.model.Object):
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
                "SustainabilityDateResponseContent",
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


class SustainabilityDateResponseContent(sob.model.Object):
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
                "SustainabilityDatesDataunits",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class SustainabilityDatesDataunits(sob.model.Object):
    """
    Properties:

    - sustnblty_season_core
    - sustnblty_season_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sustnblty_season_core: typing.Optional[
            typing.Union[
                "SustnbltySeasonCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sustnblty_season_audit: typing.Optional[
            typing.Union[
                "SustnbltySeasonAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sustnblty_season_core = sustnblty_season_core
        self.sustnblty_season_audit = sustnblty_season_audit
        super().__init__(_data)


class SustnbltySeasonAudit(sob.model.Object):
    """
    Properties:

    - create_timestamp:
      No Definition Available
    - change_timestamp:
      No Definition Available
    - created_by:
      No Definition Available
    - modified_by:
      No Definition Available
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.create_timestamp = create_timestamp
        self.change_timestamp = change_timestamp
        self.created_by = created_by
        self.modified_by = modified_by
        super().__init__(_data)


class SustnbltySeasonCore(sob.model.Object):
    """
    Properties:

    - sustainability_season_identifier
    - sustainability_season
    - sustainability_season_start_date
    - sustainability_season_second_run_date
    - sustainability_season_end_date
    - sustainability_business_unit
    - sustainability_season_order_number
    - sustainability_is_most_recent_season
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sustainability_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season_start_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season_second_run_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season_end_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_business_unit: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season_order_number: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_is_most_recent_season: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sustainability_season_identifier = (
            sustainability_season_identifier
        )
        self.sustainability_season = sustainability_season
        self.sustainability_season_start_date = (
            sustainability_season_start_date
        )
        self.sustainability_season_second_run_date = (
            sustainability_season_second_run_date
        )
        self.sustainability_season_end_date = sustainability_season_end_date
        self.sustainability_business_unit = sustainability_business_unit
        self.sustainability_season_order_number = (
            sustainability_season_order_number
        )
        self.sustainability_is_most_recent_season = (
            sustainability_is_most_recent_season
        )
        super().__init__(_data)


class SustnbltySuppliedMaterialScoreAudit(sob.model.Object):
    """
    Properties:

    - create_timestamp:
      No Definition Available
    - change_timestamp:
      No Definition Available
    - created_by:
      No Definition Available
    - modified_by:
      No Definition Available
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        create_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        change_timestamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        created_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        modified_by: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.create_timestamp = create_timestamp
        self.change_timestamp = change_timestamp
        self.created_by = created_by
        self.modified_by = modified_by
        super().__init__(_data)


class SustnbltySuppliedMaterialScoreComponents(sob.model.Object):
    """
    Properties:

    - lifecycle_assessment_score
    - recycled_content_score
    - organic_content_score
    - blends_and_composites_score
    - better_cotton_initiative_program_score
    - water_conservation_score
    - nike_green_chemistry_program_score
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        lifecycle_assessment_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        recycled_content_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        organic_content_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        blends_and_composites_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        better_cotton_initiative_program_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        water_conservation_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        nike_green_chemistry_program_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.lifecycle_assessment_score = lifecycle_assessment_score
        self.recycled_content_score = recycled_content_score
        self.organic_content_score = organic_content_score
        self.blends_and_composites_score = blends_and_composites_score
        self.better_cotton_initiative_program_score = (
            better_cotton_initiative_program_score
        )
        self.water_conservation_score = water_conservation_score
        self.nike_green_chemistry_program_score = (
            nike_green_chemistry_program_score
        )
        super().__init__(_data)


class SustnbltySuppliedMaterialScoreCore(sob.model.Object):
    """
    Properties:

    - supplied_material_identifier
    - legacy_supplied_material_number
    - supplier_location_identifier
    - legacy_supplier_location_code
    - supplied_material_sustainability_score
    - supplier_location_sustainability_score
    - sustainability_season
    - sustainability_business_unit
    - division
    - nike_sustainability_ranking_description
    - nike_sustainability_ranking
    - carbon_footprint_kg_co_2_e_per_kg
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplied_material_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_supplied_material_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_supplier_location_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material_sustainability_score: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_sustainability_score: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_season: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        sustainability_business_unit: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        division: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        nike_sustainability_ranking_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_sustainability_ranking: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        carbon_footprint_kg_co_2_e_per_kg: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplied_material_identifier = supplied_material_identifier
        self.legacy_supplied_material_number = legacy_supplied_material_number
        self.supplier_location_identifier = supplier_location_identifier
        self.legacy_supplier_location_code = legacy_supplier_location_code
        self.supplied_material_sustainability_score = (
            supplied_material_sustainability_score
        )
        self.supplier_location_sustainability_score = (
            supplier_location_sustainability_score
        )
        self.sustainability_season = sustainability_season
        self.sustainability_business_unit = sustainability_business_unit
        self.division = division
        self.nike_sustainability_ranking_description = (
            nike_sustainability_ranking_description
        )
        self.nike_sustainability_ranking = nike_sustainability_ranking
        self.carbon_footprint_kg_co_2_e_per_kg = (
            carbon_footprint_kg_co_2_e_per_kg
        )
        super().__init__(_data)


class SustnbltySupplierLocationScoreComponents(sob.model.Object):
    """
    Properties:

    - restricted_substance_list_score
    - nike_water_program_score
    - nike_energy_and_carbon_program_score
    - nike_green_chemistry_training_score
    - nike_green_chemistry_form_score
    - certifications_and_programs_score
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        restricted_substance_list_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        nike_water_program_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        nike_energy_and_carbon_program_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        nike_green_chemistry_training_score: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        nike_green_chemistry_form_score: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        certifications_and_programs_score: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.restricted_substance_list_score = restricted_substance_list_score
        self.nike_water_program_score = nike_water_program_score
        self.nike_energy_and_carbon_program_score = (
            nike_energy_and_carbon_program_score
        )
        self.nike_green_chemistry_training_score = (
            nike_green_chemistry_training_score
        )
        self.nike_green_chemistry_form_score = nike_green_chemistry_form_score
        self.certifications_and_programs_score = (
            certifications_and_programs_score
        )
        super().__init__(_data)


class PdhStreamsAdaptorDataPut0(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PDHStreamAdaptorItems"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SustainabilityDataSeasonsObjectIdGetDataunits(sob.model.Array):
    """
    The data units that would be desired, default returns just core data
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


class SustainabilityDataSuppliedMaterialIndiciesCurrentGetObjectId(
    sob.model.Array
):
    """
    A comma separated list of Ids of the object (in this case Supplied
    Materials)
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    int,
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


class SustainabilityDataSuppliedMaterialIndiciesCurrentGetDataunits(
    sob.model.Array
):
    """
    The data units that would be desired, default returns just core data
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


class SustainabilityDataSuppliedMaterialIndiciesObjectIdCurrentGetDataunits(
    sob.model.Array
):
    """
    The data units that would be desired, default returns just core data
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


sob.meta.object_writable(  # type: ignore
    PDHStreamAdaptorItems
).properties = sob.meta.Properties([
    (
        'domain',
        sob.properties.Property(
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'event_type',
        sob.properties.Property(
            name="eventType",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'source_system',
        sob.properties.Property(
            name="sourceSystem",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_id',
        sob.properties.Property(
            name="objectId",
            required=True,
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
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'object_version',
        sob.properties.Property(
            name="objectVersion",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'api_version',
        sob.properties.Property(
            name="apiVersion",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'correlation_id',
        sob.properties.Property(
            name="correlationId",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'entitlements',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PDHStreamAdaptorItemsEntitlements,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'changes',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                PDHStreamAdaptorItemsChanges,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'full_object',
        sob.properties.Property(
            name="fullObject",
            required=True,
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PDHStreamAdaptorItemsChanges
).item_types = sob.types.MutableTypes([
    PDHStreamAdaptorItemsChangesItem
])
sob.meta.object_writable(  # type: ignore
    PDHStreamAdaptorItemsChangesItem
).properties = sob.meta.Properties([
    (
        'field_name',
        sob.properties.Property(
            name="fieldName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'from_value',
        sob.properties.Property(
            name="fromValue",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'to_value',
        sob.properties.Property(
            name="toValue",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PDHStreamAdaptorItemsEntitlements
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
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
    MaterialSustainabilityIndexDataunits
).properties = sob.meta.Properties([
    (
        'sustnblty_supplied_material_score_core',
        sob.properties.Property(
            name="sustnbltySuppliedMaterialScoreCore",
            required=True,
            types=sob.types.MutableTypes([
                SustnbltySuppliedMaterialScoreCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustnblty_supplied_material_score_components',
        sob.properties.Property(
            name="sustnbltySuppliedMaterialScoreComponents",
            types=sob.types.MutableTypes([
                SustnbltySuppliedMaterialScoreComponents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustnblty_supplier_location_score_components',
        sob.properties.Property(
            name="sustnbltySupplierLocationScoreComponents",
            types=sob.types.MutableTypes([
                SustnbltySupplierLocationScoreComponents,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustnblty_supplied_material_score_audit',
        sob.properties.Property(
            name="sustnbltySuppliedMaterialScoreAudit",
            types=sob.types.MutableTypes([
                SustnbltySuppliedMaterialScoreAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SuppliedMaterialIndexBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SuppliedMaterialIndexBulkResponseContent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'count',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
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
sob.meta.array_writable(  # type: ignore
    SuppliedMaterialIndexBulkResponseContent
).item_types = sob.types.MutableTypes([
    SuppliedMaterialIndexBulkResponseContentItem
])
sob.meta.object_writable(  # type: ignore
    SuppliedMaterialIndexBulkResponseContentItem
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
                MaterialSustainabilityIndexDataunits,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'relationships',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SuppliedMaterialIndexResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SuppliedMaterialIndexResponseContent,
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
    ),
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
    )
])
sob.meta.object_writable(  # type: ignore
    SuppliedMaterialIndexResponseContent
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
                MaterialSustainabilityIndexDataunits,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'relationships',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustainabilityDateResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SustainabilityDateResponseContent,
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
    SustainabilityDateResponseContent
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
                SustainabilityDatesDataunits,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustainabilityDatesDataunits
).properties = sob.meta.Properties([
    (
        'sustnblty_season_core',
        sob.properties.Property(
            name="sustnbltySeasonCore",
            required=True,
            types=sob.types.MutableTypes([
                SustnbltySeasonCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustnblty_season_audit',
        sob.properties.Property(
            name="sustnbltySeasonAudit",
            types=sob.types.MutableTypes([
                SustnbltySeasonAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySeasonAudit
).properties = sob.meta.Properties([
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
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySeasonCore
).properties = sob.meta.Properties([
    (
        'sustainability_season_identifier',
        sob.properties.Property(
            name="sustainabilitySeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season',
        sob.properties.Property(
            name="sustainabilitySeason",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season_start_date',
        sob.properties.Property(
            name="sustainabilitySeasonStartDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season_second_run_date',
        sob.properties.Property(
            name="sustainabilitySeasonSecondRunDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season_end_date',
        sob.properties.Property(
            name="sustainabilitySeasonEndDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_business_unit',
        sob.properties.Property(
            name="sustainabilityBusinessUnit",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season_order_number',
        sob.properties.Property(
            name="sustainabilitySeasonOrderNumber",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_is_most_recent_season',
        sob.properties.Property(
            name="sustainabilityIsMostRecentSeason",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySuppliedMaterialScoreAudit
).properties = sob.meta.Properties([
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
        'modified_by',
        sob.properties.Property(
            name="modifiedBy",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySuppliedMaterialScoreComponents
).properties = sob.meta.Properties([
    (
        'lifecycle_assessment_score',
        sob.properties.Property(
            name="lifecycleAssessmentScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'recycled_content_score',
        sob.properties.Property(
            name="recycledContentScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'organic_content_score',
        sob.properties.Property(
            name="organicContentScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'blends_and_composites_score',
        sob.properties.Property(
            name="blendsAndCompositesScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'better_cotton_initiative_program_score',
        sob.properties.Property(
            name="betterCottonInitiativeProgramScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'water_conservation_score',
        sob.properties.Property(
            name="waterConservationScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_green_chemistry_program_score',
        sob.properties.Property(
            name="nikeGreenChemistryProgramScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySuppliedMaterialScoreCore
).properties = sob.meta.Properties([
    (
        'supplied_material_identifier',
        sob.properties.Property(
            name="suppliedMaterialIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_supplied_material_number',
        sob.properties.Property(
            name="legacySuppliedMaterialNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_identifier',
        sob.properties.Property(
            name="supplierLocationIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_supplier_location_code',
        sob.properties.Property(
            name="legacySupplierLocationCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material_sustainability_score',
        sob.properties.Property(
            name="suppliedMaterialSustainabilityScore",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_sustainability_score',
        sob.properties.Property(
            name="supplierLocationSustainabilityScore",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_season',
        sob.properties.Property(
            name="sustainabilitySeason",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sustainability_business_unit',
        sob.properties.Property(
            name="sustainabilityBusinessUnit",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
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
        'nike_sustainability_ranking_description',
        sob.properties.Property(
            name="nikeSustainabilityRankingDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_sustainability_ranking',
        sob.properties.Property(
            name="nikeSustainabilityRanking",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'carbon_footprint_kg_co_2_e_per_kg',
        sob.properties.Property(
            name="carbonFootprintKgCO2ePerKg",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SustnbltySupplierLocationScoreComponents
).properties = sob.meta.Properties([
    (
        'restricted_substance_list_score',
        sob.properties.Property(
            name="restrictedSubstanceListScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_water_program_score',
        sob.properties.Property(
            name="nikeWaterProgramScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_energy_and_carbon_program_score',
        sob.properties.Property(
            name="nikeEnergyAndCarbonProgramScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_green_chemistry_training_score',
        sob.properties.Property(
            name="nikeGreenChemistryTrainingScore",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nike_green_chemistry_form_score',
        sob.properties.Property(
            name="nikeGreenChemistryFormScore",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'certifications_and_programs_score',
        sob.properties.Property(
            name="certificationsAndProgramsScore",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    PdhStreamsAdaptorDataPut0
).item_types = sob.types.MutableTypes([
    PDHStreamAdaptorItems
])
sob.meta.array_writable(  # type: ignore
    SustainabilityDataSeasonsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SustainabilityDataSuppliedMaterialIndiciesCurrentGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SustainabilityDataSuppliedMaterialIndiciesCurrentGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SustainabilityDataSuppliedMaterialIndiciesObjectIdCurrentGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/definitions/PDHStreamAdaptorItems": PDHStreamAdaptorItems,
    "#/definitions/PDHStreamAdaptorItems/properties/changes":
    PDHStreamAdaptorItemsChanges,
    "#/definitions/PDHStreamAdaptorItems/properties/changes/items":
    PDHStreamAdaptorItemsChangesItem,
    "#/definitions/PDHStreamAdaptorItems/properties/entitlements":
    PDHStreamAdaptorItemsEntitlements,
    "#/definitions/_error": Error,
    "#/definitions/_links": Links,
    "#/definitions/_reference": Reference,
    "#/definitions/materialSustainabilityIndex_dataunits":
    MaterialSustainabilityIndexDataunits,
    "#/definitions/suppliedMaterialIndexBulkResponse":
    SuppliedMaterialIndexBulkResponse,
    "#/definitions/suppliedMaterialIndexBulkResponse/properties/content":
    SuppliedMaterialIndexBulkResponseContent,
    "#/definitions/suppliedMaterialIndexBulkResponse/properties/content/items":
    SuppliedMaterialIndexBulkResponseContentItem,
    "#/definitions/suppliedMaterialIndexResponse":
    SuppliedMaterialIndexResponse,
    "#/definitions/suppliedMaterialIndexResponse/properties/content":
    SuppliedMaterialIndexResponseContent,
    "#/definitions/sustainabilityDateResponse": SustainabilityDateResponse,
    "#/definitions/sustainabilityDateResponse/properties/content":
    SustainabilityDateResponseContent,
    "#/definitions/sustainabilityDates_dataunits":
    SustainabilityDatesDataunits,
    "#/definitions/sustnbltySeasonAudit": SustnbltySeasonAudit,
    "#/definitions/sustnbltySeasonCore": SustnbltySeasonCore,
    "#/definitions/sustnbltySuppliedMaterialScoreAudit":
    SustnbltySuppliedMaterialScoreAudit,
    "#/definitions/sustnbltySuppliedMaterialScoreComponents":
    SustnbltySuppliedMaterialScoreComponents,
    "#/definitions/sustnbltySuppliedMaterialScoreCore":
    SustnbltySuppliedMaterialScoreCore,
    "#/definitions/sustnbltySupplierLocationScoreComponents":
    SustnbltySupplierLocationScoreComponents,
    "#/paths/~1pdhStreamsAdaptor~1data/put/parameters/0/schema":
    PdhStreamsAdaptorDataPut0,
    "#/paths/~1sustainability~1data~1seasons~1{objectId}/get/parameters/1":
    SustainabilityDataSeasonsObjectIdGetDataunits,
    "#/paths/~1sustainability~1data~1suppliedMaterialIndicies~1current/get/parameters/0":  # noqa
    SustainabilityDataSuppliedMaterialIndiciesCurrentGetObjectId,
    "#/paths/~1sustainability~1data~1suppliedMaterialIndicies~1current/get/parameters/1":  # noqa
    SustainabilityDataSuppliedMaterialIndiciesCurrentGetDataunits,
    "#/paths/~1sustainability~1data~1suppliedMaterialIndicies~1{objectId}~1current/get/parameters/1":  # noqa
    SustainabilityDataSuppliedMaterialIndiciesObjectIdCurrentGetDataunits,
}
