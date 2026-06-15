'''

Problem:
https://leetcode.com/problems/search-a-2d-matrix/


'''



'''

Approach:
Treat matrix as long list, do simple math to convert to 2d coords


'''


def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    lo = 0
    hi = rows * cols - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        midR, midC = mid // cols, mid % cols
    
        if matrix[midR][midC] > target:
            hi = mid - 1
        elif matrix[midR][midC] < target:
            lo = mid + 1
        else:
            return True
        
    return False



"""

Time complexity:

binary search on input of m*n size
so overall ---> O(log(m*n))

Space complexity:

all in place overall ---> O(1)


"""