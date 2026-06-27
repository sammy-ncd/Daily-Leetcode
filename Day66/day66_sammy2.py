"""

Problem:
https://leetcode.com/problems/k-closest-points-to-origin/description/


"""

"""

Approach:
initialize a maxheap
for each point compute its distance from the origin
then pass (distance, x, y) into the maxheap 
heap compares in order of items in the tuple 
ex: p1:(1,3,5) p2:(1,3,6) in this case p2 > p1 because 6 > 5

as we push ensure we have size k if we are > k then pop
return all points in the maxheap since we popped off all the n - k
largest points we are left with the k smallest 


"""


import heapq, math


def kClosest(points, k):
    def dist(point):
        x, y = point
        # dont need to take square root here but I just wanna stay true to the formula
        return math.sqrt(pow(x,2) + pow(y,2))
    
    heap = []
    
    for point in points:
        distance = dist(point)
        x, y = point
        heapq.heappush_max(heap, (distance, x, y))
        
        if len(heap) > k:
            heapq.heappop_max(heap)
    
    return [(x, y) for (dist, x, y) in heap]


"""

Time complexity:

for each point is pushed or popped at most once 
into a heap of size no more than k + 1
so overall ---> O(nlogk)

Space complexity:
size k maxheap so overall ---> O(k)


"""