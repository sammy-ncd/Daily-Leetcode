'''

Problem:
https://leetcode.com/problems/course-schedule/description/


'''



"""

Approach:
create and adjacency list of the form course ---> [prereqs]
track already visited courses and courses along the current dfs path
if while exploring a path we encounter a cycle return false because we will have a prereq that cannot be completed
otherwise if we get through and see no cycles we can complete all the prereqs


"""



def canFinish(numCourses, prerequisites):

    # construct adjacency list
    adj = [[] for _ in range(numCourses)]

    for pre, course in prerequisites:
        adj[course].append(pre)

    # init visited array and visiting set
    visited = [False for _ in range(numCourses)]
    visiting = set()

    def dfs(course):

        # if we encounter a course for the second time in its dfs path we have a cycle
        if course in visiting:
            return False
        
        # if the course' prereq chain is safe then we can continue
        if visited[course]:
            return True
        
        # add the current course the the prereq chain
        visiting.add(course)
        
        # dfs down all the prereqs return false immediately if one of the prereqs is in a cycle
        for pre in adj[course]:
            if not dfs(pre):
                return False
            
        visiting.remove(course)
        visited[course] = True

        return True

    # graph may not be connected so make sure to dfs each subgraph
    for course in range(numCourses):

        if not dfs(course):
            return False
        
    return True



"""

let V = number of courses in the graph
let E = number of course --> prereq connections in the graph

Time complexity:

All of the runtime comes down to DFS on the entire graph so this is O(V + E) time

Space complexity:
The largest thing we are storing is our graph (adjacency list) so overall space ---> O(V + E)


"""