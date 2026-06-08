'''

Problem:
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2026-06-08


'''


'''


Approach:
Store smaller elements than pivot in their own array
equal elements in their own array
and larger in their own array
add arrays back together in the end


'''



def pivotArray(nums, pivot):
    smaller = []
    larger = []
    equal = []

    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else:
            equal.append(num)

    return smaller + equal + larger


"""

Let n = length of nums

Time complexity:
One scan to build all arrays ---> O(n)
One length n scan to put arrays together


Space complexity:
ovrall the sum of all three arrays used is going to be of length n
so total space is O(n) 

"""