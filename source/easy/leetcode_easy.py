def lengthLastWord(s):
    """
    https://leetcode.com/problems/length-of-last-word/description/
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    """
    return len(s.split()[-1])

def longest_common_prefix(strs):
    '''
    https://leetcode.com/problems/longest-common-prefix/description/
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    '''
    shortest = strs[0]
    temp = set()
# find a least word
    for item in strs[1:]:
        if len(item) < len(shortest):
            shortest = item
    prf = shortest[0]
# sort through the list based on the smallest word
    for item in shortest:
        idx =  shortest.index(item)
        for content in strs:
            temp.add(content[idx])
        if len(prf) != len(temp):
            if len(prf) != 1:
                return prf[1:]
                break
            else:
                return ""
                break
        prf += item

def merged_two_sorted_lists(list1,list2):
    '''
    https://leetcode.com/problems/merge-two-sorted-lists/description/
    Merge the two lists into one sorted list. The list should be made by
    splicing together the nodes of the first two lists.
    '''
    result = []
    result.extend(list1)
    result.extend(list2)
    result.sort()
    return result

def search_insert(nums,target):
    '''
    https://leetcode.com/problems/search-insert-position/description/
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the
    index where it would be if it were inserted in order.
    '''
    new_nums = nums
    number = int(len(new_nums)/2)
    while number !=0:
        if target <= new_nums[number-1]:
            # move left
            new_nums = new_nums[0:number]
        else:
            # move right
            new_nums = new_nums[number:]
        if number == 2:
            result = None
            if target > new_nums[1]:
                result = nums.index(new_nums[1]) + 1
            elif target == new_nums[0]:
                result = nums.index(new_nums[0])
            elif target < new_nums[1]:
                result = nums.index(new_nums[1])
            return result
            break
        number = int(len(new_nums)/2)
        print(number)

def remove_duplicates(nums):
    '''
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    Given an integer array nums sorted in non-decreasing order, remove the duplicates
    in-place such that each unique element appears only once. The relative order of
    the elements should be kept the same. Then return the number of unique elements in nums.
    '''
    nums = list(set(nums))
    k = len(nums)
    return k, nums

def remove_element(nums, val):
    '''
    https://leetcode.com/problems/remove-element/description/
    Given an integer array nums and an integer val, remove all
    occurrences of val in nums in-place. The order of the elements
    may be changed. Then return the number of elements in nums
    which are not equal to val.
    '''
    for item in nums[:]:
        if item == val:
            nums.remove(item)
    result = len(nums)
    return result, nums