"""

Problem:
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19


"""

"""

Approach:
Keep track of the current max altitude
keep adding the gains update max accordingly


"""


def largestAltitude(gain):
    maxAlt = 0
    currAlt = 0
    for g in gain:
        currAlt += g
        maxAlt = max(maxAlt, currAlt)
    return maxAlt



"""

Time complexity:
one pass through gain so overall ---> O(n)


Space complexity:
just a couple ints so overall ---> O(1)


"""