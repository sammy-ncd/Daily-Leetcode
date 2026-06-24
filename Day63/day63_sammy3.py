"""

Problem:
https://leetcode.com/problems/combinations/description/?envType=problem-list-v2&envId=backtracking


"""

"""

Approach:
Backtrack

basecase:
if current combination is of len k

choices:
either add current number
or dont add current number


"""


def combine(n, k):
    combinations = []

    def backtrack(start, sol):
        if len(sol) == k:
            combinations.append(sol[:])
            return
        
        for i in range(start, n + 1):
            sol.append(i)
            backtrack(i + 1, sol)
            sol.pop()
    
    backtrack(1, [])
    return combinations



"""

Time complexity:

there are C(n, k) valid combos copying solutions [:] takes O(k) time
overall ---> O(k * C(n, k))

Space complexity:
excluding output overall ---> Space: O(k)


"""