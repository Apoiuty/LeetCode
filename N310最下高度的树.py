from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # 生成图
        V = set()
        E = defaultdict(list)
        for edge in edges:
            E[edge[1]].append(edge[0])
            E[edge[0]].append(edge[1])
            V.add(edge[1])
            V.add(edge[0])

        def bfs(v):
            """
            获取最深节点
            :param v:
            :return:
            """
            layer = 0
            queue = deque()
            queue.append(v)
            queue.append(None)
            visit = set()
            max_depth = 0
            max_depth_v = v
            while queue:
                item = queue.popleft()
                if item != None:
                    if layer >= max_depth:
                        max_depth = layer
                        max_depth_v = item
                    visit.add(item)
                    for adj in E[item]:
                        if adj not in visit:
                            queue.append(adj)
                else:
                    layer += 1
                    if queue:
                        queue.append(None)
                    else:
                        break

            return max_depth_v

        def dfs(v, e, path, visited):
            """
            获取从v出发到e的路径
            :param v:
            :param path:
            :param e:
            :return:
            """
            path.append(v)
            if v == e:
                raise UserWarning
            # 深度优先遍历
            for adj in E[v]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj, e, path, visited)
            path.pop()

        x = bfs(0)
        y = bfs(x)
        path = []
        try:
            dfs(x, y, path, set())
        except UserWarning:
            pass

        if len(path) % 2:
            return path[len(path) // 2:len(path) // 2 + 1]
        else:
            return path[len(path) // 2 - 1:len(path) // 2 + 1]


s = Solution()
print(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
