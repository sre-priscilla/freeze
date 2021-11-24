class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        curr: Node = root
        while curr:
            head: Node = Node(val=0)
            prev = head
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                # 平移
                curr = curr.next
            # 换行
            curr = head.next
        return root


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    Solution().connect(root)
    print(root.left.next.val)
    print(root.left.left.next.val)
    print(root.left.right.next.val)
    print(root.right.left.next.val)