"""

Problem:
https://leetcode.com/problems/walking-robot-simulation/description/


"""


"""

Approach:

Simply code the simulation as is (brute force)
However store obstacles in a set for fast lookup

"""


def robotSim(commands, obstacles):

    maxDist = 0

    obs = set()
    for o in obstacles:
        obs.add((o[0], o[1]))

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0

    pos = (0, 0)

    for cmd in commands:

        if cmd == -1:
            d = (d + 1) % 4
        
        if cmd == -2:
            d = (d - 1) % 4

        while cmd > 0:

            dx, dy = dirs[d]
            x, y = pos[0] + dx, pos[1] + dy

            if (x, y) in obs:
                break

            maxDist = max(maxDist, x * x + y * y)
            pos = (x, y)
            cmd -= 1

    return maxDist


"""

let n = # of commands
let m = # of obstacles
let k = # total steps across all commands


Time Complexity:

    Total time ---> O(m + n + k)

    
Space Complexity:

    Total space ---> O(m)

"""