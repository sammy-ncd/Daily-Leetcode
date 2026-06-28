"""

Problem:
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/


"""

"""

Approach:
sort 
ensure differences are no more than 1

def look into the better greedy solution

"""


def maximumElementAfterDecrementingAndRearranging(arr):
    arr.sort()
    arr[0] = 1
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            arr[i + 1] = arr[i] + 1
    return arr[-1]


"""

Time:
O(nlogn)

Space:
timsort so O(n)


"""