# include <iostream>
//palindrome
//Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution {
public:
    bool isPalindrome(int x) {
        string p=to_string(x);
        int left=0;
        int right= p.size()-1;

        while (left<right){
            if (p[left]!=p[right]){
                return false;
}        
left++;
right--;
        }
        return true;

        
    }
};

