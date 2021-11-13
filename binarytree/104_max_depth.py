from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     ret, queue = 0, deque([root])
    #     while len(queue) > 0:
    #         ret += 1
    #         n = len(queue)
    #         for _ in range(n):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #     return ret

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    print(Solution().maxDepth(root))