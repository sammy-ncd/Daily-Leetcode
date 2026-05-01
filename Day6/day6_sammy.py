import re


'''

Problem:
https://leetcode.com/problems/coupon-code-validator/?envType=daily-question&envId=2026-04-30


'''


"""
Approach:
1. Condition on the requirments by the problem
2. Store valid codes in their appropriate bin
3. Sort each bin
4. put content from each bin into result array

"""

def validateCoupons(code, businessLine, isActive):

    pattern = r'^[a-zA-Z0-9_]+$'
    res = []
    categories = ["electronics", "grocery", "pharmacy", "restaurant"]
    arr = {"electronics": [], "grocery": [], "pharmacy": [], "restaurant": []}
    
    for i in range(len(code)):
        if (re.match(pattern, code[i]) and
            businessLine[i] in categories and
            isActive[i]):

            arr[businessLine[i]].append(code[i])
    
    for key in arr:
        arr[key].sort()

    print(arr)

    for key in arr:
        for c in arr[key]:
            res.append(c)

    return res

print(validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True]))


'''

Time complexity:
O(nlogn) for n bins need to sort each so this is what takes the most time

Space complexity:
Roughly O(n)

'''