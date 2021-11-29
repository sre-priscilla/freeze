from typing import List

class UnionFindSet:

    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, index: int) -> int:
        while index != self.root[index]:
            index = self.root[index]
        return index

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        print(f'union({x}, {y})', root_x, root_y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find_set = UnionFindSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union_find_set.union(i, j)
                    print(f'union({i}, {j})', union_find_set.root, union_find_set.rank)
        return sum(i == x for i, x in enumerate(union_find_set.root))


if __name__ == '__main__':
    # graph = [
    #     [1, 1, 0],
    #     [1, 1, 0],
    #     [0, 0, 1],
    # ]
    # print(Solution().findCircleNum(graph))
    
    # graph = [
    #     [1, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 1],
    # ]
    # print(Solution().findCircleNum(graph))

    graph = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
    ]
    print(Solution().findCircleNum(graph))
