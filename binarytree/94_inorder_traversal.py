from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return [*self.inorderTraversal(root.left), root.val, *self.inorderTraversal(root.right)]

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack: List[TreeNode] = []

        curr: TreeNode = root
        nums: List[int] = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack:
                curr = stack.pop()
                nums.append(curr.val)
                curr = curr.right
        return nums

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().inorderTraversal(root))