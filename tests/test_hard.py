from symbol import parameters

import pytest
from source.hard.leetcode_hard import *


@pytest.mark.parametrize("s, expected_result", [
    ("(()", 2),
    (")()())", 4),
    ("", None)
])
def test_longest_valid_parentheses(s, expected_result):
    result = longest_valid_parentheses(s)
    assert result == expected_result


@pytest.mark. parametrize("lists, expected_result", [
    ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
    ([], []),
    ([[]], [])
])
def test_merge_k_sorted_lists_positive(lists, expected_result):
    result = merge_k_lists(lists)
    assert result == expected_result


@pytest.mark.parametrize("s, words,expected_result", [
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12])
])
def test_substring_with_concatenation_of_all_words_positive(s, words, expected_result):
    result = find_substring(s,words)
    assert result == expected_result