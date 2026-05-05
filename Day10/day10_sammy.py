'''

Problem:
https://leetcode.com/problems/rotate-list/?envType=daily-question&envId=2026-05-05


'''


'''

Convert data into a deque rotate deque k times. Assign head and tail at the end.

'''

from collections import deque


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):

    nodes = []
    curr = head
    
    while curr != None:
        nodes.append(curr)
        curr = curr.next

    if len(nodes) == 0 or k == 0:
        return head
    
    d = deque(nodes)
    d.rotate(k)
    nodes = list(d)

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    head = nodes[0]
    nodes[len(nodes)-1].next = None

    return head


"""

Time complexity:
O(n) to build nodes array
O(n) to build deque
O(n) max for rotating
O(n) reconnecting linked list

Overall --> O(n)

Space complexity:
O(n) = nodes
O(n) = d
Overall --> O(n)

"""


def printLL(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next


five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

#t2 = ListNode(2, None)
o1 = ListNode(1, None)
zero = ListNode(0, o1)

#printLL(one)
printLL(rotateRight(one, 2))
print()
printLL(rotateRight(zero, 1))