'''

Problem:
https://leetcode.com/problems/rotated-digits/description/?envType=daily-question&envId=2026-05-01

'''



"""

Approach:
Build the rotated numbers check if they are good based on their requirements.

"""


def rotatedDigits(n):
    valid = {'0': '0', 
             '1': '1', 
             '2': '5', 
             '3': False, 
             '4': False,
             '5': '2', 
             '6': '9', 
             '7': False, 
             '8': '8', 
             '9': '6'}
    
    def isGood(s):
        st = ''
        for c in s:
            if type(valid[c]) == str:
                st += valid[c]
            else:
                return False
        if int(s) != int(st): return True
        else: return False

    good = 0
    for i in range(1, n + 1):
        s = str(i)
        if (isGood(s)):
            good += 1

    return good

print(rotatedDigits(10))


"""

Time complexity:
For n numbers we create each of their rotated versions to create this rotation
it depends on the number of digits in the number so scales logarithmically
overall: O(nlogn)

Space complexity:
both s and st store rotated number so overall O(logn) space 

"""