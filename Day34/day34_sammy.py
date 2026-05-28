"""

Problem:
https://leetcode.com/problems/binary-tree-paths/description/


"""


"""

Approach:
DFS store (node, path up to this node) pairs
when we reach a leaf append the current path to that leaf node to paths array

"""

def binaryTreePaths(root):
    paths = []

    if not root:
        return paths
    
    path = ""
    stack = [(root, path)]
    
    while stack:
        node, path = stack.pop()
    
        path += str(node.val)     
        if not node.left and not node.right:
            paths.append(path)
            path = str(root.val)
    
        if node.left:
            stack.append((node.left, path + "->"))
    
        if node.right:
            stack.append((node.right, path + "->"))
            
    return paths


"""

Time complexity:
just dfs so overall and string building ---> O(n * h) where n is number of nodes
                                                      and h is max height of a root to leaf path


Space complexity:
O(n * h) same reasoning as time complexity


"""