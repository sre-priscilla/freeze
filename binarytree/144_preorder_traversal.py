from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def dfs(self, root: TreeNode, nums: List[int]):
#         if not root:
#             return
#         nums.append(root.val)
#         if root.left:
#             self.dfs(root.left, nums)
#         if root.right:
#             self.dfs(root.right, nums)

#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         nums: List[int] = []
#         self.dfs(root, nums)
#         return nums

# class Solution:

#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         return [
#             root.val,
#             *self.preorderTraversal(root.left),
#             *self.preorderTraversal(root.right)
#         ]

# class Solution:

#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         nums: List[int] = []
#         stack: List[TreeNode] = [root]
#         while stack:
#             node = stack.pop()
#             nums.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return nums

class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nums: List[int] = []
        stack: List[TreeNode] = []
        curr: TreeNode = root
        while curr or stack:
            if curr:
                stack.append(curr)
                nums.append(curr.val)
                curr = curr.left
            else:
                node: TreeNode = stack.pop()
                curr = node.right
        return nums




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().preorderTraversal(root))