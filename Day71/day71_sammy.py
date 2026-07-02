"""

Problem:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


"""

"""

Approach:
since its sorted we start at both ends (two pointers)
if sum of numbers at pointers < target move the left pointer up we need a bigger sum
if sum of numbers at pointers > target move the right pointer down we need a smaller sum
other wise return the indicies


"""


def twoSum(numbers, target):
    n = len(numbers)
    i = 0
    j = n - 1
    while i < j:
        curSum = numbers[i] + numbers[j]
        if curSum < target:
            i += 1
        elif curSum > target:
            j -=1
        else:
            return [i + 1, j + 1]
        

"""

Time complexity:

O(n)


Space complexity:

O(1)



"""