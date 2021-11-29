class UnionFind:

    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
        print(f'union({x} {y})', self.root)

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))
    print(uf.connected(5, 7))
    print(uf.connected(4, 9))
    uf.union(9, 4)
    print(uf.connected(4, 9))