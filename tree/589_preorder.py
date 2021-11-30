from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children[::-1])
        return result
