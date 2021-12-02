# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, target: int) -> TreeNode:
        while root:
            if root.val == target:
                return root
            root = root.left if root.val > target else root.right
        return None