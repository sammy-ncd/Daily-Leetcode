"""

Problem:
https://leetcode.com/problems/game-of-life/description/


"""


"""

Approach:
Just follow the simulation step by step (brute force)
To ensure O(1) space have temporary "died" and "revived" states


"""


def gameOfLife(board):

    m = len(board)
    n = len(board[0])

    def validatePos(pos):
        x, y = pos
        return 0 <= x < m and 0 <= y < n
    
    dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

    for i in range(m):
        for j in range(n):
            neighbors = 0
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if validatePos((x, y)) and board[x][y] in [1, 2]: 
                    neighbors += 1
            
            if board[i][j]:
                if neighbors < 2 or neighbors > 3:
                    board[i][j] = 2
            else:
                if neighbors == 3:
                    board[i][j] = 3

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1

"""

Let m = num rows in board
Let n = num cols in board

Time Complexity:

Play Game is O(m*n*len(dirs))
Replace temp states = O(m*n)
Since the length of dirs is fixed total runtime ---> O(mn)


Space Complexity:

Everything is done in place, overall ---> O(1)

"""