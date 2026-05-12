'''

Problem:
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=daily-question&envId=2026-05-12


'''



"""

Approach:
I AM GOING TO DO THE NAIVE APPROACH OF JUST GRID SCAN
BUT SHOULD DO STAIRCASE SEARCH

"""


def countNegatives(grid):

    m = len(grid)
    n = len(grid[0])
    cnt = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] < 0:
                cnt += 1

    return cnt


"""

Time complexity:
O(nm) ---> 2D scan

Space complexity:
O(1) ---> one int

"""