'''

Problem:
https://leetcode.com/problems/reverse-vowels-of-a-string/


'''


'''

Approach:
Two pointers look for vowels on both pointers and then swap if both vowels

'''


def reverseVowels(s):

    vowels = "aeiouAEIOU"

    i = 0
    j = len(s) - 1
    arr = [c for c in s]

    while i < j:

        if arr[i] in vowels and arr[j] in vowels:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1

        if arr[i] not in vowels:
            i += 1

        if arr[j] not in vowels:
            j -= 1

    return "".join(arr)


print(reverseVowels("IceCreAm"))



"""

Time complexity:
O(n) linear scan with 2 pointers 
O(n) linear scan to build str
Overall ---> O(n)


Space complexity:
just need arr for each character overall ---> O(n)

"""