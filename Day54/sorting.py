'''

Problem:
https://leetcode.com/problems/sort-an-array/description/


'''


'''

insertion sort, merge sort, quick sort, bucket sort


'''

# start on 2nd value verify that we are in sorted order if not perform a swap now we know first two elements are sorted
# keep doing this process where at each point we have a partially sorted array and we just have to find insertion point
def insertionSort(nums):

    for i in range(1, len(nums)):

        j = i - 1

        while(j >= 0 and nums[j] > nums[j + 1]):
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
            j -= 1
    
    return nums
# Best case O(n) --> nums is already sorted
# Worst case O(n^2) --> nums initially sorted in reverse order
# Space O(1) all done in place

# print(insertionSort([3,4,5,1,6]))
# print(insertionSort([1]))
# print(insertionSort([6,5,4,3,2,1]))