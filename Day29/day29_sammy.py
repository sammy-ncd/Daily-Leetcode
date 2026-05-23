from collections import deque



'''

Problem:


'''


'''

Approach:
Use BFS to level order search as soon as we find a leaf node 
its guaranteed to be the first leaf so we its return depth 


'''

def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def minDepth(root):
        
    if not root:
        return 0
    
    q = deque([(root, 1)])

    while q:
        node, depth = q.popleft()

        if node.left == None and node.right == None:
            return depth
        
        if node.left:
            q.append((node.left, depth + 1))
        
        if node.right:
            q.append((node.right, depth + 1))


'''

Time complexity:
just BFS ---> overall O(n)


Space complexity:
if we have a skewed tree we can have a full queue ---> overall O(n)


'''