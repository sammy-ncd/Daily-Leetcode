"""

Problem:
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2026-07-27


"""


"""

Approach:
get max num and second max num finally compute what is needed


"""


def maxProduct(nums) -> int:
    maxNumIdx = 0
    for i in range(len(nums)):
        if nums[i] > nums[maxNumIdx]:
            maxNumIdx = i
    secondMaxNum = 0
    for i in range(len(nums)):
        if i != maxNumIdx:
            secondMaxNum = max(secondMaxNum, nums[i])
    return (nums[maxNumIdx]-1)*(secondMaxNum-1)


"""

Time complexity:

2 linear scans, so overall ----> O(n)


Space complexity:

just a couple ints, so overall ----> O(1)


"""