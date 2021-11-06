#include <stack>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack_result;
        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i].size() > 1 || isdigit(tokens[i][0])) {
                stack_result.push(atoi(tokens[i].c_str()));
            } else {
                int x = stack_result.top();
                stack_result.pop();
                int y = stack_result.top();
                stack_result.pop();
                if (tokens[i] == "+") stack_result.push(y + x);
                if (tokens[i] == "-") stack_result.push(y - x);
                if (tokens[i] == "*") stack_result.push(y * x);
                if (tokens[i] == "/") stack_result.push(y / x);
            }
        }
        return stack_result.top();
    }
};

int main() {
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    printf("%d\n", Solution().evalRPN(tokens));
    tokens = {"4", "13", "5", "/", "+"};
    printf("%d\n", Solution().evalRPN(tokens));
}