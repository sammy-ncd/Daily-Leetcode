"""

Problem:
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/


"""

"""

Approach:
dfs build contaminated binary tree
store node values in a set
find just return if target is in the set

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.data = set()
        
        def dfs(root):
            stack = [root]
            while stack:
                curr = stack.pop()
                self.data.add(curr.val)
                if curr.left:
                    curr.left.val = 2 * curr.val + 1
                    stack.append(curr.left)
                if curr.right:
                    curr.right.val = 2 * curr.val + 2
                    stack.append(curr.right)
            return False
        dfs(self.root)


    def find(self, target: int) -> bool:
        return target in self.data
    
"""

Time Complexity:

dfs --> O(n)
find --> O(1)

Space Complexity:

dfs stack / init --> O(n)
find --> O(1)


"""