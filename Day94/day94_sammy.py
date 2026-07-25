"""

Problem:
https://leetcode.com/problems/maximum-product-of-two-digits/description/?envType=daily-question&envId=2026-07-25


"""


"""

Approach:
find the 2 max nums and return their product


"""


def maxProduct(n: int) -> int:
    strnum = str(n)
    maxNumIdx = 0
    for i in range(len(strnum)):
        if strnum[i] > strnum[maxNumIdx]:
            maxNumIdx = i
    secondMaxNum = 0
    for i in range(len(strnum)):
        if i != maxNumIdx:
            secondMaxNum = max(secondMaxNum, int(strnum[i]))
    return int(strnum[maxNumIdx]) * secondMaxNum


"""

let n be the number of digits in n


Time complexity:

need to do 2 sweeps of array, so overall ---> O(n)


Space complexity:

nothing stored, so overall ---> O(1)


"""