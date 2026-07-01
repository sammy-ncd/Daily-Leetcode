"""

Problem:
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/


"""

"""

Approach:

root is always a good node

for each node x push that node alongside the current max node in the path to x
for a node x if it has a child with a value >= max node then we have + 1 good nodes

better explanation:
for a node x, if it has a child with value >= max node,
then that child is a good node

"""


def goodNodes(root) -> int:
    
    def dfs(root):
        good = 1
        stack = [(root, root.val)]

        while stack:
            curr, maxNode = stack.pop()
            if curr.left:
                if curr.left.val >= maxNode:
                    good += 1
                stack.append((curr.left, max(maxNode, curr.left.val))) # store the max mode along the path to the current node
            
            if curr.right:
                if curr.right.val >= maxNode:
                    good += 1
                stack.append((curr.right, max(maxNode, curr.right.val)))
        
        return good
    
    return dfs(root)

"""

Time complexity:

dfs so overall ---> O(n)

Space complexity:

dfs stack can hold up to n nodes so overall ---> O(n)


"""