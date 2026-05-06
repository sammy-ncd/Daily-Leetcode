'''

Problem:
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/

'''



"""

Approach sort nums, use two pointers at both edges move them in and check for max pair

"""


def minPairSum(nums):
    nums.sort()
    max_Pair = 0
    l = 0
    r = len(nums) - 1

    while l < r:
        max_Pair = max(max_Pair, nums[l] + nums[r])
        l += 1
        r -= 1
    return max_Pair

print(minPairSum([3,5,2,3]))
print(minPairSum([3,5,4,2,4,6]))