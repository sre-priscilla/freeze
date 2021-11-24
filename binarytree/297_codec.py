from typing import AnyStr, List, Optional, Deque
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> AnyStr:
        queue: Deque[Optional[TreeNode]] = deque([root])
        values: List[AnyStr] = []
        while queue:
            node: Optional[TreeNode] = queue.popleft()
            if not node:
                values.append('#')
            else:
                values.append(f'{node.val}')
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(values)

        

    def deserialize(self, data: AnyStr) -> Optional[TreeNode]:
        if data == '#':
            return None
        values: Deque[AnyStr] = deque(data.split(','))
        
        root = TreeNode(int(values.popleft()))
        queue: Deque[Optional[TreeNode]] = deque([root])
        while values:
            node: TreeNode = queue.popleft()
            l_val, r_val = values.popleft(), values.popleft()
            if l_val != '#':
                node.left = TreeNode(int(l_val))
                queue.append(node.left)
            if r_val != '#':
                node.right = TreeNode(int(r_val))
                queue.append(node.right)
        return root

        

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    data: AnyStr = Codec().serialize(root)
    print(data)
    tree: TreeNode = Codec().deserialize(data)
    print(tree.val)
    print(tree.left.val)
    print(tree.right.val)