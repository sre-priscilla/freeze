#include <map>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> res;
        map<int, int> m;

        for (int i = 0; i < nums.size(); i++)
        {
            if (m.find(nums[i]) != m.end())
            {
                res = {m[nums[i]], i};
                return res;
            }
            m[target - nums[i]] = i;
        }

        return res;
    }
};

int main()
{
    // Solution solution();
    vector<int> vec = {2, 7, 11, 15};
    for_each(vec.begin(), vec.end(), [](int &i)
             { printf("%d\n", i); });
    vector<int> res = Solution().twoSum(vec, 9);
    for_each(res.begin(), res.end(), [](int &i)
             { printf("%d\n", i); });
    return 0;
}