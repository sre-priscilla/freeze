from typing import List, NoReturn


class Heap:

    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        for i in reversed(range(len(nums) // 2)):
            self._sift_down(i)

    def size(self) -> int:
        return len(self.nums)
    
    def top(self):
        return self.nums[0]

    def push(self, x: int):
        self.nums.append(x)
        self._sift_up(len(self.nums) - 1)


    def pop(self) -> int:
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        last: int = self.nums.pop()
        if len(self.nums) > 1:
            self._sift_down(0)
        return last
    
    def _sift_up(self, i):
        while i > 0 and self.nums[i] < self.nums[(i - 1) // 2]:
            self.nums[i], self.nums[(i - 1) // 2] = self.nums[(i - 1) // 2], self.nums[i]
            i = (i - 1) // 2

    def _sift_down(self, i: int):
        while i < len(self.nums) // 2:
            _min: int = i
            if 2 * i + 1 < len(self.nums) and self.nums[2 * i + 1] < self.nums[_min]:
                _min = 2 * i + 1
            if 2 * i + 2 < len(self.nums) and self.nums[2 * i + 2] < self.nums[_min]:
                _min = 2 * i + 2
            if _min == i:
                break
            self.nums[_min], self.nums[i] = self.nums[i], self.nums[_min]
            i = _min

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = Heap([x for x in nums])

    def add(self, val: int) -> int:
        self.heap.push(val)
        while self.heap.size() > self.k:
            self.heap.pop()
        return self.heap.top()
        

if __name__ == '__main__':
    kl = KthLargest(3, [4, 5, 8, 2])
    print(kl.heap.nums)
    print(kl.add(3))
    print(kl.heap.nums)
    print(kl.add(5))
    print(kl.add(10))
    print(kl.add(9))
    print(kl.add(4))