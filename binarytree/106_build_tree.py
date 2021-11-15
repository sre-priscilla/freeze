from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        map_inorder = {x: i for i, x in enumerate(inorder)}
        i_root = map_inorder[postorder[-1]]
        left_subtree = self.buildTree(inorder[:i_root], postorder[:i_root])
        right_subtree = self.buildTree(inorder[i_root + 1:], postorder[i_root:len(postorder)-1])
        return TreeNode(postorder[-1], left_subtree, right_subtree)


if __name__ == '__main__':
    root = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)
