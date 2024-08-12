def searchInsert(nums,target):
    result = 0
    for item in nums:
        print("....", item, result)
        if item > target:
            result = nums.index(item) -1
            print(item, result)
        elif item == target:
            result = nums.index(item)
    if result == 0:
        print(len(nums))
    else:
        print(result)


if __name__ == "__main__":
    nums, target = [1,3,5,6], 5
    # nums, target = [1,3,5,6], 2
    # nums, target = [1,3,5,6], 7
    searchInsert(nums,target)