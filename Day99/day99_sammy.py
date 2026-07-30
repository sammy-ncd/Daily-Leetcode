"""

Problem:
https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/?envType=daily-question&envId=2026-07-30


"""

"""

Essentially perform a counting sort on the input string sorting by lexicographical order
then build result string by building half then mirroring this half using the sorted letters


"""


def smallestPalindrome(s: str) -> str:
    counts = [0] * 26
    for letter in s:
        counts[ord(letter) - ord('a')] += 1
    left = ""
    mid = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        count = counts[ord(letter) - ord('a')]
        if count > 0:
            if count % 2 == 1:
                mid = letter
            left += letter * (count // 2)
    return left + mid + left[::-1]


"""

Time complexity:

need to scan through string, and reverse half the string and loop through alphabet characters, so overall ---> O(n)


Space complexity:

map of size 26, so O(26) therefore overall ----> O(1)


"""