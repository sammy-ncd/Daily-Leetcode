"""

Problem:
https://leetcode.com/problems/insert-into-a-binary-search-tree/description/


"""


"""

Approach:
Recursion
base case is when current node is null, then this node will be the insertion point
otherwise recurse left if root.val > val
recurse right if root.val < val


"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val < val:
        root.right = insertIntoBST(root.right, val)  
    else:
        root.left = insertIntoBST(root.left, val)
    
    return root


"""

Let h = height of the tree

Time complexity:

balanced tree ---> O(logn)
skewed tree ---> O(n)

overall ---> O(h)


Space complexity:

same idea as time, overall ---> O(h)


"""