#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            max_profit += max(0, prices[i] - prices[i - 1]);
        }
        return max_profit;
    }
};

int main()
{
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    printf("%d\n", Solution().maxProfit(prices));
}