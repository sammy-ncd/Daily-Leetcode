'''

Problem:
https://leetcode.com/problems/mirror-distance-of-an-integer/?envType=daily-question&envId=2026-04-27


'''

'''

Approach: Keep peeling off the last digit in n and moving it to the first position
          of a newly constructed integer, then simply perform the needed subtraction.

'''


def mirrorDistance(n):
    rev = 0
    while (n % 10 != n):
        rev *= 10
        rev += (n % 10)
        n //= 10
    rev *= 10
    rev += n
    return abs(n - rev)

print(mirrorDistance(51))
print(mirrorDistance(29))
print(mirrorDistance(26))

"""

Time Complexity: O(logn) --> log base 10 depends on how many digits the integer is.
Space Complexity: O(1) --> Only uses ints to store the reversed number.

"""