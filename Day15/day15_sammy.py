"""

Problem:
https://leetcode.com/problems/separate-the-digits-in-an-array/?envType=daily-question&envId=2026-05-12


"""


"""

Approach:
Build string of each number pull digits out append to res arr

"""


def separateDigits(nums):

    res = []

    for num in nums:
        s = str(num)
        for c in s:
            res.append(int(c))

    print(res)
    return res


"""

Time complexity:
Loop through nums ---> O(n)
Loop through string ---> O(d), d is number of digits
Total ---> O(n * d)

Space complexity:
Overall ----> O(n * d) same reasoning as time

"""