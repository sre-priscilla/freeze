from typing import List, Tuple


class Solution:
    def sift_down(self, heap: List[Tuple[int, int]], i: int):
        while i < len(heap) // 2:
            _max = i
            if 2 * i + 1 < len(heap) and heap[2 * i + 1][1] > heap[_max][1]:
                _max = 2 * i + 1
            if 2 * i + 2 < len(heap) and heap[2 * i + 2][1] > heap[_max][1]:
                _max = 2 * i + 2
            if _max == i:
                break
            heap[i], heap[_max] = heap[_max], heap[i]
            i = _max

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for x in nums:
            counter[x] = counter.get(x, 0) + 1
        heap = []
        for key, val in counter.items():
            heap.append((key, val))

        n = len(heap)
        for i in reversed(range(n // 2)):
            self.sift_down(heap, i)

        ret: List[int] = []
        for _ in range(k):
            heap[0], heap[-1] = heap[-1], heap[0]
            ret.append(heap.pop()[0])
            if len(heap) > 1:
                self.sift_down(heap, 0)
        return ret


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent([1], 1))
