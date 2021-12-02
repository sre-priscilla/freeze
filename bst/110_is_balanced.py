# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def H(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.H(root.left), self.H(root.right))


#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return abs(self.H(root.left) - self.H(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:

    def H(self, root: TreeNode) -> int:
        if not root:
            return 0
        l_height = self.H(root.left)
        r_height = self.H(root.right)
        if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1:
            return -1
        else:
            return max(l_height, r_height) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.H(root) >= 0