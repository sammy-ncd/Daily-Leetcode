"""

Problem:
https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=binary-tree


"""

"""

Approach:
simply replace left subtree with right subtree then recurse down these trees


"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root):

    if not root:
        return

    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)        
    
    return root


"""

Time complexity:
we do the swapping for all nodes in the tree so overall ----> O(n)

Space complexity:
no additional memory used ---> overall O(1) XXXX

correction: in the case of a skewed tree the recursion stack holds all nodes
            so overall ---> O(n)


"""