"""

Problem:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


"""


"""

Approach:
recursively add the middle node in the sorted array to maintain
a balanced height


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):

    def buildTree(start, end):

        if start > end:
            return None
        
        mid = (end + start) // 2
        root = TreeNode(nums[mid])
        root.left = buildTree(start, mid - 1)
        root.right = buildTree(mid + 1, end)
        return root
   
    return buildTree(0, len(nums) - 1)



"""

Time complexity:
need to go through every node so overall ---> O(n)

Space complexity:
need to create a node for each in the array overall ---> O(n)


"""