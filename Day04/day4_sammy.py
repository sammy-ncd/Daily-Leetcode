"""

Problem:

https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/?envType=daily-question&envId=2026-04-27

"""


"""

Approach: Cycle backwards and forwards simultaneously
          immediately return the distance closest to target.

"""
def closestTarget(words, target, startIndex):
    n = len(words)
    for i in range(n):
        if words[(startIndex + i) % n] == target:
            return i
        if words[(startIndex - i) % n] == target:
            return i
    return -1


print(closestTarget(["hello","i","am","leetcode","hello"],
                     "hello",
                     1
                     ))

print(closestTarget(["a","b","leetcode"], "leetcode", 0))

print(closestTarget(["i","eat","leetcode"], target = "ate", startIndex = 0))

"""

Time complexity: O(n) the distance can never be greater than n 
                      so we can cycle through at most n times

Space complexity: O(1) only storing n in an int.

"""