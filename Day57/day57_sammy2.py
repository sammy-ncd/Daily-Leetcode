'''

Problem:
https://leetcode.com/problems/binary-search/description/


'''



'''

Approach:
Binary search


'''


def search(nums, target):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
    
        mid = lo + (hi - lo) // 2
    
        if nums[mid] > target:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            return mid
    
    return -1 


"""

Time complexity:

just binary search, so overall ----> O(logn)


Space complexity:
just 2 pointers, so overall -----> O(1)



"""