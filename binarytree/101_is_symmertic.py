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
        

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     return self.dfs(root, root)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     stack: List[TreeNode] = [root, root]
    #     while stack:
    #         node_a, node_b = stack.pop(), stack.pop()
    #         if not (node_a and node_b):
    #             if node_a is None and node_b is None:
    #                 continue
    #             return False
    #         else:
    #             if node_a.val != node_b.val:
    #                 return False
    #             stack.extend([node_a.left, node_b.right, node_a.right, node_b.left])
    #     return True

    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque

        queue = deque([root, root])
        while queue:
            node_a, node_b = queue.popleft(), queue.popleft()
            if not (node_a and node_b):
                if node_a is None and node_b is None:
                    continue
                return False
            else:
                if node_a.val != node_b.val:
                    return False
                queue.extend([node_a.left, node_b.right, node_a.right, node_b.left])
        return True



if __name__ == '__main__':  
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().isSymmetric(root))
