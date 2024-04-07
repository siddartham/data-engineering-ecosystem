import functools
from inspect import Parameter, Signature, signature
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)

from .config import CERBERUS_URL
from .get import get_secret

__all__: List[str] = [
    "apply_cerberus_path_arguments",
]
lru_cache: Callable[..., Any] = functools.lru_cache


def _merge_function_signature_args_kwargs(
    function_signature: Signature, args: Iterable[Any], kwargs: Dict[str, Any]
) -> None:
    """
    This function merges positional/keyword arguments for a function
    into the keyword argument dictionary
    """
    value: Any
    parameter: Parameter
    if args:
        for parameter, value in zip(
            function_signature.parameters.values(), args
        ):
            assert parameter.kind == Parameter.POSITIONAL_OR_KEYWORD
            kwargs[parameter.name] = value


def _remove_function_signature_inapplicable_kwargs(
    function_signature: Signature, kwargs: Dict[str, Any]
) -> None:
    def get_parameter_name(parameter_: Parameter) -> str:
        return parameter_.name

    key: str
    for key in set(kwargs.keys()) - set(
        map(
            get_parameter_name,
            function_signature.parameters.values(),
        )
    ):
        del kwargs[key]


def _get_function_signature_parameter_value_or_default(
    function_signature: Signature,
    parameter_name: str,
    kwargs: Dict[str, Any],
    default: Any,
) -> Any:
    value: Any = default
    if parameter_name and (parameter_name in kwargs):
        value = kwargs[parameter_name] or default
    elif parameter_name in function_signature.parameters:
        value = (
            function_signature.parameters[parameter_name].default or default
        )
    return value


def apply_cerberus_path_arguments(
    cerberus_path_parameter_names: Union[
        Mapping[str, str], Iterable[Tuple[str, str]]
    ] = (),
    cerberus_url_parameter_name: str = "",
    cerberus_arn_parameter_name: str = "",
    **kwargs: str,
) -> Callable[..., Callable[..., Any]]:
    """
    This decorator maps parameter names. Each key represents the
    name of a parameter in the decorated function which accepts an explicit
    input, and the corresponding mapped value is the name of a second parameter
    which accepts a cerberus path from where a value for the first parameter
    can be retrieved when not explicitly provided.

    Parameters:
    - cerberus_path_parameter_names ({str: str}|[(str, str)]):
      A mapping of parameter names to Cerberus path parameter names.
    - ** (str): All additional keyword map a
    - cerberus_url_parameter_name (str) = "":
      The name of the Cerberus API URL parameter
    - cerberus_arn_parameter_name (str) = "": The name of the
      parameter holding the Amazon Resource Name to assume when retrieving
      Cerberus secrets. If this argument is not provided to the decorated
      function, the environment variable AWS_ROLE_ARN will also be checked.
    - ** (str): Synonymous with `cerberus_path_parameter_names`. When
      both `cerberus_path_parameter_names` is provided *and* `**kwargs`
      are provided, `cerberus_path_parameter_names` is updated from
      `**kwargs` in order to merge the two.
    """
    cerberus_path_parameter_names_: Dict[str, str] = dict(
        cerberus_path_parameter_names
    )
    cerberus_path_parameter_names_.update(**kwargs)

    def decorating_function(
        function: Callable[..., Any]
    ) -> Callable[..., Any]:
        function_signature: Signature = signature(function)

        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            This function wraps the original and performs lookups for
            any parameters for which an argument is not passed
            """
            # First we consolidate the keyword arguments with any arguments
            # which are passed to parameters which can be either positional
            # *or* keyword arguments, and were passed as positional arguments
            _merge_function_signature_args_kwargs(
                function_signature, args, kwargs
            )
            # Determine the Cerberus API URL
            url: str = _get_function_signature_parameter_value_or_default(
                function_signature,
                cerberus_url_parameter_name,
                kwargs,
                CERBERUS_URL,
            )
            # Determine the ARN to assume (if any)
            arn: str = _get_function_signature_parameter_value_or_default(
                function_signature, cerberus_arn_parameter_name, kwargs, ""
            )
            # For any arguments where we have a cerberus path and do not have
            # an explicitly passed value, perform a lookup in cerberus
            key: str
            for key in set(cerberus_path_parameter_names_.keys()) - set(
                kwargs.keys()
            ):
                cerberus_path_key: str = cerberus_path_parameter_names_[key]
                if (cerberus_path_key in kwargs) and kwargs[cerberus_path_key]:
                    kwargs[key] = get_secret(
                        kwargs[cerberus_path_key],
                        url=url,
                        arn=arn,
                    )
                elif cerberus_path_key in function_signature.parameters:
                    default: Optional[str] = function_signature.parameters[
                        cerberus_path_key
                    ].default
                    if default:
                        kwargs[key] = get_secret(
                            default,
                            url=url,
                            arn=arn,
                        )
            # Remove arguments which do not correspond to
            # any of the function's parameter names
            _remove_function_signature_inapplicable_kwargs(
                function_signature, kwargs
            )
            # Execute the wrapped function
            return function(**kwargs)

        return wrapper

    return decorating_function
