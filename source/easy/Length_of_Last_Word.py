def lengthLastWord(s):
    '''
    https://leetcode.com/problems/length-of-last-word/description/
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    '''
    print(len(s.split()[-1]))


if __name__ == "__main__":
    # s = "Hello World"
    # s = "   fly me   to   the moon  "
    s = "luffy is still joyboy"
    lengthLastWord(s)