"""

Problem:
https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/?envType=daily-question&envId=2026-07-15


"""

"""

Approach:
a little bit of number theory
sum of first odd numbers ---> n^2
sum of first even numbers ---> n(n+1)


"""

import math


def gcdOfOddEvenSums(n: int) -> int:
    return math.gcd(n**2, n*(n+1))

def gcdOfOddEvenSums_optimal(n):
    return n


"""

Time complexity:

depends on how long it takes to compute the gcd, so overall ---> O(gcd(sumOdd, sumEven))


Space complexity:

nothing stored so overall ---> O(1)

Optimal:

why its possible because gcd(sumOdd, sumEven) = n
because they are coprime gcd(n, n+1) = 1

Time and space O(n)


"""