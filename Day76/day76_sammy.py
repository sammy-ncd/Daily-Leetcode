"""

Problem:
https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/?envType=daily-question&envId=2026-07-07


"""


"""

Just follow problem instructions


"""


def sumAndMultiply(n: int) -> int:
    if n == 0:
        return 0
    x = str(n).replace("0", "")
    xsum = sum(int(dig) for dig in x)
    return int(x) * xsum


"""

Time complexity:
O(d), where d is the number of digits in n

Space complexity:
O(d), because we create string x


"""