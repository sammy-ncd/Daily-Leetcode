'''

Problem:
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

'''



"""

Approach:
recurse all left then down then right

"""



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversalHelper(root, arr):
    if root == None:
        return
    
    inorderTraversalHelper(root.left, arr)
    arr.append(root.val)
    inorderTraversalHelper(root.right, arr)

    return arr



def inorderTraversal(root):
    return inorderTraversalHelper(root, [])



root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)


print(inorderTraversal(root1))

root2 = TreeNode(1)

root2.left = TreeNode(2)
root2.right = TreeNode(3)

root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(8)

root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right.left = TreeNode(9)

print(inorderTraversal(root2))


'''

Time complexity:
O(n) standard tree traversal

Space complexity:
O(n) returns array with all nodes in tree

'''