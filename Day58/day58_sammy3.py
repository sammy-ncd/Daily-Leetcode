"""

Problem:
https://leetcode.com/problems/validate-binary-tree-nodes/description/?envType=problem-list-v2&envId=binary-tree


"""


"""

Need to check for a lot of things:
- only 1 root 
- only one component
- no cycles
- all nodes have 1 parent


"""



def validateBinaryTreeNodes(n, leftChild, rightChild):
    
    seen = set()
    for i in range(n):
        
        if leftChild[i] != -1:
            if leftChild[i] in seen:
                return False
            seen.add(leftChild[i]) 
        
        if rightChild[i] != -1:
            if rightChild[i] in seen:
                return False
            seen.add(rightChild[i])
    
    if len(seen) != n - 1:
        return False
   
    root = 0
    for i in range(n):
        if i not in seen: 
            root = i
            break
   
    totalNodesVisited = 0
    stack = [root]
    vis = set()
    
    while stack:
        curr = stack.pop()
        
        if curr in vis:
            return False
        
        vis.add(curr)
        totalNodesVisited += 1
        
        if leftChild[curr] != -1:
            stack.append(leftChild[curr])
        
        if rightChild[curr] != -1:
            stack.append(rightChild[curr])

    return totalNodesVisited == n


'''

Time complexity:
im lazy but first loop is O(n) then we just do dfs which is also O(n) so overall ---> O(n)


Space complexity:
we have dfs stack so overall ----> O(n)



'''