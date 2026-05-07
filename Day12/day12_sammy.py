'''

Problem:
https://leetcode.com/problems/plus-one/description/

'''



"""

Approach create string of integer 

"""


def plusOne(digits):

    s = ""
    for dig in digits:
        s += str(dig)
    
    s = str(int(s) + 1)
    return [int(ch) for ch in s]



print(plusOne([1,2,3]))
print(plusOne([4,3,2,2]))
print(plusOne([1,0]))
print(plusOne([9,9,9,9]))


"""

Time complexity:
O(n) one scan to build int
O(n) build array from str

Overall --> O(n)


Space Complexity:
just a string so O(n)

"""