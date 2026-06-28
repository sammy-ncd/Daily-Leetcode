"""

Problem:
https://leetcode.com/problems/design-circular-deque/description/


"""


"""

Approach:
I used a doubly-linked list
could also use a circular array


"""



class Node:
    

    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next

class MyCircularDeque:


    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(None, value, None)
        
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(None, value, None)
        
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        self.tail = self.tail.prev
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        self.head = self.head.next
        return True


    def getFront(self) -> int:
        return -1 if self.size == 0 else self.tail.val
        

    def getRear(self) -> int:
        return -1 if self.size == 0 else self.head.val


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
    
"""

Time complexity:
all operations are O(1) so overall ---> O(1

Space complexity:
it can have up to k nodes so overall ---> O(k)


"""