'''

Problem:
https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/?envType=daily-question&envId=2026-05-25


'''



'''

Approach:

1. initialize 2 arrays one for storing the index of the last occurrence of each lowercase letter
   and the second for storing the earliest index of each uppercase letter

2. loop through the letters in word
    - if its lowercase store the index for that letter
    - if its uppercase and we have seen it before dont store the index
    - its its upper case and we havent seen it before store the index

3. finally do a loop over both the lower and upper array in parallel to check over both versions of a letter
   if the index of the lower case letter is < its uppercase version increment the number of special characters by one

4. return the number of special characters


'''


def numberOfSpecialChars(word):
    special = 0

    lower = [-1] * 26
    upper = [-1] * 26 
    seen = set()

    for i in range(len(word)):
        
        val = ord(word[i]) 
        
        if val >= 97: # check if char is lowercase
            lower[val - ord('a')] = i
        elif val - 32 in seen:
            continue
        else:
            upper[val - ord('A')] = i
            seen.add(val - 32)
    
    for i in range(len(lower)):
        if lower[i] < upper[i] and lower[i] != -1 and upper[i] != -1:
            special += 1
    
    return special


"""

Time Complexity:

loop through the word to build upper and lower arrays -> O(n)
final loop through upper and lower arrays -> O(26)
Overall ---> O(n)


Space Complexity:

lower array --> O(26)
upper array --> O(26)
seen stores at most all uppercase english letters -> O(26)


Overall ---> O(1)

"""