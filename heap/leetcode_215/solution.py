from typing import List


class Heap:

    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        for i in reversed(range(len(nums) // 2)):
            self._sift_down(i)

    def pop(self) -> int:
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        last: int = self.nums.pop()
        if len(self.nums) > 1:
            self._sift_down(0)
        return last

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


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap([-x for x in nums])
        for _ in range(k - 1):
            heap.pop()
        return -heap.pop()


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
