"""

Problem:
https://leetcode.com/problems/find-center-of-star-graph/description/


"""


"""

Approach:
take any two edges return the node appearing in both edges


"""


def findCenter(edges) -> int:
    return (set(edges[0]) & set(edges[1])).pop()


"""

Time complexity:

O(1)


Space complexity:

O(1)


"""