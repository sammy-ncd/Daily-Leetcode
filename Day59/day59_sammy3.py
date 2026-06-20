"""

Problem:
https://leetcode.com/problems/delete-node-in-a-bst/description/


"""

"""

Approach:
0 or 1 children case:
either remove the node and done, or replace the node with the one child

2 children case:
copy the successors value into the node we want to delete then delete the successor node from the right subtree

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root, key):

    if not root:
        return None
    
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else: # in this branch we have 2 children
            curr = root.right # defintely have a right node
            
            while curr and curr.left: # find successor (leftmost node in the right subtree)
                curr = curr.left
            
            root.val = curr.val # swap values between deletion node and successor 
            root.right = deleteNode(root.right, curr.val) # delete the node that took upon the deletion key
    
    return root



"""

Time complexity:

worst case we have to delete a node with 2 children
so in a balanced tree we have to find the deletion node
then we have to find its successor
so overall ---> O(logn)

Space complexity:

if the tree is balanced ---> O(logn) 


For both skewed tree time and space ---> O(n)

"""