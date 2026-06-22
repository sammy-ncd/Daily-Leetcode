"""

Problem:
Check if a binary tree has a root to leaf path without any zeros


"""

"""

Approach:
DFS
if current dfs node has 0 as its value dont push its neighbors


"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasZeroFreePath(root):

    if not root:
        return False

    stack = [root]

    while stack:

        curr = stack.pop()
        if curr.val == 0:
            continue

        if not curr.left and not curr.right:
            return True
        
        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    return False

def hasZeroFreePathRecursive(root):

    def dfs(root):
        if not root:
            return False
        
        if root.val == 0:
            return False

        if not root.left and not root.right:
            return True

        return dfs(root.left) or dfs(root.right)

    return dfs(root)

def hasZeroFreePath_Recursive(root):

    path = []

    def dfs(root):

        if not root or root.val == 0:
            return False
        
        path.append(root.val)

        if not root.left and not root.right:
            return True
        
        if dfs(root.left) or dfs(root.right):
            return True

        path.pop()
        return False
    
    return path if dfs(root) else []


# Test 1: Empty tree
root = None
print(hasZeroFreePath(root))  # False


# Test 2: Single node, nonzero
root = TreeNode(1)
print(hasZeroFreePath(root))  # True


# Test 3: Single node, zero
root = TreeNode(0)
print(hasZeroFreePath(root))  # False


# Test 4:
#       1
#      / \
#     2   3
# Root-to-leaf paths: 1->2, 1->3
# Both have no zero
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(hasZeroFreePath(root))  # True


# Test 5:
#       1
#      / \
#     0   3
# Path 1->3 has no zero
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(3)
print(hasZeroFreePath(root))  # True
#print(hasZeroFreePath_Recursive(root))


# Test 6:
#       1
#      / \
#     0   0
# Both paths contain zero
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
print(hasZeroFreePath(root))  # False
#print(hasZeroFreePath_Recursive(root))


# Test 7:
#       0
#      / \
#     1   2
# Root is zero, so every root-to-leaf path has zero
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
print(hasZeroFreePath(root))  # False


# Test 8:
#        1
#       /
#      2
#     /
#    3
# One skewed path, no zeros
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(hasZeroFreePath(root))  # True


# Test 9:
#        1
#       /
#      2
#     /
#    0
# Skewed path contains zero
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
print(hasZeroFreePath(root))  # False


# Test 10:
#          1
#        /   \
#       0     2
#            / \
#           0   5
# Path 1->2->5 has no zero
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(5)
print(hasZeroFreePath(root))  # True


print(hasZeroFreePathRecursive(root))

"""

Time complexity:

dfs, so overall ---> O(n)

Space complexity:
DFS stack so overall ---> O(n)

"""


print(hasZeroFreePath_Recursive(root))