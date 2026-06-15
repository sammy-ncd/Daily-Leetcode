"""

Problem:
https://leetcode.com/problems/binary-tree-right-side-view/description/


"""


"""

Approach:
Level order traversal with BFS scanning right to left
for each level add the first node we scan through


"""


from collections import deque


def rightSideView(root):

    view = []

    if not root:
        return view
    
    q = deque([root])

    while q:

        for i in range(len(q)):
            
            curr = q.popleft()

            if i == 0:
                view.append(curr.val)

            if curr.right:
                q.append(curr.right)

            if curr.left:
                q.append(curr.left)

    return view



"""

Time complexity:

just bfs so overall ---> O(n)


Space complexity:

in the case of a skewed tree view can hold all nodes so overall ---> O(n)


"""