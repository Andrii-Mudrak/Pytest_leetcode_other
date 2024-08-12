def longestCommonPrefix(strs):
    shortest = strs[0]
    prf = ""
    temp = set()
# шукаю найменше слово
    for item in strs[1:]:
        if len(item) < len(shortest):
            shortest = item
    prf = shortest[0]
# перебираю список взявши за основу найменше слово
    for item in shortest:
        idx =  shortest.index(item)
        for content in strs:
            temp.add(content[idx])
        if len(prf) != len(temp):
            if len(prf) != 1:
                print(prf[1:])
                break
            else:
                print("no such preffics")
                break
        prf += item




if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    # strs = ["dog","racecar","car"]
    longestCommonPrefix(strs)
