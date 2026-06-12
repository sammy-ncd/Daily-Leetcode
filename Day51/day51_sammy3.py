"""

Problem:
https://leetcode.com/problems/design-browser-history/


"""



"""

Approach:
Doubly linked list


"""


class Node():
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class BrowserHistory(object):

    def __init__(self, homepage):
        self.homePage = Node(homepage, None, None)
        self.currPage = self.homePage
        

    def visit(self, url):
        newPage = Node(url, self.currPage, None)
        self.currPage.next = newPage
        self.currPage = newPage

        
    def back(self, steps):
        curr = self.currPage
        
        while curr != self.homePage and steps > 0:
            curr = curr.prev
            steps -= 1

        self.currPage = curr

        return curr.val


    def forward(self, steps):
        curr = self.currPage

        while curr.next and steps > 0:
            curr = curr.next
            steps -= 1

        self.currPage = curr
        
        return curr.val
    

"""

Time Complexity:

init ---> O(1)
visit ---> O(1)
back ---> O(n)
forward ---> O(n)

Space Complexity:

init ---> O(1)
visit ---> O(1)
back ---> O(1)
forward ---> O(1)


"""