'''

Problem:
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-05-13


'''


"""

Approach:
Set a flag once we have seen a 0 and if that flag is true
and we found another one return false, otherwise true


"""


def checkOnesSegment(s):

    seen_zero = False

    for c in s:
        if c == '0':
            seen_zero = True
        
        if seen_zero and c == '1':
            return False
        
    return True


print(checkOnesSegment("1001"))
print(checkOnesSegment("110"))


"""

Time Complexity:
Just a scan through the string so O(n)

Space Complexity:
Just have a boolean so nothing really ---> O(1)

"""