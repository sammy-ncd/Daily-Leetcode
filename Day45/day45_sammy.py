"""

Problem:


"""


"""

Approach:
flatten the tree into its in order traversal
keep track of position in iterator



"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def inOrder(self, root, arr):
        if not root:
            return arr

        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        return arr


    def __init__(self, root):
        self.data = self.inOrder(root, [])
        self.pos = 0
        
        
    def next(self):
        val = self.data[self.pos]
        self.pos += 1
        return val


    def hasNext(self):
        return self.pos < len(self.data)
    

"""

Time Complexity:

init ---> O(n) in order traversal
next ---> O(1)
hasNext ---> O(1)


Space complexity:

data array --> O(n)


"""