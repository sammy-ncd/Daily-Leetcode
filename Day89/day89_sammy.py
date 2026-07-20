"""

Problem:
https://leetcode.com/problems/shift-2d-grid/description/?envType=daily-question&envId=2026-07-20


"""


"""

Approach:
flatten then compute new index after k shifts
put new ordering back into grid


"""


def shiftGrid(grid, k: int):
    n = len(grid)
    m = len(grid[0])

    flat = []
    flat2 = [0] * (n * m)

    for i in range(n):
        for j in range(m):
            flat.append(grid[i][j])
    
    for idx in range(len(flat)):
        flat2[(idx + k) % len(flat)] = flat[idx]
    
    idx = 0
    for i in range(n):
        for j in range(m):
            grid[i][j] = flat2[idx]
            idx += 1
    return grid


"""

n = num rows
m = num cols


Time complexity:
dominated by scanning through array, so overall ---> O(m*n)


Space complexity:
flattened matrix so overall ---> O(m*n)


"""