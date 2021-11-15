from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
    #     if root.left is None and root.right is None:
    #         return root.val == targetSum
    #     else:
    #         return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     from typing import Deque
    #     from collections import deque    

    #     if not root:
    #         return False
    #     queue: Deque[TreeNode] = deque([TreeNode(root.val, root.left, root.right)])
    #     while queue:
    #         node: TreeNode = queue.popleft()
    #         if node.left is None and node.right is None:
    #             if node.val != targetSum:
    #                 continue
    #             return True
    #         if node.left:
    #             queue.append(TreeNode(node.left.val + node.val, node.left.left, node.left.right))
    #         if node.right:
    #             queue.append(TreeNode(node.right.val + node.val, node.right.left, node.right.right))
    #     return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque    

        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, path_sum = queue.popleft()
            if node.left is None and node.right is None:
                if path_sum != targetSum:
                    continue
                return True
            if node.left:
                queue.append((node.left, path_sum + node.left.val))
            if node.right:
                queue.append((node.right, path_sum + node.right.val))
        return False



if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4) 
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().hasPathSum(root, 22))