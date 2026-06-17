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



def merge(arr, start, mid, end):

    l1 = [arr[i] for i in range(start, mid)]
    l2 = [arr[i] for i in range(mid, end)]
    i = j = 0
    k = start

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
            
        k += 1

    while i < len(l1):
        arr[k] = l1[i]
        k += 1
        i += 1

    while j < len(l2):
        arr[k] = l2[j]
        k += 1
        j += 1

    return arr


# Time O(nlogn), Space O(n)
def mergeSort(arr, start, end):

    if (end - start) <= 1:
        return arr
    
    mid = (start + end) // 2
    
    mergeSort(arr, start, mid)
    mergeSort(arr, mid, end)

    merge(arr, start, mid, end)

    return arr

# arr = [1,2,3,1,3,4]
# start = 0
# end = len(arr)
# mid = (start + end) // 2
# print(merge(arr, start, mid, end))
# print(mergeSort([6,5,4,3,2,1], start, end))


# Time: worst O(n^2) avg (Onlogn) Space: O(1)
def quickSort(arr, start, end):

    if (end - start) + 1 <= 1:
        return arr
    
    # There are better ways of picking the pivot, this is just for simplicity
    pivot = arr[end]
    swap = start

    for i in range(start, end):
        if arr[i] < pivot:
            temp = arr[swap]
            arr[swap] = arr[i]
            arr[i] = temp
            swap += 1

    # swapping point ends at the point where all things to the left of swap are < pivot and all things to the right of swap are > pivot
    arr[end] = arr[swap]
    arr[swap] = pivot

    quickSort(arr, start, swap - 1)
    quickSort(arr, swap + 1, end)

    return arr 


# arr = [1,2,3,1,3,4]
# start = 0
# end = len(arr) - 1
# print(quickSort(arr, start, end))