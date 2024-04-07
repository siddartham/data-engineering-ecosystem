import datetime
import decimal
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


class BillOfMaterialsBulkResponse(sob.model.Object):
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
                "BillOfMaterialsBulkResponseContents",
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


class BillOfMaterialsBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BillOfMaterialsBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BillOfMaterialsBulkResponseContent(sob.model.Object):
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
                "BillOfMaterialsDataunits",
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


class BillOfMaterialsResponse(sob.model.Object):
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
                "BillOfMaterialsResponseContent",
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


class BillOfMaterialsResponseContent(sob.model.Object):
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
                "BillOfMaterialsDataunits",
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


class BillOfMaterialsSourceBulkResponse(sob.model.Object):
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
                "BillOfMaterialsSourceBulkResponseContents",
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


class BillOfMaterialsSourceBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BillOfMaterialsSourceBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BillOfMaterialsSourceBulkResponseContent(sob.model.Object):
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
                "BillOfMaterialsSourceDataunits",
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


class BillOfMaterialsSourceResponse(sob.model.Object):
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
                "BillOfMaterialsSourceResponseContent",
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


class BillOfMaterialsSourceResponseContent(sob.model.Object):
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
                "BillOfMaterialsSourceDataunits",
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


class BillOfMaterialsSourceDataunits(sob.model.Object):
    """
    Properties:

    - bom_core
    - bom_sourcing_configuration_colorway_season
    - bom_classification
    - bom_description
    - bom_status
    - bom_header_audit
    - bom_line_item_detail
    - bom_line_item_comments
    - bom_line_audit
    - bom_season
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_core: typing.Optional[
            typing.Union[
                "BillOfMaterialsSourceDataunitsBomCore",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_sourcing_configuration_colorway_season: typing.Optional[
            typing.Union[
                "BomSourcingConfigurationColorwaySeason",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_classification: typing.Optional[
            typing.Union[
                "BomClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_description: typing.Optional[
            typing.Union[
                "BomDescription",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_status: typing.Optional[
            typing.Union[
                "BomStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_header_audit: typing.Optional[
            typing.Union[
                "BomHeaderAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_detail: typing.Optional[
            typing.Union[
                "BomLineItemDetailSources",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_comments: typing.Optional[
            typing.Union[
                "BomLineItemComments",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_audit: typing.Optional[
            typing.Union[
                "BomLineAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_season: typing.Optional[
            typing.Union[
                "BillOfMaterialsSourceDataunitsBomSeason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_core = bom_core
        self.bom_sourcing_configuration_colorway_season = (
            bom_sourcing_configuration_colorway_season
        )
        self.bom_classification = bom_classification
        self.bom_description = bom_description
        self.bom_status = bom_status
        self.bom_header_audit = bom_header_audit
        self.bom_line_item_detail = bom_line_item_detail
        self.bom_line_item_comments = bom_line_item_comments
        self.bom_line_audit = bom_line_audit
        self.bom_season = bom_season
        super().__init__(_data)


class BillOfMaterialsSourceDataunitsBomCore(sob.model.Object):

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_converted: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_guid: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_colorway_source_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        product_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        style_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_identifier = bom_identifier
        self.development_colorway_identifier = development_colorway_identifier
        self.bom_name = bom_name
        self.bom_converted = bom_converted
        self.bom_guid = bom_guid
        self.bom_colorway_source_identifier = bom_colorway_source_identifier
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        self.product_identifier = product_identifier
        self.style_number = style_number
        super().__init__(_data)


class BillOfMaterialsSourceDataunitsBomSeason(sob.model.Object):

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            typing.Union[
                "BomSeasonDevelopmentColorwaySeasonIdentifier",
                sob.utilities.types.Null
            ]
        ] = None,
        cycle_year: typing.Optional[
            typing.Union[
                "BillOfMaterialsSourceDataunitsBomSeasonCycleYear",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_season_identifier = (
            development_colorway_season_identifier
        )
        self.cycle_year = cycle_year
        super().__init__(_data)


class BillOfMaterialsSourceDataunitsBomSeasonCycleYear(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Reference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BillOfMaterialsDataunits(sob.model.Object):
    """
    Properties:

    - bom_core
    - bom_season
    - bom_sourcing_configuration
    - bom_classification
    - bom_description
    - bom_status
    - bom_header_audit
    - bom_line_item_detail
    - bom_line_item_comments
    - bom_line_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_core: typing.Optional[
            typing.Union[
                "BomCore",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_season: typing.Optional[
            typing.Union[
                "BomSeason",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_sourcing_configuration: typing.Optional[
            typing.Union[
                "BomSourcingConfigurations",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_classification: typing.Optional[
            typing.Union[
                "BomClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_description: typing.Optional[
            typing.Union[
                "BomDescription",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_status: typing.Optional[
            typing.Union[
                "BomStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_header_audit: typing.Optional[
            typing.Union[
                "BomHeaderAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_detail: typing.Optional[
            typing.Union[
                "BomLineItemDetails",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_comments: typing.Optional[
            typing.Union[
                "BomLineItemComments",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_audit: typing.Optional[
            typing.Union[
                "BomLineAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_core = bom_core
        self.bom_season = bom_season
        self.bom_sourcing_configuration = bom_sourcing_configuration
        self.bom_classification = bom_classification
        self.bom_description = bom_description
        self.bom_status = bom_status
        self.bom_header_audit = bom_header_audit
        self.bom_line_item_detail = bom_line_item_detail
        self.bom_line_item_comments = bom_line_item_comments
        self.bom_line_audit = bom_line_audit
        super().__init__(_data)


class BomClassification(sob.model.Object):
    """
    Properties:

    - development_style_type
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
        development_style_type: typing.Optional[
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
        ] = None
    ) -> None:
        self.development_style_type = development_style_type
        self.division = division
        super().__init__(_data)


class BomCore(sob.model.Object):
    """
    Properties:

    - bom_identifier:
      No Definition Available
    - development_colorway_identifier:
      No Definition Available
    - bom_name:
      No Definition Available
    - bom_converted
    - bom_guid
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_converted: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_guid: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_identifier = bom_identifier
        self.development_colorway_identifier = development_colorway_identifier
        self.bom_name = bom_name
        self.bom_converted = bom_converted
        self.bom_guid = bom_guid
        super().__init__(_data)


class BomDescription(sob.model.Object):
    """
    Properties:

    - bom_description:
      No Definition Available
    - bom_comments:
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
        bom_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_description = bom_description
        self.bom_comments = bom_comments
        super().__init__(_data)


class BomHeaderAudit(sob.model.Object):
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


class BomLineAudit(sob.model.Object):
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


class BomLineItemComments(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BomLineItemComment"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomLineItemComment(sob.model.Object):
    """
    Properties:

    - bom_line_item_identifier:
      No Definition Available
    - bom_line_item_comments:
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
        bom_line_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_line_item_identifier = bom_line_item_identifier
        self.bom_line_item_comments = bom_line_item_comments
        super().__init__(_data)


class BomLineItemDetails(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BomLineItemDetail"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomLineItemDetail(sob.model.Object):
    """
    Properties:

    - bom_line_item_identifier:
      No Definition Available
    - bom_line_item_number:
      No Definition Available
    - parent_bom_line_item_identifier:
      No Definition Available
    - line_item_quantity:
      No Definition Available
    - color
    - bill_of_materials_section
    - part_primary
    - part_secondary
    - part_modifier
    - part_suffix
    - part_name:
      No Definition Available
    - material_item_identifier:
      No Definition Available
    - supplied_material
    - supplied_material_color_identifier
    - supplied_material_color_is_multiple_colors:
      No Definition Available
    - color_placeholder_description:
      Freeform text for users to input color description when it does not exist
      in PCX library yet
    - material_item_placeholder_description:
      Freeform text for users to input material description when it does not
      exist in PCX library yet
    - part_pattern
    - part_prefix
    - bom_line_item_guid
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_line_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        parent_bom_line_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        line_item_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        color: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        bill_of_materials_section: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_primary: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_secondary: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_modifier: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_suffix: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        material_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material_color_is_multiple_colors: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        color_placeholder_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        material_item_placeholder_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        part_pattern: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_prefix: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_guid: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_line_item_identifier = bom_line_item_identifier
        self.bom_line_item_number = bom_line_item_number
        self.parent_bom_line_item_identifier = parent_bom_line_item_identifier
        self.line_item_quantity = line_item_quantity
        self.color = color
        self.bill_of_materials_section = bill_of_materials_section
        self.part_primary = part_primary
        self.part_secondary = part_secondary
        self.part_modifier = part_modifier
        self.part_suffix = part_suffix
        self.part_name = part_name
        self.material_item_identifier = material_item_identifier
        self.supplied_material = supplied_material
        self.supplied_material_color_identifier = (
            supplied_material_color_identifier
        )
        self.supplied_material_color_is_multiple_colors = (
            supplied_material_color_is_multiple_colors
        )
        self.color_placeholder_description = color_placeholder_description
        self.material_item_placeholder_description = (
            material_item_placeholder_description
        )
        self.part_pattern = part_pattern
        self.part_prefix = part_prefix
        self.bom_line_item_guid = bom_line_item_guid
        super().__init__(_data)


class BomLineItemDetailSources(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BomLineItemDetailSource"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomLineItemDetailSource(sob.model.Object):
    """
    Properties:

    - bom_line_item_identifier
    - bom_line_item_number
    - parent_bom_line_item_identifier
    - line_item_quantity
    - color
    - bill_of_materials_section
    - part
    - pattern_part
    - material_item_identifier
    - supplied_material
    - supplied_material_color_identifier
    - supplied_material_color_is_multiple_colors
    - color_placeholder_description:
      Freeform text for users to input color description when it does not exist
      in PCX library yet
    - material_item_placeholder_description:
      Freeform text for users to input material description when it does not
      exist in PCX library yet
    - net_usage
    - waste_usage
    - gross_usage
    - usage_unit_of_measure
    - bom_line_item_guid
    - part_pattern
    - part_prefix
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        bom_line_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        parent_bom_line_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        line_item_quantity: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        color: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        bill_of_materials_section: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        pattern_part: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        material_item_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material_color_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplied_material_color_is_multiple_colors: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        color_placeholder_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        material_item_placeholder_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        net_usage: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        waste_usage: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        gross_usage: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        usage_unit_of_measure: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        bom_line_item_guid: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        part_pattern: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        part_prefix: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bom_line_item_identifier = bom_line_item_identifier
        self.bom_line_item_number = bom_line_item_number
        self.parent_bom_line_item_identifier = parent_bom_line_item_identifier
        self.line_item_quantity = line_item_quantity
        self.color = color
        self.bill_of_materials_section = bill_of_materials_section
        self.part = part
        self.pattern_part = pattern_part
        self.material_item_identifier = material_item_identifier
        self.supplied_material = supplied_material
        self.supplied_material_color_identifier = (
            supplied_material_color_identifier
        )
        self.supplied_material_color_is_multiple_colors = (
            supplied_material_color_is_multiple_colors
        )
        self.color_placeholder_description = color_placeholder_description
        self.material_item_placeholder_description = (
            material_item_placeholder_description
        )
        self.net_usage = net_usage
        self.waste_usage = waste_usage
        self.gross_usage = gross_usage
        self.usage_unit_of_measure = usage_unit_of_measure
        self.bom_line_item_guid = bom_line_item_guid
        self.part_pattern = part_pattern
        self.part_prefix = part_prefix
        super().__init__(_data)


class BomSeason(sob.model.Object):
    """
    Properties:

    - development_colorway_season_identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            typing.Union[
                "BomSeasonDevelopmentColorwaySeasonIdentifier",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_season_identifier = (
            development_colorway_season_identifier
        )
        super().__init__(_data)


class BomSeasonDevelopmentColorwaySeasonIdentifier(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Reference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomSourcingConfigurations(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_list
    - sourcing_configuration_identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sourcing_configuration_list: typing.Optional[
            typing.Union[
                "BomSourcingConfigurationsList",
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                "BomSourcingConfigurationSourcingConfigurationIdentifier",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_list = sourcing_configuration_list
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        super().__init__(_data)


class BomSourcingConfigurationSourcingConfigurationIdentifier(sob.model.Array):

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


class BomSourcingConfigurationsList(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "BomSourcingConfiguration"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomSourcingConfiguration(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_identifier
    - sourcing_configuration_season
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_season: typing.Optional[
            typing.Union[
                "BomSourcingConfigurationSeason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        self.sourcing_configuration_season = sourcing_configuration_season
        super().__init__(_data)


class BomSourcingConfigurationSeason(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Reference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomSourcingConfigurationColorwaySeason(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_colorway_season
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sourcing_configuration_colorway_season: typing.Optional[
            typing.Union[
                "BomSourcingConfigurationColorwaySeasonSourcingConfigurationColorwaySeason",  # noqa
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_colorway_season = (
            sourcing_configuration_colorway_season
        )
        super().__init__(_data)


class BomSourcingConfigurationColorwaySeasonSourcingConfigurationColorwaySeason(  # noqa
    sob.model.Array
):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Reference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class BomStatus(sob.model.Object):
    """
    Properties:

    - bill_of_material_status_indicator:
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
        bill_of_material_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.bill_of_material_status_indicator = (
            bill_of_material_status_indicator
        )
        super().__init__(_data)


class DSampleAudit(sob.model.Object):
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


class DSampleClassification(sob.model.Object):
    """
    Properties:

    - development_style_type
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
        development_style_type: typing.Optional[
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
        ] = None
    ) -> None:
        self.development_style_type = development_style_type
        self.division = division
        super().__init__(_data)


class DSampleComments(sob.model.Object):
    """
    Properties:

    - development_sample_comments:
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
        development_sample_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_comments = development_sample_comments
        super().__init__(_data)


class DSampleCore(sob.model.Object):
    """
    Properties:

    - development_sample_identifier:
      Dev Sample Identifier - Same Identifier as Dev Sample Shipment Identifier
    - development_style_identifier
    - development_colorway_identifier
    - development_sample_type
    - development_sample_format
    - development_sample_need_by_date
    - development_sample_shipment
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_sample_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_type: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_format: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_need_by_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_shipment: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_identifier = development_sample_identifier
        self.development_style_identifier = development_style_identifier
        self.development_colorway_identifier = development_colorway_identifier
        self.development_sample_type = development_sample_type
        self.development_sample_format = development_sample_format
        self.development_sample_need_by_date = development_sample_need_by_date
        self.development_sample_shipment = development_sample_shipment
        super().__init__(_data)


class DSampleEvaluation(sob.model.Object):
    """
    Properties:

    - reviewed_date
    - development_sample_evaluation_state
    - fit_date
    - change_request_reason_code
    - development_sample_evaluation_comments:
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
        reviewed_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_evaluation_state: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        fit_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        change_request_reason_code: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_evaluation_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.reviewed_date = reviewed_date
        self.development_sample_evaluation_state = (
            development_sample_evaluation_state
        )
        self.fit_date = fit_date
        self.change_request_reason_code = change_request_reason_code
        self.development_sample_evaluation_comments = (
            development_sample_evaluation_comments
        )
        super().__init__(_data)


class DSampleOrderDetail(sob.model.Object):
    """
    Properties:

    - development_sample_destination_name:
      Development Sample Destination Description
    - development_sample_address:
      No Definition Available
    - developer_destination_address:
      No Definition Available
    - attention_to:
      No Definition Available
    - sample_size:
      No Definition Available
    - developer_order_quantity:
      No Definition Available
    - sample_order_quantity_or_pair_quantity:
      No Definition Available
    - sample_order_right_quantity:
      No Definition Available
    - sample_order_left_quantity:
      No Definition Available
    - cost_center_number:
      Cost Center Name
    - cost_center_approver:
      No Definition Available
    - general_ledger_number:
      No Definition Available
    - requested_on_behalf_of:
      No Definition Available
    - fabric_instruction
    - quote_requirement
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_sample_destination_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_address: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        developer_destination_address: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        attention_to: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        sample_size: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        developer_order_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sample_order_quantity_or_pair_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sample_order_right_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sample_order_left_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        cost_center_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        cost_center_approver: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        general_ledger_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        requested_on_behalf_of: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        fabric_instruction: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        quote_requirement: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_destination_name = (
            development_sample_destination_name
        )
        self.development_sample_address = development_sample_address
        self.developer_destination_address = developer_destination_address
        self.attention_to = attention_to
        self.sample_size = sample_size
        self.developer_order_quantity = developer_order_quantity
        self.sample_order_quantity_or_pair_quantity = (
            sample_order_quantity_or_pair_quantity
        )
        self.sample_order_right_quantity = sample_order_right_quantity
        self.sample_order_left_quantity = sample_order_left_quantity
        self.cost_center_number = cost_center_number
        self.cost_center_approver = cost_center_approver
        self.general_ledger_number = general_ledger_number
        self.requested_on_behalf_of = requested_on_behalf_of
        self.fabric_instruction = fabric_instruction
        self.quote_requirement = quote_requirement
        super().__init__(_data)


class DSampleRequestAudit(sob.model.Object):
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


class DSampleRequestComments(sob.model.Object):
    """
    Properties:

    - development_sample_request_comments:
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
        development_sample_request_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_request_comments = (
            development_sample_request_comments
        )
        super().__init__(_data)


class DSampleRequestCore(sob.model.Object):
    """
    Properties:

    - development_sample_request_identifier:
      No Definition Available
    - development_sample_request_name:
      No Definition Available
    - sourcing_configuration
    - development_sample_request_season
    - development_sample_request_date
    - development_sample_request_purpose
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_sample_request_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_request_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_request_season: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_request_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_request_purpose: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_request_identifier = (
            development_sample_request_identifier
        )
        self.development_sample_request_name = development_sample_request_name
        self.sourcing_configuration = sourcing_configuration
        self.development_sample_request_season = (
            development_sample_request_season
        )
        self.development_sample_request_date = development_sample_request_date
        self.development_sample_request_purpose = (
            development_sample_request_purpose
        )
        super().__init__(_data)


class DSampleRequestStatus(sob.model.Object):
    """
    Properties:

    - development_sample_request_status_indicator:
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
        development_sample_request_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_request_status_indicator = (
            development_sample_request_status_indicator
        )
        super().__init__(_data)


class DSampleShipmentAudit(sob.model.Object):
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


class DSampleShipmentCore(sob.model.Object):
    """
    Properties:

    - development_sample_shipment_identifier:
      Dev Sample Identifier - Same Identifier as Dev Sample Identifier
    - development_sample
    - development_sample_state
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_sample_shipment_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_sample_state: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_shipment_identifier = (
            development_sample_shipment_identifier
        )
        self.development_sample = development_sample
        self.development_sample_state = development_sample_state
        super().__init__(_data)


class DSampleShipmentDetails(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DSampleShipmentDetail"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DSampleShipmentDetail(sob.model.Object):
    """
    Properties:

    - estimated_ship_date
    - actual_ship_date
    - received_date
    - shipping_service
    - shipment_tracking_number:
      No Definition Available
    - ship_pairs_quantity:
      No Definition Available
    - ship_right_quantity:
      No Definition Available
    - ship_left_quantity:
      No Definition Available
    - goods_at_consolidator_reason
    - goods_at_consolidator_ap_reason
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        estimated_ship_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        actual_ship_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        received_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None,
        shipping_service: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        shipment_tracking_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        ship_pairs_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        ship_right_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        ship_left_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        goods_at_consolidator_reason: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        goods_at_consolidator_ap_reason: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.estimated_ship_date = estimated_ship_date
        self.actual_ship_date = actual_ship_date
        self.received_date = received_date
        self.shipping_service = shipping_service
        self.shipment_tracking_number = shipment_tracking_number
        self.ship_pairs_quantity = ship_pairs_quantity
        self.ship_right_quantity = ship_right_quantity
        self.ship_left_quantity = ship_left_quantity
        self.goods_at_consolidator_reason = goods_at_consolidator_reason
        self.goods_at_consolidator_ap_reason = goods_at_consolidator_ap_reason
        super().__init__(_data)


class DSampleShipmentFactoryComments(sob.model.Object):
    """
    Properties:

    - factory_sample_comments:
      No Definition Available
    - factory_sub_location_im_number:
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
        factory_sample_comments: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        factory_sub_location_im_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.factory_sample_comments = factory_sample_comments
        self.factory_sub_location_im_number = factory_sub_location_im_number
        super().__init__(_data)


class DSampleStatus(sob.model.Object):
    """
    Properties:

    - development_sample_status_indicator:
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
        development_sample_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_sample_status_indicator = (
            development_sample_status_indicator
        )
        super().__init__(_data)


class DcAudit(sob.model.Object):
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


class DcCore(sob.model.Object):
    """
    Properties:

    - development_colorway_identifier:
      No Definition Available
    - development_colorway_description:
      No Definition Available
    - development_colorway_name:
      No Definition Available
    - development_style_identifier:
      No Definition Available
    - development_colorway_type
    - development_colorway_state
    - development_colorway_gate
    - product_identifier:
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
        development_colorway_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_type: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_state: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_gate: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        product_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_identifier = development_colorway_identifier
        self.development_colorway_description = (
            development_colorway_description
        )
        self.development_colorway_name = development_colorway_name
        self.development_style_identifier = development_style_identifier
        self.development_colorway_type = development_colorway_type
        self.development_colorway_state = development_colorway_state
        self.development_colorway_gate = development_colorway_gate
        self.product_identifier = product_identifier
        super().__init__(_data)


class DcSeasonAudit(sob.model.Object):
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


class DcSeasonCore(sob.model.Object):
    """
    Properties:

    - development_colorway_season_identifier:
      No Definition Available
    - development_colorway_identifier:
      No Definition Available
    - development_style_season_identifier:
      No Definition Available
    - product_offering_identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        product_offering_identifier: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_season_identifier = (
            development_colorway_season_identifier
        )
        self.development_colorway_identifier = development_colorway_identifier
        self.development_style_season_identifier = (
            development_style_season_identifier
        )
        self.product_offering_identifier = product_offering_identifier
        super().__init__(_data)


class DcSeasonFOB(sob.model.Object):
    """
    Properties:

    - target_fob:
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
        target_fob: typing.Optional[
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
        self.target_fob = target_fob
        super().__init__(_data)


class DcSeasonQuantity(sob.model.Object):
    """
    Properties:

    - prototype_quantity:
      No Definition Available
    - sample_quantity:
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
        prototype_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sample_quantity: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.prototype_quantity = prototype_quantity
        self.sample_quantity = sample_quantity
        super().__init__(_data)


class DcSeasonSourcingConfig(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_colorway_season:
      Reference Link to Sourcing Configuration Colorway Season endpoint
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sourcing_configuration_colorway_season: typing.Optional[
            typing.Union[
                "DcSeasonSourcingConfigSourcingConfigurationColorwaySeason",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_colorway_season = (
            sourcing_configuration_colorway_season
        )
        super().__init__(_data)


class DcSeasonSourcingConfigSourcingConfigurationColorwaySeason(
    sob.model.Array
):
    """
    Reference Link to Sourcing Configuration Colorway Season endpoint
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "Reference"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DcSeasonStatus(sob.model.Object):
    """
    Properties:

    - development_colorway_season_status_indicator:
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
        development_colorway_season_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_season_status_indicator = (
            development_colorway_season_status_indicator
        )
        super().__init__(_data)


class DcSeasonTrial(sob.model.Object):
    """
    Properties:

    - nike_production_trial
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        nike_production_trial: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.nike_production_trial = nike_production_trial
        super().__init__(_data)


class DcStatus(sob.model.Object):
    """
    Properties:

    - development_colorway_status_indicator:
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
        development_colorway_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_colorway_status_indicator = (
            development_colorway_status_indicator
        )
        super().__init__(_data)


class DevelopmentColorwayBulkResponse(sob.model.Object):
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
                "DevelopmentColorwayBulkResponseContents",
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


class DevelopmentColorwayBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "DevelopmentColorwayBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class DevelopmentColorwayBulkResponseContent(sob.model.Object):
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
                "DevelopmentColorwayDataunits",
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


class DevelopmentColorwayResponse(sob.model.Object):
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
                "DevelopmentColorwayResponseContent",
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


class DevelopmentColorwayResponseContent(sob.model.Object):
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
                "DevelopmentColorwayDataunits",
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


class DevelopmentColorwayDataunits(sob.model.Object):
    """
    Properties:

    - dc_season_core
    - dc_season_status
    - dc_season_sourcing_config
    - dc_season_quantity
    - dc_season_trial
    - dc_season_fob
    - dc_season_audit
    - ds_season_core
    - ds_season_resource
    - ds_season_technical_difficulty
    - ds_season_fob
    - ds_season_track
    - ds_season_status
    - ds_season_audit
    - dc_core
    - dc_status
    - dc_audit
    - ds_core
    - ds_classification
    - ds_last
    - ds_status
    - ds_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        dc_season_core: typing.Optional[
            typing.Union[
                "DcSeasonCore",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_status: typing.Optional[
            typing.Union[
                "DcSeasonStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_sourcing_config: typing.Optional[
            typing.Union[
                "DcSeasonSourcingConfig",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_quantity: typing.Optional[
            typing.Union[
                "DcSeasonQuantity",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_trial: typing.Optional[
            typing.Union[
                "DcSeasonTrial",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_fob: typing.Optional[
            typing.Union[
                "DcSeasonFOB",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_season_audit: typing.Optional[
            typing.Union[
                "DcSeasonAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_core: typing.Optional[
            typing.Union[
                "DsSeasonCore",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_resource: typing.Optional[
            typing.Union[
                "DsSeasonResource",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_technical_difficulty: typing.Optional[
            typing.Union[
                "DsSeasonTechnicalDifficulty",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_fob: typing.Optional[
            typing.Union[
                "DsSeasonFOB",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_track: typing.Optional[
            typing.Union[
                "DsSeasonTrack",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_status: typing.Optional[
            typing.Union[
                "DsSeasonStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_season_audit: typing.Optional[
            typing.Union[
                "DsSeasonAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_core: typing.Optional[
            typing.Union[
                "DcCore",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_status: typing.Optional[
            typing.Union[
                "DcStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        dc_audit: typing.Optional[
            typing.Union[
                "DcAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_core: typing.Optional[
            typing.Union[
                "DsCore",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_classification: typing.Optional[
            typing.Union[
                "DsClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_last: typing.Optional[
            typing.Union[
                "DsLast",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_status: typing.Optional[
            typing.Union[
                "DsStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_audit: typing.Optional[
            typing.Union[
                "DsAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.dc_season_core = dc_season_core
        self.dc_season_status = dc_season_status
        self.dc_season_sourcing_config = dc_season_sourcing_config
        self.dc_season_quantity = dc_season_quantity
        self.dc_season_trial = dc_season_trial
        self.dc_season_fob = dc_season_fob
        self.dc_season_audit = dc_season_audit
        self.ds_season_core = ds_season_core
        self.ds_season_resource = ds_season_resource
        self.ds_season_technical_difficulty = ds_season_technical_difficulty
        self.ds_season_fob = ds_season_fob
        self.ds_season_track = ds_season_track
        self.ds_season_status = ds_season_status
        self.ds_season_audit = ds_season_audit
        self.dc_core = dc_core
        self.dc_status = dc_status
        self.dc_audit = dc_audit
        self.ds_core = ds_core
        self.ds_classification = ds_classification
        self.ds_last = ds_last
        self.ds_status = ds_status
        self.ds_audit = ds_audit
        super().__init__(_data)


class DevelopmentMeasurementResponse(sob.model.Object):
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
                "DevelopmentMeasurementResponseContent",
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


class DevelopmentMeasurementResponseContent(sob.model.Object):
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
                "DevelopmentMeasurementDataunits",
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


class DevelopmentMeasurementDataunits(sob.model.Object):
    """
    Properties:

    - ms_core
    - ms_template
    - ms_size
    - ms_point_of_measurement
    - ms_status
    - ms_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        ms_core: typing.Optional[
            typing.Union[
                "MsCore",
                sob.utilities.types.Null
            ]
        ] = None,
        ms_template: typing.Optional[
            typing.Union[
                "MsTemplate",
                sob.utilities.types.Null
            ]
        ] = None,
        ms_size: typing.Optional[
            typing.Union[
                "MsSize",
                sob.utilities.types.Null
            ]
        ] = None,
        ms_point_of_measurement: typing.Optional[
            typing.Union[
                "MsPointOfMeasurementBreakdowns",
                sob.utilities.types.Null
            ]
        ] = None,
        ms_status: typing.Optional[
            typing.Union[
                "MsStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        ms_audit: typing.Optional[
            typing.Union[
                "MsAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.ms_core = ms_core
        self.ms_template = ms_template
        self.ms_size = ms_size
        self.ms_point_of_measurement = ms_point_of_measurement
        self.ms_status = ms_status
        self.ms_audit = ms_audit
        super().__init__(_data)


class DevelopmentPointOfMeasurementResponse(sob.model.Object):
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
                "DevelopmentPointOfMeasurementResponseContent",
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


class DevelopmentPointOfMeasurementResponseContent(sob.model.Object):
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
                "DevelopmentPointOfMeasurementDataunits",
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


class DevelopmentPointOfMeasurementDataunits(sob.model.Object):
    """
    Properties:

    - pom_core
    - pom_status
    - pom_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        pom_core: typing.Optional[
            typing.Union[
                "PomCore",
                sob.utilities.types.Null
            ]
        ] = None,
        pom_status: typing.Optional[
            typing.Union[
                "PomStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        pom_audit: typing.Optional[
            typing.Union[
                "PomAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.pom_core = pom_core
        self.pom_status = pom_status
        self.pom_audit = pom_audit
        super().__init__(_data)


class DevelopmentSampleResponse(sob.model.Object):
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
                "DevelopmentSampleResponseContent",
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


class DevelopmentSampleResponseContent(sob.model.Object):
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
                "DevelopmentSampleDataunits",
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


class DevelopmentSampleShipmentResponse(sob.model.Object):
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
                "DevelopmentSampleShipmentResponseContent",
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


class DevelopmentSampleShipmentResponseContent(sob.model.Object):
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
                "DevelopmentSampleShipmentDataunits",
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


class DevelopmentSampleShipmentDataunits(sob.model.Object):
    """
    Properties:

    - d_sample_shipment_core
    - d_sample_shipment_factory_comments
    - d_sample_shipment_audit
    - d_sample_shipment_detail
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        d_sample_shipment_core: typing.Optional[
            typing.Union[
                "DSampleShipmentCore",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_shipment_factory_comments: typing.Optional[
            typing.Union[
                "DSampleShipmentFactoryComments",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_shipment_audit: typing.Optional[
            typing.Union[
                "DSampleShipmentAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_shipment_detail: typing.Optional[
            typing.Union[
                "DSampleShipmentDetails",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.d_sample_shipment_core = d_sample_shipment_core
        self.d_sample_shipment_factory_comments = (
            d_sample_shipment_factory_comments
        )
        self.d_sample_shipment_audit = d_sample_shipment_audit
        self.d_sample_shipment_detail = d_sample_shipment_detail
        super().__init__(_data)


class DevelopmentSampleDataunits(sob.model.Object):
    """
    Properties:

    - d_sample_core
    - d_sample_status
    - d_sample_classification
    - d_sample_comments
    - d_sample_audit
    - d_sample_request_core
    - d_sample_request_comments
    - d_sample_request_status
    - d_sample_request_audit
    - d_sample_order_detail
    - d_sample_evaluation
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        d_sample_core: typing.Optional[
            typing.Union[
                "DSampleCore",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_status: typing.Optional[
            typing.Union[
                "DSampleStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_classification: typing.Optional[
            typing.Union[
                "DSampleClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_comments: typing.Optional[
            typing.Union[
                "DSampleComments",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_audit: typing.Optional[
            typing.Union[
                "DSampleAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_request_core: typing.Optional[
            typing.Union[
                "DSampleRequestCore",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_request_comments: typing.Optional[
            typing.Union[
                "DSampleRequestComments",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_request_status: typing.Optional[
            typing.Union[
                "DSampleRequestStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_request_audit: typing.Optional[
            typing.Union[
                "DSampleRequestAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_order_detail: typing.Optional[
            typing.Union[
                "DSampleOrderDetail",
                sob.utilities.types.Null
            ]
        ] = None,
        d_sample_evaluation: typing.Optional[
            typing.Union[
                "DSampleEvaluation",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.d_sample_core = d_sample_core
        self.d_sample_status = d_sample_status
        self.d_sample_classification = d_sample_classification
        self.d_sample_comments = d_sample_comments
        self.d_sample_audit = d_sample_audit
        self.d_sample_request_core = d_sample_request_core
        self.d_sample_request_comments = d_sample_request_comments
        self.d_sample_request_status = d_sample_request_status
        self.d_sample_request_audit = d_sample_request_audit
        self.d_sample_order_detail = d_sample_order_detail
        self.d_sample_evaluation = d_sample_evaluation
        super().__init__(_data)


class DevelopmentStyleResponse(sob.model.Object):
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
                "DevelopmentStyleResponseContent",
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


class DevelopmentStyleResponseContent(sob.model.Object):
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
                "DevelopmentStyleDataunits",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.object_id = object_id
        self.object_type = object_type
        self.data = data
        super().__init__(_data)


class DevelopmentStyleDataunits(sob.model.Object):
    """
    Properties:

    - ds_core
    - ds_classification
    - ds_last
    - ds_status
    - ds_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        ds_core: typing.Optional[
            typing.Union[
                "DsCore",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_classification: typing.Optional[
            typing.Union[
                "DsClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_last: typing.Optional[
            typing.Union[
                "DsLast",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_status: typing.Optional[
            typing.Union[
                "DsStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        ds_audit: typing.Optional[
            typing.Union[
                "DsAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.ds_core = ds_core
        self.ds_classification = ds_classification
        self.ds_last = ds_last
        self.ds_status = ds_status
        self.ds_audit = ds_audit
        super().__init__(_data)


class DsAudit(sob.model.Object):
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


class DsClassification(sob.model.Object):
    """
    Properties:

    - development_style_type
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
        development_style_type: typing.Optional[
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
        ] = None
    ) -> None:
        self.development_style_type = development_style_type
        self.division = division
        super().__init__(_data)


class DsCore(sob.model.Object):
    """
    Properties:

    - development_style_identifier:
      No Definition Available
    - model_identifier:
      No Definition Available
    - style_number:
      No Definition Available
    - development_style_name:
      No Definition Available
    - development_style_description:
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
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        model_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        style_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_description: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_identifier = development_style_identifier
        self.model_identifier = model_identifier
        self.style_number = style_number
        self.development_style_name = development_style_name
        self.development_style_description = development_style_description
        super().__init__(_data)


class DsLast(sob.model.Object):
    """
    Properties:

    - last_identifier:
      No Definition Available
    - additional_last_identifier:
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
        last_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        additional_last_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.last_identifier = last_identifier
        self.additional_last_identifier = additional_last_identifier
        super().__init__(_data)


class DsSeasonAudit(sob.model.Object):
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


class DsSeasonCore(sob.model.Object):
    """
    Properties:

    - development_style_season_identifier:
      No Definition Available
    - development_style_identifier:
      No Definition Available
    - cycle_year
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_style_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        cycle_year: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_season_identifier = (
            development_style_season_identifier
        )
        self.development_style_identifier = development_style_identifier
        self.cycle_year = cycle_year
        super().__init__(_data)


class DsSeasonFOB(sob.model.Object):
    """
    Properties:

    - target_fob:
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
        target_fob: typing.Optional[
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
        self.target_fob = target_fob
        super().__init__(_data)


class DsSeasonResource(sob.model.Object):
    """
    Properties:

    - nlo_chemical_engineer_user_identifier:
      No Definition Available
    - nlo_costing_user_identifier:
      No Definition Available
    - nlo_developer_user_identifier:
      No Definition Available
    - nlo_knit_engineer_user_identifier:
      No Definition Available
    - nlo_knit_programmer_user_identifier:
      No Definition Available
    - nlo_material_user_identifier:
      No Definition Available
    - nlo_product_engineer_user_identifier:
      No Definition Available
    - nlo_category_director_user_identifier:
      No Definition Available
    - whq_color_designer_user_identifier:
      No Definition Available
    - whq_costing_user_identifier:
      No Definition Available
    - whq_designer_user_identifier:
      No Definition Available
    - whq_developer_user_identifier:
      No Definition Available
    - whq_footwear_development_director_user_identifier:
      No Definition Available
    - whq_knit_developer_user_identifier:
      No Definition Available
    - whq_knit_engineer_user_identifier:
      No Definition Available
    - whq_knit_programmer_user_identifier:
      No Definition Available
    - whq_material_user_identifier:
      No Definition Available
    - whq_product_engineer_user_identifier:
      No Definition Available
    - whq_product_testing_user_identifier:
      No Definition Available
    - knit_center_developer_user_identifier:
      No Definition Available
    - new_upper_indicator:
      No Definition Available
    - new_midsole_indicator:
      No Definition Available
    - new_outsole_indicator:
      No Definition Available
    - product_season_development_team
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        nlo_chemical_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_costing_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_developer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_knit_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_knit_programmer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_material_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_product_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        nlo_category_director_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_color_designer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_costing_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_designer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_developer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_footwear_development_director_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_knit_developer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_knit_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_knit_programmer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_material_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_product_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        whq_product_testing_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        knit_center_developer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        new_upper_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        new_midsole_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        new_outsole_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        product_season_development_team: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.nlo_chemical_engineer_user_identifier = (
            nlo_chemical_engineer_user_identifier
        )
        self.nlo_costing_user_identifier = nlo_costing_user_identifier
        self.nlo_developer_user_identifier = nlo_developer_user_identifier
        self.nlo_knit_engineer_user_identifier = (
            nlo_knit_engineer_user_identifier
        )
        self.nlo_knit_programmer_user_identifier = (
            nlo_knit_programmer_user_identifier
        )
        self.nlo_material_user_identifier = nlo_material_user_identifier
        self.nlo_product_engineer_user_identifier = (
            nlo_product_engineer_user_identifier
        )
        self.nlo_category_director_user_identifier = (
            nlo_category_director_user_identifier
        )
        self.whq_color_designer_user_identifier = (
            whq_color_designer_user_identifier
        )
        self.whq_costing_user_identifier = whq_costing_user_identifier
        self.whq_designer_user_identifier = whq_designer_user_identifier
        self.whq_developer_user_identifier = whq_developer_user_identifier
        self.whq_footwear_development_director_user_identifier = (
            whq_footwear_development_director_user_identifier
        )
        self.whq_knit_developer_user_identifier = (
            whq_knit_developer_user_identifier
        )
        self.whq_knit_engineer_user_identifier = (
            whq_knit_engineer_user_identifier
        )
        self.whq_knit_programmer_user_identifier = (
            whq_knit_programmer_user_identifier
        )
        self.whq_material_user_identifier = whq_material_user_identifier
        self.whq_product_engineer_user_identifier = (
            whq_product_engineer_user_identifier
        )
        self.whq_product_testing_user_identifier = (
            whq_product_testing_user_identifier
        )
        self.knit_center_developer_user_identifier = (
            knit_center_developer_user_identifier
        )
        self.new_upper_indicator = new_upper_indicator
        self.new_midsole_indicator = new_midsole_indicator
        self.new_outsole_indicator = new_outsole_indicator
        self.product_season_development_team = product_season_development_team
        super().__init__(_data)


class DsSeasonStatus(sob.model.Object):
    """
    Properties:

    - development_style_season_status_indicator:
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
        development_style_season_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_season_status_indicator = (
            development_style_season_status_indicator
        )
        super().__init__(_data)


class DsSeasonTechnicalDifficulty(sob.model.Object):
    """
    Properties:

    - technical_difficulty
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        technical_difficulty: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.technical_difficulty = technical_difficulty
        super().__init__(_data)


class DsSeasonTrack(sob.model.Object):
    """
    Properties:

    - development_track
    - product_track
    - start_date:
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
        development_track: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        product_track: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        start_date: typing.Optional[
            typing.Union[
                datetime.date,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_track = development_track
        self.product_track = product_track
        self.start_date = start_date
        super().__init__(_data)


class DsStatus(sob.model.Object):
    """
    Properties:

    - development_style_status_indicator:
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
        development_style_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_status_indicator = (
            development_style_status_indicator
        )
        super().__init__(_data)


class MsAudit(sob.model.Object):
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


class MsCore(sob.model.Object):
    """
    Properties:

    - measurement_set_identifier:
      Dev Measurement Identifier
    - measurement_set_name
    - measurement_set_state
    - measurement_set_applicability_list
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        measurement_set_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_set_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_set_state: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_set_applicability_list: typing.Optional[
            typing.Union[
                "MsCoreMeasurementSetApplicabilityList",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_set_identifier = measurement_set_identifier
        self.measurement_set_name = measurement_set_name
        self.measurement_set_state = measurement_set_state
        self.measurement_set_applicability_list = (
            measurement_set_applicability_list
        )
        super().__init__(_data)


class MsCoreMeasurementSetApplicabilityList(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "MsCoreMeasurementSetApplicability"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MsCoreMeasurementSetApplicability(sob.model.Object):
    """
    Properties:

    - development_style_identifier
    - style_number
    - cycle_year
    - sourcing_configuration_identifier
    - sourcing_configuration_season_identifier:
      Sourcing Configuration Season Identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        style_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        cycle_year: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_identifier = development_style_identifier
        self.style_number = style_number
        self.cycle_year = cycle_year
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        self.sourcing_configuration_season_identifier = (
            sourcing_configuration_season_identifier
        )
        super().__init__(_data)


class MsPointOfMeasurementBreakdowns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "MsPointOfMeasurementBreakdown"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MsPointOfMeasurementBreakdown(sob.model.Object):
    """
    Properties:

    - size
    - size_breakdown
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        size: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        size_breakdown: typing.Optional[
            typing.Union[
                "MsPointOfMeasurementSizeBreakdowns",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.size = size
        self.size_breakdown = size_breakdown
        super().__init__(_data)


class MsPointOfMeasurementSizeBreakdowns(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "MsPointOfMeasurementSizeBreakdown"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class MsPointOfMeasurementSizeBreakdown(sob.model.Object):
    """
    Properties:

    - measurement_code:
      No Definition Available
    - point_of_measurement_name:
      No Definition Available
    - sort_order:
      No Definition Available
    - measurement_instructions:
      No Definition Available
    - measurement_detail:
      No Definition Available
    - point_of_measurement_criticality
    - tolerance_negative
    - tolerance_positive
    - measurement_size_value
    - point_of_measurement
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        measurement_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        sort_order: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_instructions: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_detail: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_criticality: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        tolerance_negative: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        tolerance_positive: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_size_value: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_code = measurement_code
        self.point_of_measurement_name = point_of_measurement_name
        self.sort_order = sort_order
        self.measurement_instructions = measurement_instructions
        self.measurement_detail = measurement_detail
        self.point_of_measurement_criticality = (
            point_of_measurement_criticality
        )
        self.tolerance_negative = tolerance_negative
        self.tolerance_positive = tolerance_positive
        self.measurement_size_value = measurement_size_value
        self.point_of_measurement = point_of_measurement
        super().__init__(_data)


class MsSize(sob.model.Object):
    """
    Properties:

    - development_style_size_definition:
      No Definition Available
    - measurement_value_unit_of_measure
    - base_size:
      No Definition Available
    - size_selection_list
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        development_style_size_definition: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_value_unit_of_measure: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        base_size: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        size_selection_list: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.development_style_size_definition = (
            development_style_size_definition
        )
        self.measurement_value_unit_of_measure = (
            measurement_value_unit_of_measure
        )
        self.base_size = base_size
        self.size_selection_list = size_selection_list
        super().__init__(_data)


class MsStatus(sob.model.Object):
    """
    Properties:

    - measurement_set_status_indicator:
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
        measurement_set_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_set_status_indicator = (
            measurement_set_status_indicator
        )
        super().__init__(_data)


class MsTemplate(sob.model.Object):
    """
    Properties:

    - measurement_set_template_name:
      No Definition Available
    - size_definition_template:
      No Definition Available
    - grade_rule_template:
      No Definition Available
    - measurement_template_type
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        measurement_set_template_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        size_definition_template: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        grade_rule_template: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_template_type: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.measurement_set_template_name = measurement_set_template_name
        self.size_definition_template = size_definition_template
        self.grade_rule_template = grade_rule_template
        self.measurement_template_type = measurement_template_type
        super().__init__(_data)


class PomAudit(sob.model.Object):
    """
    Properties:

    - create_timestamp:
      No Definition Available
    - change_timestamp:
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
        ] = None
    ) -> None:
        self.create_timestamp = create_timestamp
        self.change_timestamp = change_timestamp
        super().__init__(_data)


class PomCore(sob.model.Object):
    """
    Properties:

    - sort_order:
      No Definition Available
    - measurement_code:
      No Definition Available
    - point_of_measurement_name:
      No Definition Available
    - measurement_instructions:
      No Definition Available
    - measurement_detail:
      No Definition Available
    - point_of_measurement_criticality
    - tolerance_negative
    - tolerance_positive
    - point_of_measurement_identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sort_order: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_instructions: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        measurement_detail: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_criticality: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        tolerance_negative: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        tolerance_positive: typing.Optional[
            typing.Union[
                typing.Union[
                    float,
                    int,
                    decimal.Decimal
                ],
                sob.utilities.types.Null
            ]
        ] = None,
        point_of_measurement_identifier: typing.Optional[
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
        self.sort_order = sort_order
        self.measurement_code = measurement_code
        self.point_of_measurement_name = point_of_measurement_name
        self.measurement_instructions = measurement_instructions
        self.measurement_detail = measurement_detail
        self.point_of_measurement_criticality = (
            point_of_measurement_criticality
        )
        self.tolerance_negative = tolerance_negative
        self.tolerance_positive = tolerance_positive
        self.point_of_measurement_identifier = point_of_measurement_identifier
        super().__init__(_data)


class PomStatus(sob.model.Object):
    """
    Properties:

    - point_of_measurement_status_indicator:
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
        point_of_measurement_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.point_of_measurement_status_indicator = (
            point_of_measurement_status_indicator
        )
        super().__init__(_data)


class RelationshipResponse(sob.model.Object):
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
                "RelationshipResponseContents",
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


class RelationshipResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "RelationshipResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class RelationshipResponseContent(sob.model.Object):
    """
    Properties:

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
        relationships: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.relationships = relationships
        super().__init__(_data)


class ScAudit(sob.model.Object):
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


class ScClassification(sob.model.Object):
    """
    Properties:

    - development_style_type
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
        development_style_type: typing.Optional[
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
        ] = None
    ) -> None:
        self.development_style_type = development_style_type
        self.division = division
        super().__init__(_data)


class ScColorwaySeasonAudit(sob.model.Object):
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


class ScColorwaySeasonClassification(sob.model.Object):
    """
    Properties:

    - development_style_type
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
        development_style_type: typing.Optional[
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
        ] = None
    ) -> None:
        self.development_style_type = development_style_type
        self.division = division
        super().__init__(_data)


class ScColorwaySeasonCore(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_colorway_season_identifier:
      No Definition Available
    - development_colorway_season_identifier:
      No Definition Available
    - sourcing_configuration_colorway_season_primary_indicator:
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
        sourcing_configuration_colorway_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        development_colorway_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_colorway_season_primary_indicator: typing.Optional[  # noqa
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_colorway_season_identifier = (
            sourcing_configuration_colorway_season_identifier
        )
        self.development_colorway_season_identifier = (
            development_colorway_season_identifier
        )
        self.sourcing_configuration_colorway_season_primary_indicator = (
            sourcing_configuration_colorway_season_primary_indicator
        )
        super().__init__(_data)


class ScColorwaySeasonStatus(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_colorway_season_status_indicator:
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
        sourcing_configuration_colorway_season_status_indicator: typing.Optional[  # noqa
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_colorway_season_status_indicator = (
            sourcing_configuration_colorway_season_status_indicator
        )
        super().__init__(_data)


class ScCore(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_identifier:
      No Definition Available
    - sourcing_configuration_name:
      No Definition Available
    - development_style_identifier:
      No Definition Available
    - product_creation_center_identifier:
      No Definition Available
    - legacy_factory_code:
      No Definition Available
    - legacy_product_creation_center_code
    - sourcing_configuration_primary_indicator:
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
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        product_creation_center_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_factory_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_product_creation_center_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_primary_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        self.sourcing_configuration_name = sourcing_configuration_name
        self.development_style_identifier = development_style_identifier
        self.product_creation_center_identifier = (
            product_creation_center_identifier
        )
        self.legacy_factory_code = legacy_factory_code
        self.legacy_product_creation_center_code = (
            legacy_product_creation_center_code
        )
        self.sourcing_configuration_primary_indicator = (
            sourcing_configuration_primary_indicator
        )
        super().__init__(_data)


class ScSeasonAudit(sob.model.Object):
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


class ScSeasonCore(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_identifier:
      No Definition Available
    - sourcing_configuration_season_identifier:
      No Definition Available
    - product_creation_center_identifier:
      No Definition Available
    - legacy_product_creation_center_code
    - product_creation_centre_developer:
      No Definition Available
    - development_style_season_identifier:
      No Definition Available
    - sourcing_identifier:
      Sourcing Identifier linked to Global Sourcing - Sourcing endpoint
    - sourcing_configuration_season_primary_indicator:
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
        sourcing_configuration_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        product_creation_center_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_product_creation_center_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        product_creation_centre_developer: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        development_style_season_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        sourcing_configuration_season_primary_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_identifier = (
            sourcing_configuration_identifier
        )
        self.sourcing_configuration_season_identifier = (
            sourcing_configuration_season_identifier
        )
        self.product_creation_center_identifier = (
            product_creation_center_identifier
        )
        self.legacy_product_creation_center_code = (
            legacy_product_creation_center_code
        )
        self.product_creation_centre_developer = (
            product_creation_centre_developer
        )
        self.development_style_season_identifier = (
            development_style_season_identifier
        )
        self.sourcing_identifier = sourcing_identifier
        self.sourcing_configuration_season_primary_indicator = (
            sourcing_configuration_season_primary_indicator
        )
        super().__init__(_data)


class ScSeasonResource(sob.model.Object):
    """
    Properties:

    - pmo_chemical_engineer_user_identifier:
      No Definition Available
    - pmo_costing_user_identifier:
      No Definition Available
    - pmo_developer_user_identifier:
      No Definition Available
    - pmo_material_user_identifier:
      No Definition Available
    - pmo_product_engineer_user_identifier:
      No Definition Available
    - pmo_category_director_user_identifier:
      No Definition Available
    - pmo_manufacturing_engineer_user_identifier:
      No Definition Available
    - pmo_manufacturing_chemical_engineer_user_identifier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        pmo_chemical_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_costing_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_developer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_material_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_product_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_category_director_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_manufacturing_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        pmo_manufacturing_chemical_engineer_user_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.pmo_chemical_engineer_user_identifier = (
            pmo_chemical_engineer_user_identifier
        )
        self.pmo_costing_user_identifier = pmo_costing_user_identifier
        self.pmo_developer_user_identifier = pmo_developer_user_identifier
        self.pmo_material_user_identifier = pmo_material_user_identifier
        self.pmo_product_engineer_user_identifier = (
            pmo_product_engineer_user_identifier
        )
        self.pmo_category_director_user_identifier = (
            pmo_category_director_user_identifier
        )
        self.pmo_manufacturing_engineer_user_identifier = (
            pmo_manufacturing_engineer_user_identifier
        )
        self.pmo_manufacturing_chemical_engineer_user_identifier = (
            pmo_manufacturing_chemical_engineer_user_identifier
        )
        super().__init__(_data)


class ScSeasonStatus(sob.model.Object):
    """
    Properties:

    - sourcing_configuration_season_status_indicator:
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
        sourcing_configuration_season_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sourcing_configuration_season_status_indicator = (
            sourcing_configuration_season_status_indicator
        )
        super().__init__(_data)


class SearchResponse(sob.model.Object):
    """
    Properties:

    - content
    - count:
      The number of entries returned in this responses
    - offset:
      The number of entries offset (can be used to derive the "Page Number" by
      using count)
    - total_count:
      The total number of records in this search
    - next_
    - prev
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
                "SearchResponseContents",
                sob.utilities.types.Null
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        offset: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        total_count: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        next_: typing.Optional[
            typing.Union[
                "Links",
                sob.utilities.types.Null
            ]
        ] = None,
        prev: typing.Optional[
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
        self.offset = offset
        self.total_count = total_count
        self.next_ = next_
        self.prev = prev
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class SearchResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SearchResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SearchResponseContent(sob.model.Object):
    """
    Properties:

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
        relationships: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.relationships = relationships
        super().__init__(_data)


class SourcingConfigurationColorwaySeasonDataunits(sob.model.Object):
    """
    Properties:

    - sc_colorway_season_core
    - sc_colorway_season_classification
    - sc_colorway_season_status
    - sc_colorway_season_audit
    - sc_season_core
    - sc_season_status
    - sc_season_audit
    - sc_season_resource
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sc_colorway_season_core: typing.Optional[
            typing.Union[
                "ScColorwaySeasonCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_colorway_season_classification: typing.Optional[
            typing.Union[
                "ScColorwaySeasonClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_colorway_season_status: typing.Optional[
            typing.Union[
                "ScColorwaySeasonStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_colorway_season_audit: typing.Optional[
            typing.Union[
                "ScColorwaySeasonAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_season_core: typing.Optional[
            typing.Union[
                "ScSeasonCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_season_status: typing.Optional[
            typing.Union[
                "ScSeasonStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_season_audit: typing.Optional[
            typing.Union[
                "ScSeasonAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_season_resource: typing.Optional[
            typing.Union[
                "ScSeasonResource",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sc_colorway_season_core = sc_colorway_season_core
        self.sc_colorway_season_classification = (
            sc_colorway_season_classification
        )
        self.sc_colorway_season_status = sc_colorway_season_status
        self.sc_colorway_season_audit = sc_colorway_season_audit
        self.sc_season_core = sc_season_core
        self.sc_season_status = sc_season_status
        self.sc_season_audit = sc_season_audit
        self.sc_season_resource = sc_season_resource
        super().__init__(_data)


class SourcingConfigurationDataunits(sob.model.Object):
    """
    Properties:

    - sc_core
    - sc_classification
    - sc_audit
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sc_core: typing.Optional[
            typing.Union[
                "ScCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_classification: typing.Optional[
            typing.Union[
                "ScClassification",
                sob.utilities.types.Null
            ]
        ] = None,
        sc_audit: typing.Optional[
            typing.Union[
                "ScAudit",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sc_core = sc_core
        self.sc_classification = sc_classification
        self.sc_audit = sc_audit
        super().__init__(_data)


class SourcingConfigurationsBulkResponse(sob.model.Object):
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
                "SourcingConfigurationsBulkResponseContents",
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


class SourcingConfigurationsBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SourcingConfigurationsBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SourcingConfigurationsBulkResponseContent(sob.model.Object):
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
                "SourcingConfigurationDataunits",
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


class SourcingConfigurationsColorwaySeasonBulkResponse(sob.model.Object):
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
                "SourcingConfigurationsColorwaySeasonBulkResponseContents",
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


class SourcingConfigurationsColorwaySeasonBulkResponseContents(
    sob.model.Array
):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SourcingConfigurationsColorwaySeasonBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SourcingConfigurationsColorwaySeasonBulkResponseContent(
    sob.model.Object
):
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
                "SourcingConfigurationColorwaySeasonDataunits",
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


class SourcingConfigurationsColorwaySeasonResponse(sob.model.Object):
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
                "SourcingConfigurationsColorwaySeasonResponseContent",
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


class SourcingConfigurationsColorwaySeasonResponseContent(sob.model.Object):
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
                "SourcingConfigurationColorwaySeasonDataunits",
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


class SourcingConfigurationsResponse(sob.model.Object):
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
                "SourcingConfigurationsResponseContent",
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


class SourcingConfigurationsResponseContent(sob.model.Object):
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
                "SourcingConfigurationDataunits",
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


class DataBillOfMaterialsGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Product
    Development Bill Of Materials)
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


class DataBillOfMaterialsGetDataunits(sob.model.Array):
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


class DataBillOfMaterialsSourcesGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Product
    Development Bill Of Materials)
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


class DataBillOfMaterialsSourcesGetDataunits(sob.model.Array):
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


class DataBillOfMaterialsSourcesObjectIdGetDataunits(sob.model.Array):
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


class DataBillOfMaterialsObjectIdGetDataunits(sob.model.Array):
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


class DataColorwaySeasonsGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Product
    Development Development Colorway)
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


class DataColorwaySeasonsGetDataunits(sob.model.Array):
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


class DataColorwaySeasonsObjectIdGetDataunits(sob.model.Array):
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


class DataDevelopmentSamplesSamplesObjectIdGetDataunits(sob.model.Array):
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


class DataDevelopmentSamplesShipmentsObjectIdGetDataunits(sob.model.Array):
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


class DataDevelopmentStylesObjectIdGetDataunits(sob.model.Array):
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


class DataMeasurementSetsObjectIdGetDataunits(sob.model.Array):
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


class DataPointsOfMeasurementObjectIdGetDataunits(sob.model.Array):
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


class DataSourcingConfigurationsGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Source
    Configuration Identifier)
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


class DataSourcingConfigurationsGetDataunits(sob.model.Array):
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


class DataSourcingConfigurationsColorwaySeasonsGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Source
    Configuration Colorway Season Identifier)
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


class DataSourcingConfigurationsColorwaySeasonsGetDataunits(sob.model.Array):
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


class DataSourcingConfigurationsColorwaySeasonsObjectIdGetDataunits(
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


class DataSourcingConfigurationsObjectIdGetDataunits(sob.model.Array):
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


class SearchBillOfMaterialsGetSourcingConfigurationSeason(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetDevelopmentStyleType(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetDivision(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomDescription(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomComments(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBillOfMaterialStatusIndicator(sob.model.Array):
    """
    The reference key associated with this item
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    bool,
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


class SearchBillOfMaterialsGetBomLineItemIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomLineItemComments(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomLineItemNumber(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetParentBomLineItemIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetLineItemQuantity(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetColor(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBillOfMaterialsSection(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetPartPrimary(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetPartSecondary(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetPartModifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetPartSuffix(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetPartName(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetMaterialItemIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetSuppliedMaterial(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetSuppliedMaterialColorIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetSuppliedMaterialColorIsMultipleColors(
    sob.model.Array
):
    """
    The reference key associated with this item
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    bool,
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


class SearchBillOfMaterialsGetColorPlaceholderDescription(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetMaterialItemPlaceholderDescription(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomGUID(sob.model.Array):
    """
    The Bill of Material's Universally Unique Identifier
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


class SearchBillOfMaterialsGetBomIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetDevelopmentColorwayIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetBomName(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetDevelopmentColorwaySeasonIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsGetSourcingConfigurationIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetProductIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetStyleNumber(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetSourcingConfigurationSeason(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetCycleYear(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetDevelopmentStyleType(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetDivision(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetBillOfMaterialStatusIndicator(
    sob.model.Array
):
    """
    The reference key associated with this item
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    bool,
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


class SearchBillOfMaterialsSourcesGetBomLineItemIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetBomLineItemNumber(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetParentBomLineItemIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetLineItemQuantity(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetColor(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetBillOfMaterialsSection(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetPart(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetMaterialItemIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetSuppliedMaterial(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIsMultipleColors(
    sob.model.Array
):
    """
    The reference key associated with this item
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    bool,
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


class SearchBillOfMaterialsSourcesGetColorPlaceholderDescription(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetMaterialItemPlaceholderDescription(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetNetUsage(sob.model.Array):
    """
    The number (float) for netUsage
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchBillOfMaterialsSourcesGetWasteUsage(sob.model.Array):
    """
    The number (float) for wasteUsage
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchBillOfMaterialsSourcesGetGrossUsage(sob.model.Array):
    """
    The number (float) for grossUsage
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchBillOfMaterialsSourcesGetUsageUnitOfMeasure(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetBomGUID(sob.model.Array):
    """
    The Bill of Material's Universally Unique Identifier
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


class SearchBillOfMaterialsSourcesGetBomIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetDevelopmentColorwayIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetBomName(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetDevelopmentColorwaySeasonIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchBillOfMaterialsSourcesGetSourcingConfigurationIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetSampleQuantity(sob.model.Array):
    """
    The number associated with sampleQuantity
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


class SearchColorwaySeasonsGetNikeProductionTrial(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetTargetFOB(sob.model.Array):
    """
    The number for target FOB
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchColorwaySeasonsGetSourcingConfigurationColorwaySeason(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentStyleIdentifier(sob.model.Array):
    """
    The Id for develpment style season
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


class SearchColorwaySeasonsGetCycleYear(sob.model.Array):
    """
    The reference key associated with this item: cycleYear
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


class SearchColorwaySeasonsGetWhqColorDesignerUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqCostingUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqDesignerUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqDeveloperUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqFootwearDevelopmentDirectorUserIdentifier(
    sob.model.Array
):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqKnitDeveloperUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqKnitEngineerUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqKnitProgrammerUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqMaterialUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqProductEngineerUserIdentifier(
    sob.model.Array
):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetWhqProductTestingUserIdentifier(sob.model.Array):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetKnitCenterDeveloperUserIdentifier(
    sob.model.Array
):
    """
    The email address for this user
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


class SearchColorwaySeasonsGetProductSeasonDevelopmentTeam(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetTechnicalDifficulty(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayTargetFOB(sob.model.Array):
    """
    The reference key associated with this item
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchColorwaySeasonsGetDevelopmentTrack(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetProductTrack(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetStartDate(sob.model.Array):
    """
    The date assocated with the start of development
    """

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    datetime.date,
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


class SearchColorwaySeasonsGetLastIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetAdditionalLastIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayDescription(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayType(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayState(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayGate(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetProductIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentStyleType(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDivision(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentColorwayIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetDevelopmentStyleSeasonIdentifier(
    sob.model.Array
):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetProductOfferingIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchColorwaySeasonsGetPrototypeQuantity(sob.model.Array):
    """
    The number associated with prototypeQuantity
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


class SearchDevelopmentStylesGetDevelopmentStyleType(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetDivision(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetDevelopmentStyleName(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetModelIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetStyleNumber(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetLastIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchDevelopmentStylesGetAdditionalLastIdentifier(sob.model.Array):
    """
    The reference key associated with this item
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


class SearchMeasurementSetsGetSourcingConfigurationIdentifier(sob.model.Array):

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


class SearchMeasurementSetsGetSourcingConfigurationSeasonIdentifier(
    sob.model.Array
):

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


class SearchMeasurementSetsGetMeasurementSetTemplateName(sob.model.Array):

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


class SearchMeasurementSetsGetSizeDefinitionTemplate(sob.model.Array):

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


class SearchMeasurementSetsGetGradeRuleTemplate(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementTemplateType(sob.model.Array):

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


class SearchMeasurementSetsGetDevelopmentStyleSizeDefinition(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementValueUnitOfMeasure(sob.model.Array):

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


class SearchMeasurementSetsGetBaseSize(sob.model.Array):

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


class SearchMeasurementSetsGetSizeSelectionList(sob.model.Array):

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


class SearchMeasurementSetsGetSize(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementCode(sob.model.Array):

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


class SearchMeasurementSetsGetPointOfMeasurementName(sob.model.Array):

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


class SearchMeasurementSetsGetSortOrder(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementInstructions(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementDetail(sob.model.Array):

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


class SearchMeasurementSetsGetPointOfMeasurementCriticality(sob.model.Array):

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


class SearchMeasurementSetsGetToleranceNegative(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchMeasurementSetsGetTolerancePositive(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchMeasurementSetsGetMeasurementSizeValue(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    typing.Union[
                        float,
                        int,
                        decimal.Decimal
                    ],
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


class SearchMeasurementSetsGetPointOfMeasurement(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementSetStatusIndicator(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                typing.Union[
                    bool,
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


class SearchMeasurementSetsGetMeasurementSetName(sob.model.Array):

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


class SearchMeasurementSetsGetMeasurementSetState(sob.model.Array):

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


class SearchMeasurementSetsGetDevelopmentStyleIdentifier(sob.model.Array):

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


class SearchMeasurementSetsGetStyleNumber(sob.model.Array):

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


class SearchMeasurementSetsGetCycleYear(sob.model.Array):

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
    BillOfMaterialsBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsBulkResponseContents,
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
    BillOfMaterialsBulkResponseContents
).item_types = sob.types.MutableTypes([
    BillOfMaterialsBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsBulkResponseContent
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
                BillOfMaterialsDataunits,
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
    BillOfMaterialsResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsResponseContent,
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
    BillOfMaterialsResponseContent
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
                BillOfMaterialsDataunits,
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
    BillOfMaterialsSourceBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSourceBulkResponseContents,
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
    BillOfMaterialsSourceBulkResponseContents
).item_types = sob.types.MutableTypes([
    BillOfMaterialsSourceBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSourceBulkResponseContent
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
                BillOfMaterialsSourceDataunits,
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
    BillOfMaterialsSourceResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                BillOfMaterialsSourceResponseContent,
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
    BillOfMaterialsSourceResponseContent
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
                BillOfMaterialsSourceDataunits,
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
    BillOfMaterialsSourceDataunits
).properties = sob.meta.Properties([
    (
        'bom_core',
        sob.properties.Property(
            name="bomCore",
            required=True,
            types=sob.types.MutableTypes([
                BillOfMaterialsSourceDataunitsBomCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_sourcing_configuration_colorway_season',
        sob.properties.Property(
            name="bomSourcingConfigurationColorwaySeason",
            types=sob.types.MutableTypes([
                BomSourcingConfigurationColorwaySeason,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_classification',
        sob.properties.Property(
            name="bomClassification",
            types=sob.types.MutableTypes([
                BomClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_description',
        sob.properties.Property(
            name="bomDescription",
            types=sob.types.MutableTypes([
                BomDescription,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_status',
        sob.properties.Property(
            name="bomStatus",
            types=sob.types.MutableTypes([
                BomStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_header_audit',
        sob.properties.Property(
            name="bomHeaderAudit",
            types=sob.types.MutableTypes([
                BomHeaderAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_detail',
        sob.properties.Property(
            name="bomLineItemDetail",
            types=sob.types.MutableTypes([
                BomLineItemDetailSources,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_comments',
        sob.properties.Property(
            name="bomLineItemComments",
            types=sob.types.MutableTypes([
                BomLineItemComments,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_audit',
        sob.properties.Property(
            name="bomLineAudit",
            types=sob.types.MutableTypes([
                BomLineAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_season',
        sob.properties.Property(
            name="bomSeason",
            types=sob.types.MutableTypes([
                BillOfMaterialsSourceDataunitsBomSeason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSourceDataunitsBomCore
).properties = sob.meta.Properties([
    (
        'bom_identifier',
        sob.properties.Property(
            name="bomIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_identifier',
        sob.properties.Property(
            name="developmentColorwayIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_name',
        sob.properties.Property(
            name="bomName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_converted',
        sob.properties.Property(
            name="bomConverted",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_guid',
        sob.properties.Property(
            name="bomGUID",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_colorway_source_identifier',
        sob.properties.Property(
            name="bomColorwaySourceIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_identifier',
        sob.properties.Property(
            name="productIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'style_number',
        sob.properties.Property(
            name="styleNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsSourceDataunitsBomSeason
).properties = sob.meta.Properties([
    (
        'development_colorway_season_identifier',
        sob.properties.Property(
            name="developmentColorwaySeasonIdentifier",
            types=sob.types.MutableTypes([
                BomSeasonDevelopmentColorwaySeasonIdentifier,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'cycle_year',
        sob.properties.Property(
            name="cycleYear",
            types=sob.types.MutableTypes([
                BillOfMaterialsSourceDataunitsBomSeasonCycleYear,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BillOfMaterialsSourceDataunitsBomSeasonCycleYear
).item_types = sob.types.MutableTypes([
    Reference
])
sob.meta.object_writable(  # type: ignore
    BillOfMaterialsDataunits
).properties = sob.meta.Properties([
    (
        'bom_core',
        sob.properties.Property(
            name="bomCore",
            required=True,
            types=sob.types.MutableTypes([
                BomCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_season',
        sob.properties.Property(
            name="bomSeason",
            types=sob.types.MutableTypes([
                BomSeason,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_sourcing_configuration',
        sob.properties.Property(
            name="bomSourcingConfiguration",
            types=sob.types.MutableTypes([
                BomSourcingConfigurations,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_classification',
        sob.properties.Property(
            name="bomClassification",
            types=sob.types.MutableTypes([
                BomClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_description',
        sob.properties.Property(
            name="bomDescription",
            types=sob.types.MutableTypes([
                BomDescription,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_status',
        sob.properties.Property(
            name="bomStatus",
            types=sob.types.MutableTypes([
                BomStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_header_audit',
        sob.properties.Property(
            name="bomHeaderAudit",
            types=sob.types.MutableTypes([
                BomHeaderAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_detail',
        sob.properties.Property(
            name="bomLineItemDetail",
            types=sob.types.MutableTypes([
                BomLineItemDetails,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_comments',
        sob.properties.Property(
            name="bomLineItemComments",
            types=sob.types.MutableTypes([
                BomLineItemComments,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_audit',
        sob.properties.Property(
            name="bomLineAudit",
            types=sob.types.MutableTypes([
                BomLineAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BomClassification
).properties = sob.meta.Properties([
    (
        'development_style_type',
        sob.properties.Property(
            name="developmentStyleType",
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
    )
])
sob.meta.object_writable(  # type: ignore
    BomCore
).properties = sob.meta.Properties([
    (
        'bom_identifier',
        sob.properties.Property(
            name="bomIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_identifier',
        sob.properties.Property(
            name="developmentColorwayIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_name',
        sob.properties.Property(
            name="bomName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_converted',
        sob.properties.Property(
            name="bomConverted",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_guid',
        sob.properties.Property(
            name="bomGUID",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BomDescription
).properties = sob.meta.Properties([
    (
        'bom_description',
        sob.properties.Property(
            name="bomDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_comments',
        sob.properties.Property(
            name="bomComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BomHeaderAudit
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
    BomLineAudit
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
sob.meta.array_writable(  # type: ignore
    BomLineItemComments
).item_types = sob.types.MutableTypes([
    BomLineItemComment
])
sob.meta.object_writable(  # type: ignore
    BomLineItemComment
).properties = sob.meta.Properties([
    (
        'bom_line_item_identifier',
        sob.properties.Property(
            name="bomLineItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_comments',
        sob.properties.Property(
            name="bomLineItemComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomLineItemDetails
).item_types = sob.types.MutableTypes([
    BomLineItemDetail
])
sob.meta.object_writable(  # type: ignore
    BomLineItemDetail
).properties = sob.meta.Properties([
    (
        'bom_line_item_identifier',
        sob.properties.Property(
            name="bomLineItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_number',
        sob.properties.Property(
            name="bomLineItemNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'parent_bom_line_item_identifier',
        sob.properties.Property(
            name="parentBomLineItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'line_item_quantity',
        sob.properties.Property(
            name="lineItemQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'color',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bill_of_materials_section',
        sob.properties.Property(
            name="billOfMaterialsSection",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_primary',
        sob.properties.Property(
            name="partPrimary",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_secondary',
        sob.properties.Property(
            name="partSecondary",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_modifier',
        sob.properties.Property(
            name="partModifier",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_suffix',
        sob.properties.Property(
            name="partSuffix",
            types=sob.types.MutableTypes([
                Reference,
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
        'material_item_identifier',
        sob.properties.Property(
            name="materialItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material',
        sob.properties.Property(
            name="suppliedMaterial",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material_color_identifier',
        sob.properties.Property(
            name="suppliedMaterialColorIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material_color_is_multiple_colors',
        sob.properties.Property(
            name="suppliedMaterialColorIsMultipleColors",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'color_placeholder_description',
        sob.properties.Property(
            name="colorPlaceholderDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'material_item_placeholder_description',
        sob.properties.Property(
            name="materialItemPlaceholderDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_pattern',
        sob.properties.Property(
            name="partPattern",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_prefix',
        sob.properties.Property(
            name="partPrefix",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_guid',
        sob.properties.Property(
            name="bomLineItemGUID",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomLineItemDetailSources
).item_types = sob.types.MutableTypes([
    BomLineItemDetailSource
])
sob.meta.object_writable(  # type: ignore
    BomLineItemDetailSource
).properties = sob.meta.Properties([
    (
        'bom_line_item_identifier',
        sob.properties.Property(
            name="bomLineItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_number',
        sob.properties.Property(
            name="bomLineItemNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'parent_bom_line_item_identifier',
        sob.properties.Property(
            name="parentBomLineItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'line_item_quantity',
        sob.properties.Property(
            name="lineItemQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'color',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bill_of_materials_section',
        sob.properties.Property(
            name="billOfMaterialsSection",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pattern_part',
        sob.properties.Property(
            name="patternPart",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'material_item_identifier',
        sob.properties.Property(
            name="materialItemIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material',
        sob.properties.Property(
            name="suppliedMaterial",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material_color_identifier',
        sob.properties.Property(
            name="suppliedMaterialColorIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplied_material_color_is_multiple_colors',
        sob.properties.Property(
            name="suppliedMaterialColorIsMultipleColors",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'color_placeholder_description',
        sob.properties.Property(
            name="colorPlaceholderDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'material_item_placeholder_description',
        sob.properties.Property(
            name="materialItemPlaceholderDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'net_usage',
        sob.properties.Property(
            name="netUsage",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'waste_usage',
        sob.properties.Property(
            name="wasteUsage",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'gross_usage',
        sob.properties.Property(
            name="grossUsage",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'usage_unit_of_measure',
        sob.properties.Property(
            name="usageUnitOfMeasure",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'bom_line_item_guid',
        sob.properties.Property(
            name="bomLineItemGUID",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_pattern',
        sob.properties.Property(
            name="partPattern",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'part_prefix',
        sob.properties.Property(
            name="partPrefix",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    BomSeason
).properties = sob.meta.Properties([
    (
        'development_colorway_season_identifier',
        sob.properties.Property(
            name="developmentColorwaySeasonIdentifier",
            types=sob.types.MutableTypes([
                BomSeasonDevelopmentColorwaySeasonIdentifier,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomSeasonDevelopmentColorwaySeasonIdentifier
).item_types = sob.types.MutableTypes([
    Reference
])
sob.meta.object_writable(  # type: ignore
    BomSourcingConfigurations
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_list',
        sob.properties.Property(
            name="sourcingConfigurationList",
            types=sob.types.MutableTypes([
                BomSourcingConfigurationsList,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                BomSourcingConfigurationSourcingConfigurationIdentifier,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomSourcingConfigurationSourcingConfigurationIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    BomSourcingConfigurationsList
).item_types = sob.types.MutableTypes([
    BomSourcingConfiguration
])
sob.meta.object_writable(  # type: ignore
    BomSourcingConfiguration
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_season',
        sob.properties.Property(
            name="sourcingConfigurationSeason",
            types=sob.types.MutableTypes([
                BomSourcingConfigurationSeason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomSourcingConfigurationSeason
).item_types = sob.types.MutableTypes([
    Reference
])
sob.meta.object_writable(  # type: ignore
    BomSourcingConfigurationColorwaySeason
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_colorway_season',
        sob.properties.Property(
            name="sourcingConfigurationColorwaySeason",
            types=sob.types.MutableTypes([
                BomSourcingConfigurationColorwaySeasonSourcingConfigurationColorwaySeason,  # noqa
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    BomSourcingConfigurationColorwaySeasonSourcingConfigurationColorwaySeason  # noqa
).item_types = sob.types.MutableTypes([
    Reference
])
sob.meta.object_writable(  # type: ignore
    BomStatus
).properties = sob.meta.Properties([
    (
        'bill_of_material_status_indicator',
        sob.properties.Property(
            name="billOfMaterialStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleAudit
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
    DSampleClassification
).properties = sob.meta.Properties([
    (
        'development_style_type',
        sob.properties.Property(
            name="developmentStyleType",
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
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleComments
).properties = sob.meta.Properties([
    (
        'development_sample_comments',
        sob.properties.Property(
            name="developmentSampleComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleCore
).properties = sob.meta.Properties([
    (
        'development_sample_identifier',
        sob.properties.Property(
            name="developmentSampleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_identifier',
        sob.properties.Property(
            name="developmentColorwayIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_type',
        sob.properties.Property(
            name="developmentSampleType",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_format',
        sob.properties.Property(
            name="developmentSampleFormat",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_need_by_date',
        sob.properties.Property(
            name="developmentSampleNeedByDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_shipment',
        sob.properties.Property(
            name="developmentSampleShipment",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleEvaluation
).properties = sob.meta.Properties([
    (
        'reviewed_date',
        sob.properties.Property(
            name="reviewedDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_evaluation_state',
        sob.properties.Property(
            name="developmentSampleEvaluationState",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'fit_date',
        sob.properties.Property(
            name="fitDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'change_request_reason_code',
        sob.properties.Property(
            name="changeRequestReasonCode",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_evaluation_comments',
        sob.properties.Property(
            name="developmentSampleEvaluationComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleOrderDetail
).properties = sob.meta.Properties([
    (
        'development_sample_destination_name',
        sob.properties.Property(
            name="developmentSampleDestinationName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_address',
        sob.properties.Property(
            name="developmentSampleAddress",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'developer_destination_address',
        sob.properties.Property(
            name="developerDestinationAddress",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'attention_to',
        sob.properties.Property(
            name="attentionTo",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sample_size',
        sob.properties.Property(
            name="sampleSize",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'developer_order_quantity',
        sob.properties.Property(
            name="developerOrderQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sample_order_quantity_or_pair_quantity',
        sob.properties.Property(
            name="sampleOrderQuantityOrPairQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sample_order_right_quantity',
        sob.properties.Property(
            name="sampleOrderRightQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sample_order_left_quantity',
        sob.properties.Property(
            name="sampleOrderLeftQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'cost_center_number',
        sob.properties.Property(
            name="costCenterNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'cost_center_approver',
        sob.properties.Property(
            name="costCenterApprover",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'general_ledger_number',
        sob.properties.Property(
            name="generalLedgerNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'requested_on_behalf_of',
        sob.properties.Property(
            name="requestedOnBehalfOf",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'fabric_instruction',
        sob.properties.Property(
            name="fabricInstruction",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'quote_requirement',
        sob.properties.Property(
            name="quoteRequirement",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleRequestAudit
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
    DSampleRequestComments
).properties = sob.meta.Properties([
    (
        'development_sample_request_comments',
        sob.properties.Property(
            name="developmentSampleRequestComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleRequestCore
).properties = sob.meta.Properties([
    (
        'development_sample_request_identifier',
        sob.properties.Property(
            name="developmentSampleRequestIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_request_name',
        sob.properties.Property(
            name="developmentSampleRequestName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration',
        sob.properties.Property(
            name="sourcingConfiguration",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_request_season',
        sob.properties.Property(
            name="developmentSampleRequestSeason",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_request_date',
        sob.properties.Property(
            name="developmentSampleRequestDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_request_purpose',
        sob.properties.Property(
            name="developmentSampleRequestPurpose",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleRequestStatus
).properties = sob.meta.Properties([
    (
        'development_sample_request_status_indicator',
        sob.properties.Property(
            name="developmentSampleRequestStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleShipmentAudit
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
    DSampleShipmentCore
).properties = sob.meta.Properties([
    (
        'development_sample_shipment_identifier',
        sob.properties.Property(
            name="developmentSampleShipmentIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample',
        sob.properties.Property(
            name="developmentSample",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_sample_state',
        sob.properties.Property(
            name="developmentSampleState",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DSampleShipmentDetails
).item_types = sob.types.MutableTypes([
    DSampleShipmentDetail
])
sob.meta.object_writable(  # type: ignore
    DSampleShipmentDetail
).properties = sob.meta.Properties([
    (
        'estimated_ship_date',
        sob.properties.Property(
            name="estimatedShipDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'actual_ship_date',
        sob.properties.Property(
            name="actualShipDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'received_date',
        sob.properties.Property(
            name="receivedDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'shipping_service',
        sob.properties.Property(
            name="shippingService",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'shipment_tracking_number',
        sob.properties.Property(
            name="shipmentTrackingNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ship_pairs_quantity',
        sob.properties.Property(
            name="shipPairsQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ship_right_quantity',
        sob.properties.Property(
            name="shipRightQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ship_left_quantity',
        sob.properties.Property(
            name="shipLeftQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'goods_at_consolidator_reason',
        sob.properties.Property(
            name="goodsAtConsolidatorReason",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'goods_at_consolidator_ap_reason',
        sob.properties.Property(
            name="goodsAtConsolidatorAPReason",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleShipmentFactoryComments
).properties = sob.meta.Properties([
    (
        'factory_sample_comments',
        sob.properties.Property(
            name="factorySampleComments",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'factory_sub_location_im_number',
        sob.properties.Property(
            name="factorySubLocationIMNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DSampleStatus
).properties = sob.meta.Properties([
    (
        'development_sample_status_indicator',
        sob.properties.Property(
            name="developmentSampleStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcAudit
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
    DcCore
).properties = sob.meta.Properties([
    (
        'development_colorway_identifier',
        sob.properties.Property(
            name="developmentColorwayIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_description',
        sob.properties.Property(
            name="developmentColorwayDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_name',
        sob.properties.Property(
            name="developmentColorwayName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_type',
        sob.properties.Property(
            name="developmentColorwayType",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_state',
        sob.properties.Property(
            name="developmentColorwayState",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_gate',
        sob.properties.Property(
            name="developmentColorwayGate",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_identifier',
        sob.properties.Property(
            name="productIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcSeasonAudit
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
    DcSeasonCore
).properties = sob.meta.Properties([
    (
        'development_colorway_season_identifier',
        sob.properties.Property(
            name="developmentColorwaySeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_identifier',
        sob.properties.Property(
            name="developmentColorwayIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_season_identifier',
        sob.properties.Property(
            name="developmentStyleSeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_offering_identifier',
        sob.properties.Property(
            name="productOfferingIdentifier",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcSeasonFOB
).properties = sob.meta.Properties([
    (
        'target_fob',
        sob.properties.Property(
            name="targetFOB",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcSeasonQuantity
).properties = sob.meta.Properties([
    (
        'prototype_quantity',
        sob.properties.Property(
            name="prototypeQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sample_quantity',
        sob.properties.Property(
            name="sampleQuantity",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcSeasonSourcingConfig
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_colorway_season',
        sob.properties.Property(
            name="sourcingConfigurationColorwaySeason",
            types=sob.types.MutableTypes([
                DcSeasonSourcingConfigSourcingConfigurationColorwaySeason,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DcSeasonSourcingConfigSourcingConfigurationColorwaySeason
).item_types = sob.types.MutableTypes([
    Reference
])
sob.meta.object_writable(  # type: ignore
    DcSeasonStatus
).properties = sob.meta.Properties([
    (
        'development_colorway_season_status_indicator',
        sob.properties.Property(
            name="developmentColorwaySeasonStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcSeasonTrial
).properties = sob.meta.Properties([
    (
        'nike_production_trial',
        sob.properties.Property(
            name="nikeProductionTrial",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DcStatus
).properties = sob.meta.Properties([
    (
        'development_colorway_status_indicator',
        sob.properties.Property(
            name="developmentColorwayStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayBulkResponseContents,
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
    DevelopmentColorwayBulkResponseContents
).item_types = sob.types.MutableTypes([
    DevelopmentColorwayBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    DevelopmentColorwayBulkResponseContent
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
                DevelopmentColorwayDataunits,
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
    DevelopmentColorwayResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentColorwayResponseContent,
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
    DevelopmentColorwayResponseContent
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
                DevelopmentColorwayDataunits,
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
    DevelopmentColorwayDataunits
).properties = sob.meta.Properties([
    (
        'dc_season_core',
        sob.properties.Property(
            name="dcSeasonCore",
            required=True,
            types=sob.types.MutableTypes([
                DcSeasonCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_status',
        sob.properties.Property(
            name="dcSeasonStatus",
            types=sob.types.MutableTypes([
                DcSeasonStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_sourcing_config',
        sob.properties.Property(
            name="dcSeasonSourcingConfig",
            required=True,
            types=sob.types.MutableTypes([
                DcSeasonSourcingConfig,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_quantity',
        sob.properties.Property(
            name="dcSeasonQuantity",
            types=sob.types.MutableTypes([
                DcSeasonQuantity,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_trial',
        sob.properties.Property(
            name="dcSeasonTrial",
            types=sob.types.MutableTypes([
                DcSeasonTrial,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_fob',
        sob.properties.Property(
            name="dcSeasonFOB",
            types=sob.types.MutableTypes([
                DcSeasonFOB,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_season_audit',
        sob.properties.Property(
            name="dcSeasonAudit",
            types=sob.types.MutableTypes([
                DcSeasonAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_core',
        sob.properties.Property(
            name="dsSeasonCore",
            required=True,
            types=sob.types.MutableTypes([
                DsSeasonCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_resource',
        sob.properties.Property(
            name="dsSeasonResource",
            types=sob.types.MutableTypes([
                DsSeasonResource,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_technical_difficulty',
        sob.properties.Property(
            name="dsSeasonTechnicalDifficulty",
            types=sob.types.MutableTypes([
                DsSeasonTechnicalDifficulty,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_fob',
        sob.properties.Property(
            name="dsSeasonFOB",
            types=sob.types.MutableTypes([
                DsSeasonFOB,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_track',
        sob.properties.Property(
            name="dsSeasonTrack",
            types=sob.types.MutableTypes([
                DsSeasonTrack,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_status',
        sob.properties.Property(
            name="dsSeasonStatus",
            types=sob.types.MutableTypes([
                DsSeasonStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_season_audit',
        sob.properties.Property(
            name="dsSeasonAudit",
            types=sob.types.MutableTypes([
                DsSeasonAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_core',
        sob.properties.Property(
            name="dcCore",
            required=True,
            types=sob.types.MutableTypes([
                DcCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_status',
        sob.properties.Property(
            name="dcStatus",
            types=sob.types.MutableTypes([
                DcStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'dc_audit',
        sob.properties.Property(
            name="dcAudit",
            types=sob.types.MutableTypes([
                DcAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_core',
        sob.properties.Property(
            name="dsCore",
            required=True,
            types=sob.types.MutableTypes([
                DsCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_classification',
        sob.properties.Property(
            name="dsClassification",
            required=True,
            types=sob.types.MutableTypes([
                DsClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_last',
        sob.properties.Property(
            name="dsLast",
            types=sob.types.MutableTypes([
                DsLast,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_status',
        sob.properties.Property(
            name="dsStatus",
            types=sob.types.MutableTypes([
                DsStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_audit',
        sob.properties.Property(
            name="dsAudit",
            types=sob.types.MutableTypes([
                DsAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentMeasurementResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentMeasurementResponseContent,
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
    DevelopmentMeasurementResponseContent
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
                DevelopmentMeasurementDataunits,
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
    DevelopmentMeasurementDataunits
).properties = sob.meta.Properties([
    (
        'ms_core',
        sob.properties.Property(
            name="msCore",
            required=True,
            types=sob.types.MutableTypes([
                MsCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ms_template',
        sob.properties.Property(
            name="msTemplate",
            types=sob.types.MutableTypes([
                MsTemplate,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ms_size',
        sob.properties.Property(
            name="msSize",
            types=sob.types.MutableTypes([
                MsSize,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ms_point_of_measurement',
        sob.properties.Property(
            name="msPointOfMeasurement",
            types=sob.types.MutableTypes([
                MsPointOfMeasurementBreakdowns,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ms_status',
        sob.properties.Property(
            name="msStatus",
            types=sob.types.MutableTypes([
                MsStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ms_audit',
        sob.properties.Property(
            name="msAudit",
            types=sob.types.MutableTypes([
                MsAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentPointOfMeasurementResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentPointOfMeasurementResponseContent,
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
    DevelopmentPointOfMeasurementResponseContent
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
                DevelopmentPointOfMeasurementDataunits,
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
    DevelopmentPointOfMeasurementDataunits
).properties = sob.meta.Properties([
    (
        'pom_core',
        sob.properties.Property(
            name="pomCore",
            required=True,
            types=sob.types.MutableTypes([
                PomCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pom_status',
        sob.properties.Property(
            name="pomStatus",
            types=sob.types.MutableTypes([
                PomStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pom_audit',
        sob.properties.Property(
            name="pomAudit",
            types=sob.types.MutableTypes([
                PomAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleResponseContent,
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
    DevelopmentSampleResponseContent
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
                DevelopmentSampleDataunits,
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
    DevelopmentSampleShipmentResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentSampleShipmentResponseContent,
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
    DevelopmentSampleShipmentResponseContent
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
                DevelopmentSampleShipmentDataunits,
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
    DevelopmentSampleShipmentDataunits
).properties = sob.meta.Properties([
    (
        'd_sample_shipment_core',
        sob.properties.Property(
            name="dSampleShipmentCore",
            required=True,
            types=sob.types.MutableTypes([
                DSampleShipmentCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_shipment_factory_comments',
        sob.properties.Property(
            name="dSampleShipmentFactoryComments",
            types=sob.types.MutableTypes([
                DSampleShipmentFactoryComments,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_shipment_audit',
        sob.properties.Property(
            name="dSampleShipmentAudit",
            types=sob.types.MutableTypes([
                DSampleShipmentAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_shipment_detail',
        sob.properties.Property(
            name="dSampleShipmentDetail",
            types=sob.types.MutableTypes([
                DSampleShipmentDetails,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentSampleDataunits
).properties = sob.meta.Properties([
    (
        'd_sample_core',
        sob.properties.Property(
            name="dSampleCore",
            required=True,
            types=sob.types.MutableTypes([
                DSampleCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_status',
        sob.properties.Property(
            name="dSampleStatus",
            types=sob.types.MutableTypes([
                DSampleStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_classification',
        sob.properties.Property(
            name="dSampleClassification",
            types=sob.types.MutableTypes([
                DSampleClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_comments',
        sob.properties.Property(
            name="dSampleComments",
            types=sob.types.MutableTypes([
                DSampleComments,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_audit',
        sob.properties.Property(
            name="dSampleAudit",
            types=sob.types.MutableTypes([
                DSampleAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_request_core',
        sob.properties.Property(
            name="dSampleRequestCore",
            required=True,
            types=sob.types.MutableTypes([
                DSampleRequestCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_request_comments',
        sob.properties.Property(
            name="dSampleRequestComments",
            types=sob.types.MutableTypes([
                DSampleRequestComments,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_request_status',
        sob.properties.Property(
            name="dSampleRequestStatus",
            types=sob.types.MutableTypes([
                DSampleRequestStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_request_audit',
        sob.properties.Property(
            name="dSampleRequestAudit",
            types=sob.types.MutableTypes([
                DSampleRequestAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_order_detail',
        sob.properties.Property(
            name="dSampleOrderDetail",
            types=sob.types.MutableTypes([
                DSampleOrderDetail,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'd_sample_evaluation',
        sob.properties.Property(
            name="dSampleEvaluation",
            types=sob.types.MutableTypes([
                DSampleEvaluation,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                DevelopmentStyleResponseContent,
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
    DevelopmentStyleResponseContent
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
                DevelopmentStyleDataunits,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DevelopmentStyleDataunits
).properties = sob.meta.Properties([
    (
        'ds_core',
        sob.properties.Property(
            name="dsCore",
            required=True,
            types=sob.types.MutableTypes([
                DsCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_classification',
        sob.properties.Property(
            name="dsClassification",
            required=True,
            types=sob.types.MutableTypes([
                DsClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_last',
        sob.properties.Property(
            name="dsLast",
            types=sob.types.MutableTypes([
                DsLast,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_status',
        sob.properties.Property(
            name="dsStatus",
            types=sob.types.MutableTypes([
                DsStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'ds_audit',
        sob.properties.Property(
            name="dsAudit",
            types=sob.types.MutableTypes([
                DsAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsAudit
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
    DsClassification
).properties = sob.meta.Properties([
    (
        'development_style_type',
        sob.properties.Property(
            name="developmentStyleType",
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
    )
])
sob.meta.object_writable(  # type: ignore
    DsCore
).properties = sob.meta.Properties([
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'model_identifier',
        sob.properties.Property(
            name="modelIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'style_number',
        sob.properties.Property(
            name="styleNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_name',
        sob.properties.Property(
            name="developmentStyleName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_description',
        sob.properties.Property(
            name="developmentStyleDescription",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsLast
).properties = sob.meta.Properties([
    (
        'last_identifier',
        sob.properties.Property(
            name="lastIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'additional_last_identifier',
        sob.properties.Property(
            name="additionalLastIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonAudit
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
    DsSeasonCore
).properties = sob.meta.Properties([
    (
        'development_style_season_identifier',
        sob.properties.Property(
            name="developmentStyleSeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'cycle_year',
        sob.properties.Property(
            name="cycleYear",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonFOB
).properties = sob.meta.Properties([
    (
        'target_fob',
        sob.properties.Property(
            name="targetFOB",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonResource
).properties = sob.meta.Properties([
    (
        'nlo_chemical_engineer_user_identifier',
        sob.properties.Property(
            name="nloChemicalEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_costing_user_identifier',
        sob.properties.Property(
            name="nloCostingUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_developer_user_identifier',
        sob.properties.Property(
            name="nloDeveloperUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_knit_engineer_user_identifier',
        sob.properties.Property(
            name="nloKnitEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_knit_programmer_user_identifier',
        sob.properties.Property(
            name="nloKnitProgrammerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_material_user_identifier',
        sob.properties.Property(
            name="nloMaterialUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_product_engineer_user_identifier',
        sob.properties.Property(
            name="nloProductEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'nlo_category_director_user_identifier',
        sob.properties.Property(
            name="nloCategoryDirectorUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_color_designer_user_identifier',
        sob.properties.Property(
            name="whqColorDesignerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_costing_user_identifier',
        sob.properties.Property(
            name="whqCostingUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_designer_user_identifier',
        sob.properties.Property(
            name="whqDesignerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_developer_user_identifier',
        sob.properties.Property(
            name="whqDeveloperUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_footwear_development_director_user_identifier',
        sob.properties.Property(
            name="whqFootwearDevelopmentDirectorUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_knit_developer_user_identifier',
        sob.properties.Property(
            name="whqKnitDeveloperUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_knit_engineer_user_identifier',
        sob.properties.Property(
            name="whqKnitEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_knit_programmer_user_identifier',
        sob.properties.Property(
            name="whqKnitProgrammerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_material_user_identifier',
        sob.properties.Property(
            name="whqMaterialUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_product_engineer_user_identifier',
        sob.properties.Property(
            name="whqProductEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'whq_product_testing_user_identifier',
        sob.properties.Property(
            name="whqProductTestingUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'knit_center_developer_user_identifier',
        sob.properties.Property(
            name="knitCenterDeveloperUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'new_upper_indicator',
        sob.properties.Property(
            name="newUpperIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'new_midsole_indicator',
        sob.properties.Property(
            name="newMidsoleIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'new_outsole_indicator',
        sob.properties.Property(
            name="newOutsoleIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_season_development_team',
        sob.properties.Property(
            name="productSeasonDevelopmentTeam",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonStatus
).properties = sob.meta.Properties([
    (
        'development_style_season_status_indicator',
        sob.properties.Property(
            name="developmentStyleSeasonStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonTechnicalDifficulty
).properties = sob.meta.Properties([
    (
        'technical_difficulty',
        sob.properties.Property(
            name="technicalDifficulty",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsSeasonTrack
).properties = sob.meta.Properties([
    (
        'development_track',
        sob.properties.Property(
            name="developmentTrack",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_track',
        sob.properties.Property(
            name="productTrack",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'start_date',
        sob.properties.Property(
            name="startDate",
            types=sob.types.MutableTypes([
                sob.properties.Date(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    DsStatus
).properties = sob.meta.Properties([
    (
        'development_style_status_indicator',
        sob.properties.Property(
            name="developmentStyleStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MsAudit
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
    MsCore
).properties = sob.meta.Properties([
    (
        'measurement_set_identifier',
        sob.properties.Property(
            name="measurementSetIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_set_name',
        sob.properties.Property(
            name="measurementSetName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_set_state',
        sob.properties.Property(
            name="measurementSetState",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_set_applicability_list',
        sob.properties.Property(
            name="measurementSetApplicabilityList",
            types=sob.types.MutableTypes([
                MsCoreMeasurementSetApplicabilityList,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    MsCoreMeasurementSetApplicabilityList
).item_types = sob.types.MutableTypes([
    MsCoreMeasurementSetApplicability
])
sob.meta.object_writable(  # type: ignore
    MsCoreMeasurementSetApplicability
).properties = sob.meta.Properties([
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'style_number',
        sob.properties.Property(
            name="styleNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'cycle_year',
        sob.properties.Property(
            name="cycleYear",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_season_identifier',
        sob.properties.Property(
            name="sourcingConfigurationSeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    MsPointOfMeasurementBreakdowns
).item_types = sob.types.MutableTypes([
    MsPointOfMeasurementBreakdown
])
sob.meta.object_writable(  # type: ignore
    MsPointOfMeasurementBreakdown
).properties = sob.meta.Properties([
    (
        'size',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'size_breakdown',
        sob.properties.Property(
            name="sizeBreakdown",
            types=sob.types.MutableTypes([
                MsPointOfMeasurementSizeBreakdowns,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    MsPointOfMeasurementSizeBreakdowns
).item_types = sob.types.MutableTypes([
    MsPointOfMeasurementSizeBreakdown
])
sob.meta.object_writable(  # type: ignore
    MsPointOfMeasurementSizeBreakdown
).properties = sob.meta.Properties([
    (
        'measurement_code',
        sob.properties.Property(
            name="measurementCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_name',
        sob.properties.Property(
            name="pointOfMeasurementName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sort_order',
        sob.properties.Property(
            name="sortOrder",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_instructions',
        sob.properties.Property(
            name="measurementInstructions",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_detail',
        sob.properties.Property(
            name="measurementDetail",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_criticality',
        sob.properties.Property(
            name="pointOfMeasurementCriticality",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tolerance_negative',
        sob.properties.Property(
            name="toleranceNegative",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tolerance_positive',
        sob.properties.Property(
            name="tolerancePositive",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_size_value',
        sob.properties.Property(
            name="measurementSizeValue",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement',
        sob.properties.Property(
            name="pointOfMeasurement",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MsSize
).properties = sob.meta.Properties([
    (
        'development_style_size_definition',
        sob.properties.Property(
            name="developmentStyleSizeDefinition",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_value_unit_of_measure',
        sob.properties.Property(
            name="measurementValueUnitOfMeasure",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'base_size',
        sob.properties.Property(
            name="baseSize",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'size_selection_list',
        sob.properties.Property(
            name="sizeSelectionList",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MsStatus
).properties = sob.meta.Properties([
    (
        'measurement_set_status_indicator',
        sob.properties.Property(
            name="measurementSetStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    MsTemplate
).properties = sob.meta.Properties([
    (
        'measurement_set_template_name',
        sob.properties.Property(
            name="measurementSetTemplateName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'size_definition_template',
        sob.properties.Property(
            name="sizeDefinitionTemplate",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'grade_rule_template',
        sob.properties.Property(
            name="gradeRuleTemplate",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_template_type',
        sob.properties.Property(
            name="measurementTemplateType",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PomAudit
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
    )
])
sob.meta.object_writable(  # type: ignore
    PomCore
).properties = sob.meta.Properties([
    (
        'sort_order',
        sob.properties.Property(
            name="sortOrder",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_code',
        sob.properties.Property(
            name="measurementCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_name',
        sob.properties.Property(
            name="pointOfMeasurementName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_instructions',
        sob.properties.Property(
            name="measurementInstructions",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'measurement_detail',
        sob.properties.Property(
            name="measurementDetail",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_criticality',
        sob.properties.Property(
            name="pointOfMeasurementCriticality",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tolerance_negative',
        sob.properties.Property(
            name="toleranceNegative",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'tolerance_positive',
        sob.properties.Property(
            name="tolerancePositive",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'point_of_measurement_identifier',
        sob.properties.Property(
            name="pointOfMeasurementIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Number(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PomStatus
).properties = sob.meta.Properties([
    (
        'point_of_measurement_status_indicator',
        sob.properties.Property(
            name="pointOfMeasurementStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    RelationshipResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                RelationshipResponseContents,
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
    RelationshipResponseContents
).item_types = sob.types.MutableTypes([
    RelationshipResponseContent
])
sob.meta.object_writable(  # type: ignore
    RelationshipResponseContent
).properties = sob.meta.Properties([
    (
        'relationships',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScAudit
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
    ScClassification
).properties = sob.meta.Properties([
    (
        'development_style_type',
        sob.properties.Property(
            name="developmentStyleType",
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
    )
])
sob.meta.object_writable(  # type: ignore
    ScColorwaySeasonAudit
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
    ScColorwaySeasonClassification
).properties = sob.meta.Properties([
    (
        'development_style_type',
        sob.properties.Property(
            name="developmentStyleType",
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
    )
])
sob.meta.object_writable(  # type: ignore
    ScColorwaySeasonCore
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_colorway_season_identifier',
        sob.properties.Property(
            name="sourcingConfigurationColorwaySeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_colorway_season_identifier',
        sob.properties.Property(
            name="developmentColorwaySeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_colorway_season_primary_indicator',
        sob.properties.Property(
            name="sourcingConfigurationColorwaySeasonPrimaryIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScColorwaySeasonStatus
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_colorway_season_status_indicator',
        sob.properties.Property(
            name="sourcingConfigurationColorwaySeasonStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScCore
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_name',
        sob.properties.Property(
            name="sourcingConfigurationName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_identifier',
        sob.properties.Property(
            name="developmentStyleIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_creation_center_identifier',
        sob.properties.Property(
            name="productCreationCenterIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_factory_code',
        sob.properties.Property(
            name="legacyFactoryCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_product_creation_center_code',
        sob.properties.Property(
            name="legacyProductCreationCenterCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_primary_indicator',
        sob.properties.Property(
            name="sourcingConfigurationPrimaryIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScSeasonAudit
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
    ScSeasonCore
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_identifier',
        sob.properties.Property(
            name="sourcingConfigurationIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_season_identifier',
        sob.properties.Property(
            name="sourcingConfigurationSeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_creation_center_identifier',
        sob.properties.Property(
            name="productCreationCenterIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_product_creation_center_code',
        sob.properties.Property(
            name="legacyProductCreationCenterCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'product_creation_centre_developer',
        sob.properties.Property(
            name="productCreationCentreDeveloper",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'development_style_season_identifier',
        sob.properties.Property(
            name="developmentStyleSeasonIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_identifier',
        sob.properties.Property(
            name="sourcingIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sourcing_configuration_season_primary_indicator',
        sob.properties.Property(
            name="sourcingConfigurationSeasonPrimaryIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScSeasonResource
).properties = sob.meta.Properties([
    (
        'pmo_chemical_engineer_user_identifier',
        sob.properties.Property(
            name="pmoChemicalEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_costing_user_identifier',
        sob.properties.Property(
            name="pmoCostingUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_developer_user_identifier',
        sob.properties.Property(
            name="pmoDeveloperUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_material_user_identifier',
        sob.properties.Property(
            name="pmoMaterialUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_product_engineer_user_identifier',
        sob.properties.Property(
            name="pmoProductEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_category_director_user_identifier',
        sob.properties.Property(
            name="pmoCategoryDirectorUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_manufacturing_engineer_user_identifier',
        sob.properties.Property(
            name="pmoManufacturingEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'pmo_manufacturing_chemical_engineer_user_identifier',
        sob.properties.Property(
            name="pmoManufacturingChemicalEngineerUserIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    ScSeasonStatus
).properties = sob.meta.Properties([
    (
        'sourcing_configuration_season_status_indicator',
        sob.properties.Property(
            name="sourcingConfigurationSeasonStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SearchResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SearchResponseContents,
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
        'offset',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
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
        'next_',
        sob.properties.Property(
            name="next",
            types=sob.types.MutableTypes([
                Links,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'prev',
        sob.properties.Property(
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
    SearchResponseContents
).item_types = sob.types.MutableTypes([
    SearchResponseContent
])
sob.meta.object_writable(  # type: ignore
    SearchResponseContent
).properties = sob.meta.Properties([
    (
        'relationships',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SourcingConfigurationColorwaySeasonDataunits
).properties = sob.meta.Properties([
    (
        'sc_colorway_season_core',
        sob.properties.Property(
            name="scColorwaySeasonCore",
            required=True,
            types=sob.types.MutableTypes([
                ScColorwaySeasonCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_colorway_season_classification',
        sob.properties.Property(
            name="scColorwaySeasonClassification",
            required=True,
            types=sob.types.MutableTypes([
                ScColorwaySeasonClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_colorway_season_status',
        sob.properties.Property(
            name="scColorwaySeasonStatus",
            required=True,
            types=sob.types.MutableTypes([
                ScColorwaySeasonStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_colorway_season_audit',
        sob.properties.Property(
            name="scColorwaySeasonAudit",
            types=sob.types.MutableTypes([
                ScColorwaySeasonAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_season_core',
        sob.properties.Property(
            name="scSeasonCore",
            required=True,
            types=sob.types.MutableTypes([
                ScSeasonCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_season_status',
        sob.properties.Property(
            name="scSeasonStatus",
            required=True,
            types=sob.types.MutableTypes([
                ScSeasonStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_season_audit',
        sob.properties.Property(
            name="scSeasonAudit",
            types=sob.types.MutableTypes([
                ScSeasonAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_season_resource',
        sob.properties.Property(
            name="scSeasonResource",
            types=sob.types.MutableTypes([
                ScSeasonResource,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SourcingConfigurationDataunits
).properties = sob.meta.Properties([
    (
        'sc_core',
        sob.properties.Property(
            name="scCore",
            required=True,
            types=sob.types.MutableTypes([
                ScCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_classification',
        sob.properties.Property(
            name="scClassification",
            required=True,
            types=sob.types.MutableTypes([
                ScClassification,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sc_audit',
        sob.properties.Property(
            name="scAudit",
            types=sob.types.MutableTypes([
                ScAudit,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SourcingConfigurationsBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SourcingConfigurationsBulkResponseContents,
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
    SourcingConfigurationsBulkResponseContents
).item_types = sob.types.MutableTypes([
    SourcingConfigurationsBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    SourcingConfigurationsBulkResponseContent
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
                SourcingConfigurationDataunits,
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
    SourcingConfigurationsColorwaySeasonBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SourcingConfigurationsColorwaySeasonBulkResponseContents,
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
    SourcingConfigurationsColorwaySeasonBulkResponseContents
).item_types = sob.types.MutableTypes([
    SourcingConfigurationsColorwaySeasonBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    SourcingConfigurationsColorwaySeasonBulkResponseContent
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
                SourcingConfigurationColorwaySeasonDataunits,
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
    SourcingConfigurationsColorwaySeasonResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SourcingConfigurationsColorwaySeasonResponseContent,
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
    SourcingConfigurationsColorwaySeasonResponseContent
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
                SourcingConfigurationColorwaySeasonDataunits,
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
    SourcingConfigurationsResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SourcingConfigurationsResponseContent,
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
    SourcingConfigurationsResponseContent
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
                SourcingConfigurationDataunits,
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
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsSourcesGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsSourcesGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsSourcesObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataBillOfMaterialsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataColorwaySeasonsGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataColorwaySeasonsGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataColorwaySeasonsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataDevelopmentSamplesSamplesObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataDevelopmentSamplesShipmentsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataDevelopmentStylesObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMeasurementSetsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataPointsOfMeasurementObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsColorwaySeasonsGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsColorwaySeasonsGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsColorwaySeasonsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataSourcingConfigurationsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetSourcingConfigurationSeason
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetDevelopmentStyleType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetDivision
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomComments
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBillOfMaterialStatusIndicator
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Boolean(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomLineItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomLineItemComments
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomLineItemNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetParentBomLineItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetLineItemQuantity
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetColor
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBillOfMaterialsSection
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetPartPrimary
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetPartSecondary
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetPartModifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetPartSuffix
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetPartName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetMaterialItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetSuppliedMaterial
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetSuppliedMaterialColorIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetSuppliedMaterialColorIsMultipleColors
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Boolean(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetColorPlaceholderDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetMaterialItemPlaceholderDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomGUID
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetDevelopmentColorwayIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetBomName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetDevelopmentColorwaySeasonIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsGetSourcingConfigurationIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetProductIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetStyleNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetSourcingConfigurationSeason
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetCycleYear
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetDevelopmentStyleType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetDivision
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBillOfMaterialStatusIndicator
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Boolean(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBomLineItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBomLineItemNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetParentBomLineItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetLineItemQuantity
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetColor
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBillOfMaterialsSection
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetPart
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetMaterialItemIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetSuppliedMaterial
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIsMultipleColors
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Boolean(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetColorPlaceholderDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetMaterialItemPlaceholderDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetNetUsage
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetWasteUsage
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetGrossUsage
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetUsageUnitOfMeasure
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBomGUID
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBomIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetDevelopmentColorwayIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetBomName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetDevelopmentColorwaySeasonIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchBillOfMaterialsSourcesGetSourcingConfigurationIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetSampleQuantity
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetNikeProductionTrial
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetTargetFOB
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetSourcingConfigurationColorwaySeason
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentStyleIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetCycleYear
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqColorDesignerUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqCostingUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqDesignerUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqDeveloperUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqFootwearDevelopmentDirectorUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqKnitDeveloperUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqKnitEngineerUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqKnitProgrammerUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqMaterialUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqProductEngineerUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetWhqProductTestingUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetKnitCenterDeveloperUserIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetProductSeasonDevelopmentTeam
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetTechnicalDifficulty
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayTargetFOB
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentTrack
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetProductTrack
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetStartDate
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Date(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetLastIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetAdditionalLastIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayDescription
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayState
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayGate
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetProductIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentStyleType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDivision
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentColorwayIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetDevelopmentStyleSeasonIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetProductOfferingIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchColorwaySeasonsGetPrototypeQuantity
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetDevelopmentStyleType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetDivision
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetDevelopmentStyleName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetModelIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetStyleNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetLastIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchDevelopmentStylesGetAdditionalLastIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSourcingConfigurationIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSourcingConfigurationSeasonIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementSetTemplateName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSizeDefinitionTemplate
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetGradeRuleTemplate
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementTemplateType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetDevelopmentStyleSizeDefinition
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementValueUnitOfMeasure
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetBaseSize
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSizeSelectionList
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSize
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementCode
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetPointOfMeasurementName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetSortOrder
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementInstructions
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementDetail
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetPointOfMeasurementCriticality
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetToleranceNegative
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetTolerancePositive
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementSizeValue
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Number(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetPointOfMeasurement
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementSetStatusIndicator
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Boolean(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementSetName
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetMeasurementSetState
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetDevelopmentStyleIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetStyleNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMeasurementSetsGetCycleYear
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
    "#/definitions/_error": Error,
    "#/definitions/_links": Links,
    "#/definitions/_reference": Reference,
    "#/definitions/billOfMaterialsBulkResponse": BillOfMaterialsBulkResponse,
    "#/definitions/billOfMaterialsBulkResponse/properties/content":
    BillOfMaterialsBulkResponseContents,
    "#/definitions/billOfMaterialsBulkResponse/properties/content/items":
    BillOfMaterialsBulkResponseContent,
    "#/definitions/billOfMaterialsResponse": BillOfMaterialsResponse,
    "#/definitions/billOfMaterialsResponse/properties/content":
    BillOfMaterialsResponseContent,
    "#/definitions/billOfMaterialsSourceBulkResponse":
    BillOfMaterialsSourceBulkResponse,
    "#/definitions/billOfMaterialsSourceBulkResponse/properties/content":
    BillOfMaterialsSourceBulkResponseContents,
    "#/definitions/billOfMaterialsSourceBulkResponse/properties/content/items":
    BillOfMaterialsSourceBulkResponseContent,
    "#/definitions/billOfMaterialsSourceResponse":
    BillOfMaterialsSourceResponse,
    "#/definitions/billOfMaterialsSourceResponse/properties/content":
    BillOfMaterialsSourceResponseContent,
    "#/definitions/billOfMaterialsSource_dataunits":
    BillOfMaterialsSourceDataunits,
    "#/definitions/billOfMaterialsSource_dataunits/properties/bomCore":
    BillOfMaterialsSourceDataunitsBomCore,
    "#/definitions/billOfMaterialsSource_dataunits/properties/bomSeason":
    BillOfMaterialsSourceDataunitsBomSeason,
    "#/definitions/billOfMaterialsSource_dataunits/properties/bomSeason/allOf/1/properties/cycleYear":  # noqa
    BillOfMaterialsSourceDataunitsBomSeasonCycleYear,
    "#/definitions/billOfMaterials_dataunits": BillOfMaterialsDataunits,
    "#/definitions/bomClassification": BomClassification,
    "#/definitions/bomCore": BomCore,
    "#/definitions/bomDescription": BomDescription,
    "#/definitions/bomHeaderAudit": BomHeaderAudit,
    "#/definitions/bomLineAudit": BomLineAudit,
    "#/definitions/bomLineItemComments": BomLineItemComments,
    "#/definitions/bomLineItemComments/items": BomLineItemComment,
    "#/definitions/bomLineItemDetail": BomLineItemDetails,
    "#/definitions/bomLineItemDetail/items": BomLineItemDetail,
    "#/definitions/bomLineItemDetailSource": BomLineItemDetailSources,
    "#/definitions/bomLineItemDetailSource/items": BomLineItemDetailSource,
    "#/definitions/bomSeason": BomSeason,
    "#/definitions/bomSeason/properties/developmentColorwaySeasonIdentifier":
    BomSeasonDevelopmentColorwaySeasonIdentifier,
    "#/definitions/bomSourcingConfiguration": BomSourcingConfigurations,
    "#/definitions/bomSourcingConfiguration/properties/sourcingConfigurationIdentifier":  # noqa
    BomSourcingConfigurationSourcingConfigurationIdentifier,
    "#/definitions/bomSourcingConfiguration/properties/sourcingConfigurationList":  # noqa
    BomSourcingConfigurationsList,
    "#/definitions/bomSourcingConfiguration/properties/sourcingConfigurationList/items":  # noqa
    BomSourcingConfiguration,
    "#/definitions/bomSourcingConfiguration/properties/sourcingConfigurationList/items/properties/sourcingConfigurationSeason":  # noqa
    BomSourcingConfigurationSeason,
    "#/definitions/bomSourcingConfigurationColorwaySeason":
    BomSourcingConfigurationColorwaySeason,
    "#/definitions/bomSourcingConfigurationColorwaySeason/properties/sourcingConfigurationColorwaySeason":  # noqa
    BomSourcingConfigurationColorwaySeasonSourcingConfigurationColorwaySeason,
    "#/definitions/bomStatus": BomStatus,
    "#/definitions/dSampleAudit": DSampleAudit,
    "#/definitions/dSampleClassification": DSampleClassification,
    "#/definitions/dSampleComments": DSampleComments,
    "#/definitions/dSampleCore": DSampleCore,
    "#/definitions/dSampleEvaluation": DSampleEvaluation,
    "#/definitions/dSampleOrderDetail": DSampleOrderDetail,
    "#/definitions/dSampleRequestAudit": DSampleRequestAudit,
    "#/definitions/dSampleRequestComments": DSampleRequestComments,
    "#/definitions/dSampleRequestCore": DSampleRequestCore,
    "#/definitions/dSampleRequestStatus": DSampleRequestStatus,
    "#/definitions/dSampleShipmentAudit": DSampleShipmentAudit,
    "#/definitions/dSampleShipmentCore": DSampleShipmentCore,
    "#/definitions/dSampleShipmentDetail": DSampleShipmentDetails,
    "#/definitions/dSampleShipmentDetail/items": DSampleShipmentDetail,
    "#/definitions/dSampleShipmentFactoryComments":
    DSampleShipmentFactoryComments,
    "#/definitions/dSampleStatus": DSampleStatus,
    "#/definitions/dcAudit": DcAudit,
    "#/definitions/dcCore": DcCore,
    "#/definitions/dcSeasonAudit": DcSeasonAudit,
    "#/definitions/dcSeasonCore": DcSeasonCore,
    "#/definitions/dcSeasonFOB": DcSeasonFOB,
    "#/definitions/dcSeasonQuantity": DcSeasonQuantity,
    "#/definitions/dcSeasonSourcingConfig": DcSeasonSourcingConfig,
    "#/definitions/dcSeasonSourcingConfig/properties/sourcingConfigurationColorwaySeason":  # noqa
    DcSeasonSourcingConfigSourcingConfigurationColorwaySeason,
    "#/definitions/dcSeasonStatus": DcSeasonStatus,
    "#/definitions/dcSeasonTrial": DcSeasonTrial,
    "#/definitions/dcStatus": DcStatus,
    "#/definitions/developmentColorwayBulkResponse":
    DevelopmentColorwayBulkResponse,
    "#/definitions/developmentColorwayBulkResponse/properties/content":
    DevelopmentColorwayBulkResponseContents,
    "#/definitions/developmentColorwayBulkResponse/properties/content/items":
    DevelopmentColorwayBulkResponseContent,
    "#/definitions/developmentColorwayResponse": DevelopmentColorwayResponse,
    "#/definitions/developmentColorwayResponse/properties/content":
    DevelopmentColorwayResponseContent,
    "#/definitions/developmentColorway_dataunits":
    DevelopmentColorwayDataunits,
    "#/definitions/developmentMeasurementResponse":
    DevelopmentMeasurementResponse,
    "#/definitions/developmentMeasurementResponse/properties/content":
    DevelopmentMeasurementResponseContent,
    "#/definitions/developmentMeasurement_dataunits":
    DevelopmentMeasurementDataunits,
    "#/definitions/developmentPointOfMeasurementResponse":
    DevelopmentPointOfMeasurementResponse,
    "#/definitions/developmentPointOfMeasurementResponse/properties/content":
    DevelopmentPointOfMeasurementResponseContent,
    "#/definitions/developmentPointOfMeasurement_dataunits":
    DevelopmentPointOfMeasurementDataunits,
    "#/definitions/developmentSampleResponse": DevelopmentSampleResponse,
    "#/definitions/developmentSampleResponse/properties/content":
    DevelopmentSampleResponseContent,
    "#/definitions/developmentSampleShipmentResponse":
    DevelopmentSampleShipmentResponse,
    "#/definitions/developmentSampleShipmentResponse/properties/content":
    DevelopmentSampleShipmentResponseContent,
    "#/definitions/developmentSampleShipment_dataunits":
    DevelopmentSampleShipmentDataunits,
    "#/definitions/developmentSample_dataunits": DevelopmentSampleDataunits,
    "#/definitions/developmentStyleResponse": DevelopmentStyleResponse,
    "#/definitions/developmentStyleResponse/properties/content":
    DevelopmentStyleResponseContent,
    "#/definitions/developmentStyle_dataunits": DevelopmentStyleDataunits,
    "#/definitions/dsAudit": DsAudit,
    "#/definitions/dsClassification": DsClassification,
    "#/definitions/dsCore": DsCore,
    "#/definitions/dsLast": DsLast,
    "#/definitions/dsSeasonAudit": DsSeasonAudit,
    "#/definitions/dsSeasonCore": DsSeasonCore,
    "#/definitions/dsSeasonFOB": DsSeasonFOB,
    "#/definitions/dsSeasonResource": DsSeasonResource,
    "#/definitions/dsSeasonStatus": DsSeasonStatus,
    "#/definitions/dsSeasonTechnicalDifficulty": DsSeasonTechnicalDifficulty,
    "#/definitions/dsSeasonTrack": DsSeasonTrack,
    "#/definitions/dsStatus": DsStatus,
    "#/definitions/msAudit": MsAudit,
    "#/definitions/msCore": MsCore,
    "#/definitions/msCore/properties/measurementSetApplicabilityList":
    MsCoreMeasurementSetApplicabilityList,
    "#/definitions/msCore/properties/measurementSetApplicabilityList/items":
    MsCoreMeasurementSetApplicability,
    "#/definitions/msPointOfMeasurementBreakdown":
    MsPointOfMeasurementBreakdowns,
    "#/definitions/msPointOfMeasurementBreakdown/items":
    MsPointOfMeasurementBreakdown,
    "#/definitions/msPointOfMeasurementBreakdown/items/properties/sizeBreakdown":  # noqa
    MsPointOfMeasurementSizeBreakdowns,
    "#/definitions/msPointOfMeasurementBreakdown/items/properties/sizeBreakdown/items":  # noqa
    MsPointOfMeasurementSizeBreakdown,
    "#/definitions/msSize": MsSize,
    "#/definitions/msStatus": MsStatus,
    "#/definitions/msTemplate": MsTemplate,
    "#/definitions/pomAudit": PomAudit,
    "#/definitions/pomCore": PomCore,
    "#/definitions/pomStatus": PomStatus,
    "#/definitions/relationshipResponse": RelationshipResponse,
    "#/definitions/relationshipResponse/properties/content":
    RelationshipResponseContents,
    "#/definitions/relationshipResponse/properties/content/items":
    RelationshipResponseContent,
    "#/definitions/scAudit": ScAudit,
    "#/definitions/scClassification": ScClassification,
    "#/definitions/scColorwaySeasonAudit": ScColorwaySeasonAudit,
    "#/definitions/scColorwaySeasonClassification":
    ScColorwaySeasonClassification,
    "#/definitions/scColorwaySeasonCore": ScColorwaySeasonCore,
    "#/definitions/scColorwaySeasonStatus": ScColorwaySeasonStatus,
    "#/definitions/scCore": ScCore,
    "#/definitions/scSeasonAudit": ScSeasonAudit,
    "#/definitions/scSeasonCore": ScSeasonCore,
    "#/definitions/scSeasonResource": ScSeasonResource,
    "#/definitions/scSeasonStatus": ScSeasonStatus,
    "#/definitions/searchResponse": SearchResponse,
    "#/definitions/searchResponse/properties/content": SearchResponseContents,
    "#/definitions/searchResponse/properties/content/items":
    SearchResponseContent,
    "#/definitions/sourcingConfigurationColorwaySeason_dataunits":
    SourcingConfigurationColorwaySeasonDataunits,
    "#/definitions/sourcingConfiguration_dataunits":
    SourcingConfigurationDataunits,
    "#/definitions/sourcingConfigurationsBulkResponse":
    SourcingConfigurationsBulkResponse,
    "#/definitions/sourcingConfigurationsBulkResponse/properties/content":
    SourcingConfigurationsBulkResponseContents,
    "#/definitions/sourcingConfigurationsBulkResponse/properties/content/items":  # noqa
    SourcingConfigurationsBulkResponseContent,
    "#/definitions/sourcingConfigurationsColorwaySeasonBulkResponse":
    SourcingConfigurationsColorwaySeasonBulkResponse,
    "#/definitions/sourcingConfigurationsColorwaySeasonBulkResponse/properties/content":  # noqa
    SourcingConfigurationsColorwaySeasonBulkResponseContents,
    "#/definitions/sourcingConfigurationsColorwaySeasonBulkResponse/properties/content/items":  # noqa
    SourcingConfigurationsColorwaySeasonBulkResponseContent,
    "#/definitions/sourcingConfigurationsColorwaySeasonResponse":
    SourcingConfigurationsColorwaySeasonResponse,
    "#/definitions/sourcingConfigurationsColorwaySeasonResponse/properties/content":  # noqa
    SourcingConfigurationsColorwaySeasonResponseContent,
    "#/definitions/sourcingConfigurationsResponse":
    SourcingConfigurationsResponse,
    "#/definitions/sourcingConfigurationsResponse/properties/content":
    SourcingConfigurationsResponseContent,
    "#/paths/~1data~1billOfMaterials/get/parameters/0":
    DataBillOfMaterialsGetObjectId,
    "#/paths/~1data~1billOfMaterials/get/parameters/1":
    DataBillOfMaterialsGetDataunits,
    "#/paths/~1data~1billOfMaterials~1sources/get/parameters/0":
    DataBillOfMaterialsSourcesGetObjectId,
    "#/paths/~1data~1billOfMaterials~1sources/get/parameters/1":
    DataBillOfMaterialsSourcesGetDataunits,
    "#/paths/~1data~1billOfMaterials~1sources~1{objectId}/get/parameters/1":
    DataBillOfMaterialsSourcesObjectIdGetDataunits,
    "#/paths/~1data~1billOfMaterials~1{objectId}/get/parameters/1":
    DataBillOfMaterialsObjectIdGetDataunits,
    "#/paths/~1data~1colorwaySeasons/get/parameters/0":
    DataColorwaySeasonsGetObjectId,
    "#/paths/~1data~1colorwaySeasons/get/parameters/1":
    DataColorwaySeasonsGetDataunits,
    "#/paths/~1data~1colorwaySeasons~1{objectId}/get/parameters/1":
    DataColorwaySeasonsObjectIdGetDataunits,
    "#/paths/~1data~1developmentSamples~1samples~1{objectId}/get/parameters/1":
    DataDevelopmentSamplesSamplesObjectIdGetDataunits,
    "#/paths/~1data~1developmentSamples~1shipments~1{objectId}/get/parameters/1":  # noqa
    DataDevelopmentSamplesShipmentsObjectIdGetDataunits,
    "#/paths/~1data~1developmentStyles~1{objectId}/get/parameters/1":
    DataDevelopmentStylesObjectIdGetDataunits,
    "#/paths/~1data~1measurementSets~1{objectId}/get/parameters/1":
    DataMeasurementSetsObjectIdGetDataunits,
    "#/paths/~1data~1pointsOfMeasurement~1{objectId}/get/parameters/1":
    DataPointsOfMeasurementObjectIdGetDataunits,
    "#/paths/~1data~1sourcingConfigurations~1/get/parameters/0":
    DataSourcingConfigurationsGetObjectId,
    "#/paths/~1data~1sourcingConfigurations~1/get/parameters/1":
    DataSourcingConfigurationsGetDataunits,
    "#/paths/~1data~1sourcingConfigurations~1colorwaySeasons/get/parameters/0":
    DataSourcingConfigurationsColorwaySeasonsGetObjectId,
    "#/paths/~1data~1sourcingConfigurations~1colorwaySeasons/get/parameters/1":
    DataSourcingConfigurationsColorwaySeasonsGetDataunits,
    "#/paths/~1data~1sourcingConfigurations~1colorwaySeasons~1{objectId}/get/parameters/1":  # noqa
    DataSourcingConfigurationsColorwaySeasonsObjectIdGetDataunits,
    "#/paths/~1data~1sourcingConfigurations~1{objectId}/get/parameters/1":
    DataSourcingConfigurationsObjectIdGetDataunits,
    "#/paths/~1search~1billOfMaterials/get/parameters/10":
    SearchBillOfMaterialsGetSourcingConfigurationSeason,
    "#/paths/~1search~1billOfMaterials/get/parameters/11":
    SearchBillOfMaterialsGetDevelopmentStyleType,
    "#/paths/~1search~1billOfMaterials/get/parameters/12":
    SearchBillOfMaterialsGetDivision,
    "#/paths/~1search~1billOfMaterials/get/parameters/13":
    SearchBillOfMaterialsGetBomDescription,
    "#/paths/~1search~1billOfMaterials/get/parameters/14":
    SearchBillOfMaterialsGetBomComments,
    "#/paths/~1search~1billOfMaterials/get/parameters/15":
    SearchBillOfMaterialsGetBillOfMaterialStatusIndicator,
    "#/paths/~1search~1billOfMaterials/get/parameters/16":
    SearchBillOfMaterialsGetBomLineItemIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/17":
    SearchBillOfMaterialsGetBomLineItemComments,
    "#/paths/~1search~1billOfMaterials/get/parameters/18":
    SearchBillOfMaterialsGetBomLineItemNumber,
    "#/paths/~1search~1billOfMaterials/get/parameters/19":
    SearchBillOfMaterialsGetParentBomLineItemIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/20":
    SearchBillOfMaterialsGetLineItemQuantity,
    "#/paths/~1search~1billOfMaterials/get/parameters/21":
    SearchBillOfMaterialsGetColor,
    "#/paths/~1search~1billOfMaterials/get/parameters/22":
    SearchBillOfMaterialsGetBillOfMaterialsSection,
    "#/paths/~1search~1billOfMaterials/get/parameters/23":
    SearchBillOfMaterialsGetPartPrimary,
    "#/paths/~1search~1billOfMaterials/get/parameters/24":
    SearchBillOfMaterialsGetPartSecondary,
    "#/paths/~1search~1billOfMaterials/get/parameters/25":
    SearchBillOfMaterialsGetPartModifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/26":
    SearchBillOfMaterialsGetPartSuffix,
    "#/paths/~1search~1billOfMaterials/get/parameters/27":
    SearchBillOfMaterialsGetPartName,
    "#/paths/~1search~1billOfMaterials/get/parameters/28":
    SearchBillOfMaterialsGetMaterialItemIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/29":
    SearchBillOfMaterialsGetSuppliedMaterial,
    "#/paths/~1search~1billOfMaterials/get/parameters/30":
    SearchBillOfMaterialsGetSuppliedMaterialColorIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/31":
    SearchBillOfMaterialsGetSuppliedMaterialColorIsMultipleColors,
    "#/paths/~1search~1billOfMaterials/get/parameters/32":
    SearchBillOfMaterialsGetColorPlaceholderDescription,
    "#/paths/~1search~1billOfMaterials/get/parameters/33":
    SearchBillOfMaterialsGetMaterialItemPlaceholderDescription,
    "#/paths/~1search~1billOfMaterials/get/parameters/34":
    SearchBillOfMaterialsGetBomGUID,
    "#/paths/~1search~1billOfMaterials/get/parameters/5":
    SearchBillOfMaterialsGetBomIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/6":
    SearchBillOfMaterialsGetDevelopmentColorwayIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/7":
    SearchBillOfMaterialsGetBomName,
    "#/paths/~1search~1billOfMaterials/get/parameters/8":
    SearchBillOfMaterialsGetDevelopmentColorwaySeasonIdentifier,
    "#/paths/~1search~1billOfMaterials/get/parameters/9":
    SearchBillOfMaterialsGetSourcingConfigurationIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/10":
    SearchBillOfMaterialsSourcesGetProductIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/11":
    SearchBillOfMaterialsSourcesGetStyleNumber,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/12":
    SearchBillOfMaterialsSourcesGetSourcingConfigurationSeason,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/13":
    SearchBillOfMaterialsSourcesGetCycleYear,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/14":
    SearchBillOfMaterialsSourcesGetDevelopmentStyleType,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/15":
    SearchBillOfMaterialsSourcesGetDivision,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/16":
    SearchBillOfMaterialsSourcesGetBillOfMaterialStatusIndicator,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/17":
    SearchBillOfMaterialsSourcesGetBomLineItemIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/18":
    SearchBillOfMaterialsSourcesGetBomLineItemNumber,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/19":
    SearchBillOfMaterialsSourcesGetParentBomLineItemIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/20":
    SearchBillOfMaterialsSourcesGetLineItemQuantity,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/21":
    SearchBillOfMaterialsSourcesGetColor,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/22":
    SearchBillOfMaterialsSourcesGetBillOfMaterialsSection,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/23":
    SearchBillOfMaterialsSourcesGetPart,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/24":
    SearchBillOfMaterialsSourcesGetMaterialItemIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/25":
    SearchBillOfMaterialsSourcesGetSuppliedMaterial,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/26":
    SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/27":
    SearchBillOfMaterialsSourcesGetSuppliedMaterialColorIsMultipleColors,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/28":
    SearchBillOfMaterialsSourcesGetColorPlaceholderDescription,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/29":
    SearchBillOfMaterialsSourcesGetMaterialItemPlaceholderDescription,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/30":
    SearchBillOfMaterialsSourcesGetNetUsage,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/31":
    SearchBillOfMaterialsSourcesGetWasteUsage,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/32":
    SearchBillOfMaterialsSourcesGetGrossUsage,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/33":
    SearchBillOfMaterialsSourcesGetUsageUnitOfMeasure,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/34":
    SearchBillOfMaterialsSourcesGetBomGUID,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/5":
    SearchBillOfMaterialsSourcesGetBomIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/6":
    SearchBillOfMaterialsSourcesGetDevelopmentColorwayIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/7":
    SearchBillOfMaterialsSourcesGetBomName,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/8":
    SearchBillOfMaterialsSourcesGetDevelopmentColorwaySeasonIdentifier,
    "#/paths/~1search~1billOfMaterials~1sources/get/parameters/9":
    SearchBillOfMaterialsSourcesGetSourcingConfigurationIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/10":
    SearchColorwaySeasonsGetSampleQuantity,
    "#/paths/~1search~1colorwaySeasons/get/parameters/11":
    SearchColorwaySeasonsGetNikeProductionTrial,
    "#/paths/~1search~1colorwaySeasons/get/parameters/12":
    SearchColorwaySeasonsGetTargetFOB,
    "#/paths/~1search~1colorwaySeasons/get/parameters/13":
    SearchColorwaySeasonsGetSourcingConfigurationColorwaySeason,
    "#/paths/~1search~1colorwaySeasons/get/parameters/14":
    SearchColorwaySeasonsGetDevelopmentStyleIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/15":
    SearchColorwaySeasonsGetCycleYear,
    "#/paths/~1search~1colorwaySeasons/get/parameters/16":
    SearchColorwaySeasonsGetWhqColorDesignerUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/17":
    SearchColorwaySeasonsGetWhqCostingUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/18":
    SearchColorwaySeasonsGetWhqDesignerUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/19":
    SearchColorwaySeasonsGetWhqDeveloperUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/20":
    SearchColorwaySeasonsGetWhqFootwearDevelopmentDirectorUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/21":
    SearchColorwaySeasonsGetWhqKnitDeveloperUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/22":
    SearchColorwaySeasonsGetWhqKnitEngineerUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/23":
    SearchColorwaySeasonsGetWhqKnitProgrammerUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/24":
    SearchColorwaySeasonsGetWhqMaterialUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/25":
    SearchColorwaySeasonsGetWhqProductEngineerUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/26":
    SearchColorwaySeasonsGetWhqProductTestingUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/27":
    SearchColorwaySeasonsGetKnitCenterDeveloperUserIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/31":
    SearchColorwaySeasonsGetProductSeasonDevelopmentTeam,
    "#/paths/~1search~1colorwaySeasons/get/parameters/32":
    SearchColorwaySeasonsGetTechnicalDifficulty,
    "#/paths/~1search~1colorwaySeasons/get/parameters/33":
    SearchColorwaySeasonsGetDevelopmentColorwayTargetFOB,
    "#/paths/~1search~1colorwaySeasons/get/parameters/34":
    SearchColorwaySeasonsGetDevelopmentTrack,
    "#/paths/~1search~1colorwaySeasons/get/parameters/35":
    SearchColorwaySeasonsGetProductTrack,
    "#/paths/~1search~1colorwaySeasons/get/parameters/36":
    SearchColorwaySeasonsGetStartDate,
    "#/paths/~1search~1colorwaySeasons/get/parameters/38":
    SearchColorwaySeasonsGetLastIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/39":
    SearchColorwaySeasonsGetAdditionalLastIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/41":
    SearchColorwaySeasonsGetDevelopmentColorwayDescription,
    "#/paths/~1search~1colorwaySeasons/get/parameters/42":
    SearchColorwaySeasonsGetDevelopmentColorwayType,
    "#/paths/~1search~1colorwaySeasons/get/parameters/43":
    SearchColorwaySeasonsGetDevelopmentColorwayState,
    "#/paths/~1search~1colorwaySeasons/get/parameters/44":
    SearchColorwaySeasonsGetDevelopmentColorwayGate,
    "#/paths/~1search~1colorwaySeasons/get/parameters/45":
    SearchColorwaySeasonsGetProductIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/47":
    SearchColorwaySeasonsGetDevelopmentStyleType,
    "#/paths/~1search~1colorwaySeasons/get/parameters/48":
    SearchColorwaySeasonsGetDivision,
    "#/paths/~1search~1colorwaySeasons/get/parameters/5":
    SearchColorwaySeasonsGetDevelopmentColorwayIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/6":
    SearchColorwaySeasonsGetDevelopmentStyleSeasonIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/7":
    SearchColorwaySeasonsGetProductOfferingIdentifier,
    "#/paths/~1search~1colorwaySeasons/get/parameters/9":
    SearchColorwaySeasonsGetPrototypeQuantity,
    "#/paths/~1search~1developmentStyles/get/parameters/11":
    SearchDevelopmentStylesGetDevelopmentStyleType,
    "#/paths/~1search~1developmentStyles/get/parameters/12":
    SearchDevelopmentStylesGetDivision,
    "#/paths/~1search~1developmentStyles/get/parameters/5":
    SearchDevelopmentStylesGetDevelopmentStyleName,
    "#/paths/~1search~1developmentStyles/get/parameters/6":
    SearchDevelopmentStylesGetModelIdentifier,
    "#/paths/~1search~1developmentStyles/get/parameters/7":
    SearchDevelopmentStylesGetStyleNumber,
    "#/paths/~1search~1developmentStyles/get/parameters/8":
    SearchDevelopmentStylesGetLastIdentifier,
    "#/paths/~1search~1developmentStyles/get/parameters/9":
    SearchDevelopmentStylesGetAdditionalLastIdentifier,
    "#/paths/~1search~1measurementSets/get/parameters/10":
    SearchMeasurementSetsGetSourcingConfigurationIdentifier,
    "#/paths/~1search~1measurementSets/get/parameters/11":
    SearchMeasurementSetsGetSourcingConfigurationSeasonIdentifier,
    "#/paths/~1search~1measurementSets/get/parameters/12":
    SearchMeasurementSetsGetMeasurementSetTemplateName,
    "#/paths/~1search~1measurementSets/get/parameters/13":
    SearchMeasurementSetsGetSizeDefinitionTemplate,
    "#/paths/~1search~1measurementSets/get/parameters/14":
    SearchMeasurementSetsGetGradeRuleTemplate,
    "#/paths/~1search~1measurementSets/get/parameters/15":
    SearchMeasurementSetsGetMeasurementTemplateType,
    "#/paths/~1search~1measurementSets/get/parameters/16":
    SearchMeasurementSetsGetDevelopmentStyleSizeDefinition,
    "#/paths/~1search~1measurementSets/get/parameters/17":
    SearchMeasurementSetsGetMeasurementValueUnitOfMeasure,
    "#/paths/~1search~1measurementSets/get/parameters/18":
    SearchMeasurementSetsGetBaseSize,
    "#/paths/~1search~1measurementSets/get/parameters/19":
    SearchMeasurementSetsGetSizeSelectionList,
    "#/paths/~1search~1measurementSets/get/parameters/20":
    SearchMeasurementSetsGetSize,
    "#/paths/~1search~1measurementSets/get/parameters/21":
    SearchMeasurementSetsGetMeasurementCode,
    "#/paths/~1search~1measurementSets/get/parameters/22":
    SearchMeasurementSetsGetPointOfMeasurementName,
    "#/paths/~1search~1measurementSets/get/parameters/23":
    SearchMeasurementSetsGetSortOrder,
    "#/paths/~1search~1measurementSets/get/parameters/24":
    SearchMeasurementSetsGetMeasurementInstructions,
    "#/paths/~1search~1measurementSets/get/parameters/25":
    SearchMeasurementSetsGetMeasurementDetail,
    "#/paths/~1search~1measurementSets/get/parameters/26":
    SearchMeasurementSetsGetPointOfMeasurementCriticality,
    "#/paths/~1search~1measurementSets/get/parameters/27":
    SearchMeasurementSetsGetToleranceNegative,
    "#/paths/~1search~1measurementSets/get/parameters/28":
    SearchMeasurementSetsGetTolerancePositive,
    "#/paths/~1search~1measurementSets/get/parameters/29":
    SearchMeasurementSetsGetMeasurementSizeValue,
    "#/paths/~1search~1measurementSets/get/parameters/30":
    SearchMeasurementSetsGetPointOfMeasurement,
    "#/paths/~1search~1measurementSets/get/parameters/31":
    SearchMeasurementSetsGetMeasurementSetStatusIndicator,
    "#/paths/~1search~1measurementSets/get/parameters/5":
    SearchMeasurementSetsGetMeasurementSetName,
    "#/paths/~1search~1measurementSets/get/parameters/6":
    SearchMeasurementSetsGetMeasurementSetState,
    "#/paths/~1search~1measurementSets/get/parameters/7":
    SearchMeasurementSetsGetDevelopmentStyleIdentifier,
    "#/paths/~1search~1measurementSets/get/parameters/8":
    SearchMeasurementSetsGetStyleNumber,
    "#/paths/~1search~1measurementSets/get/parameters/9":
    SearchMeasurementSetsGetCycleYear,
}
