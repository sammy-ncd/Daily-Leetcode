"""

Problem:
https://leetcode.com/problems/subsets-ii/description/


"""


"""

Approach:
backtracking
constraint: dont add a duplicate subset
2 decisions
either add current num or skip it


"""



def subsetsWithDup(nums):
    
    n = len(nums)
    powerset = []
    nums.sort()

    def backtrack(start, sol):

        powerset.append(sol[:])

        for i in range(start, n):
            if i > start and nums[i] == nums[i - 1]: # 
                continue 

            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()

    backtrack(0, [])
    return powerset



"""
Time complexity:

There can be up to 2^n subsets.
For each subset, we copy sol using sol[:], which can take up to O(n).

Overall ---> O(n * 2^n)


Space complexity:

Recursion stack and current sol can go as deep as n.
So excluding output ---> O(n)

If counting the powerset output, we store up to 2^n subsets,
and each subset can have up to n elements.

Including output ---> O(n * 2^n)
"""