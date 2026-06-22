"""

Problem:
https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-21


"""


"""

Approach:
find frequency of each letter in word = balloon
return the min occurrence of the character in the word
for 'l' and 'o' since we need two of them check freq // 2


"""



def maxNumberOfBalloons(text):
   
   wordmap = {
       'b' : 0,
       'a' : 0,
       'l' : 0,
       'o' : 0,
       'n' : 0
   }

   for c in text:
       if c in wordmap:
           wordmap[c] += 1

   return min(
       wordmap["b"],
       wordmap["a"],
       wordmap["l"] // 2,
       wordmap["o"] // 2,
       wordmap["n"]
   )              


"""

Time complexity:

we just need one pass through text to build the map so overall ---> O(n)


Space complexity:
fixed size word map so overall ---> O(1)


"""