"""

Problem:
https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2026-07-13


"""


"""

Approach:
generate all possible sequential digit numbers in range low to high


"""


def sequentialDigits(low: int, high: int):
    res = []
    nums = "123456789"
    for length in range(len(str(low)), len(str(high)) + 1):
        for i in range(len(nums) - length + 1):
            curr_num = int(nums[i:i + length])
            if low <= curr_num <= high:
                res.append(curr_num)
    return res


"""

Time complexity:

There are at most 9 digit lengths, and for each length we check at most 9 substrings.
Converting each substring to an integer takes O(d), where d is the number of digits.

Overall ---> O(d^2)

Since d <= 9 for this problem, this is effectively O(1).


Space complexity:

The result stores at most 36 sequential-digit numbers.

Overall ---> O(1)



"""