"""

Problem:
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/


"""


"""

Approach:
sort piles
greedily take every other pile starting at the 2nd pile from the end


"""


def maxCoins(piles) -> int:
    piles.sort()
    total = 0
    idx = len(piles) - 2
    for _ in range(len(piles)//3):
        total += piles[idx]
        idx -= 2
    return total


"""

Time complexity:

sorting, so overall ---> O(nlogn)


Space complexity:

all in place, so overall ---> O(1)


"""