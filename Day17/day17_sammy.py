'''


Problem:
https://leetcode.com/problems/palindrome-linked-list/


'''



"""

Approach:
Loop through LL create str of check if str is palindrome


"""


def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def isPalindrome(head):

    st = ""

    while head:
        st += str(head.val)
        head = head.next


    i = 0
    j = len(st) - 1

    while i < j:
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
        
    return True


"""

Time Complexity:
dominated by O(n) linked list scan so over all O(n)

Space Complexity:
O(n) string proportional to number of nodes


"""