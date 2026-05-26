'''

Problem:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/


'''



"""

Approach:
since this is a bst in order traversal will be in sorted order
so just return the k-1 th element in this sorting


edit: can just perform the inorder traversal for k interations and return the value there
(im not coding this cuz lazy)


"""


def kthSmallest(root, k):

    def inOrder(arr, root):
        if not root:
            return arr
        
        inOrder(arr, root.left)
        arr.append(root.val)
        inOrder(arr, root.right)
        
        return arr
    
    arr = inOrder([], root)
    return arr[k-1]


"""

Time Complexity:
just an in order traversal so overall ---> O(n)


Space Complexity:
array to store the traversal in so overall ---> O(n)

can be O(k) time with edited approach
O(1) space as well because we do not need to store anything due to returning early 


"""