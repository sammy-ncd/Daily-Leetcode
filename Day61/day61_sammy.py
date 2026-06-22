"""

Problem:
https://leetcode.com/problems/balanced-binary-tree/description/


"""

"""

Approach:
dfs keeping track of if the current subtree is balanced
and the height of the current subtree


"""


def isBalanced(root):
    
    def dfs(root):
        if not root:
            return [True, 0]
    
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]


"""

let h = height of the tree

Time complexity:

we have to dfs through all nodes 
so overall ---> O(n)

Space complexity:

overall ---> O(h)


"""