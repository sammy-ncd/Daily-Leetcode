"""

Problem:
https://leetcode.com/problems/number-of-islands/description/


"""


"""

Approach:
Loop through grid each time we see a '1' run dfs as deep as we can go replacing visited pieces of land with '0's (water)
the amount of times we need to start dfs again will be the total island count as there was a gap of water in between

"""


def numIslands(grid):
    
    m = len(grid)
    n = len(grid[0])
    islands = 0

    def dfs(grid, pos):
        r, c = pos

        grid[r][c] = '0'
                
               #   R       L        D       U         
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in dirs:
            
            r_off, c_off = r + d[0], c + d[1] 
            
            if r_off < m and c_off < n and c_off >=0 and r_off >= 0 and grid[r_off][c_off] == '1':
                dfs(grid, (r_off, c_off))
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(grid, (i, j))
                islands += 1
    
    return islands


"""

Time complexity:
this is just dfs runtime so overall ----> O(mn)


Space complexity:
dominated by dfs recursion stack so overall  ----> O(mn)


"""