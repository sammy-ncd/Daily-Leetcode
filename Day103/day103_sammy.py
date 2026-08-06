"""

Problem:
https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=daily-question&envId=2026-08-06


"""

"""

Approach:
brute force


"""


def smallestNumber(n: int, t: int) -> int:
    div = False
    while not div:
        strn = str(n)
        prod = 1 
        for c in strn:
            prod *= int(c)
        if prod % t == 0:
            return int(strn)
        n += 1



"""

Time complexity:
O((ans - n + 1) * log(ans))

We test every integer from n through ans, and computing the digit
product takes O(log(ans)) time.

Space complexity:
O(log(ans))

Converting each number to a string uses space proportional to its
number of digits.




"""