class MyHashMap:

    def __init__(self):
        self.base = 1000
        self.table = [[] for _ in range(1001)]

    def put(self, key: int, value: int):
        row = key % self.base
        if not self.table[row]:
            self.table[row] = [-1] * 1001
        self.table[row][key // 1000] = value

    def get(self, key: int) -> int:
        row = key % self.base
        if self.table[row]:
            return self.table[row][key // 1000]
        return -1

    def remove(self, key: int):
        row = key % self.base
        if self.table[row]:
            self.table[row][key // 1000] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)