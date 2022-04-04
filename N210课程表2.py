from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        # 没有限制
        if prerequisites == []:
            return list(range(numCourses))
        v = set()
        edges = defaultdict(list)
        # p0是后置课程，p1是前置课程，课程从1指向0
        for p in prerequisites:
            edges[p[1]].append(p[0])
            v.add(p[1])

        visited = set()
        path = []

        def dfs(v, before_course):
            if v not in before_course:
                before_course.add(v)
            else:
                return []
            if v in visited:
                before_course.discard(v)
                return
            else:
                visited.add(v)

            for adj in edges[v]:
                result = dfs(adj, before_course)
                if result == []:
                    return []
            before_course.discard(v)
            path.append(v)

        for node in v:
            result = dfs(node, set())
            if result == []:
                return []
        return path[::-1] + list(set(range(numCourses)) - set(path))


s = Solution()
print(s.findOrder(7, [[0, 1]]))
