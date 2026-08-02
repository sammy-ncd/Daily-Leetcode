"""

Problem:
https://leetcode.com/problems/max-area-of-island/description/


"""


"""

Approach:
DFS on each island, replace with a 2 when cell is visited return max area for given patch
move onto next island and save the area of the largest one


"""



def maxAreaOfIsland(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    def validatePos(pos):
        x, y = pos
        return 0 <= x < m and 0 <= y < n
    def dfs(root):
        stack = [root]
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        area = 1
        while stack:
            curr = stack.pop()
            for dx, dy in dirs:
                newPos = (curr[0] + dx, curr[1] + dy)
                if validatePos(newPos) and grid[newPos[0]][newPos[1]] == 1:
                    grid[newPos[0]][newPos[1]] = 2
                    stack.append(newPos)
                    area += 1
        return area
    maxArea = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 2
                maxArea = max(maxArea, dfs((i,j)))
    return maxArea


"""

m = nums rows
n = num cols

Time complexity:

dfs on whole grid, so overall ---> O(mn)


Space complexity:

dfs stack, so overall ---> O(mn)


"""