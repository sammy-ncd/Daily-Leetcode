'''

Problem:
https://leetcode.com/problems/merge-sorted-array/description/


'''


'''

Approach:
merge like you would in mergsort
should just go in reverse cuz we have extra space in the nums1 array
im lazy tho and i already coded merge earlier

'''



def merge(nums1, m, nums2, n):       
    l1 = [nums1[i] for i in range(m)]
    l2 = [nums2[i] for i in range(n)]
    i = j = k = 0
    
    while i < m and j < n:
        if l1[i] <= l2[j]:
            nums1[k] = l1[i]
            i += 1 
        else:
            nums1[k] = l2[j]
            j += 1
        k += 1
        
    while i < m:
        nums1[k] = l1[i]
        i += 1
        k += 1
    while j < n:
        nums1[k] = l2[j]
        j += 1
        k += 1



"""

Time complexity:

O(m + n) need to get all elements


Space complexity:

we allocate temporary arrays so the space is the sum of these two
O(m + n)


"""