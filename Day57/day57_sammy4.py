"""

Problem:
https://leetcode.com/problems/koko-eating-bananas/description/


"""



"""

Approach:
The upper bound for k is the max pile
so we perform a binary search on the range of [1, maxPile]
we compute the total time it takes to eat all piles using this potential k
if the k causes time <= number of hours we search for a smaller k so hi = k - 1
if k causes time > number of hours we search for a larger k so lo = k + 1


"""



from math import ceil


def minEatingSpeed(piles, h):

    lo = 1
    hi = max(piles)

    while lo <= hi:

        k = lo + (hi - lo) // 2
        
        time = 0
        for pile in piles:
            time += ceil(float(pile)/k)

        if time <= h: # if time <= h look for a slower banana eating rate
            hi = k - 1
        else: # if time > look for a faster banana eating rate
            lo = k + 1 
    
    return lo



"""

Time complexity:

O(logm) binary search over [1, max piles]
O(n) to compute each time for each potential midpoint in binary search
Overall ---> O(nlogm)

Space complexity:
nothing but some floats / ints used so overall ----> O(1)

"""