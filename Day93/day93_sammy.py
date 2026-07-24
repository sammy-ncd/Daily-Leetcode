"""

Problem:
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/


"""


"""

Approach:
compute in degrees for each node, each node with indegree zero must be added to the result because it is a source node


"""


def findSmallestSetOfVertices(n, edges):
    inDegrees = [0] * n
    for u, v in edges:
        inDegrees[v] += 1
    
    res = []
    for i in range(n):
        if not inDegrees[i]:
            res.append(i)
    return res


"""

Time complexity:

let e = number of edges

go though all edges and vertices, so overall ---> O(n + e)


Space complexity:

need a length n inDegrees array, so overall ---> O(n)


"""