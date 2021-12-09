# Definition for a Node.
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        queue, result = deque([root]), []
        while queue:
            n, values = len(queue), []
            for _ in range(n):
                node = queue.popleft()
                values.append(node.val)
                queue.extend(node.children)
            result.append(values)
        return result
