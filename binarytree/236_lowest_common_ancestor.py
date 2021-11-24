# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from typing import Deque, Dict, Set
        from collections import deque

        if not root:
            return root
        map_parent: Dict[TreeNode, TreeNode] = {root: None}
        queue: Deque[TreeNode] = deque([root])
        while queue:
            n: int = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    map_parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    map_parent[node.right] = node
                    queue.append(node.right)
        
        curr: TreeNode = p
        path: Set[TreeNode] = {curr}
        while curr:
            curr = map_parent[curr]
            path.add(curr)
        curr: TreeNode = q
        while curr:
            if curr in path:
                return curr
            curr = map_parent[curr]
        return None


if __name__ == '__main__':
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print(Solution().lowestCommonAncestor(root, root.left, root.right).val)
    print(Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val)
