"""

Problem:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=backtracking


"""

"""

Approach:
backtrack
base case: stop when we finish looping through all digits
choices: for each letter mapped to a digit pick one and move on
no need to pop because we want every single combo


"""


def letterCombinations(digits):
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    n = len(digits)
    res = []

    def backtrack(index, sol):
        
        if index == n:
            res.append(sol)
            return
        
        for letter in phoneMap[digits[index]]:
            backtrack(index + 1, sol + letter) 
    
    backtrack(0, "")
    return res



"""

Time complexity:

there are up to 4^n combos and each str can have length n
so overall ---> O(4^n)


Space complexity:

same reasons as above
excluding recursion stack ---> O(4^n)


"""