from typing import Any


def validate_type(value: Any, *args) -> Any:
    """validates the type of value

    Args:
        value: value to check for
        args: list of allowed types for the value

    Returns:
        same value if type is correct, otherwise raises an assertion error
    """
    value_type = type(value)
    type_checks = []
    for arg in args:
        if arg is None:
            check = value is None
        else:
            check = value_type == arg
        type_checks.append(check)
    assert any(
        type_checks
    ), f"{value} has incorrect type {value_type}. It should be one of {args} type."
    return value
