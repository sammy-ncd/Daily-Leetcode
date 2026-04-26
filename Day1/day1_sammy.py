'''

Problem:
https://leetcode.com/problems/furthest-point-from-origin/?envType=daily-question&envId=2026-04-26


'''

"""

My plan: 

step through string and keep 2 count where 'L' will +1 and 'R' will -1 from count
for count one let all '_' add 1 to count
for count two let all '_' minus 1 to count
take greatest count in absolute value at the end and return it

"""

def furthestDistanceFromOrigin(moves): # Totally correct approach, can code it simpler.
    count1 = 0
    count2 = 0
    for move in moves:
        if move == 'L':
            count1 += 1
            count2 += 1
        elif move == 'R':
            count1 -= 1
            count2 -= 1
        else:
            count1 -= 1
            count2 += 1
    return max(abs(count1), abs(count2))

print(furthestDistanceFromOrigin("L_RL__R"))
print(furthestDistanceFromOrigin("_R__LL_"))
print(furthestDistanceFromOrigin("_______"))


"""Exact same idea just simpler code"""

def furthestDistanceFromOrigin2(moves):
    return abs(moves.count("L") - moves.count("R")) + moves.count("_")

print(furthestDistanceFromOrigin2("L_RL__R"))
print(furthestDistanceFromOrigin2("_R__LL_"))
print(furthestDistanceFromOrigin2("_______"))


"""

Runtime analysis:
Both codes run in O(n) time first one just does a for loop over each char in the str.
second code grabs counts of each character which is just a linear scan

Space Complexity:
First code is O(1) constant complexity just stores data in 2 ints
Second code is O(1) doesnt store anything 

"""
