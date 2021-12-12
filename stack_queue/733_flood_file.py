from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque

        origin_color = image[sr][sc]
        m, n = len(image), len(image[0])
        deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))

        queue, visit = deque([(sr, sc)]), set()
        while queue:
            x, y = queue.popleft()
            image[x][y] = newColor
            visit.add((x, y))
            for delta in deltas:
                dx, dy = delta
                _x, _y = x + dx, y + dy
                if 0 <= _x < m  and 0 <= _y < n and (_x, _y) not in visit and image[_x][_y] == origin_color:
                    queue.append((x + dx, y + dy))
        return image

