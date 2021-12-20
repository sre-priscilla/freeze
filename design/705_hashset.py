class MyHashSet:

    def __init__(self):
        self.base = 1000
        self.table = [[] for _ in range(1001)]


    def add(self, key: int):
        row = key % self.base
        if not self.table[row]:
            self.table[row] = [0] * 1001
        self.table[row][key // 1000] = 1

    def remove(self, key: int) -> None:
        row = key % self.base
        if self.table[row]:
            self.table[row][key // 1000] = 0

    def contains(self, key: int) -> bool:
        row = key % self.base
        if self.table[row]:
            return self.table[row][key // 1000] == 1
        return False