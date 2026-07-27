"""

Problem:
https://leetcode.com/problems/maximum-product-of-three-numbers/description/?envType=daily-question&envId=2026-07-27


"""


"""

Approach:

i did this with sorting and checking the following:
max(2 greatest negative numbers * 1 greatest positive number, product of 3 greatest positive numbers)

Approach that is optimal that I didnt want to code up:

find 3 greatest numbers
find 2 smallest numbers
then just do the check above
this would be O(n) since its only a few linear sweeps


"""


def maximumProduct(nums) -> int:
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[1] * nums[0])


"""

Time complexity:

sorting, so overall ---> O(nlogn)


Space complexity:

python uses timsort, so overall ---> O(n)


"""