from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        from collections import defaultdict
        union_set = defaultdict(dict)

        for i, [a, b] in enumerate(equations):
            if a in union_set and b not in union_set:
                union_set[a][b] = union_set[a][a] / values[i]
                union_set[b] = union_set[a]
            elif b in union_set and a not in union_set:
                union_set[b][a] = values[i] * union_set[b][b]
                union_set[a] = union_set[b]
            elif a not in union_set and b not in union_set:
                union_set[b][b] = 1
                union_set[b][a] = values[i] * union_set[b][b]
                union_set[a] = union_set[b]
            else:
                if len(union_set[a]) < len(union_set[b]):
                    # 对每个a集合中的元素进行放缩
                    k = union_set[b][b] * values[i] / union_set[a][a]
                    for i, v in union_set[a].items():
                        union_set[b][i] = union_set[a][i] * k

                    key = union_set[a].keys()
                    for k in key:
                        union_set[k] = union_set[b]
                else:
                    k = union_set[a][a] / union_set[b][b] / values[i]
                    for i, v in union_set[b].items():
                        union_set[a][i] = union_set[b][i] * k

                    key = union_set[b].keys()
                    for k in key:
                        union_set[k] = union_set[a]

        result = []
        for a, b in queries:
            if a in union_set and b in union_set and union_set[a] == union_set[b]:
                result.append(union_set[a][a] / union_set[a][b])
            else:
                result.append(-1)

        return result


s = Solution()
print(
    s.calcEquation([["a", "b"], ["e", "f"], ["b", "e"]], [3.4, 1.4, 2.3],
                   [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]))
