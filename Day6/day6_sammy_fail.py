"""

Problem:

https://leetcode.com/problems/flip-square-submatrix-vertically/?envType=daily-question&envId=2026-04-30


"""




"""

Approach: mirror the submatrix down the middle, will use a 
          helper function to perform row swapping.


"""


def reverseSubmatrix(grid, x, y, k):

    def swap_rows(row_idx):
        for j in range(y, y + k):
            temp = grid[row_idx][j] 
            grid[row_idx][j] = grid[(row_idx + k - 1)][j]
            grid[(row_idx + k - 1)][j] = temp

    for i in range(k // 2):
        swap_rows(x - i)

    return grid


# print(reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3))
# print(reverseSubmatrix(grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2))

print(reverseSubmatrix(grid = [[14,3,18,16],
                               [2,14,11,20],
                               [19,19,4,15],
                               [11,15,18,6]], x = 0, y = 0, k = 4))

# print(reverseSubmatrix([[6,2,11,19,16],
#                        [7,14,7,16,18]], 0, 0, 2))
