'''

Problem:
https://leetcode.com/problems/search-in-a-binary-search-tree/


'''



"""

Approach:
I mean just use the properties of a BST to find your way.

"""


def searchBST(root, val):

    if root == None:
        return None
    
    while root:
        if root.val == val: return root
        if root.val < val: root = root.right
        else: root = root.left    
    
    return None


"""

Time complexity:
Problem doesnt say anything about the tree being balanced so O(n) if balanced O(logn)

Space complexity:
nothing extra stored so O(1)

"""