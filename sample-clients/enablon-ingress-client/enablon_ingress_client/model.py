import typing

import sob


class Authentication(sob.model.Object):
    """
    Authentication Credentials

    Properties:

    - userid
    - password
    - siteid
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        userid: typing.Optional[
            str
        ] = None,
        password: typing.Optional[
            str
        ] = None,
        siteid: typing.Optional[
            str
        ] = None
    ) -> None:
        self.userid = userid
        self.password = password
        self.siteid = siteid
        super().__init__(_data)


class Params(sob.model.Object):
    """
    Parameters sent to API to locate Indicator in Enablon

    Properties:

    - s_entity_code
    - n_calendar_year
    - n_calendar_month
    - n_calendar_day
    - an_indicators_ref:
      All of the array type fields must be of same length
    - an_indicators_values:
      All the arrays must be of same length. Provide value of the corresponding
      indicator
    - an_indicators_uom:
      All the arrays must be of same length. Provide an empty string, for the
      corresponding indicator, in case of no UOM
    - an_indicators_comments:
      All the arrays must be of same length. Provide an empty string, for the
      corresponding indicator, in case of no Comment
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        s_entity_code: typing.Optional[
            str
        ] = None,
        n_calendar_year: typing.Optional[
            int
        ] = None,
        n_calendar_month: typing.Optional[
            int
        ] = None,
        n_calendar_day: typing.Optional[
            int
        ] = None,
        an_indicators_ref: typing.Optional[
            "ParamsAnIndicatorsRef"
        ] = None,
        an_indicators_values: typing.Optional[
            "ParamsAnIndicatorsValues"
        ] = None,
        an_indicators_uom: typing.Optional[
            "ParamsAnIndicatorsUOM"
        ] = None,
        an_indicators_comments: typing.Optional[
            "ParamsAnIndicatorsComments"
        ] = None
    ) -> None:
        self.s_entity_code = s_entity_code
        self.n_calendar_year = n_calendar_year
        self.n_calendar_month = n_calendar_month
        self.n_calendar_day = n_calendar_day
        self.an_indicators_ref = an_indicators_ref
        self.an_indicators_values = an_indicators_values
        self.an_indicators_uom = an_indicators_uom
        self.an_indicators_comments = an_indicators_comments
        super().__init__(_data)


class ParamsAnIndicatorsComments(sob.model.Array):
    """
    All the arrays must be of same length. Provide an empty string, for the
    corresponding indicator, in case of no Comment
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


class ParamsAnIndicatorsRef(sob.model.Array):
    """
    All of the array type fields must be of same length
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


class ParamsAnIndicatorsUOM(sob.model.Array):
    """
    All the arrays must be of same length. Provide an empty string, for the
    corresponding indicator, in case of no UOM
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


class ParamsAnIndicatorsValues(sob.model.Array):
    """
    All the arrays must be of same length. Provide value of the corresponding
    indicator
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


