"""

Problem:
https://leetcode.com/problems/valid-anagram/description/


"""


"""

Approach:
First check if lenghts are the same.
If they are then we create an array storing occurences of characters
Store by index assigned by a simple hash function based on ASCII value
Check if all array entries are 0 in the end to ensure anagram properties


"""


def isAnagram(s, t):

    if len(s) != len(t):
        return False

    counts = [0] * 26

    for i in range(len(t)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1

    for count in counts:
        if count != 0:
            return False
        
    return True



"""

Time Complexity:
n = len of s
m = len of t

overall time is gonna be O(m + n)


Space Complexity:
Using fixed size array to hold alphabet characters overall ---> O(1)

"""