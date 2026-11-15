import pytest

from src.longest_substring import longest_unique_substring


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("aaaaaa", 1),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("ABCABCFKAB", 5),
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
    ],
)
def test_longest_unique_substring(input_string, expected):
    assert longest_unique_substring(input_string) == expected
