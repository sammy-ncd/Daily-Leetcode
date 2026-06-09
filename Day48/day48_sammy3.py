"""

Problem:
https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=problem-list-v2&envId=simulation


"""


"""

Approach:
If char isnt a '*' push to stack
if it is pop from stack
return string stored in stack


"""



def removeStars(s):

    ret = []
    
    for c in s:
        if c == '*':
            ret.pop()
        else:
            ret.append(c)
            
    return "".join(ret)


"""

Time complexity:

loops through whole string so overall ---> O(n)


Space complexity:

stack could hold n non '*' characters ---> O(n)


"""