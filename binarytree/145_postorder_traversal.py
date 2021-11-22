from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     return [
    #         *self.postorderTraversal(root.left),
    #         *self.postorderTraversal(root.right),
    #         root.val
    #     ]

    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     nums: List[int] = []
    #     stack: List[TreeNode] = [root]
    #     while stack:
    #         node = stack.pop()
    #         nums.append(node.val)
    #         if node.left:
    #             stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)
    #     nums.reverse()
    #     return nums

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack: List[TreeNode] = []
        
        prev: Optional[TreeNode] = None
        curr: Optional[TreeNode] = root
        nums: List[int] = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not curr.right or curr.right == prev:
                nums.append(curr.val)
                prev, curr = curr, None
            else:
                stack.append(curr)
                curr = curr.right
        return nums



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = Solution().postorderTraversal(root)
    print(res)