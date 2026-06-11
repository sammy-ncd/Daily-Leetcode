"""

Problem:
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/description/?envType=daily-question&envId=2026-06-11


"""

"""

Approach:
DFS to find max depth
if there are 2 possible edge weights then for a root ---> leaf path there is 2^depth ways to reach it
half of these paths will be even, the other half will be odd
return number of odd paths


"""


def assignEdgeWeights(edges):
    MOD = pow(10, 9) + 7
    n = len(edges) + 1

    adj = [[] for _ in range(n + 1)]
    vis = [False for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v) # u --> v
        adj[v].append(u) # v --> u
    
    max_depth = 0
    stack = []
    stack.append((1, 0))
    
    while stack:
        curr, depth = stack.pop()
        vis[curr] = True
    
        max_depth = max(max_depth, depth)
        for neigh in adj[curr]:
            if not vis[neigh]:
                stack.append((neigh, depth + 1))
        
    return pow(2, max_depth - 1) % MOD


"""

Time Complexity:

Build adjacency list --> O(n)
Build visited list --> O(n)
Find max depth (DFS) --> O(n)
Overall: O(n)

Space Complexity:
vis, adj -- O(n)
Overall: O(n)

"""