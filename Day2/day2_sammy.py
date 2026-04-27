"""

Problem:
https://leetcode.com/problems/two-furthest-houses-with-different-colors/?envType=daily-question&envId=2026-04-27


"""


"""

Idea:
Pretty simple just look at color of the first house on each end (far left and far right)
then find the farthest different color house from each point return the max of those distances.

"""

def maxDistance(colors):
    n = len(colors)
    max_dist_idx1 = 0
    color1 = colors[n - 1]

    # Right to Left Distance
    for i in range(0, n):
        if colors[i] != color1:
            max_dist_idx1 = i
            break

    # Left to Right Distance
    max_dist_idx2 = 0 
    color1 = colors[0]
    for i in range(0, n):
        if colors[i] != color1:
            max_dist_idx2 = i

    return max(n - max_dist_idx1 - 1, max_dist_idx2)
    

print(maxDistance([1,1,1,6,1,1,1]))
print(maxDistance([1,8,3,8,3]))
print(maxDistance([0,1]))
print(maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))

"""

Time Complexity:
Linear scan through the array twice ---> overall time: O(n)

Space Complexity:
O(1) only ints stored, so constant memory.

"""