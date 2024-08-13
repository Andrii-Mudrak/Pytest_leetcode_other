from source.easy.leetcode_easy import *
import pytest


@pytest.mark.parametrize("s, expected_result",[
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6)
])
def test_length_last_word_positive(s, expected_result):
    result = lengthLastWord(s)
    assert result == expected_result


@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("s, expected_result",[
    ("Hello World", 4),
    ("   fly me   to   the moon  ", 2),
    ("luffy is still joyboy", 1)
])
def test_length_last_word_negative(s, expected_result):
    result = lengthLastWord(s)
    assert result == expected_result


@pytest.mark.wip
@pytest.mark.parametrize("strs, expected_result",[
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], "")
    ])
def test_longest_common_prefix_positive(strs, expected_result):
    result = longest_common_prefix(strs)
    assert result == expected_result


@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("strs, expected_result",[
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], "")
    ])
def test_longest_common_prefix_negative(strs, expected_result):
    result = longest_common_prefix(strs)
    assert result != expected_result


@pytest.mark.parametrize("list1, list2, expected_result",[
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], [])
])
def test_merge_two_sorted_lists_positive(list1, list2, expected_result):
    result = merged_two_sorted_lists(list1, list2)
    assert result == expected_result


@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("list1, list2, expected_result",[
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], [])
])
def test_merge_two_sorted_lists_negative(list1, list2, expected_result):
    result = merged_two_sorted_lists(list1, list2)
    assert result != expected_result