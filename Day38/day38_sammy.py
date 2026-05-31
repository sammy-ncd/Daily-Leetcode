from collections import deque


'''

Problem:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


'''


"""

Approach:
level order traversal with BFS
keep prev pointer to previous node in current level chain


"""


def connect(root):

    if not root:
        return
    
    q = deque([root])

    while q:

        prev = None

        for _ in range(len(q)):

            node = q.popleft()

            if prev:
                prev.next = node
            prev = node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    return root



"""


Time Complexity:
just BFS so overall ---> O(n)


Space Complexity:
O(w), w = max width of the tree


"""