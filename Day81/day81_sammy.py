"""

Problem:
https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2026-07-12


"""


"""

Approach:
sort array + use hashmap


"""


def arrayRankTransform(arr):
    ranks = {}
    rank = 1
    for num in sorted(arr):
        if num not in ranks:
            ranks[num] = rank
            rank += 1
    for i in range(len(arr)):
        arr[i] = ranks[arr[i]]
    return arr


"""

Time complexity:

sorting, so overall ---> O(nlogn)


Space complexity:

hashmap with (element, rank) pairs so overall ---> O(n)


"""