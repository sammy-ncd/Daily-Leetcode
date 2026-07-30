"""

Problem:
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/?envType=daily-question&envId=2026-07-30


"""

"""

Approach:
find loops, take geometric sum for 8 * current loop
add the leftover buttons * loops + 1


"""



def minimumPushes(word: str) -> int:
    n = len(word)
    spare = n % 8
    loops = (n - (n % 8)) // 8
    totalPresses = 0
    for i in range(1, loops + 1):
        totalPresses += i * 8
    return totalPresses + spare * (loops + 1)


"""

Time complexity:

essentially O(1)


Space complexity:

nothing stored, so overall ---> O(1)

"""