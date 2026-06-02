'''

Problem:
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/?envType=daily-question&envId=2026-06-02


'''


'''

Approach:
Want to maximize the price of the free candy
to do this we sort in descending order then take 
a running sum ignoring each 3rd element


'''




def minimumCost(cost):
    n = len(cost)
    if n < 3:
        return sum(cost)
    
    cost.sort(reverse=True)

    for i in range(2, n, 3):
        cost[i] = 0

    return sum(cost)


'''

Time Complexity:
sorting dominates ---> overall: O(nlogn)

Space Complexity:
nothing additional used ---> overall: O(1)


'''