"""

Problem:
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""

"""

Approach:
im not thinking about how to do this in O(1) space
store the preorder traversal in an array 
then do left, right connections


"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return
    
    def preOrder(root, arr):
        if not root:
            return
        
        arr.append(root)
        preOrder(root.left, arr)
        preOrder(root.right, arr)
        return arr
    
    arr = preOrder(root, [])
    
    for i in range(len(arr) - 1):
        arr[i].left = None
        arr[i].right = arr[i + 1] 

"""

let h be the height of the tree

Time Complexity:
-> O(n) to to preorder traversal
-> O(n) to assign children
-> Overall: O(n)

Space Complexity:
O(h) -> recursion stack space for preOrder    (h = logn (balanced) or h = n (skewed))
O(n) -> preOrder traversal array
-> Overall : O(n)

"""