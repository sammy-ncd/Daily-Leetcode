"""

Problem:
https://leetcode.com/problems/encode-and-decode-strings/description/


"""


"""

Approach:
get ascii values for each char, split chars by delimiter ','
split words but another delimiter '#'


"""


def encode(strs):
    # _,_,_,_,#_,_,_#
    encoding = ""
    for s in strs:
        for c in s:
            encoding += str(ord(c)) + ','
        encoding += '#'
    return encoding

def decode(s):
    res = []
    currWord = ""
    currLetter = ""
    for ch in s:
        if ch == ',':
            currWord += chr(int(currLetter))
            currLetter = ""
        elif ch == '#':
            res.append(currWord)
            currWord = ""
        else:
            currLetter += ch
    return res


"""
let n = total length of all strings

Time complexity:

encode ---> O(n)

decode ---> O(n)

"""