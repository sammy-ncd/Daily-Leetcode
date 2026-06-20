"""

Problem:
https://leetcode.com/problems/merge-two-binary-trees/description/?envType=problem-list-v2&envId=binary-tree


"""


"""

Approach:
Run a parallel DFS on both trees at once
recursion is much better here

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1, root2):
    
    if not root1:
        return root2
    
    if not root2:
        return root1
    
    stack = [[root1, root2]]

    while stack:
        node1, node2 = stack.pop()

        if node1 and node2:

            node1.val += node2.val

            if node1.left and node2.left:
                stack.append([node1.left, node2.left])
            elif node2.left and not node1.left:
                node1.left = node2.left
                
            if node1.right and node2.right:
                stack.append([node1.right, node2.right])
            elif node2.right and not node1.right:
                node1.right = node2.right

    return root1


def mergeTreesRecursive(root1, root2):

    if not root1:
        return root2
    
    if not root2:
        return root1
    
    root = TreeNode(root1.val + root2.val, None, None)
    root.left = mergeTreesRecursive(root1.left, root2.left)
    root.right = mergeTreesRecursive(root1.right, root2.right)

    return root


"""


Time complexity:

O(n) --> DFS
so overall ---> O(n)


Space complexity (Iterative):
let h = height of the tree
worst case skewed tree so O(n), otherwise overall ---> O(h)


"""