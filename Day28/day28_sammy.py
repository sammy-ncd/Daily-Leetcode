'''

Problem:
https://leetcode.com/problems/path-sum/


'''


'''

Approach:
Use DFS where we store running sums for each given node
when DFS backtracks we can use the running sum at the next available node
we can check if the node is a leaf and if its running sum == targetSum


'''


def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False
    
    stack = [[root, root.val]]

    while stack:
        node, curr_sum = stack.pop()

        if curr_sum == targetSum and node.left == None and node.right == None:
            return True
       
        if node.left:
            stack.append([node.left, node.left.val + curr_sum])            
        
        if node.right:
            stack.append([node.right, node.right.val + curr_sum])
   
    return False

'''

Time complexity:
In the worst case we search all n nodes so overall ----> O(n)

Space complexity:
we use a stack that may have all nodes in it (skewed tree) so overall ---> O(n)


'''