class UpdateIndicatorValueRequest(sob.model.Object):
    """
    Body sent to update indicator values

    Properties:

    - fct_name:
      The table in Enablon where this activity is recorded
    - params:
      Parameters sent to API to locate Indicator in Enablon
    - authentication:
      Authentication Credentials
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
                    str,
                    sob.abc.MarshallableTypes
                ]
            ],
            sob.abc.Readable,
            str,
            bytes,
            None,
        ] = None,
        fct_name: typing.Optional[
            str
        ] = None,
        params: typing.Optional[
            "Params"
        ] = None,
        authentication: typing.Optional[
            "Authentication"
        ] = None
    ) -> None:
        self.fct_name = fct_name
        self.params = params
        self.authentication = authentication
        super().__init__(_data)


class UpdateIndicatorValueResponse(sob.model.Object):
    """
    Properties:

    - status:
      Indicates the result of the execution of the function. Its value is
      either OK or KO
    - login:
      Determine if there is a session connected with the server. 0: you are not
      connected. If you there is an error of connection you can see the
      loginErrNum:0: unknown error
       1: login or password is wrong
       2: login/password are ok but your password is expired. You need to
       change this. Actually, you can only connect to the web solution to
       change it.
      1: you are connected.
    - login_err_num:
      An optional parameter. It contains the number result
    - error:
      Defined only if status is KO, contains the error that prevented the
      Nabsic function to be executed
    - data:
      Defined only if the status is OK, contains the result of the Nabsic
      function. It can be null, a scalar (number, boolean, string), an array, a
      hash table.
    """

    def __init__(
        self,
        _data: typing.Union[
            sob.abc.Dictionary,
            typing.Mapping[
                str,
                sob.abc.MarshallableTypes
            ],
            typing.Iterable[
                typing.Tuple[
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
        ] = None,
        login: typing.Optional[
            int
        ] = None,
        login_err_num: typing.Optional[
            int
        ] = None,
        error: typing.Optional[
            str
        ] = None,
        data: typing.Optional[
            str
        ] = None
    ) -> None:
        self.status = status
        self.login = login
        self.login_err_num = login_err_num
        self.error = error
        self.data = data
        super().__init__(_data)


sob.meta.object_writable(  # type: ignore
    Authentication
).properties = sob.meta.Properties([
    (
        'userid',
        sob.properties.String(
            required=True
        )
    ),
    (
        'password',
        sob.properties.String(
            required=True
        )
    ),
    ('siteid', sob.properties.String())
])
sob.meta.object_writable(  # type: ignore
    Params
).properties = sob.meta.Properties([
    (
        's_entity_code',
        sob.properties.String(
            name="sEntityCode",
            required=True
        )
    ),
    (
        'n_calendar_year',
        sob.properties.Integer(
            name="nCalendarYear",
            required=True
        )
    ),
    (
        'n_calendar_month',
        sob.properties.Enumerated(
            name="nCalendarMonth",
            required=True,
            types=sob.types.Types([
                int
            ]),
            values={
                1,
                10,
                11,
                12,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            }
        )
    ),
    (
        'n_calendar_day',
        sob.properties.Enumerated(
            name="nCalendarDay",
            required=True,
            types=sob.types.Types([
                int
            ]),
            values={
                1
            }
        )
    ),
    (
        'an_indicators_ref',
        sob.properties.Property(
            name="anIndicatorsRef",
            required=True,
            types=sob.types.MutableTypes([
                ParamsAnIndicatorsRef
            ])
        )
    ),
    (
        'an_indicators_values',
        sob.properties.Property(
            name="anIndicatorsValues",
            required=True,
            types=sob.types.MutableTypes([
                ParamsAnIndicatorsValues
            ])
        )
    ),
    (
        'an_indicators_uom',
        sob.properties.Property(
            name="anIndicatorsUOM",
            required=True,
            types=sob.types.MutableTypes([
                ParamsAnIndicatorsUOM
            ])
        )
    ),
    (
        'an_indicators_comments',
        sob.properties.Property(
            name="anIndicatorsComments",
            types=sob.types.MutableTypes([
                ParamsAnIndicatorsComments
            ])
        )
    )
])
sob.meta.array_writable(  # type: ignore
    ParamsAnIndicatorsComments
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ParamsAnIndicatorsRef
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ParamsAnIndicatorsUOM
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.array_writable(  # type: ignore
    ParamsAnIndicatorsValues
).item_types = sob.types.MutableTypes([
    sob.properties.String()
])
sob.meta.object_writable(  # type: ignore
    UpdateIndicatorValueRequest
).properties = sob.meta.Properties([
    (
        'fct_name',
        sob.properties.Enumerated(
            required=True,
            types=sob.types.Types([
                str
            ]),
            values={
                "CS_ImportMetricsData"
            }
        )
    ),
    (
        'params',
        sob.properties.Property(
            required=True,
            types=sob.types.MutableTypes([
                Params
            ])
        )
    ),
    (
        'authentication',
        sob.properties.Property(
            required=True,
            types=sob.types.MutableTypes([
                Authentication
            ])
        )
    )
])
sob.meta.object_writable(  # type: ignore
    UpdateIndicatorValueResponse
).properties = sob.meta.Properties([
    (
        'status',
        sob.properties.Enumerated(
            required=True,
            types=sob.types.Types([
                str
            ]),
            values={
                "KO",
                "OK"
            }
        )
    ),
    (
        'login',
        sob.properties.Enumerated(
            required=True,
            types=sob.types.Types([
                int
            ]),
            values={
                0,
                1,
                2
            }
        )
    ),
    (
        'login_err_num',
        sob.properties.Enumerated(
            name="loginErrNum",
            types=sob.types.Types([
                int
            ]),
            values={
                1
            }
        )
    ),
    ('error', sob.properties.String()),
    ('data', sob.properties.String())
])
# The following is used to retain class names when re-generating
# this model from an updated OpenAPI document
_POINTERS_CLASSES: typing.Dict[str, typing.Type[sob.abc.Model]] = {
    "#/components/schemas/authentication": Authentication,
    "#/components/schemas/params": Params,
    "#/components/schemas/params/properties/anIndicatorsComments":
    ParamsAnIndicatorsComments,
    "#/components/schemas/params/properties/anIndicatorsRef":
    ParamsAnIndicatorsRef,
    "#/components/schemas/params/properties/anIndicatorsUOM":
    ParamsAnIndicatorsUOM,
    "#/components/schemas/params/properties/anIndicatorsValues":
    ParamsAnIndicatorsValues,
    "#/components/schemas/update-indicator-value-request":
    UpdateIndicatorValueRequest,
    "#/components/schemas/update-indicator-value-response":
    UpdateIndicatorValueResponse,
}
