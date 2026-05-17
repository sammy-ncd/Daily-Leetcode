'''


Problem:
https://leetcode.com/problems/climbing-stairs/description/


'''


"""

Approach:
To calculate the number of ways to get to the ith step we need the 
sum of the way to get to the twp previous steps.


"""


def climbStairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


"""

Time complexity:
linear scan through each value up to n ---> Overall: O(n)

Space complexity:
using a dp list ---> Overall: O(n)

"""