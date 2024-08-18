import pytest
from source.medium.leetcode_medium import *


@pytest.mark.parametrize("roman, expected_result", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
])
def test_roman_to_integer_positive(roman, expected_result):
    result = roman_to_integer(roman)
    assert result == expected_result


@pytest.mark.parametrize("mapping, nums, expected_result",[
    ([8,9,4,0,2,1,3,5,7,6], [991,338,38],  [338, 38, 991]),
    ([0,1,2,3,4,5,6,7,8,9], [789,456,123], [123, 456, 789])
])
def test_sort_the_jumbled_numbers_positive(mapping,nums,expected_result):
    result = sort_jumbled(mapping,nums)
    assert result == expected_result
