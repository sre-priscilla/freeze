# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        if not (p and q):
            return False
        return p.val == q.val and self.dfs(p.left, q.right) and self.dfs(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root, root)
        