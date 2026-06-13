from collections import deque


"""

Problem:
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/


"""

"""

Approach:
just go through simulation
stopping condition is when the student q is empty or if we have rotated it len(q) times because then we know there isnt a sandwich for the remaining students
return len student q

"""


def countStudents(students, sandwiches):
    stuq = deque(students)
    sanq = deque(sandwiches)
    rotations = 0
    while stuq and rotations < len(stuq):
        stu = stuq.popleft()
        if stu == sanq[0]:
            sanq.popleft()
            rotations = 0
        else:
            stuq.append(stu)
            rotations += 1
    return len(stuq)


"""


Time complexity:
worst case we have to loop through every sandwich for every student
so overall ---> O(n^2)

Space complexity:
both q's ---> O(n)
so overall ---> O(n)


"""