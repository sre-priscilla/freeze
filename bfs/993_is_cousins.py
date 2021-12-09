# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     from collections import deque

    #     if not root:
    #         return False
    #     queue = deque([root])
    #     map_parent = {root.val: None}
    #     while queue:
    #         n = len(queue)
    #         has_x, has_y = False, False
    #         for _ in range(n):
    #             node = queue.popleft()
    #             if node.val == x:
    #                 has_x = True
    #             if node.val == y:
    #                 has_y = True
    #             if has_x and has_y and map_parent[x] != map_parent[y]:
    #                 return True
    #             if node.left:
    #                 queue.append(node.left)
    #                 map_parent[node.left.val] = node.val
    #             if node.right:
    #                 queue.append(node.right)
    #                 map_parent[node.right.val] = node.val
    #     return False

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque

        if not root:
            return False
        queue, level = deque([root]), 0
        found_x, x_level, x_parent = False, -1, None
        fount_y, y_level, y_parent = False, -1, None
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if (node.left and node.left.val == x) or (node.right and node.right.val == x):
                    found_x, x_level, x_parent = True, level + 1, node.val
                if (node.left and node.left.val == y) or (node.right and node.right.val == y):
                    fount_y, y_level, y_parent = True, level + 1, node.val
            if found_x and fount_y and x_level == y_level and x_parent != y_parent:
                return True
            level += 1              
        return False

        