'''

Problem:
https://leetcode.com/problems/evaluate-division/description/


'''

'''

Approach:
Treat problem as a graph problem
we have bidirectional edges u --> v with weight u/v and v --> u with weight v/u
for each query dfs and see if a c ---> d path exists, if it does return its value


'''


def calcEquation(equations, values, queries):
    adj = {}
    i = 0

    for u, v in equations:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, values[i]))
        adj[v].append((u, 1 / values[i]))
        i += 1

    def dfs(root, target):
        seen = set([root])
        stack = [(root, 1)]
        
        while stack:
            node, val = stack.pop()
        
            if node == target:
                return val
        
            for neigh, weight in adj[node]:
                if neigh not in seen:
                    stack.append((neigh, val * weight))
                    seen.add(neigh)
        
        return -1
    
    res = []
    for c, d in queries:
        if c not in adj or d not in adj:
            res.append(-1)
            continue
        res.append(dfs(c, d))
    
    return res


"""

let V = the number of nodes in our graph
let E = the number of edges in our graph
let Q = the number of queries

Time Complexity:

Build graph ---> O(E)
dfs ---> O(V + E)
dfs over all queries ---> O(Q*(V + E))
so overall ---> O(Q*(V + E))


Space Complexity:
just the graph, so overall ---> O(V + E)

"""