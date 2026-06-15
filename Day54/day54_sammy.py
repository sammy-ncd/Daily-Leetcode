'''

Problem:
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=daily-question&envId=2026-06-14


'''


'''

Approach:
Use slow and fast pointers to get to the middle of the linked list
keep track of prev on the slow pointer
then just perform the deletion

'''


def deleteMiddle(head):
    if not head or not head.next:
        return None
    
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    slow.next = None
    return head


'''

Time Complexity:

n/2 is still n in big O
so slow/fast pointers ---> O(n)
overall ---> O(n)


Space Complexity:
deletion is done in place, so overall ---> O(1)

'''