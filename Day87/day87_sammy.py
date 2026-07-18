"""

Problem:
https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/?envType=daily-question&envId=2026-07-18


"""


"""

Approach:
just do it


"""

import math


def findGCD(nums) -> int:
    return math.gcd(max(nums), min(nums))


"""

Time complexity:

need to find min and max so overall ---> O(n)


Space complexity:

nothing stored so overall ---> O(1)


"""