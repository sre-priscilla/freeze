import math
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result: List[int] = [0] * (n + 1)
        for i in range(0, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result[:n+1]


if __name__ == '__main__':
    for n in range(5):
        print(Solution().countBits(n))

