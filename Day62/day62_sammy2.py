"""

Problem:
https://leetcode.com/problems/subsets/description/


"""


"""

Approach:
recursively backtrack
loop through array, make 2 decisions, either add current number or dont
recurse on both decisions, make sure to pop before we choose to not add the number


"""



def subsets(nums):

    n = len(nums)
    powerset = []

    def backtrack(index, sol):
        if index == n:
            powerset.append(sol[:])
            return
        
        sol.append(nums[index])
        backtrack(index + 1, sol)
        sol.pop()
        
        backtrack(index + 1, sol)
    
    backtrack(0, [])
    return powerset



"""

Time complexity:

for each number we have to fully recursively backtrack
overall ---> O(n * 2^n)


Space complexity:

recursion stack, so overalll ---> O(n)


"""