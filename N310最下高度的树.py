import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        V = set()
        E = defaultdict(list)
        for edge in edges:
            E[edge[1]].append(edge[0])
            E[edge[0]].append(edge[1])
            V.add(edge[1])
            V.add(edge[0])

        def bfs(v):
            layer = 0
            queue = deque()
            queue.append(v)
            queue.append(None)
            visit = set()
            while queue:
                item = queue.popleft()
                if item != None:
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

            return layer

        ans = []
        min_depth = math.inf
        for v in V:
            depth = bfs(v)
            if depth < min_depth:
                ans = [v]
                min_depth = depth
            elif depth == min_depth:
                ans.append(v)

        return ans


s = Solution()
print(s.findMinHeightTrees(1, []))
