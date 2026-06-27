"""

Problem:
https://leetcode.com/problems/kth-largest-element-in-an-array/description/


"""

"""

Approach:

either have an empty min heap and push into it maintaining size k
OR
turn nums array into a min heap popping until it is size k
(would have to heapify here which is slower)

then return the number at the root of the min heap
this number will be the kth largest (popped off n - k smaller ones)


"""



import heapq


def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


"""

for approach 1

Time complexity:

pushing and popping into a size k minheap, so overall ---> O(nlogk)

Space complexity:

size at most k + 1 min heap, so overall ---> O(k)


"""