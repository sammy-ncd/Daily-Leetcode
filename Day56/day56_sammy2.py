"""

Problem:
https://leetcode.com/problems/sort-colors/


"""


"""

Approach:
Bucket Sort


"""



def sortColors(nums):
    counts = [0,0,0]

    for num in nums:
        counts[num] += 1

    j = 0
    for i in range(len(counts)):
        for _ in range(counts[i]):
            nums[j] = i
            j += 1


"""

Time complexity:

O(n) to build counts
O(n) to fill arr
overall ---> O(n)


Space complexity:

all done in place, so overall ---> O(1)

"""