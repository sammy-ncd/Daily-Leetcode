"""

Problem:
https://leetcode.com/problems/path-with-maximum-gold/description/


"""


"""

Approach:
Backtracking dfs
perform dfs from every nonzero cell because any gold cell can be the start of the path
base case:
while next choice is in range and nonzero
choices:
left, right, up, down neighbors
to mark a choice as visited swap that cell to zero backtrack on it
then replace this cell back with its original value
return:
maxGold path from given root

try all roots because 0s can essentially break the graph up into different components

"""



def getMaximumGold(grid):
    
    m = len(grid)
    n = len(grid[0])
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    def validatePos(pos):
        x, y = pos
        return 0 <= x < m and 0 <= y < n

    def dfs(x, y):
        if not validatePos((x, y)) or grid[x][y] == 0:
            return 0
    
        gold = grid[x][y]
        grid[x][y] = 0

        best = 0
        for u, v in directions:
            dx, dy = u + x, v + y
            best = max(best, dfs(dx, dy))
    
        grid[x][y] = gold
    
        return grid[x][y] + best
    
    maxGold = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                maxGold = max(maxGold, dfs(i, j))

    return maxGold


"""

m = number of rows
n = number of columns
g = number of nonzero gold cells

Time complexity:

for each gold cell there are up to 4 choices you can make up down left right
overall ---> O(m * n * 4^g)

Space complexity:
overall ---> O(g)


"""