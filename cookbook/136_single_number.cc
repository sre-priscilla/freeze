#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        int result = 0;
        for (auto x: nums)
        {
            result ^= x;
        }
        return result;
    }
};

int main()
{
    vector<int> nums = {1, 2, 1, 2, 3};
    printf("%d\n", Solution().singleNumber(nums));
}
