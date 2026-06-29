"""

Problem:
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/?envType=daily-question&envId=2026-06-29


"""

"""

Approach:
bro


"""


def numOfStrings(patterns, word) -> int:
    count = 0
    for p in patterns:
        if p in word:
            count += 1
    return count


"""

let n = len of patterns
let m = len of word

Time complexity:

overall ---> O(mn)

Space complexity:

overall ---> O(1)


"""