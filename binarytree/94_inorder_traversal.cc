#include <stack>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> ret;
        if (root == nullptr)
        {
            return ret;
        }
        TreeNode *curr = root;
        stack<TreeNode *> _stack;
        while (curr != nullptr || !_stack.empty())
        {
            while (curr != nullptr)
            {
                _stack.push(curr);
                curr = curr->left;
            }
            if (!_stack.empty())
            {
                curr = _stack.top();
                _stack.pop();
                ret.push_back(curr->val);
                curr = curr->right;
            }
        }
        return ret;
    }
};

int main()
{
    TreeNode *root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    vector<int> ret = Solution().inorderTraversal(root);
    for_each(ret.begin(), ret.end(), [](int &i)
             { printf("%d\n", i); });
    return 0;
}