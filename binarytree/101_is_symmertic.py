from typing import List, Deque
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue: Deque[TreeNode] = deque([root.left, root.right])
        while len(queue) > 0:
            n = len(queue)
            tmp = deque([])
            for _ in range(n):
                node: TreeNode = queue.popleft()
                if node:
                    queue.append(node.left, node.right)
                tmp.append(node)
            if len(tmp) % 2 != 0:
                return False
            while tmp:
                if tmp[0] is None and tmp[-1] is None:
                    tmp.pop()
                    tmp.popleft()
                elif tmp[0] and tmp[-1] and tmp[0].val == tmp[-1].val:
                    tmp.pop()
                    tmp.popleft()
                else:
                    return False
        return True