"""

Problem:
https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/


"""

"""

Approach:
heap sort via kth score


"""


import heapq

class Solution:
    def sortTheStudents(score, k):
        heap = []
        for i in range(len(score)):
            heapq.heappush_max(heap, (score[i][k], score[i]))

        i = 0
        res = []
        while heap:
            res.append(heapq.heappop_max(heap)[1])
        
        return res
    

"""

n = number of students (rows)
m = number of scores per student (columns)


Time complexity:

sort + fil result array so overall ---> O(nlogn + nm)


Space complexity:

maxheap so overall ---> O(n)


"""