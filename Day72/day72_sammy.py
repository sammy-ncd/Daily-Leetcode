"""

Problem:
https://leetcode.com/problems/count-digit-appearances/description/


"""

"""

convert num for num in nums to a string
add occurences of digit in num to counter


"""



def countDigitOccurrences(nums: list[int], digit: int) -> int:    
    counts = 0
    for num in nums:
        s = str(num)
        counts += s.count(str(digit))
    return counts


"""
Time complexity:

Let D = total number of digits across all numbers.
Converting each number to a string and counting the digit scans the digits.
overall ---> O(D)

Space complexity:

Each string conversion takes space proportional to the number of digits
in the current number.
overall ---> O(d), where d is the max number of digits in one number.

"""