class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l_height = self.minDepth(root.left)
        r_height = self.minDepth(root.right)
        return  (l_height + r_height + 1) if (l_height == 0 or r_height == 0) else (1 + min(l_height, r_height))