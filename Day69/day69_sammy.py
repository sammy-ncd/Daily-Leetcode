"""

Problem:
https://leetcode.com/problems/top-k-frequent-elements/description/


"""


"""

Approach:
create n buckets labeled 1 to n, each bucket holds elements with
its buckets label frequency
at the end loop from n to 1 and add the k most frequent to the res array


"""


def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    n = len(nums)
    buckets = [set() for _ in range(n + 1)]
    for num in freq:
        buckets[freq[num]].add(num)
   
    res = []
    for i in range(n, 0, -1):
        for j in buckets[i]:
            res.append(j)
            if len(res) == k:
                return res
            

"""

Time complexity:
O(n)

Space complexity:
O(n)


"""