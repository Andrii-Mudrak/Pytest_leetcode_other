class Solution:
    def twoSum(self, nums, target):
        pair_idx = {}
        for i, num in enumerate(nums):
            # print(pair_idx)
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
        print(reminder,number,reverse_num)

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


if __name__ == "__main__":
    a = Solution
    print("======================================")
    k = a.twoSum(Solution, [2,7,11,15], 9)
    print(k)
    print("======================================")
    k = a.twoSum(Solution,[3,2,4], 6)
    print(k)
    print("======================================")
    k = a.twoSum(Solution, [3,3], 6)
    print(k)

    palindrome(12321)