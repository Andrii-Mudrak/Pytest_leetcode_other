def roman_to_integer(roman):
    '''
    https://leetcode.com/problems/roman-to-integer/description/
    Given a roman numeral, convert it to an integer.
   '''
    s = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for item in range(len(roman)):
        if item < len(roman)-1 and s[roman[item]] < s[roman[item + 1]]:
            result -= s[roman[item]]
        else:
            result += s[roman[item]]
    return result


def sort_jumbled(mapping, nums):
    '''
    https://leetcode.com/problems/sort-the-jumbled-numbers/description/
    Sort the Jumbled Numbers
    '''
    result,actualresult = {}, []
    temp = ''
    for num in nums:
        for index in str(num):
            temp += str(mapping[int(index)])
        result[temp] = num
        temp = ''
    sortDict = sorted(result)
    for item in sortDict:
        actualresult.append(result[item])
    return actualresult