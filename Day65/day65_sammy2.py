"""

Problem:
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


"""

"""

Approach:
keep a size k minheap
on init we heapify nums
then keep popping until it is size k
this will leave the k largest items in the heap
with the root being the kth largest (smallest out of all k items)
then when we add to the heap we maintain size k by popping
return the root after each insertion


"""


import heapq


class KthLargest(object):

    def __init__(self, k, nums):

        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
    

"""

Time complexity:

init:
O(n) heapify
n - k pops so conversion to size k heap ---> O((n-k)logn)
Overall ---> O(n + (n-k)logn)

add:
push ---> O(logk)
pop to maintain size ---> O(logk)
Overall ---> O(logk)

Space complexity:

just the heap so overall ---> O(k)


"""