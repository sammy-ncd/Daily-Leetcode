import math


'''

Problem:
https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-05-19


'''


'''

First Approach: 
Brute force

Second Approach:
Use math to see whether it will take us longer in x or y direction to
reach the next point add the max of those distances to point


'''


def minTimeToVisitAllPoints_BruteForce(points):
    
    if len(points) == 1:
        return 0
    
    time = 0
    cur_point = points[0]

    points = points[1:]

    for point in points:
        while cur_point != point:

            dirs = [[-1,0], [1,0], [0,1] ,[0,-1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
            min_dist = 3000
            best_point = cur_point

            for dir in dirs:
                x_off, y_off = cur_point[0] + dir[0], cur_point[1] + dir[1]
                dist = math.sqrt(math.pow((x_off - point[0]), 2) +
                                 math.pow((y_off - point[1]), 2))
                
                if dist < min_dist:
                    best_point = [x_off, y_off]
                    min_dist = dist
                
                if dist == 0:
                    cur_point = [x_off, y_off]
                    break
            
            cur_point = best_point
            time += 1
   
    return time


def minTimeToVisitAllPoints(points):

    n = len(points)
    
    time = 0

    x1, y1 = points[0]

    for i in range(1, n):
        
        x2, y2 = points[i]

        time += max(abs(x2 - x1), abs(y2 - y1))

        x1, y1 = x2, y2 

    return time

print(minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
print(minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))



"""

Time Complexity:
Loop through points list once overall ----> O(n)

Space Complexity:
Only storing points so really nothing overall ----> O(1)


"""