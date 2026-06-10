"""

Problem:
https://leetcode.com/problems/reverse-linked-list/


"""



"""

Approach:
in place reversal by keeping track of prev pointer


"""



def reverseList(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev



"""

Time:
O(n) just one pass


Space:
O(1) only a few pointers

"""