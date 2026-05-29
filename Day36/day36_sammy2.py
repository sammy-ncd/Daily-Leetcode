"""

Problem:
https://leetcode.com/problems/path-sum-ii/description/?envType=problem-list-v2&envId=binary-tree


"""


"""

Approach:
DFS traversal
store current node path and pathsum at each node
if node is leaf and pathsum == targetsum append path to paths list
return paths list

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    paths = []
    
    if not root:
       return paths
    
    stack = [(root, [root.val], root.val)]

    while stack:
       node, path, currSum = stack.pop()
       
       if not node.left and not node.right and currSum == targetSum:
           paths.append(path)
       
       if node.left:
           stack.append((node.left, path + [node.left.val], currSum + node.left.val))
       
       if node.right:
           stack.append((node.right, path + [node.right.val], currSum + node.right.val))
    
    return paths



"""

let h = height of the tree


Time Complexity:
if we have a skewed tree we are copying a length n list for each node
so this would be O(n^2)
otherwise if its height balanced runtime ---> O(n * h)

Space Complexity:

O(n^2)
or 
O(n * h)
for the same reasons above


can probably use recursion to have better space complexity

"""