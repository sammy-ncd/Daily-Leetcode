from collections import deque


"""

Problem:
https://leetcode.com/problems/clone-graph/


"""



"""

Approach:
BFS to traverse graph
hashmap to clone nodes


# """


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None
    
    root = Node(node.val, [])

    q = deque([node])
    old_to_new = {node : root}
    
    while q:
        curr = q.popleft()
        for n in curr.neighbors:
            
            if n not in old_to_new:
                n_clone = Node(n.val, [])
                q.append(n)
                old_to_new[n] = n_clone
            
            old_to_new[curr].neighbors.append(old_to_new[n])
    
    return root



"""

V = # of nodes
E = # of edges


Time complexity:
just BFS ---> overall: O(V + E)


Space complexity:
adj list with a copy for each node ---> overall: O(V)



"""