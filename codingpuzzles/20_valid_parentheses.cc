#include <map>
#include <stack>
#include <iostream>

using namespace std;

class Solution {
public:
    // bool isValid(string s) {
    //     stack<char> _stack;
    //     for (char& ch : s) {
    //         if (_stack.size() == 0) {
    //             _stack.push(ch);
    //         } else {
    //             if (_stack.top() == '(' && ch == ')' || _stack.top() == '[' && ch == ']' || _stack.top() == '{' && ch == '}') {
    //                 _stack.pop();
    //             } else {
    //                 _stack.push(ch);
    //             }
    //         }
    //     }
    //     return _stack.size() == 0;
    // }

    bool isValid(string s) {
        stack<char> _stack;
        map<char, char> _map {{')', '('}, {']', '['}, {'}', '{'}};
        
        for (char& ch : s) {
            if (_stack.size() == 0 || _map.find(ch) == _map.end()) {
                _stack.push(ch);
            } else {
                if (_map[ch] == _stack.top()) {
                    _stack.pop();
                } else {
                    return false;
                }
            }
        }
        return _stack.size() == 0;
    }
};

int main() {
    printf("%d", Solution().isValid("()"));
    printf("%d", Solution().isValid("()[]{}"));
    printf("%d", Solution().isValid("(]"));
    printf("%d", Solution().isValid("([)]"));
    printf("%d", Solution().isValid("{[]}"));
    return 0;
}