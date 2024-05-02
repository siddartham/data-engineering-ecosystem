import datetime
import typing
import sob


class Entitlements(sob.model.Object):
    """
    Properties:

    - entitlements
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        entitlements: typing.Optional[
            typing.Union[
                "EntitlementsEntitlements",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.entitlements = entitlements
        super().__init__(_data)


class EntitlementsEntitlements(sob.model.Array):

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


class MaterialPerformanceTestLabResponse(sob.model.Object):
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
    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "MaterialPerformanceTestLabResponseContent",
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


class MaterialPerformanceTestLabResponseContent(sob.model.Object):
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
                "TestLabDataunits",
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


class PerformanceTestLabAddress(sob.model.Object):
    """
    Properties:

    - street_address_1:
      No Definition Available
    - street_address_2:
      No Definition Available
    - city_name:
      No Definition Available
    - state_province:
      No Definition Available
    - postal_code:
      No Definition Available
    - country
    - phone_number:
      No Definition Available
    - fax_number:
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
        street_address_1: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        street_address_2: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        city_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        state_province: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        postal_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        country: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        phone_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        fax_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.street_address_1 = street_address_1
        self.street_address_2 = street_address_2
        self.city_name = city_name
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.phone_number = phone_number
        self.fax_number = fax_number
        super().__init__(_data)


class PerformanceTestLabAudit(sob.model.Object):
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


class PerformanceTestLabContacts(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "PerformanceTestLabContact"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class PerformanceTestLabContact(sob.model.Object):
    """
    Properties:

    - test_lab_contact_role:
      No Definition Available
    - test_lab_primary_contact_indicator
    - full_name:
      No Definition Available
    - email_address:
      No Definition Available
    - primary_phone_number:
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
        test_lab_contact_role: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        test_lab_primary_contact_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        full_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        email_address: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        primary_phone_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.test_lab_contact_role = test_lab_contact_role
        self.test_lab_primary_contact_indicator = (
            test_lab_primary_contact_indicator
        )
        self.full_name = full_name
        self.email_address = email_address
        self.primary_phone_number = primary_phone_number
        super().__init__(_data)


class PerformanceTestLabCore(sob.model.Object):
    """
    Properties:

    - test_lab_identifier:
      supplierIdentifier
    - test_lab_code:
      No Definition Available
    - test_lab_name:
      No Definition Available
    - division
    - parent_company_name:
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
        test_lab_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        test_lab_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        test_lab_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        parent_company_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.test_lab_identifier = test_lab_identifier
        self.test_lab_code = test_lab_code
        self.test_lab_name = test_lab_name
        self.division = division
        self.parent_company_name = parent_company_name
        super().__init__(_data)


class PerformanceTestLabGeneral(sob.model.Object):
    """
    Properties:

    - responsible_nike_liaison_office
    - accredited_test_facility
    - security_vendor_access_group
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        responsible_nike_liaison_office: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        accredited_test_facility: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        security_vendor_access_group: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.responsible_nike_liaison_office = responsible_nike_liaison_office
        self.accredited_test_facility = accredited_test_facility
        self.security_vendor_access_group = security_vendor_access_group
        super().__init__(_data)


class PerformanceTestLabState(sob.model.Object):
    """
    Properties:

    - test_lab_state
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        test_lab_state: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.test_lab_state = test_lab_state
        super().__init__(_data)


class PerformanceTestLabStatus(sob.model.Object):
    """
    Properties:

    - test_lab_status_indicator
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        test_lab_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.test_lab_status_indicator = test_lab_status_indicator
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


class SupplierAgent(sob.model.Object):
    """
    Properties:

    - agent_identifier
    - agent_full_name:
      No Definition Available
    - agent_parent_company_name:
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
        agent_identifier: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        agent_full_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        agent_parent_company_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.agent_identifier = agent_identifier
        self.agent_full_name = agent_full_name
        self.agent_parent_company_name = agent_parent_company_name
        super().__init__(_data)


class SupplierAgentLegacy(sob.model.Object):
    """
    Properties:

    - legacy_agent_code:
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
        legacy_agent_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.legacy_agent_code = legacy_agent_code
        super().__init__(_data)


class SupplierAudit(sob.model.Object):
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


class SupplierCore(sob.model.Object):
    """
    Properties:

    - supplier_identifier:
      No Definition Available
    - supplier_name:
      No Definition Available
    - division_code
    - parent_company_name:
      No Definition Available
    - vendor_ownership_type:
      No Definition Available
    - web_site_address:
      No Definition Available
    - has_agent_indicator:
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
        supplier_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null,
                int
            ]
        ] = None,
        supplier_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        division_code: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        parent_company_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        vendor_ownership_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        web_site_address: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        has_agent_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_identifier = supplier_identifier
        self.supplier_name = supplier_name
        self.division_code = division_code
        self.parent_company_name = parent_company_name
        self.vendor_ownership_type = vendor_ownership_type
        self.web_site_address = web_site_address
        self.has_agent_indicator = has_agent_indicator
        super().__init__(_data)


