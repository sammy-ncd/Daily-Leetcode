'''

Problem:
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=daily-question&envId=2026-06-14


'''


'''

Approach:
Store linked list into array
compute twin sums via indexing


'''


def pairSum(head):
    ll = []

    while head:
        ll.append(head.val)
        head = head.next

    maxTwinSum = float("-inf")
    n = len(ll)

    for i in range(n // 2):
        maxTwinSum = max(maxTwinSum, ll[i] + ll[n - 1])
        n -= 1 

    return maxTwinSum


"""

Time Complexity:

O(n) build list
O(n) compute twin sums
Overall ---> O(n)

Space Complexity:

O(n) build list
Overall ---> O(n)

"""