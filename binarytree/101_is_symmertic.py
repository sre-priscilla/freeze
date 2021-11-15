from typing import List, Deque
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, a: TreeNode, b: TreeNode) -> bool:
        if not (a and b):
            return a is None and b is None
        else:
            return a.val == b.val and self.dfs(a.left, b.right) and self.dfs(a.right, b.left)
        

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().isSymmetric(root))
