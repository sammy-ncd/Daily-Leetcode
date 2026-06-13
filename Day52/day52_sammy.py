"""

Problem:
https://leetcode.com/problems/weighted-word-mapping/description/?envType=daily-question&envId=2026-06-13


"""


"""

Approach:
Map for weight -> char conversion
loop through append resulting chars for each string to an array
join the array at the end

"""


def mapWordWeights(words, weights):
    MOD = 26
    d = {}
    a = "zyxwvutsrqponmlkjihgfedcba"
    for i in range(MOD):
        d[i] = a[i]
        
    res = []
    for word in words:
        total_weight = 0
        for c in word:
            total_weight += weights[ord(c) - ord('a')]
        res.append(d[total_weight % MOD])
    
    return "".join(res)

"""

let L = total number of characters across all words in words

Time Complexity:

O(1) ---> build map
O(L) ---> compute weights 
O(n) ---> join res

Overall ---> O(L + n)

Space Complexity:

O(1) ---> map
O(n) ---> res

Overall ---> O(n)

"""