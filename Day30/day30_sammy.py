from collections import deque


"""

Problem:
https://leetcode.com/problems/binary-tree-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree


"""


'''

Approach:
Use BFS to perform level order traversal
create and append new array to result array for each level


'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def levelOrder(root):
    if not root:
        return []
    
    q = deque([root])
    levels = []
   
    while q:
       
        level = []
        
        # build level based off of what is in the q at the given iteration
        for _ in range(len(q)):

            curr_node = q.popleft()
            level.append(curr_node.val)
           
            if curr_node.left:
                q.append(curr_node.left)
            
            if curr_node.right:
                q.append(curr_node.right)
       
        levels.append(level)
    
    return levels


"""

Time Complexity:
this is just BFS so overall ----> O(n)


Space Complexity:
only one level at a time is in the q
so the maximum space occupied is the widest level
let w = the widest level space complexity ----> O(w) 


"""