class SupplierLegacy(sob.model.Object):
    """
    Properties:

    - legacy_supplier_code:
      No Definition Available
    - legacy_supplier_name
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        legacy_supplier_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        legacy_supplier_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.legacy_supplier_code = legacy_supplier_code
        self.legacy_supplier_name = legacy_supplier_name
        super().__init__(_data)


class SupplierState(sob.model.Object):
    """
    Properties:

    - supplier_state_identifier
    - supplier_state_identifier_reference
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_state_identifier_reference: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_state_identifier = supplier_state_identifier
        self.supplier_state_identifier_reference = (
            supplier_state_identifier_reference
        )
        super().__init__(_data)


class SupplierStatus(sob.model.Object):
    """
    Properties:

    - supplier_status_indicator:
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
        supplier_status_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_status_indicator = supplier_status_indicator
        super().__init__(_data)


class SupplierLocationAddresses(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SupplierLocationAddress"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SupplierLocationAddress(sob.model.Object):
    """
    Properties:

    - supplier_location_address_type:
      No Definition Available
    - street_address_1:
      No Definition Available
    - street_address_2:
      No Definition Available
    - city_name:
      No Definition Available
    - state_province:
      No Definition Available
    - postal_code:
      No Definition Available
    - geographic_area:
      No Definition Available
    - supplier_location_latest_record_indicator:
      No Definition Available
    - phone_number:
      No Definition Available
    - fax_number:
      No Definition Available
    - supplier_location_change_time_stamp:
      No Definition Available
    - country
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplier_location_address_type: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        street_address_1: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        street_address_2: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        city_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        state_province: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        postal_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        geographic_area: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_latest_record_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        phone_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        fax_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_change_time_stamp: typing.Optional[
            typing.Union[
                datetime.datetime,
                sob.utilities.types.Null
            ]
        ] = None,
        country: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_address_type = supplier_location_address_type
        self.street_address_1 = street_address_1
        self.street_address_2 = street_address_2
        self.city_name = city_name
        self.state_province = state_province
        self.postal_code = postal_code
        self.geographic_area = geographic_area
        self.supplier_location_latest_record_indicator = (
            supplier_location_latest_record_indicator
        )
        self.phone_number = phone_number
        self.fax_number = fax_number
        self.supplier_location_change_time_stamp = (
            supplier_location_change_time_stamp
        )
        self.country = country
        super().__init__(_data)


class SupplierLocationAudit(sob.model.Object):
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


