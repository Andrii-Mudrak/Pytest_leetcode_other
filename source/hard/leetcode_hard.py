import itertools

def longest_valid_parentheses(s):
    '''
    https://leetcode.com/problems/longest-valid-parentheses/description/
    Return the length of the longest valid (well-formed) parentheses
    '''
    k = dict(enumerate(s))
    counter = 0
    for key,value in k.items():
        if value == '(' and k[key + 1] == ')':
            counter +=1
    if counter != 0:
        return counter * 2
    else:
        return None

def merge_k_lists(lists):
    '''
    https://leetcode.com/problems/merge-k-sorted-lists/description/
    Merge all the linked-lists into one sorted linked-list and return it.
    '''
    merged = []
    for item in lists:
        for num in item:
            merged.append(num)
    merged.sort()
    return merged

def find_substring(s,words):
    '''
    https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
    Substring with Concatenation of All Words
    '''
    combinations, final_result = [], []
    result = itertools.product(words, repeat=len(words))
    for item in result:
        sub_list = list(item)
        sub_list.sort()
        sub_words = words
        sub_words.sort()
        if sub_list == sub_words:
            results = ''
            for ch in item:
                results += ch
            combinations.append(results)
    for item in combinations:
        if item in s:
            index =s.index(item)
            final_result.append(index)
    final_result.sort()
    return final_result