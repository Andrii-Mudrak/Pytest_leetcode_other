import itertools

def findSubstring(s,words):
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
    print(final_result)




if __name__ == "__main__":
    s, words = "barfoothefoobarman", ["foo","bar"]
    # s, words = "wordgoodgoodgoodbestword", ["word","good","best","word"]
    # s, words = "barfoofoobarthefoobarman", ["bar","foo","the"]
    findSubstring(s, words)