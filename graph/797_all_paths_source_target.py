from typing import List


class Solution:
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #     result: List[List[int]] = []
    #     if len(graph) == 0:
    #         return result
    #     self.dfs(graph, 0, [], result)
    #     return result

    # def dfs(self, graph: List[List[int]], node: int, path: List[int], result: List[List[int]]):
    #     path.append(node)
    #     if node == len(graph) - 1:
    #         result.append([node for node in path])
    #         return
    #     next_nodes = graph[node]
    #     for node in next_nodes:
    #         self.dfs(graph, node, path, result)
    #         path.pop()

    # def dfs(self, graph: List[List[int]], curr: int, path: List[int], result: List[List[int]]):
    #     if curr == len(graph) - 1:
    #         result.append([*path, curr])
    #     else:
    #         for node in graph[curr]:
    #             # path.append(curr)
    #             # self.dfs(graph, node, path, result)
    #             # path.pop()
    #             self.dfs(graph, node, [*path, curr], result)
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        result: List[List[int]] = []
        if len(graph) == 0:
            return result
        queue = deque([[0]])
        while queue:
            n = len(queue)
            path = queue.popleft()
            if path[-1] == len(graph) - 1:
                result.append(path)
            else:
                for node in graph[path[-1]]:
                    queue.append([*path, node])        
        return result


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget(
        [[4, 3, 1], [3, 2, 4], [3], [4], []]))
    print(Solution().allPathsSourceTarget(
        [[1], []]))
    print(Solution().allPathsSourceTarget(
        [[1, 2, 3], [2], [3], []]))
    print(Solution().allPathsSourceTarget(
        [[1, 3], [2], [3], []]))
