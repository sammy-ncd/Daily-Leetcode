'''

Problem:
https://leetcode.com/problems/two-sum/


'''


"""

Approach:
1. create dict 
2. check if target - nums[i] in dict
3. if not add nums[i] to dict
4. repeat until solution is found

"""


def twoSum(nums, target):

    ht = {}

    for i in range(len(nums)):
        try:
            ht[target - nums[i]]
            return [i, ht[target - nums[i]]]
        except KeyError:
            ht[nums[i]] = i

        
print(twoSum([2,7,11,15], target = 9))
print(twoSum([3,2,4], target = 6))


"""

Time complexity:
O(n) just a linear scan

Space complexity:
O(n) map that possible holds n key, value pairs.

"""