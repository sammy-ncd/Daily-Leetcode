"""

Problem:
https://leetcode.com/problems/linked-list-cycle-ii/?envType=problem-list-v2&envId=linked-list

"""



"""

Approach: 
Keep a visited map if we ever come back to a visited node return that node
otherwise if we reach the end return -1

loooooooooooool this one is identical pretty much

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):    
    curr = head

    visited = {}

    while (curr != None):
        try:
            visited[curr]
            return curr
        except KeyError:
            visited[curr] = 0
            curr = curr.next
    return None


four = ListNode(-4)
three = ListNode(0).next = four
two = ListNode(2).next = three
one = ListNode(3).next = two
four.next = two

print(two)
print(detectCycle(one))


"""
Time: O(n) at most one entire pass through the linked-list
Space: O(n) map might hold all nodes if no cycle

"""