"""

Problem:
https://leetcode.com/problems/last-stone-weight/description/


"""

"""

Approach:
keep a max-heap
while we have 2 elements in the max-heap
pop them off if the max stones are differing weights
push a stone which has the difference of their weights to the heap
if we have a stone left return its weight
otherwise return 0


"""


import heapq


def lastStoneWeight(stones):
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            stoneY = heapq.heappop_max(stones)
            stoneX = heapq.heappop_max(stones)

            if stoneY != stoneX:
                heapq.heappush_max(stones, stoneY - stoneX)
        
        if not stones:
            return 0
            
        return stones[0]


"""

Time complexity:
heapify ---> O(n)
popping and adding stones ---> O(nlogn)
overall ---> O(nlogn)

Space complexity:

we turn the stones array into a max-heap in place so overall ---> O(1)


"""