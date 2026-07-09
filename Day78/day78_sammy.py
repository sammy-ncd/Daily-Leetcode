"""

Problem:
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/


"""

"""

Approach:
just follow the problem description


"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []
        

    def push(self, x: int) -> None:
        if len(self.data) + 1 > self.maxSize:
            return
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop() if self.data else -1


    def increment(self, k: int, val: int) -> None:
        if len(self.data) < k:
            for i in range(len(self.data)):
                self.data[i] += val
        else:
            for i in range(k):
                self.data[i] += val

"""

Time complexity:

push ---> O(1)
pop ---> O(1)
increment ---> O(n) // potentially increment all elements

Space complexity:

let n = maxSize if we have maxsize elements overall ---> O(n)


"""