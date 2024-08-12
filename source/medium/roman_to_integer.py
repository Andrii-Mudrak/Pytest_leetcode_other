def roman_to_integer(roman):
    s = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for item in range(len(roman)):
        # print(item, s[roman[item]],s[roman[item + 1]])
        if item < len(roman)-1 and s[roman[item]] < s[roman[item + 1]]:
            result -= s[roman[item]]
        else:
            result += s[roman[item]]

    print(result)





if __name__ == "__main__":
    # s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    # s = "III"
    # s = "LVIII"
    s = "MCMXCIV"
    roman_to_integer(s)