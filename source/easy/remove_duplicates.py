def remove_duplicates(nums):
    set(nums)
    k = len(set(nums))
    print(k, set(nums))

def removeElement(nums, val):
    for item in nums[:]:
        if item == val:
            nums.remove(item)
    result = len(nums)
    return result



# if __name__ == "__main__":
    # nums = [1,1,2]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    # remove_duplicates(nums)
    #
    # # nums, val = [3,2,2,3], 3
    # nums, val = [0,1,2,2,3,0,4,2], 2
    # removeElement(nums, val)
