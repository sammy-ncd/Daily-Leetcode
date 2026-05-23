'''

Problem:
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2026-05-23


'''


'''

First approach Approach (doesnt work):


Find the minimum 
Then scan n times to see if its sorted in a rotated order.


Second approach:
We can just check to see if the array is sorted
if when checking it fails once this is okay because it may just mean it was rotated
if it fails twice its impossible that it could be rotated in sorted order
so we just need to verify it only broke at most once


'''

def check_fail(nums):

    n = len(nums)
    first_min_idx = 0
    last_min_idx = 0

    for i in range(n):
        if nums[i] < nums[first_min_idx]:
            first_min_idx = i
        if nums[i] <= nums[last_min_idx]:
            last_min_idx = i

    firstWorks = True
    lastWorks = True

    for _ in range(n - 1):
        if nums[first_min_idx] > nums[(first_min_idx + 1) % n]:
            firstWorks = False
        if nums[last_min_idx] > nums[(last_min_idx + 1) % n]:
            lastWorks = False
        
        first_min_idx = (first_min_idx + 1) % n
        last_min_idx = (last_min_idx + 1) % n


    return firstWorks or lastWorks


print(check_fail([3,4,5,1,2])) # true
print(check_fail([2,1,3,4])) # false
print(check_fail([1,2,3])) # true


def check(nums):

    n = len(nums)
    breaks = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            breaks += 1

    return breaks < 2


print(check([3,4,5,1,2])) # true
print(check([2,1,3,4])) # false
print(check([1,2,3])) # true


"""

Time Complexity:
just one linear pass ---> Overall O(n)

Space Complexity:
only a couple ints ---> Overall O(1)


"""