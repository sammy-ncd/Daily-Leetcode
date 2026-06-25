"""

Problem:
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/


"""


"""

Approach:
traverse by two nodes
take gcd
when we insert make sure we move to the node to the right of the insertion point

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertGreatestCommonDivisors(head):
    def compute_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    curr = head
    while curr and curr.next:
        val = compute_gcd(curr.val, curr.next.val)
        node = ListNode(val, curr.next)
        curr.next = node
        curr = node.next
    
    return head



"""

Time complexity:

this is treating gcd as constant time
adding is O(1)
traverse linked list O(n)
so overall ---> O(n)

Space complexity:
n-1 nodes added (one node between each pair) so overall ---> O(n)


"""