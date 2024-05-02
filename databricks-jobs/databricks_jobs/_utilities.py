import functools
from copy import deepcopy
from inspect import Parameter, Signature, signature
from typing import Any, Callable, Dict, Iterable, List, Tuple


def as_tuple(
    user_function: Callable[..., Iterable[Any]]
) -> Callable[..., Tuple[Any, ...]]:
    """
    This is a decorator which will return an iterable as a tuple.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, ...]:
        return tuple(user_function(*args, **kwargs) or ())

    return functools.update_wrapper(wrapper, user_function)


def as_list(
    user_function: Callable[..., Iterable[Any]]
) -> Callable[..., List[Any]]:
    """
    This is a decorator which will return an iterable as a list.
    """

    def wrapper(*args: Any, **kwargs: Any) -> List[Any]:
        return list(user_function(*args, **kwargs) or ())

    return functools.update_wrapper(wrapper, user_function)


def _item_value_is_not_none(item: Tuple[str, Any]) -> bool:
    """
    This function returns the last item in a sequence.
    """
    return item[1] is not None


def apply_defaults(**defaults: Any) -> Callable[..., Callable[..., Any]]:
    """
    This is decorator to apply default values to a function
    """

    def decorating_function(
        user_function: Callable[..., Any]
    ) -> Callable[..., List[Any]]:
        """
        This is a decorator which will apply default values
        to a function
        """
        function_signature: Signature = signature(user_function)

        def wrapper(*args: Any, **kwargs: Any) -> List[Any]:
            """
            This function wraps the original and applies defaults for
            any parameters for which an argument is not passed
            """
            key: str
            value: Any
            # Pass the arguments and keyword arguments provided to the
            # condition function to determine if we should apply these
            # defaults
            defaults_or_kwargs: Dict[str, Any] = deepcopy(defaults)
            # First we get any arguments which are passed to parameters
            # which can be either positional *or* keyword arguments,
            # and were passed as positional arguments
            parameter: Parameter
            if args:
                for parameter, value in zip(
                    function_signature.parameters.values(), args
                ):
                    assert parameter.kind == Parameter.POSITIONAL_OR_KEYWORD
                    if value or (parameter.name not in defaults_or_kwargs):
                        defaults_or_kwargs[parameter.name] = value
            defaults_or_kwargs.update(
                **{
                    key: value
                    for key, value in filter(
                        _item_value_is_not_none, kwargs.items()
                    )
                }
            )
            # Remove arguments which do not correspond to
            # any of the function's parameter names

            def get_parameter_name(parameter_: Parameter) -> str:
                return parameter_.name

            for key in set(defaults_or_kwargs.keys()) - set(
                map(
                    get_parameter_name,
                    function_signature.parameters.values(),
                )
            ):
                del defaults_or_kwargs[key]
            # Execute the wrapped function
            return user_function(**defaults_or_kwargs)

        return functools.update_wrapper(wrapper, user_function)

    return decorating_function
