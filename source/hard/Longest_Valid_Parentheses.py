def longestValidParentheses(s):
    k = dict(enumerate(s))
    counter = 0
    for key,value in k.items():
        if value == '(' and k[key + 1] == ')':
            counter +=1

    if counter != 0:
        print(counter * 2)
    else:
        print("None")

if __name__ == "__main__":
    # s = "(()"
    # s = ")()())"
    s = ""
    longestValidParentheses(s)