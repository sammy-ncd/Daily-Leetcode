"""

Problem:
https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=linked-list

"""



"""

Approach: 
Keep a visited map if we ever come back to a visited node return true
otherwise if we reach the end return false

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):    
    curr = head

    visited = {}

    while (curr != None):
        try:
            visited[curr]
            return True
        except KeyError:
            visited[curr] = 0
            curr = curr.next
    return False


four = ListNode(-4)
three = ListNode(0).next = four
two = ListNode(2).next = three
one = ListNode(3).next = two
four.next = two

print(hasCycle(one))

"""
Time: O(n) at most one entire pass through the linked-list
Space: O(n) map might hold all nodes if no cycle

"""