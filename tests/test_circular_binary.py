import pytest

from src.circular_binary import has_four_consecutive_ones_circular


@pytest.mark.parametrize(
    "binary, expected",
    [
        ("1010111", True),
        ("1111000", True),
        ("0001111", True),
        ("0111100", True),
        ("1111111", True),
        ("1010101", False),
        ("0000000", False),
        ("1100110", False),
        ("1000001", False),
    ],
)
def test_has_four_consecutive_ones_circular(binary, expected):
    assert has_four_consecutive_ones_circular(binary) == expected


@pytest.mark.parametrize(
    "binary",
    [
        "10101",
        "10101010",
        "",
    ],
)
def test_invalid_length_raises_value_error(binary):
    with pytest.raises(ValueError):
        has_four_consecutive_ones_circular(binary)


def test_non_binary_input_raises_value_error():
    with pytest.raises(ValueError):
        has_four_consecutive_ones_circular("10101A1")
