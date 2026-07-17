"""

Problem:
https://leetcode.com/problems/keys-and-rooms/description/


"""


"""

Approach:
Just dfs then check if size of visited set == number of rooms


"""


def canVisitAllRooms(rooms) -> bool:
    vis = set([0])
    stack = [0]
    while stack:
        curr = stack.pop()
        for neigh in rooms[curr]:
            if neigh not in vis:
                stack.append(neigh)
                vis.add(neigh)
    return len(vis) == len(rooms)


"""

let n be the number of rooms and k be the total number of keys


Time complexity:

visit each room once and check each key once so overall ---> O(n + k)


Space complexity:

vis can contain n rooms, so overall ---> O(n)


"""