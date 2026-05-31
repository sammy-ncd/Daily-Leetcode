'''

Problem:
https://leetcode.com/problems/destroying-asteroids/description/


'''


"""

Approach 1:
sort asteroids array
loop through sorted array keep adding while asteroids[i] < mass
if at some point the asteroid is bigger than mass return False
if we can add all return True

Approach 2:
use constraints to achieve better runtime
create a frequency array for amount of times a specific mass asteroid appears
loop through frequency array and snowball add to mass while possible
if at some point we cant return False
otherwise return true


"""

# Approach 1

def asteroidsDestroyed_1(mass, asteroids):
    asteroids.sort()

    for a in asteroids:
        if mass >= a:
            mass += a
        else:
            return False

    return True

# Approach 2

def asteroidsDestroyed_2(mass, asteroids):

    maxAstSz = 100000
    freq = [0] * (maxAstSz + 1)

    for a in asteroids:
        freq[a] += 1

    for i in range(1, maxAstSz + 1):

        if freq[i] > 0:
            if mass < i:
                return False

            mass += i * freq[i]

    return True


"""

Time complexities:

Approach 1: O(nlogn) because of sorting

Approach 2:
-> build freqs = O(100000)
-> establish frequencies = O(n)
-> validate solution O(n + 100000)
Overall ---> O(n + 100000)


Space complexities:

Approach 1:
Whatever python sort function is O(1) or O(n)

Approach 2:
O(100000) b/c thats the max size of the freq array

"""