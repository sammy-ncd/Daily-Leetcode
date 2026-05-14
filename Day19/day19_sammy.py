"""

Problem:
https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14


"""



"""

Approach: add n to the sum of all numbers in range [1,n]
          for each number in nums subtract from that sum
          if we have 0 return true else false
          have map to validate all numbers were seen once


"""


def isGood(nums):

        d = {}
        n = max(nums)
        total = 0
        
        for i in range(1, n + 1):
            total += i
            d[i] = False
        
        for num in nums:
            d[num] = True
            total -= num
        
        total += n
        
        for i in range(1, n + 1):
            if not d[i]:
                return False
        
        if total == 0 and nums.count(n) == 2:
            return True
        else:
            return False
        

"""

Time complexity: 

make dict and sum ---> O(n)
scan through dict ---> O(n)

Overall ---> O(n)


Space complexity:

make dict ---> O(n)

Overall ---> O(n)

"""