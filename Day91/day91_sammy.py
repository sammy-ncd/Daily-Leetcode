"""

Problem:
https://leetcode.com/problems/deepest-leaves-sum/description/


"""

"""

Approach:
level order traversal with bfs, save the last level sum only, return final sum.


"""


from collections import deque


def deepestLeavesSum(root) -> int:
    def bfs(root):
        q = deque([root])
        while q:
            deepSum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                deepSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return deepSum
    return bfs(root)


"""

let n = number of nodes in the binary tree


Time Complexity:

bfs, so overall ---> O(n)


Space Complexity:

bfs, so overall ---> O(n)

"""