from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping, result = dict(), list()
        for x in nums1:
            mapping[x] = mapping.get(x, 0) + 1
        for y in nums2:
            if y in mapping and mapping[y] > 0:
                result.append(y)
                mapping[y] = mapping.get(y) - 1
        return result