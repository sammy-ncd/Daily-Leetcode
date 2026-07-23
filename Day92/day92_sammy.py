"""

Problem:
https://leetcode.com/problems/find-triangular-sum-of-an-array/description/


"""

"""

Approach:
just code the simulation as is, however no need to create a new array each time
just reduce the size of nums in each loop iteration


"""


def triangularSum(nums) -> int:
    n = len(nums)
    while n > 1:
        for i in range(n - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        n -= 1
    return nums[0]


"""

Let n be the length of nums.

Time complexity:

The loops process:

(n - 1) + (n - 2) + ... + 1

elements, so the overall time complexity is O(n^2).


Space complexity:

The array is modified in place and only a few variables are used,
so the extra space complexity is O(1).


"""