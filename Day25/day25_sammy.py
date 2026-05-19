"""

Problem:
https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2026-05-19


"""


"""

Approach:
Two pointers starting at beginning of both arrays
if both pointers are equal return the number
if one pointer is smaller than the other move the small pointer up
repeat while both pointers are in bounds
return -1 if no common minimum


"""


def getCommon(nums1, nums2):
    
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        x, y = nums1[i], nums2[j] 

        if x == y: return x
        
        if x < y:
            i += 1
        else:
            j += 1
    
    return -1


"""

Time Complexity:
let n be the length of nums1
len m be the length of nums2

overall runtime is gonna be the length of the smaller list
so overall ---> O(min(m, n))


Space Complexity:
just two pointers, overall ---> O(1)

"""