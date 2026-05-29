'''

Problem:
https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-25


'''


"""


Aproach:
Store occurences of lowercase and upper case in alphabetical order
do a parallel sweep of lower and upper arrays to see if we have seen both cases of a letter


"""



def numberOfSpecialChars(word):
    special = 0

    lower = [0] * 26
    upper = [0] * 26 
    
    for c in word:
        val = ord(c) 

        if val >= 97:
            lower[val - ord('a')] += 1
        else:
            upper[val - ord('A')] += 1
    
    for i in range(len(lower)):
        if lower[i] > 0 and upper[i] > 0:
            special += 1
    
    return special


"""

Time Complexity:
O(n) sweep through word
O(26) sweep through lower and upper 
so overall ---> O(n)


Space Complexity:
lower and upper array are both O(26)
so overall ---> O(1)


"""