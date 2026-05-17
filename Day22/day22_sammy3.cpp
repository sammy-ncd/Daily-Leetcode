#include <vector>
#include <string>
using namespace std;


/*

Problem:
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

*/


/*

Approach:
convert to string and check string length (dont feel like doing math to go through digits)


*/



int findNumbers(vector<int>& nums) {

    int amount = 0;
    
    for (auto num : nums) {
        if (to_string(num).length() % 2 == 0) {
            amount++;
        }
    }
    
    return amount;   
}

/*

Time Complexity:

O(n * d) where d is the number of digits per integer

converting the number to a string is time proportional to the number of digits in this number.


Space Complexity:

O(d) where d is number of digits per number


*/