import heapq

"""

Problem:
https://leetcode.com/problems/minimum-path-sum/


"""

"""

Approach:
Dijkstras like a retard


"""

def minPathSum(grid):
    m = len(grid[0])
    n = len(grid)

    dist = [[float("inf") for _ in range(m)] for _ in range(n)]
    pq = []
    dist[0][0] = grid[0][0]
    heapq.heappush(pq, (grid[0][0], (0,0)))
    
    dirs = [(0,1), (1, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u[0]][u[1]]:
            continue
       
        for di in dirs:
            x_off, y_off = u[0] + di[0], u[1] + di[1]
            
            if 0 <= x_off < n and 0 <= y_off < m and dist[u[0]][u[1]] + grid[x_off][y_off] < dist[x_off][y_off]:
                dist[x_off][y_off] = dist[u[0]][u[1]] + grid[x_off][y_off]
                heapq.heappush(pq, (dist[x_off][y_off], (x_off, y_off)))
    
    return dist[n - 1][m - 1]



"""

Time: O(mn log(mn))
Space: O(mn)


"""