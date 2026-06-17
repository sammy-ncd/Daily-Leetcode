"""

Problem:
https://leetcode.com/problems/merge-k-sorted-lists/description/


"""

"""

Approach:
have a merge function for 2 linked lists
then repeatedly merge lists in pairs, merging those pairs in pairs


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def mergeKLists(lists):

    def merge(list1, list2):

        dummy = ListNode(-420, None)
        head = ListNode(-69, dummy)

        while list1 and list2:

            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        dummy.next = list1 if list1 else list2
        
        return head.next.next
    

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists) - 1, 2):
            head = merge(lists[i], (lists[i + 1]))
            merged.append(head)
        
        if len(lists) % 2 != 0:
            merged.append(lists[-1])

        lists = merged
    
    if not lists:
        return None
    
    return lists[0]


"""

let n = total number of nodes across all lists

Time complexity:

we keep splitting the number of lists in half because we merge pairs to already merged pairs

so overall ---> O(nlogk)


Space complexity:

merged list will be size k/2 during first merges

so overall ---> O(k)


"""