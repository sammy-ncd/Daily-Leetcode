"""

Problem:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


"""



"""

Approach:
Two pointers move right pointer in if sum at the pointers > target
move left pointer in if sum at pointers is < target


"""



def twoSum(numbers, target):

    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            return [i + 1, j + 1]
        

print(twoSum([2,7,11,15], target = 9))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [-1,0], target = -1))


"""

Time complexity:
Two pointers closing at worst we move pointers collectively n times
either far left 2 numbers are the solution or both middle numbers or 
both far right numbers.

Overall ---> O(n)


Space Complexity:
only storing a couple ints

Overall ---> O(1)


"""