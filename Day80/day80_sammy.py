"""

Problem:
https://leetcode.com/problems/count-the-number-of-complete-components/?envType=daily-question&envId=2026-07-11


"""


"""

Approach:
dfs in each components count number of nodes and edges in each component
verify each component is the complete component on n nodes


"""


def countCompleteComponents(n, edges) -> int:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    vis = set()
    def dfs(root):
        stack = [root]
        vis.add(root)
        nodes = set([root])
        edges = 0
        while stack:
            curr = stack.pop()
            for node in adj[curr]:
                edges += 1
                if node not in vis:
                    nodes.add(node)
                    vis.add(node)
                    stack.append(node)
        numNodes = len(nodes)
        if (numNodes * (numNodes - 1)) == edges:
            return True
        return False
    components = 0
    for i in range(n):
        if i not in vis:
            if dfs(i):
                components += 1
    return components


"""

Time complexity:

n = num nodes
m = num edges

dfs, so overall ---> O(n + m)


Space complexity:

dfs, so overall ---> O(n + m)


"""