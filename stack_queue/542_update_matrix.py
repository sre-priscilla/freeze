from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque

        m, n = len(mat), len(mat[0])
        queue, visit = deque([(0, 0)]), set()
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = 10001
        while queue:
            x, y = queue.popleft()
            for dx, dy in deltas:
                _x, _y = x + dx, y + dy
                if 0 <= _x < m and 0 <= _y < n and mat[_x][_y] > mat[x][y] + 1:
                    queue.append((_x, _y))
                    mat[_x][_y] = mat[x][y] + 1
        return mat


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().updateMatrix(mat))

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().updateMatrix(mat))
