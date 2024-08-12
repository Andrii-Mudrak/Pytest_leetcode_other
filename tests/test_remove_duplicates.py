import pytest
from source.easy.remove_duplicates import *

@pytest.mark.parametrize("nums, val, expected", [([0,1,2,2,3,0,4,2], 2, 5)])
def test_remove_duplicates_positive(nums, val, expected):
    result = removeElement(nums, val)
    assert result == expected


@pytest.mark.parametrize("nums, val, expected", [([0,1,2,2,3,0,4,2], 2, 5)])
def test_remove_duplicates_negative(nums, val, expected):
    result = removeElement(nums, val)
    assert result == expected