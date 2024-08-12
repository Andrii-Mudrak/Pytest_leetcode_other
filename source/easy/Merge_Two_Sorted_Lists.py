def merged_two_sorted_lists(list1,list2):
    result = []
    result.extend(list1)
    result.extend(list2)
    result.sort()

    print(result)

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    # list1 = []
    # list2 = []
    # list1 = []
    # list2 = [0]
    merged_two_sorted_lists(list1, list2)