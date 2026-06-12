"""

Problem:
https://leetcode.com/problems/baseball-game/description/


"""


"""

Approach:
Use a stack to keep track of operations


"""



def calPoints(operations):
    
    record = []
    
    for op in operations:
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(record[-1] * 2) 
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
    
    return sum(record)


"""

Time Complexity:

just one pass through the operations string, so overall ---> O(n)


Space Complexity
:
stack could hold a element for each char in operations, so overall ---> O(n)


"""