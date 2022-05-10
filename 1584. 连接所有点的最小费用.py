from typing import List
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = []
        for i in range(n):
            for j in range(i + 1, n):
                d.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])

        d.sort()

        edge_cnt = 0
        union_set = defaultdict(list)
        cnt = 0
        for distance, i, j in d:
            if union_set[i] == [] and union_set[j] == []:
                union_set[i] = union_set[j] = [i, j]
            elif union_set[i] == []:
                union_set[j].append(i)
                union_set[i] = union_set[j]
            elif union_set[j] == []:
                union_set[i].append(j)
                union_set[j] = union_set[i]
            elif union_set[i] != union_set[j]:
                index_i = union_set[i][:]
                index_j = union_set[j][:]
                value = union_set[i] + union_set[j]
                for key in index_i + index_j:
                    union_set[key] = value
            else:
                continue

            cnt += distance
            edge_cnt += 1
            if edge_cnt + 1 == len(points):
                break

        return cnt


s = Solution()
print(s.minCostConnectPoints([[-8, 14], [16, -18], [-19, -13], [-18, 19], [20, 20], [13, -20], [-15, 9], [-4, -8]]))
