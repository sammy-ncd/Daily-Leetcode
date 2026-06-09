"""

Problem:
https://leetcode.com/problems/min-max-game/description/?envType=problem-list-v2&envId=simulation


"""

"""

Approach:
Literally just do what the problem tells you to do lol


"""



def minMaxGame(nums):
    n = len(nums)
    while n != 1:
        newNums = [0 for _ in range(n//2)]
        
        for i in range(n):
            if 0 <= i < n // 2:
                if i % 2 == 0:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
        n //= 2
        nums = newNums
    return nums[0]



"""

Time:
we halve n each time so this isnt as long as it may seem overall ---> O(n)

Space:
we at least have a n/2 size array newNums at some point so overall space ----> O(n)


"""