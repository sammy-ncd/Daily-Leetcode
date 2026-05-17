#include <vector>
#include <string>
using namespace std;


/*

Problem: https://leetcode.com/problems/fizz-buzz/

*/


/*

Approach: its fizzbuzz.

*/


vector<string> fizzBuzz(int n) {
    vector<string> answer;

    for (int i = 1; i < n + 1; ++i) {

        if (i % 3 == 0 and i % 5 == 0) {
            answer.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            answer.push_back("Fizz");
        } else if (i % 5 == 0) {
            answer.push_back("Buzz");
        } else {
            answer.push_back(to_string(i));
        }
    }
    return answer;
}


/*

Time Complexity:
A scan n times ----> Overall: O(n)


Space Complexity:
Answer array ----> Overall: O(n)

*/