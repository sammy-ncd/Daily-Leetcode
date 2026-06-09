'''

Problem:
https://leetcode.com/problems/check-knight-tour-configuration/description/?envType=problem-list-v2&envId=simulation


'''

'''

Approach:
Check if we can get to i + 1 position from i
if we cant return false


'''


def checkValidGrid(grid):

    n = len(grid)

    def validatePos(pos):
        x, y = pos
        return 0 <= x < n and 0 <= y < n
    
    moves = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
    
    if grid[0][0] != 0:
        return False
    
    pos = (0, 0)
    for i in range(1, n * n):
        found = False
        for dx, dy in moves:
            x, y = pos[0] + dx, pos[1] + dy
            
            if validatePos((x, y)) and grid[x][y] == i:
                pos = (x, y)
                found = True
                break
        
        if not found:
            return False
   
    return True


"""

Time complexity:

O(n^2)


Space complexity:

all in place ---> O(1)


"""