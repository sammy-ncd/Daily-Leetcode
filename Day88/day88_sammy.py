"""

Problem:
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2026-07-19

"""


"""

Approach:
Brute force


"""


def findKthBit(n: int, k: int) -> str:
    
    def invert(bits):
        res = ""
        for bit in bits:
            if bit == "1":
                res += "0"
            else:
                res += "1"
        return res
    
    def reverse(bits):
        return bits[::-1]
    
    si = "0"
    for _ in range(1, n):
        si = si + "1" + reverse(invert(si))
    return si[k-1]


"""

Time complexity:

For each level, we invert and reverse the current string.
The string lengths are:

1, 3, 7, ..., 2^n - 1

So the total work is:

O(1 + 2 + 4 + ... + 2^n) = O(2^n)

Note: repeated string concatenation inside invert() can make that helper
less efficient in Python, but the intended overall complexity is O(2^n).


Space complexity:

We store the full binary string S_n, whose length is 2^n - 1.

The temporary inverted/reversed strings are also proportional to the
current string length.

Overall ---> O(2^n)


"""