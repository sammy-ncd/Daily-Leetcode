"""

Problem:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


"""


"""

Approach:
for each nums[i] map nums[nums[i] - 1] as negative to indicate nums[i] exists
2nd pass check to see which mappings exists


"""


def findDisappearedNumbers(nums):
    n = len(nums)

    for i in range(n):
        value = abs(nums[i])
        if nums[value - 1] > 0:
            nums[value - 1] *= -1
   
    res = []

    for i in range(1, n + 1):
        if nums[i - 1] > 0:
            res.append(i)

    return res



"""

Time complexity:
two O(n) passes ----> Overall: O(n)

Space complexity:
no additional memory used (not counting output) ---> Overall: O(1)


"""