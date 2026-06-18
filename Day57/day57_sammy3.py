"""

Problem:



"""

"""

Approach:
Binary search


"""

import random


n = int(input("pick n: "))
pick = random.randint(1, n)

def guess(attempt):
    if attempt > pick:
        return -1
    elif attempt < pick:
        return 1
    else:
        return 0

def guessNumber(n):

    lo = 1
    hi = n

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        g = guess(mid)
        
        if g == -1:
            hi = mid - 1
        elif g == 1:
            lo = mid + 1
        else:
            return mid
        
print(guessNumber(n))


"""

Time complexity:

Just binary search, so overall ----> O(logn)


Space complexity:

constant, overall ---> O(1)


"""