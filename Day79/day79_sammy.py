"""

Problem:
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


"""


"""

Approach:
dfs store current number inside nodes value, update as we go down to leaves
once we hit a leaf add its number to a total counter

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root) -> int:
    def dfs(root):
        totalSum = 0
        if not root:
            return totalSum
        root.val = str(root.val)
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                totalSum += int(curr.val)
            if curr.left:
                curr.left.val = curr.val + str(curr.left.val)
                stack.append(curr.left)
            if curr.right:
                curr.right.val = curr.val + str(curr.right.val)
                stack.append(curr.right)
        return totalSum
    return dfs(root)


"""

Time complexity:

Each node is visited once, but concatenating strings takes time proportional
to the current path length.

Worst case, for a skewed tree:
1 + 2 + 3 + ... + n = O(n^2)

overall ---> O(n^2)

For a balanced tree, it would be O(n log n).


Space complexity:

The stack can contain O(h) nodes, where h is the tree height.

However, each node stores a newly created path string. In the worst case,
the total length of all these strings is O(n^2).

overall ---> O(n^2)

"""