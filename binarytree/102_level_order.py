from typing import List
from collections import deque

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ret, queue = [], deque([root])
        while len(queue) > 0:
            n, nums = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                nums.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(nums)
        return ret


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().levelOrder(root))
