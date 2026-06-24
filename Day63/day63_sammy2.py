"""

Problem:
https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=backtracking

"""

"""

Approach:
backtrack
base case: stop when len(sol) = 2*n, n opening and n closing
decisions:
if we have < n opening parenthesis add one
if we have more opening than closing parens add a closing paren


"""



def generateParenthesis(n):
    res = []

    def backtrack(sol, left, right):

        if len(sol) == 2 * n:
            res.append(sol)
            return
        
        if left < n:
            backtrack(sol + "(", left + 1, right)
        if right < left:
            backtrack(sol + ")", left, right + 1)
            
    backtrack("", 0, 0)
    return res


"""

gpt cuz lazy

Time complexity:
O(4^n / sqrt(n)), because there are Catalan number many valid combinations.

Space complexity:
O(n) recursion stack excluding output.
O(n * 4^n / sqrt(n)) including output.

"""