"""

Problem:
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

"""

"""

Approach:
BFS to get levels
reverse levels array at the end


"""


from collections import deque


def levelOrderBottom(root):
    levels = []
    def bfs(root):
        if not root:
            return levels
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                
                level.append(curr.val)
            
            levels.append(level)
        
        levels.reverse()
        return levels
    
    return bfs(root)


"""

Time complexity:

BFS + reversing an array, so overall ---> O(n)

Space comeplexity:

BFS q, so overall ---> O(n)

"""