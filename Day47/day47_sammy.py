"""

Problem:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


"""


"""

Approach:
If p and q < curr node move curr node left
If p and q > curr node move curr node right
otherwise p and q split paths and this is the LCA


"""







# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def lowestCommonAncestor(root, p, q):
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            break
    return root


"""

Let h = the height of the BST

Time Complexity:
We move left or right every time so at most we go the height of the tree so overall ---> O(h)

Space Complexity:
no additional memory used ---> O(1)


"""