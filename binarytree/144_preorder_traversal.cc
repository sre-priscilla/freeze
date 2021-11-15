#include <stack>
#include <vector>

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
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> ret;
        if (root == nullptr)
        {
            return ret;
        }

        stack<TreeNode*> _stack {{root}};

        while (!_stack.empty())
        {
            TreeNode* node = _stack.top();
            ret.push_back(node->val);
            _stack.pop();

            if (node->right != nullptr)
            {
                _stack.push(node->right);
            }
            if (node->left != nullptr)
            {
                _stack.push(node->left);
            }
        }
        return ret;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    vector<int> ret = Solution().preorderTraversal(root);
    for_each(ret.begin(), ret.end(), [](int &i){ printf("%d\n", i); });
    return 0;
}