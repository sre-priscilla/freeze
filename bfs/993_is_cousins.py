# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque

        if not root:
            return False
        queue = deque([root])
        map_parent = {root.val: None}
        while queue:
            n = len(queue)
            has_x, has_y = False, False
            for _ in range(n):
                node = queue.popleft()
                if node.val == x:
                    has_x = True
                if node.val == y:
                    has_y = True
                if has_x and has_y and map_parent[x] != map_parent[y]:
                    return True
                if node.left:
                    queue.append(node.left)
                    map_parent[node.left.val] = node.val
                if node.right:
                    queue.append(node.right)
                    map_parent[node.right.val] = node.val
        return False

        