'''

Problem:
https://leetcode.com/problems/min-stack/


'''


"""

Approach:
Keep a stack for actual data
Keep a second stack for current minimum at given state of the stack


"""


class MinStack(object):

    def __init__(self):
        self.data = []
        self.history = []
        self.minValue = float("inf")
        

    def push(self, value):
        
        if self.data:
            if value <= self.minValue:
                self.minValue = value
        else:
            self.minValue = value

        self.history.append(self.minValue)
        self.data.append(value)


    def pop(self):

        val = self.data.pop()
        self.history.pop()
        
        if val == self.minValue:
            if self.history:
                self.minValue = self.history[-1]
            else:
                self.minValue = float("inf")

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.minValue
    


"""

Time Complexity:

By design all operations are O(1)

push --> O(1)
pop --> O(1)
top --> O(1)
getMin --> O(1)

Overall --> O(1) per operation

Space Complexity:
O(n) for actual data
O(n) for minimum history stack

Overall --> O(n)

"""