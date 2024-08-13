def lengthLastWord(s):
    '''
    https://leetcode.com/problems/length-of-last-word/description/
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    '''
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