"""

Problem:
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2026-07-27


"""


"""

Approach:
get max num and second max num finally compute what is needed


"""


def maxProduct(nums) -> int:
    max1 = 0
    max2 = 0
    for i in range(len(nums)):
        if nums[i] >= max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i] >= max2:
            max2 = nums[i]
    return (max1-1)*(max2-1)


"""

Time complexity:

one linear scan, so overall ----> O(n)


Space complexity:

just a couple ints, so overall ----> O(1)


"""