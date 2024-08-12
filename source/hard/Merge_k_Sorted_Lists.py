def mergeKLists(lists):
    merged = []
    for item in lists:
        for num in item:
            merged.append(num)
    merged.sort()
    print(merged)



if __name__ == "__main__":
    lists =[[1,4,5],[1,3,4],[2,6]]
    # lists = [[]]
    mergeKLists(lists)