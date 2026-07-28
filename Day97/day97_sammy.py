"""

Problem:
https://leetcode.com/problems/digit-frequency-score/description/


"""


"""

Approach:
sum all of the digits


"""



def digitFrequencyScore(n: int) -> int:
    total = 0
    for c in str(n):
        total += int(c)
    return total


"""

Time complexity:
one linear scan, so overall ---> O(n)


Space complexity:
just one int, so overall ---> O(1)


"""