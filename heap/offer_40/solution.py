from typing import List

def heapify(nums: List[int]):
    for i in reversed(range(len(nums) // 2)):
        _sift_down(nums, i)

def heappop(nums: List[int]) -> int:
    nums[0], nums[-1] = nums[-1], nums[0]
    top: int = nums.pop()
    if len(nums) > 0:
        _sift_down(nums, 0)
    return top

def _sift_up(nums: List[int], i: int):
    while i > 0 and nums[i] < nums[(i - 1) // 2]:
        parent = (i - 1) // 2
        nums[i], nums[parent] = nums[parent], nums[i]
        i = parent

def _sift_down(nums: List[int], i: int):
    while i < len(nums) // 2:
        _min = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < len(nums) and nums[l] < nums[_min]:
            _min = l
        if r < len(nums) and nums[r] < nums[_min]:
            _min = r
        if _min == i:
            break
        nums[i], nums[_min] = nums[_min], nums[i]
        i = _min

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapify(arr)
        return [heappop(arr) for _ in range(k)]


if __name__ == '__main__':
    print(Solution().getLeastNumbers([3, 2, 1], 2))
    print(Solution().getLeastNumbers([0, 1, 2, 1], 1))
