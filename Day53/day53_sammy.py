"""

Problem:
https://leetcode.com/problems/implement-stack-using-queues/description/


"""


"""

Approach:

cycle = dequeue then enqueue again

Use one queue
append(x) ---> enqueue x to the queue
pop() ---> cycle through the queue n-1 time then remove and return the top
top() ---> cycle through the queue n time then return the last element that was cycled through
empty ---> return len queue


"""


from collections import deque


class MyStack(object):

    def __init__(self):
        self.data = deque()
        

    def push(self, x):
        self.data.append(x)
        

    def pop(self):
        for _ in range(len(self.data) - 1):
            x = self.data.popleft()
            self.data.append(x)
        
        return self.data.popleft()

    def top(self):
        for _ in range(len(self.data)):
            top = self.data.popleft()
            self.data.append(top)
        
        return top
        

    def empty(self):
        return len(self.data) == 0
        

"""

Time complexity:

init ---> O(1)
push ---> O(1)
pop ---> O(n)
top ---> O(n)
empty ---> O(1)

Space complexity:

push ---> O(1)
pop ---> O(1)
top ---> O(1)
empty ---> O(1)
O(n) for the stack itself


"""