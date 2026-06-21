"""

Problem:
https://leetcode.com/problems/maximum-ice-cream-bars/description/?envType=daily-question&envId=2026-06-21


"""


"""

Approach:
Counting sort to sort costs
greedily pick the smallest costs until we cant buy anymore bars


"""



def maxIceCream(costs, coins):
    maxx = max(costs)
    counts = [0 for _ in range(maxx + 1)]

    for i in range(len(costs)):
        counts[costs[i]] += 1
    
    i = 0
    for j in range(len(counts)):
        for _ in range(counts[j]):
            costs[i] = j
            i += 1
    
    bars = 0 
    for c in costs:
        coins -= c
        if coins < 0:
            break
        bars += 1
    
    return bars



"""

let m = max value in costs
let n = len of costs

Time complexity:

create counts array ---> O(m)
fill counts ---> O(n)
rebuild sorted costs from counts ---> O(n)
find max number of bars ---> O(n)

Overall ---> O(m + n)


Space complexity:

counts array so overall ---> O(m)



"""