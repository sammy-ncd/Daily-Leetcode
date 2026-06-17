"""

Problem:
https://leetcode.com/problems/merge-two-sorted-lists/description/


"""

"""

Approach:
keep a dummy node to build on perform comparisons and add to the dummy node
make sure to get remaning nodes if they exist in the case the linked lists are different sizes


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(-1, None)
        head = ListNode(-69, dummy)

        while list1 and list2:

            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        while list1:
            dummy.next = list1
            dummy = dummy.next
            list1 = list1.next

        while list2:
            dummy.next = list2
            dummy = dummy.next
            list2 = list2.next     

        return head.next.next
    

"""

Let m = len list 1
Len n = len list 2

Time Complexity:

O(m + n) need to get all elements


Space Complexity:

only use some dummy pointers so overall ----> O(1)


"""