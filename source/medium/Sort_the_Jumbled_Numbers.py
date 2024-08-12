def sortJumbled(mapping, nums):
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
    print(nums, actualresult)


if __name__ == "__main__":
    mapping = [8,9,4,0,2,1,3,5,7,6]; nums = [991,338,38]
    # mapping = [0,1,2,3,4,5,6,7,8,9]; nums = [789,456,123]
    sortJumbled(mapping,nums)