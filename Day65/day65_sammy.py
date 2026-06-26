"""

Problem:
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2026-06-26


"""

"""

Approach:
flatten matrix into an array and sort it
take the median
for each element in the array see if we can convert it into the median (all numbers must have the same remainder mod x)
if we can, add the number of operations it will take to ops
otherwise return -1


"""


def minOperations(grid, x):
    nums = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            nums.append(grid[i][j])
    
    nums.sort()
    
    median = nums[len(nums) // 2]
    ops = 0
    
    for i in range(len(nums)):
        num = nums[i] 
        if abs(num - median) % x == 0:
            ops += abs(num - median) // x
        else:
            return -1
    
    return ops


"""

Time complexity:
dominated by sorting, so overall ---> O(mn*log(mn))


Space complexity:
flattened matrix, so overall ---> O(mn)


"""