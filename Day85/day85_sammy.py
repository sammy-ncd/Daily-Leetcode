"""

Problem:
https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/description/?envType=daily-question&envId=2026-07-16


"""

"""

Approach:
code the simulation as is 
to optimally find the max keep a current max and compare as we traverse nums


"""

import math

def gcdSum(nums: list[int]) -> int:
    prefixGcd = []
    maxSoFar = 0
    for num in nums:
        maxSoFar = max(maxSoFar, num)
        prefixGcd.append(math.gcd(num, maxSoFar))
    prefixGcd.sort()
    gcdSum = 0
    i = 0
    j = len(prefixGcd) - 1
    
    while i < j:
        gcdSum += math.gcd(prefixGcd[i], prefixGcd[j])
        i += 1
        j -= 1
    return gcdSum


"""

Time complexity:

Building prefixGcd takes O(n log M), where M is the largest number
Sorting takes O(n log n)
Pairing the elements takes O(n log M)

Overall ---> O(n log n + n log M)


Space complexity:

prefixGcd stores n elements

Overall ---> O(n)


"""