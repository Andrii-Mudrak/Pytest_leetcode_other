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


# @pytest.mark.wip
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


@pytest.mark.parametrize("nums, target, expected_result", [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7, 4)
])
def test_search_insert_positive(nums, target, expected_result):
    result = search_insert(nums,target)
    assert result == expected_result


@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("nums, target, expected_result", [
    ([1,3,5,6], 5, 1),
    ([1,3,5,6], 2, 2),
    ([1,3,5,6], 7, 3)
])
def test_search_insert_negative(nums, target, expected_result):
    result = search_insert(nums,target)
    assert result == expected_result

@pytest.mark.parametrize("nums, len, expected_result", [
    ([1,1,2], 2 , [1,2]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4])
])
def test_remove_duplicates_positive(nums, len, expected_result):
    lenght,result = remove_duplicates(nums)
    assert lenght == len and result == expected_result

@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("nums, len, expected_result", [
    ([1,1,2], 2 , [1,3]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,5])
])
def test_remove_duplicates_negative(nums, len, expected_result):
    lenght,result = remove_duplicates(nums)
    assert lenght == len and result == expected_result


@pytest.mark.parametrize("nums, val, expected_val, expected_nums ", [
    ([3,2,2,3], 3, 2, [2,2]),
    ([0,1,2,2,3,0,4,2], 2, 5, [0, 1, 3, 0, 4])
])
def test_remove_elements_positive(nums, val, expected_val, expected_nums):
    new_val, new_nums = remove_element(nums,val)
    assert new_val == expected_val and new_nums == expected_nums


@pytest.mark.xfail(reason="Negative")
@pytest.mark.parametrize("nums, val, expected_val, expected_nums ", [
    ([3,2,2,3], 3, 2, [2,2]),
    ([0,1,2,2,3,0,4,2], 2, 5, [0, 1, 3, 0, 4])
])
def test_remove_elements_negative(nums, val, expected_val, expected_nums):
    new_val, new_nums = remove_element(nums,val)
    assert new_val == expected_val and new_nums == expected_nums