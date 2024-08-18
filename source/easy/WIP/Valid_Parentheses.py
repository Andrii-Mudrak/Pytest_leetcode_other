def isValid(s):
    right_way = ['()','{}','[]']
    stack = []
    for item in s:
        stack.append(item)
        print(item)
        if len(stack) > 1:
            stack_1 = "".join(stack)
            if stack_1 not in right_way:
                idx = 0
            else:
                idx = 1
                stack.clear()
    if idx == 1:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    # s = "()"
    # s = "()[]{}"
    s = "(](){}"
    isValid(s)