"""

Problem:
https://leetcode.com/problems/angle-between-hands-of-a-clock/description/?envType=daily-question&envId=2026-06-18


"""

"""

Approach:
its a math problem


"""



def angleClock(hour, minutes):
    
    hourHand = ((hour + (float(minutes) / float(60))) * 30) % 360
    minHand = ((float(minutes) / float(5)) * 30) % 360
    time = abs(hourHand - minHand)

    return min(time, abs(360 - time))



"""

Time complexity:

just simple math so overall ----> O(1) 


Space complexity:

only use a few ints so overall ----> O(1)


"""