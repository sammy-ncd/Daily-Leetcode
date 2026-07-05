"""

Problem:
https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/


"""

"""

Approach:
in the code


"""


def minOperations(n: int) -> int:
        # sum first n odd numbers = n^2
        # we want to convert the left half to the median
        # and the right half to the median
        # so total ops will be (n / 2)^2
        # interested in the total for half of the odd numbers
        return (n * n) // 4


"""

Time complexity:
just math so overall ---> O(1)

Space complexity:
nothing stored so overall ---> O(1)


"""