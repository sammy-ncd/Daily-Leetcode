"""

Problem:
https://leetcode.com/problems/design-linked-list/description/


"""

"""

Approach:
Dont fucking do this one, its such a pain in the ass


"""



class MyLinkedList(object):

    class ListNode:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None
        

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        
        if self.head:
            node = self.ListNode(val, None, self.head)
            self.head = node
            self.head.next.prev = self.head
        else:
            self.head = self.ListNode(val, None, None)
            self.tail = self.head

        self.size += 1 

    def addAtTail(self, val):
        
        node = self.ListNode(val, self.tail, None)

        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.size += 1

    def addAtIndex(self, index, val):
        
        if index < 0 or index > self.size:
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            node = self.ListNode(val, curr.prev, curr)
            curr.prev.next = node
            curr.prev = node
            self.size += 1 

    def deleteAtIndex(self, index):
        if index < 0 or index > self.size - 1:
            return
        
        if index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        elif index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        
        self.size -= 1 
        



"""

Time:

O(n) get
O(1) addAtHead
O(1) addAtTail
O(n) addAtIndex
O(n) deleteAtIndex


Space:

O(1) extra space per operation
O(n) total space for the linked list

"""