class SupplierLocationContacts(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SupplierLocationContact"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SupplierLocationContact(sob.model.Object):
    """
    Properties:

    - supplier_location_contact_role
    - supplier_location_contact_priority_identifier
    - full_name:
      No Definition Available
    - email_address:
      No Definition Available
    - primary_phone_number:
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
        supplier_location_contact_role: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_contact_priority_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        full_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        email_address: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        primary_phone_number: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_contact_role = supplier_location_contact_role
        self.supplier_location_contact_priority_identifier = (
            supplier_location_contact_priority_identifier
        )
        self.full_name = full_name
        self.email_address = email_address
        self.primary_phone_number = primary_phone_number
        super().__init__(_data)


class SupplierLocationCore(sob.model.Object):
    """
    Properties:

    - supplier_location_identifier:
      supplier Location Identifier
    - supplier_location_name:
      No Definition Available
    - supplier
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplier_location_identifier: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_name: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_identifier = supplier_location_identifier
        self.supplier_location_name = supplier_location_name
        self.supplier = supplier
        super().__init__(_data)


class SupplierLocationGeneral(sob.model.Object):
    """
    Properties:

    - responsible_nike_liaison_office_identifier:
      No Definition Available
    - supplier_reason_retired_identifier:
      No Definition Available
    - supplier_location_founded_year_number:
      No Definition Available
    - accredited_test_facility
    - security_vendor_access_group
    - global_development_center
    - responsible_nike_liaison_office_identifier_reference
    - confidentiality_agreement_indicator
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_reason_retired_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_founded_year_number: typing.Optional[
            typing.Union[
                int,
                sob.utilities.types.Null
            ]
        ] = None,
        accredited_test_facility: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        security_vendor_access_group: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        global_development_center: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None,
        responsible_nike_liaison_office_identifier_reference: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        confidentiality_agreement_indicator: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.responsible_nike_liaison_office_identifier = (
            responsible_nike_liaison_office_identifier
        )
        self.supplier_reason_retired_identifier = (
            supplier_reason_retired_identifier
        )
        self.supplier_location_founded_year_number = (
            supplier_location_founded_year_number
        )
        self.accredited_test_facility = accredited_test_facility
        self.security_vendor_access_group = security_vendor_access_group
        self.global_development_center = global_development_center
        self.responsible_nike_liaison_office_identifier_reference = (
            responsible_nike_liaison_office_identifier_reference
        )
        self.confidentiality_agreement_indicator = (
            confidentiality_agreement_indicator
        )
        super().__init__(_data)


class SupplierLocationGeography(sob.model.Object):
    """
    Properties:

    - supplier_location_country
    - port_of_origin_country
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplier_location_country: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None,
        port_of_origin_country: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_country = supplier_location_country
        self.port_of_origin_country = port_of_origin_country
        super().__init__(_data)


class SupplierLocationLegacy(sob.model.Object):
    """
    Properties:

    - legacy_supplier_location_code:
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
        legacy_supplier_location_code: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.legacy_supplier_location_code = legacy_supplier_location_code
        super().__init__(_data)


class SupplierLocationState(sob.model.Object):
    """
    Properties:

    - supplier_location_state_identifier
    - supplier_location_state_identifier_reference
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplier_location_state_identifier: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_state_identifier_reference: typing.Optional[
            typing.Union[
                "Reference",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_state_identifier = (
            supplier_location_state_identifier
        )
        self.supplier_location_state_identifier_reference = (
            supplier_location_state_identifier_reference
        )
        super().__init__(_data)


class SupplierLocationStatus(sob.model.Object):
    """
    Properties:

    - supplier_location_status_indicator
    - supplier_location_status_indicator_boolean
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        supplier_location_status_indicator: typing.Optional[
            typing.Union[
                str,
                sob.utilities.types.Null
            ]
        ] = None,
        supplier_location_status_indicator_boolean: typing.Optional[
            typing.Union[
                bool,
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.supplier_location_status_indicator = (
            supplier_location_status_indicator
        )
        self.supplier_location_status_indicator_boolean = (
            supplier_location_status_indicator_boolean
        )
        super().__init__(_data)


class SupplierBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - count:
      The number of entries returned in this responses
    - offset:
      The number of entries offset (can be used to derive the "Page Number" by
      using count)
    - next_
    - prev
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
                "SupplierBulkResponseContents",
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
        self.offset = offset
        self.next_ = next_
        self.prev = prev
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class SupplierBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SupplierBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SupplierBulkResponseContent(sob.model.Object):
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
                "SupplierDataunits",
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


class SupplierLocationBulkResponse(sob.model.Object):
    """
    Properties:

    - content
    - count:
      The number of entries returned in this responses
    - offset:
      The number of entries offset (can be used to derive the "Page Number" by
      using count)
    - next_
    - prev
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
                "SupplierLocationBulkResponseContents",
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
        self.offset = offset
        self.next_ = next_
        self.prev = prev
        self.self_ = self_
        self.request_time = request_time
        self.request_status = request_status
        super().__init__(_data)


class SupplierLocationBulkResponseContents(sob.model.Array):

    def __init__(
        self,
        items: typing.Union[
            typing.Iterable[
                "SupplierLocationBulkResponseContent"
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None
    ) -> None:
        super().__init__(items)


class SupplierLocationBulkResponseContent(sob.model.Object):
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
                "SupplierLocationDataunits",
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


class SupplierLocationResponse(sob.model.Object):
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
    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "SupplierLocationResponseContent",
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


class SupplierLocationResponseContent(sob.model.Object):
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
                "SupplierLocationDataunits",
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


class SupplierLocationDataunits(sob.model.Object):
    """
    Properties:

    - suploc_core
    - suploc_legacy
    - suploc_general
    - suploc_state
    - suploc_status
    - suploc_address
    - suploc_contact
    - suploc_geography
    - suploc_audit
    - suploc_entitlement
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        suploc_core: typing.Optional[
            typing.Union[
                "SupplierLocationCore",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_legacy: typing.Optional[
            typing.Union[
                "SupplierLocationLegacy",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_general: typing.Optional[
            typing.Union[
                "SupplierLocationGeneral",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_state: typing.Optional[
            typing.Union[
                "SupplierLocationState",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_status: typing.Optional[
            typing.Union[
                "SupplierLocationStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_address: typing.Optional[
            typing.Union[
                "SupplierLocationAddresses",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_contact: typing.Optional[
            typing.Union[
                "SupplierLocationContacts",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_geography: typing.Optional[
            typing.Union[
                "SupplierLocationGeography",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_audit: typing.Optional[
            typing.Union[
                "SupplierLocationAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        suploc_entitlement: typing.Optional[
            typing.Union[
                "Entitlements",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.suploc_core = suploc_core
        self.suploc_legacy = suploc_legacy
        self.suploc_general = suploc_general
        self.suploc_state = suploc_state
        self.suploc_status = suploc_status
        self.suploc_address = suploc_address
        self.suploc_contact = suploc_contact
        self.suploc_geography = suploc_geography
        self.suploc_audit = suploc_audit
        self.suploc_entitlement = suploc_entitlement
        super().__init__(_data)


class SupplierResponse(sob.model.Object):
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
    - object_id:
      The business key related to items requested.
    - object_type:
      The type of key that has been requested.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
                "SupplierResponseContent",
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


class SupplierResponseContent(sob.model.Object):
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
                "SupplierDataunits",
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


class SupplierDataunits(sob.model.Object):
    """
    Properties:

    - sup_core
    - sup_legacy
    - sup_state
    - sup_status
    - sup_agent
    - sup_agent_legacy
    - sup_audit
    - sup_entitlement
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        sup_core: typing.Optional[
            typing.Union[
                "SupplierCore",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_legacy: typing.Optional[
            typing.Union[
                "SupplierLegacy",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_state: typing.Optional[
            typing.Union[
                "SupplierState",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_status: typing.Optional[
            typing.Union[
                "SupplierStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_agent: typing.Optional[
            typing.Union[
                "SupplierAgent",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_agent_legacy: typing.Optional[
            typing.Union[
                "SupplierAgentLegacy",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_audit: typing.Optional[
            typing.Union[
                "SupplierAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        sup_entitlement: typing.Optional[
            typing.Union[
                "Entitlements",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.sup_core = sup_core
        self.sup_legacy = sup_legacy
        self.sup_state = sup_state
        self.sup_status = sup_status
        self.sup_agent = sup_agent
        self.sup_agent_legacy = sup_agent_legacy
        self.sup_audit = sup_audit
        self.sup_entitlement = sup_entitlement
        super().__init__(_data)


class TestLabDataunits(sob.model.Object):
    """
    Properties:

    - perf_test_lab_core
    - perf_test_lab_general
    - perf_test_lab_state
    - perf_test_lab_status
    - perf_test_lab_address
    - perf_test_lab_contact
    - perf_test_lab_audit
    - perf_test_lab_entitlement
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        perf_test_lab_core: typing.Optional[
            typing.Union[
                "PerformanceTestLabCore",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_general: typing.Optional[
            typing.Union[
                "PerformanceTestLabGeneral",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_state: typing.Optional[
            typing.Union[
                "PerformanceTestLabState",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_status: typing.Optional[
            typing.Union[
                "PerformanceTestLabStatus",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_address: typing.Optional[
            typing.Union[
                "PerformanceTestLabAddress",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_contact: typing.Optional[
            typing.Union[
                "PerformanceTestLabContacts",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_audit: typing.Optional[
            typing.Union[
                "PerformanceTestLabAudit",
                sob.utilities.types.Null
            ]
        ] = None,
        perf_test_lab_entitlement: typing.Optional[
            typing.Union[
                "Entitlements",
                sob.utilities.types.Null
            ]
        ] = None
    ) -> None:
        self.perf_test_lab_core = perf_test_lab_core
        self.perf_test_lab_general = perf_test_lab_general
        self.perf_test_lab_state = perf_test_lab_state
        self.perf_test_lab_status = perf_test_lab_status
        self.perf_test_lab_address = perf_test_lab_address
        self.perf_test_lab_contact = perf_test_lab_contact
        self.perf_test_lab_audit = perf_test_lab_audit
        self.perf_test_lab_entitlement = perf_test_lab_entitlement
        super().__init__(_data)


class DataMaterialPerformanceTestLabsObjectIdGetDataunits(sob.model.Array):
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


class DataMaterialSupplierLocationsGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Supplier Location
    )
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


class DataMaterialSupplierLocationsGetDataunits(sob.model.Array):
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


class DataMaterialSupplierLocationsObjectIdGetDataunits(sob.model.Array):
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


class DataMaterialSuppliersGetObjectId(sob.model.Array):
    """
    A comma separated list of Ids of the object (in this case Supplier)
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


class DataMaterialSuppliersGetDataunits(sob.model.Array):
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


class DataMaterialSuppliersObjectIdGetDataunits(sob.model.Array):
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


class SearchMaterialSupplierLocationsGetSecurityVendorAccessGroup(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifierReference(  # noqa
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


class SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifier(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifierReference(  # noqa
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


class SearchMaterialSupplierLocationsGetSupplierLocationStatusIndicator(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetSupplierLocationAddressType(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetStateProvince(sob.model.Array):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetGeographicArea(sob.model.Array):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetCountry(sob.model.Array):
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


class SearchMaterialSupplierLocationsGetSupplierLocationContactRole(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetSupplierLocationCountry(
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


class SearchMaterialSupplierLocationsGetPortOfOriginCountry(sob.model.Array):
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


class SearchMaterialSupplierLocationsGetSupplierIdentifier(sob.model.Array):
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


class SearchMaterialSupplierLocationsGetLegacySupplierLocationCode(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifier(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetSupplierReasonRetiredIdentifier(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSupplierLocationsGetSupplierLocationFoundedYearNumber(
    sob.model.Array
):
    """
    The value associated with this item
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


class SearchMaterialSuppliersGetSupplierStateIdentifierReference(
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


class SearchMaterialSuppliersGetAgentIdentifier(sob.model.Array):
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


class SearchMaterialSuppliersGetLegacyAgentCode(sob.model.Array):
    """
    The value associated with this item
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


class SearchMaterialSuppliersGetDivisionCode(sob.model.Array):
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


class SearchMaterialSuppliersGetVendorOwnershipType(sob.model.Array):
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


class SearchMaterialSuppliersGetLegacySupplierCode(sob.model.Array):
    """
    The balue associated with this item
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


class SearchMaterialSuppliersGetSupplierStateIdentifier(sob.model.Array):
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


sob.meta.object_writable(  # type: ignore
    Entitlements
).properties = sob.meta.Properties([
    (
        'entitlements',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                EntitlementsEntitlements,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    EntitlementsEntitlements
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
    MaterialPerformanceTestLabResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                MaterialPerformanceTestLabResponseContent,
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
    MaterialPerformanceTestLabResponseContent
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
                TestLabDataunits,
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
    PerformanceTestLabAddress
).properties = sob.meta.Properties([
    (
        'street_address_1',
        sob.properties.Property(
            name="streetAddress1",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'street_address_2',
        sob.properties.Property(
            name="streetAddress2",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'city_name',
        sob.properties.Property(
            name="cityName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'state_province',
        sob.properties.Property(
            name="stateProvince",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'postal_code',
        sob.properties.Property(
            name="postalCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'country',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'phone_number',
        sob.properties.Property(
            name="phoneNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'fax_number',
        sob.properties.Property(
            name="faxNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabAudit
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
    PerformanceTestLabContacts
).item_types = sob.types.MutableTypes([
    PerformanceTestLabContact
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabContact
).properties = sob.meta.Properties([
    (
        'test_lab_contact_role',
        sob.properties.Property(
            name="testLabContactRole",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'test_lab_primary_contact_indicator',
        sob.properties.Property(
            name="testLabPrimaryContactIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'full_name',
        sob.properties.Property(
            name="fullName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'email_address',
        sob.properties.Property(
            name="emailAddress",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'primary_phone_number',
        sob.properties.Property(
            name="primaryPhoneNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabCore
).properties = sob.meta.Properties([
    (
        'test_lab_identifier',
        sob.properties.Property(
            name="testLabIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'test_lab_code',
        sob.properties.Property(
            name="testLabCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'test_lab_name',
        sob.properties.Property(
            name="testLabName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
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
        'parent_company_name',
        sob.properties.Property(
            name="parentCompanyName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabGeneral
).properties = sob.meta.Properties([
    (
        'responsible_nike_liaison_office',
        sob.properties.Property(
            name="responsibleNikeLiaisonOffice",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'accredited_test_facility',
        sob.properties.Property(
            name="accreditedTestFacility",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'security_vendor_access_group',
        sob.properties.Property(
            name="securityVendorAccessGroup",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabState
).properties = sob.meta.Properties([
    (
        'test_lab_state',
        sob.properties.Property(
            name="testLabState",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    PerformanceTestLabStatus
).properties = sob.meta.Properties([
    (
        'test_lab_status_indicator',
        sob.properties.Property(
            name="testLabStatusIndicator",
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
    SupplierAgent
).properties = sob.meta.Properties([
    (
        'agent_identifier',
        sob.properties.Property(
            name="agentIdentifier",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'agent_full_name',
        sob.properties.Property(
            name="agentFullName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'agent_parent_company_name',
        sob.properties.Property(
            name="agentParentCompanyName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierAgentLegacy
).properties = sob.meta.Properties([
    (
        'legacy_agent_code',
        sob.properties.Property(
            name="legacyAgentCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierAudit
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
    SupplierCore
).properties = sob.meta.Properties([
    (
        'supplier_identifier',
        sob.properties.Property(
            name="supplierIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null,
                sob.properties.Integer()
            ])
        )
    ),
    (
        'supplier_name',
        sob.properties.Property(
            name="supplierName",
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
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'parent_company_name',
        sob.properties.Property(
            name="parentCompanyName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'vendor_ownership_type',
        sob.properties.Property(
            name="vendorOwnershipType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'web_site_address',
        sob.properties.Property(
            name="webSiteAddress",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'has_agent_indicator',
        sob.properties.Property(
            name="hasAgentIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLegacy
).properties = sob.meta.Properties([
    (
        'legacy_supplier_code',
        sob.properties.Property(
            name="legacySupplierCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'legacy_supplier_name',
        sob.properties.Property(
            name="legacySupplierName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
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
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_state_identifier_reference',
        sob.properties.Property(
            name="supplierStateIdentifierReference",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierStatus
).properties = sob.meta.Properties([
    (
        'supplier_status_indicator',
        sob.properties.Property(
            name="supplierStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    SupplierLocationAddresses
).item_types = sob.types.MutableTypes([
    SupplierLocationAddress
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationAddress
).properties = sob.meta.Properties([
    (
        'supplier_location_address_type',
        sob.properties.Property(
            name="supplierLocationAddressType",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'street_address_1',
        sob.properties.Property(
            name="streetAddress1",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'street_address_2',
        sob.properties.Property(
            name="streetAddress2",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'city_name',
        sob.properties.Property(
            name="cityName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'state_province',
        sob.properties.Property(
            name="stateProvince",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'postal_code',
        sob.properties.Property(
            name="postalCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'geographic_area',
        sob.properties.Property(
            name="geographicArea",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_latest_record_indicator',
        sob.properties.Property(
            name="supplierLocationLatestRecordIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'phone_number',
        sob.properties.Property(
            name="phoneNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'fax_number',
        sob.properties.Property(
            name="faxNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_change_time_stamp',
        sob.properties.Property(
            name="supplierLocationChangeTimeStamp",
            types=sob.types.MutableTypes([
                sob.properties.DateTime(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'country',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationAudit
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
    SupplierLocationContacts
).item_types = sob.types.MutableTypes([
    SupplierLocationContact
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationContact
).properties = sob.meta.Properties([
    (
        'supplier_location_contact_role',
        sob.properties.Property(
            name="supplierLocationContactRole",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_contact_priority_identifier',
        sob.properties.Property(
            name="supplierLocationContactPriorityIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'full_name',
        sob.properties.Property(
            name="fullName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'email_address',
        sob.properties.Property(
            name="emailAddress",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'primary_phone_number',
        sob.properties.Property(
            name="primaryPhoneNumber",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationCore
).properties = sob.meta.Properties([
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
        'supplier_location_name',
        sob.properties.Property(
            name="supplierLocationName",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationGeneral
).properties = sob.meta.Properties([
    (
        'responsible_nike_liaison_office_identifier',
        sob.properties.Property(
            name="responsibleNikeLiaisonOfficeIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_reason_retired_identifier',
        sob.properties.Property(
            name="supplierReasonRetiredIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_founded_year_number',
        sob.properties.Property(
            name="supplierLocationFoundedYearNumber",
            types=sob.types.MutableTypes([
                sob.properties.Integer(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'accredited_test_facility',
        sob.properties.Property(
            name="accreditedTestFacility",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'security_vendor_access_group',
        sob.properties.Property(
            name="securityVendorAccessGroup",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'global_development_center',
        sob.properties.Property(
            name="globalDevelopmentCenter",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'responsible_nike_liaison_office_identifier_reference',
        sob.properties.Property(
            name="responsibleNikeLiaisonOfficeIdentifierReference",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'confidentiality_agreement_indicator',
        sob.properties.Property(
            name="confidentialityAgreementIndicator",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationGeography
).properties = sob.meta.Properties([
    (
        'supplier_location_country',
        sob.properties.Property(
            name="supplierLocationCountry",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'port_of_origin_country',
        sob.properties.Property(
            name="portOfOriginCountry",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationLegacy
).properties = sob.meta.Properties([
    (
        'legacy_supplier_location_code',
        sob.properties.Property(
            name="legacySupplierLocationCode",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationState
).properties = sob.meta.Properties([
    (
        'supplier_location_state_identifier',
        sob.properties.Property(
            name="supplierLocationStateIdentifier",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_state_identifier_reference',
        sob.properties.Property(
            name="supplierLocationStateIdentifierReference",
            types=sob.types.MutableTypes([
                Reference,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationStatus
).properties = sob.meta.Properties([
    (
        'supplier_location_status_indicator',
        sob.properties.Property(
            name="supplierLocationStatusIndicator",
            types=sob.types.MutableTypes([
                sob.properties.String(),
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'supplier_location_status_indicator_boolean',
        sob.properties.Property(
            name="supplierLocationStatusIndicatorBoolean",
            types=sob.types.MutableTypes([
                sob.properties.Boolean(),
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierBulkResponseContents,
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
    SupplierBulkResponseContents
).item_types = sob.types.MutableTypes([
    SupplierBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    SupplierBulkResponseContent
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
                SupplierDataunits,
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
    SupplierLocationBulkResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierLocationBulkResponseContents,
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
    SupplierLocationBulkResponseContents
).item_types = sob.types.MutableTypes([
    SupplierLocationBulkResponseContent
])
sob.meta.object_writable(  # type: ignore
    SupplierLocationBulkResponseContent
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
                SupplierLocationDataunits,
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
    SupplierLocationResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierLocationResponseContent,
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
    SupplierLocationResponseContent
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
                SupplierLocationDataunits,
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
    SupplierLocationDataunits
).properties = sob.meta.Properties([
    (
        'suploc_core',
        sob.properties.Property(
            name="suplocCore",
            required=True,
            types=sob.types.MutableTypes([
                SupplierLocationCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_legacy',
        sob.properties.Property(
            name="suplocLegacy",
            types=sob.types.MutableTypes([
                SupplierLocationLegacy,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_general',
        sob.properties.Property(
            name="suplocGeneral",
            types=sob.types.MutableTypes([
                SupplierLocationGeneral,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_state',
        sob.properties.Property(
            name="suplocState",
            types=sob.types.MutableTypes([
                SupplierLocationState,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_status',
        sob.properties.Property(
            name="suplocStatus",
            types=sob.types.MutableTypes([
                SupplierLocationStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_address',
        sob.properties.Property(
            name="suplocAddress",
            types=sob.types.MutableTypes([
                SupplierLocationAddresses,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_contact',
        sob.properties.Property(
            name="suplocContact",
            types=sob.types.MutableTypes([
                SupplierLocationContacts,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_geography',
        sob.properties.Property(
            name="suplocGeography",
            types=sob.types.MutableTypes([
                SupplierLocationGeography,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_audit',
        sob.properties.Property(
            name="suplocAudit",
            types=sob.types.MutableTypes([
                SupplierLocationAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'suploc_entitlement',
        sob.properties.Property(
            name="suplocEntitlement",
            types=sob.types.MutableTypes([
                Entitlements,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    SupplierResponse
).properties = sob.meta.Properties([
    (
        'content',
        sob.properties.Property(
            types=sob.types.MutableTypes([
                SupplierResponseContent,
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
    SupplierResponseContent
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
                SupplierDataunits,
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
    SupplierDataunits
).properties = sob.meta.Properties([
    (
        'sup_core',
        sob.properties.Property(
            name="supCore",
            required=True,
            types=sob.types.MutableTypes([
                SupplierCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_legacy',
        sob.properties.Property(
            name="supLegacy",
            types=sob.types.MutableTypes([
                SupplierLegacy,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_state',
        sob.properties.Property(
            name="supState",
            types=sob.types.MutableTypes([
                SupplierState,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_status',
        sob.properties.Property(
            name="supStatus",
            types=sob.types.MutableTypes([
                SupplierStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_agent',
        sob.properties.Property(
            name="supAgent",
            types=sob.types.MutableTypes([
                SupplierAgent,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_agent_legacy',
        sob.properties.Property(
            name="supAgentLegacy",
            types=sob.types.MutableTypes([
                SupplierAgentLegacy,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_audit',
        sob.properties.Property(
            name="supAudit",
            types=sob.types.MutableTypes([
                SupplierAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'sup_entitlement',
        sob.properties.Property(
            name="supEntitlement",
            types=sob.types.MutableTypes([
                Entitlements,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    TestLabDataunits
).properties = sob.meta.Properties([
    (
        'perf_test_lab_core',
        sob.properties.Property(
            name="perfTestLabCore",
            required=True,
            types=sob.types.MutableTypes([
                PerformanceTestLabCore,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_general',
        sob.properties.Property(
            name="perfTestLabGeneral",
            types=sob.types.MutableTypes([
                PerformanceTestLabGeneral,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_state',
        sob.properties.Property(
            name="perfTestLabState",
            types=sob.types.MutableTypes([
                PerformanceTestLabState,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_status',
        sob.properties.Property(
            name="perfTestLabStatus",
            types=sob.types.MutableTypes([
                PerformanceTestLabStatus,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_address',
        sob.properties.Property(
            name="perfTestLabAddress",
            types=sob.types.MutableTypes([
                PerformanceTestLabAddress,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_contact',
        sob.properties.Property(
            name="perfTestLabContact",
            types=sob.types.MutableTypes([
                PerformanceTestLabContacts,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_audit',
        sob.properties.Property(
            name="perfTestLabAudit",
            types=sob.types.MutableTypes([
                PerformanceTestLabAudit,
                sob.utilities.types.Null
            ])
        )
    ),
    (
        'perf_test_lab_entitlement',
        sob.properties.Property(
            name="perfTestLabEntitlement",
            types=sob.types.MutableTypes([
                Entitlements,
                sob.utilities.types.Null
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialPerformanceTestLabsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSupplierLocationsGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSupplierLocationsGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSupplierLocationsObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSuppliersGetObjectId
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSuppliersGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    DataMaterialSuppliersObjectIdGetDataunits
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSecurityVendorAccessGroup
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifierReference  # noqa
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifierReference  # noqa
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationStatusIndicator
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationAddressType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetStateProvince
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetGeographicArea
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetCountry
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationContactRole
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationCountry
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetPortOfOriginCountry
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetLegacySupplierLocationCode
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifier  # noqa
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierReasonRetiredIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSupplierLocationsGetSupplierLocationFoundedYearNumber
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetSupplierStateIdentifierReference
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetAgentIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetLegacyAgentCode
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetDivisionCode
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetVendorOwnershipType
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetLegacySupplierCode
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.String(),
            sob.utilities.types.Null
        ])
    )
])
sob.meta.array_writable(  # type: ignore
    SearchMaterialSuppliersGetSupplierStateIdentifier
).item_types = sob.types.MutableTypes([
    sob.properties.Property(
        types=sob.types.MutableTypes([
            sob.properties.Integer(),
            sob.utilities.types.Null
        ])
    )
])
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/definitions/Entitlements": Entitlements,
    "#/definitions/Entitlements/properties/entitlements":
    EntitlementsEntitlements,
    "#/definitions/_error": Error,
    "#/definitions/_links": Links,
    "#/definitions/_reference": Reference,
    "#/definitions/materialPerformanceTestLabResponse":
    MaterialPerformanceTestLabResponse,
    "#/definitions/materialPerformanceTestLabResponse/properties/content":
    MaterialPerformanceTestLabResponseContent,
    "#/definitions/perfTestLabAddress": PerformanceTestLabAddress,
    "#/definitions/perfTestLabAudit": PerformanceTestLabAudit,
    "#/definitions/perfTestLabContact": PerformanceTestLabContacts,
    "#/definitions/perfTestLabContact/items": PerformanceTestLabContact,
    "#/definitions/perfTestLabCore": PerformanceTestLabCore,
    "#/definitions/perfTestLabGeneral": PerformanceTestLabGeneral,
    "#/definitions/perfTestLabState": PerformanceTestLabState,
    "#/definitions/perfTestLabStatus": PerformanceTestLabStatus,
    "#/definitions/relationshipResponse": RelationshipResponse,
    "#/definitions/relationshipResponse/properties/content":
    RelationshipResponseContents,
    "#/definitions/relationshipResponse/properties/content/items":
    RelationshipResponseContent,
    "#/definitions/searchResponse": SearchResponse,
    "#/definitions/searchResponse/properties/content": SearchResponseContents,
    "#/definitions/searchResponse/properties/content/items":
    SearchResponseContent,
    "#/definitions/supAgent": SupplierAgent,
    "#/definitions/supAgentLegacy": SupplierAgentLegacy,
    "#/definitions/supAudit": SupplierAudit,
    "#/definitions/supCore": SupplierCore,
    "#/definitions/supLegacy": SupplierLegacy,
    "#/definitions/supState": SupplierState,
    "#/definitions/supStatus": SupplierStatus,
    "#/definitions/suplocAddress": SupplierLocationAddresses,
    "#/definitions/suplocAddress/items": SupplierLocationAddress,
    "#/definitions/suplocAudit": SupplierLocationAudit,
    "#/definitions/suplocContact": SupplierLocationContacts,
    "#/definitions/suplocContact/items": SupplierLocationContact,
    "#/definitions/suplocCore": SupplierLocationCore,
    "#/definitions/suplocGeneral": SupplierLocationGeneral,
    "#/definitions/suplocGeography": SupplierLocationGeography,
    "#/definitions/suplocLegacy": SupplierLocationLegacy,
    "#/definitions/suplocState": SupplierLocationState,
    "#/definitions/suplocStatus": SupplierLocationStatus,
    "#/definitions/supplierBulkResponse": SupplierBulkResponse,
    "#/definitions/supplierBulkResponse/properties/content":
    SupplierBulkResponseContents,
    "#/definitions/supplierBulkResponse/properties/content/items":
    SupplierBulkResponseContent,
    "#/definitions/supplierLocationBulkResponse": SupplierLocationBulkResponse,
    "#/definitions/supplierLocationBulkResponse/properties/content":
    SupplierLocationBulkResponseContents,
    "#/definitions/supplierLocationBulkResponse/properties/content/items":
    SupplierLocationBulkResponseContent,
    "#/definitions/supplierLocationResponse": SupplierLocationResponse,
    "#/definitions/supplierLocationResponse/properties/content":
    SupplierLocationResponseContent,
    "#/definitions/supplierLocation_dataunits": SupplierLocationDataunits,
    "#/definitions/supplierResponse": SupplierResponse,
    "#/definitions/supplierResponse/properties/content":
    SupplierResponseContent,
    "#/definitions/supplier_dataunits": SupplierDataunits,
    "#/definitions/testLab_dataunits": TestLabDataunits,
    "#/paths/~1data~1materialPerformanceTestLabs~1{objectId}/get/parameters/1":
    DataMaterialPerformanceTestLabsObjectIdGetDataunits,
    "#/paths/~1data~1materialSupplierLocations/get/parameters/0":
    DataMaterialSupplierLocationsGetObjectId,
    "#/paths/~1data~1materialSupplierLocations/get/parameters/1":
    DataMaterialSupplierLocationsGetDataunits,
    "#/paths/~1data~1materialSupplierLocations~1{objectId}/get/parameters/1":
    DataMaterialSupplierLocationsObjectIdGetDataunits,
    "#/paths/~1data~1materialSuppliers/get/parameters/0":
    DataMaterialSuppliersGetObjectId,
    "#/paths/~1data~1materialSuppliers/get/parameters/1":
    DataMaterialSuppliersGetDataunits,
    "#/paths/~1data~1materialSuppliers~1{objectId}/get/parameters/1":
    DataMaterialSuppliersObjectIdGetDataunits,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/11":
    SearchMaterialSupplierLocationsGetSecurityVendorAccessGroup,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/13":
    SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifierReference,  # noqa
    "#/paths/~1search~1materialSupplierLocations/get/parameters/14":
    SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifier,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/15":
    SearchMaterialSupplierLocationsGetSupplierLocationStateIdentifierReference,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/16":
    SearchMaterialSupplierLocationsGetSupplierLocationStatusIndicator,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/18":
    SearchMaterialSupplierLocationsGetSupplierLocationAddressType,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/19":
    SearchMaterialSupplierLocationsGetStateProvince,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/20":
    SearchMaterialSupplierLocationsGetGeographicArea,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/21":
    SearchMaterialSupplierLocationsGetCountry,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/22":
    SearchMaterialSupplierLocationsGetSupplierLocationContactRole,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/23":
    SearchMaterialSupplierLocationsGetSupplierLocationCountry,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/24":
    SearchMaterialSupplierLocationsGetPortOfOriginCountry,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/5":
    SearchMaterialSupplierLocationsGetSupplierIdentifier,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/6":
    SearchMaterialSupplierLocationsGetLegacySupplierLocationCode,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/7":
    SearchMaterialSupplierLocationsGetResponsibleNikeLiaisonOfficeIdentifier,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/8":
    SearchMaterialSupplierLocationsGetSupplierReasonRetiredIdentifier,
    "#/paths/~1search~1materialSupplierLocations/get/parameters/9":
    SearchMaterialSupplierLocationsGetSupplierLocationFoundedYearNumber,
    "#/paths/~1search~1materialSuppliers/get/parameters/10":
    SearchMaterialSuppliersGetSupplierStateIdentifierReference,
    "#/paths/~1search~1materialSuppliers/get/parameters/12":
    SearchMaterialSuppliersGetAgentIdentifier,
    "#/paths/~1search~1materialSuppliers/get/parameters/13":
    SearchMaterialSuppliersGetLegacyAgentCode,
    "#/paths/~1search~1materialSuppliers/get/parameters/5":
    SearchMaterialSuppliersGetDivisionCode,
    "#/paths/~1search~1materialSuppliers/get/parameters/6":
    SearchMaterialSuppliersGetVendorOwnershipType,
    "#/paths/~1search~1materialSuppliers/get/parameters/8":
    SearchMaterialSuppliersGetLegacySupplierCode,
    "#/paths/~1search~1materialSuppliers/get/parameters/9":
    SearchMaterialSuppliersGetSupplierStateIdentifier,
}
