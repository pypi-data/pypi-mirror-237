import pytest
from codesnipper.utils import validate_type


@pytest.mark.parametrize(
    "value, types",
    [
        ("h", [str, int, list]),
        (None, [str, None, list]),
        (1, [int]),
    ],
)
def test_validate_type(value, types):
    assert validate_type(value, *types) == value


def test_validate_type_error():
    with pytest.raises(AssertionError):
        validate_type("i", int)
