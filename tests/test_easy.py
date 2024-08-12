from source.easy.leetcode_easy import *
import pytest


@pytest.mark.parametrize("s, expected_result",[
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6)
])
def test_length_Last_Word_positive(s, expected_result):
    result = lengthLastWord(s)
    assert result == expected_result


@pytest.mark.xfail(reason="negative")
@pytest.mark.parametrize("s, expected_result",[
    ("Hello World", 4),
    ("   fly me   to   the moon  ", 2),
    ("luffy is still joyboy", 1)
])
def test_length_Last_Word_negative(s, expected_result):
    result = lengthLastWord(s)
    assert result == expected_result