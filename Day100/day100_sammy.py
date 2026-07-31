"""------------------------------ Day 100 ------------------------------"""



"""

Problem:
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2026-07-31


"""

"""

Approach:
map characters to their frequencies, sort the frequencies so we have the greatest first
each time we cycle through 8 distinct letters up the loopFactor by 1 because we now require 
double or higher presses


"""


def minimumPushes(word: str) -> int:
    counts = [0] * 26
    for c in word:
        counts[ord(c) - ord('a')] += 1
    totalPresses = 0
    distinct = 0
    loopFactor = 1
    counts.sort(reverse=True)
    for count in counts:
        if count > 0:
            distinct += 1
            totalPresses += loopFactor * count
            if distinct % 8 == 0:
                loopFactor += 1
    return totalPresses


"""

Time complexity:

build counts --> O(n)
sort counts --> O(26log26)
overall ---> O(n)


Space complexity:
store counts ---> O(26)
overall ---> O(1)


"""