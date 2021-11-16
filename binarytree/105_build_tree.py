from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        map_inorder = {x: i for i, x in enumerate(inorder)}
        i_root = map_inorder[preorder[0]]
        left_child = self.buildTree(preorder[1:1+i_root], inorder[:i_root])
        right_child = self.buildTree(preorder[1+i_root:], inorder[i_root + 1:])
        return TreeNode(preorder[0], left_child, right_child)


if __name__ == '__main__':
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)
