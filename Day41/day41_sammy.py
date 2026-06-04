'''

Problem:
https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/?envType=daily-question&envId=2026-06-02


'''



"""

Approach:
Brute Force


"""


def totalWaviness(num1, num2):
    waviness = 0
    
    if num2 <= 100:
        return waviness
    
    if num1 < 100:
        num1 = 100

    for num in range(num1, num2 + 1):
        s = str(num)
        
        for i in range(1, len(str(num)) - 1):

            left, curr, right = int(s[i - 1]), int(s[i]), int(s[i + 1])
            
            if (left < curr) and (right < curr):
                waviness += 1
            
            if (left > curr) and (right > curr):
                waviness += 1
    
    return waviness


"""

n = num2 - num1 - 1
d = number of digits in num 2

Time complexity:

O(n*d)

Space complexity:

d = number of digits in current s

overall ---> O(d)


"""