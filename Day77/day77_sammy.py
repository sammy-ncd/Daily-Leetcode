"""

Problem:
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/


"""


"""

Approach:
check if even nodes have grandchildren
add grandchildren values if they exist

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumEvenGrandparent(root) -> int: 
    def dfs(root):
        gpsum = 0
        if not root:
            return gpsum
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
                if curr.left.left and curr.val % 2 == 0:
                    gpsum += curr.left.left.val
                if curr.left.right and curr.val % 2 == 0:
                    gpsum += curr.left.right.val
            if curr.right:
                stack.append(curr.right)
                if curr.right.left and curr.val % 2 == 0:
                    gpsum += curr.right.left.val
                if curr.right.right and curr.val % 2 == 0:
                    gpsum += curr.right.right.val
        return gpsum
    return dfs(root)


"""

Time complexity:

dfs ---> overall: O(n)


Space complexity:

dfs ---> overall: O(n)


"""