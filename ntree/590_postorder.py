# Definition for a Node.
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        from collections import deque

        if not root:
            return []
        stack, result = [root], deque([])
        while stack:
            root = stack.pop()
            result.appendleft(root.val)
            stack.extend(root.children)
        return result




