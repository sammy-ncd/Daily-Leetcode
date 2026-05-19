"""

Problem:
https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-05-19

"""



"""

Approach:
Check that we have performed both same number of up and down moves 
as well as left and right moves in this case we must have come back to the origin.

"""


def judgeCircle(moves):
    dirs = {
        'U' : 0,
        'D' : 0,
        'L' : 0,
        'R' : 0
    }
    
    for move in moves:
        dirs[move] += 1
    
    return dirs['U'] == dirs['D'] and dirs['L'] == dirs['R']


"""

Time complexity:
simply looping through the string ----> Overall: O(n)


Space complexity:
just very small hashmap used its negligable ----> Overall: O(1)


"""