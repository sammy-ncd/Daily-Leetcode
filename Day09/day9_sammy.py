"""

Problem:
https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-04


"""



"""

Aproach: keep rotating the string and checking against goal

"""


def rotateString(s, goal):

    for _ in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]
    
    return False


def rotateString_optimal(s, goal):
    return len(s) == len(goal) and goal in (s + s)



print(rotateString(s = "abcde", goal = "cdeab"))
print(rotateString(s = "abcde", goal = "abced"))


print(rotateString_optimal(s = "abcde", goal = "cdeab"))
print(rotateString_optimal(s = "abcde", goal = "abced"))


"""

Time complexity:
For slow --> O(n^2) building n length str n times = n*n
For optimal --> O(n) just checking for occurence of a substring

Space complexity:
Both O(n) --> building length n string.

"""