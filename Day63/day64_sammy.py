"""

Problem:
https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking


"""

"""

Approach:
backtrack
base case: we have tried all fixed positions
choices:
for a fixed position swap with all other positions
undo the swap before moving onto the next choice


"""



def permute(nums):

    n = len(nums)
    permutations = []

    def backtrack(start):
        
        # once we have gone through all fixed positions
        if start == n:
            permutations.append(nums[:])
            return
        
        for i in range(start, n):
            # swap fixed position with nums[i]
            nums[i], nums[start] = nums[start], nums[i]
            backtrack(start + 1)
            # undo swap so we can swap with next number
            nums[i], nums[start] = nums[start], nums[i]
    
    backtrack(0)        
    return permutations


"""

Time complexity:

there are n! permuatations
for each permutation we copy the array into the output array

so overall ----> O(n * n!)


Space complexity:

for the same reasons as above

overall ----> O(n * n!)


"""