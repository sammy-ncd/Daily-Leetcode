"""

Problem:
https://leetcode.com/problems/combination-sum/description/


"""

"""

Approach:
2 decisions:
either add the same number 
or add the next number in the array


"""


# original solution
def combinationSum(candidates, target):
        combos = []
        n = len(candidates)

        def backtrack(sol, index):

            # if current path sum > target break this branch
            if sum(sol) > target:
                return

            # if our index is out of bounds break this branch
            if index == n:
                return

            # if our current path sum == target add to result array
            if sum(sol) == target:
                combos.append(sol[:])
                return

            # keep using the same number
            sol.append(candidates[index])
            backtrack(sol, index)
            sol.pop()
            # move to the next number
            backtrack(sol, index + 1)
                
        backtrack([], 0)
        return combos


# optimized soltion
def combinationSum(candidates, target):
        combos = []
        n = len(candidates)

        def backtrack(sol, index, total):

            if total > target:
                return

            if index == n:
                return

            if total == target:
                combos.append(sol[:])
                return

            sol.append(candidates[index])
            # yes add the same number to the total
            backtrack(sol, index, total + candidates[index])
            sol.pop()
            # dont add the same number to the total
            backtrack(sol, index + 1, total) # this is why I just pass in total
                
        backtrack([], 0, 0)
        return combos


# for loop solution
def combinationSum(candidates, target):
        combos = []
        n = len(candidates)

        # start param essentially tells us which range of numbers we can choose from
        def backtrack(sol, start, total):

            if total > target:
                return

            if total == target:
                combos.append(sol[:])
                return

            # since we want only unique solutions, we never look backwards
            # the loop automatically moves for us when the base cases are triggered
            for i in range(start, n):
                sol.append(candidates[i])
                backtrack(sol, i, total + candidates[i])
                sol.pop()
                
        backtrack([], 0, 0)
        return combos


"""

Time complexity:

let m = the minimum value in the input array
let t = the target

since the smallest value can be repeated several times
total runtime is ---> O(n^(t/m))

Space complexity:

not including the output, and for the same reason above
total space ---> O(t/m)



"""