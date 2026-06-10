'''

Problem:
https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/


'''



'''

Approach:
Its just a simulation problem, so just code it directly.


'''

def valueAfterKSeconds(n, k):
    a = [1 for _ in range(n)]

    for i in range(k):
        for i in range(1,n):
            a[i] = a[i] + a[i - 1]

    return a[n-1] % (pow(10, 9) + 7)



"""


Time complexity:
For k seconds we compute the prefix sum of the array
so overall time ----> O(kn)


Space complexity:
just a array which is of length n, so overall ---> O(n)



"""