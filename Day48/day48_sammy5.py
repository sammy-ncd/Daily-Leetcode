'''

Problem:
https://leetcode.com/problems/maximum-total-subarray-value-i/description/?envType=daily-question&envId=2026-06-09


'''



'''

Approach:
Greedy just find the min and max of the array and return k * (max - min)


'''


def maxTotalValue(nums, k):
    minimum = maximum = nums[0]

    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return k * (maximum - minimum)



"""


Time Complexity:

find min and max -> O(n)
overall ---> O(n)


Space Complexity:
just min and max ints stored 
overall ---> O(1)

"""