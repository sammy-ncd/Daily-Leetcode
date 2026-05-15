"""

Problem:
https://leetcode.com/problems/guess-number-higher-or-lower/


"""


"""

Approach:
Literally just do binary search


"""

def guess():
    pass

def guessNumber(n):

    l = 1
    r = n

    while (l < r):
        
        mid = (l + r) // 2
        
        if guess(mid) == 0: return mid

        if guess(mid) == -1:
            r = mid - 1
        
        if guess(mid) == 1:
            l = mid + 1
    
    return l


"""

Time complexity:
just binary search --> O(logn)

Space complexity:
nothing stored --> O(1)


"""