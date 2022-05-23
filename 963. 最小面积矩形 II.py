import math
from typing import List
from itertools import combinations


def dot(a, b):
    return sum(i * j for i, j in zip(a, b))


def vector(a, b):
    return b[0] - a[0], a[1] - b[1]


def vector_p4(p1, p2, p3):
    p4_x = p2[0] + p3[0] - p1[0]
    p4_y = p2[1] + p3[1] - p1[1]
    return p4_x, p4_y


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = set(tuple(point) for point in points)
        min_area = math.inf
        for p1, p2, p3 in combinations(points, 3):
            p1_p2 = vector(p1, p2)
            p1_p3 = vector(p1, p3)
            p2_p3 = vector(p2, p3)
            p2_p1 = vector(p2, p1)
            p3_p1 = vector(p3, p1)
            p3_p2 = vector(p3, p2)
            if not dot(p1_p2, p1_p3):
                p4 = vector_p4(p1, p2, p3)
                if p4 in points:
                    min_area = min(min_area, math.hypot(*p1_p2) * math.hypot(*p1_p3))
            if not dot(p2_p3, p2_p1):
                p4 = vector_p4(p2, p3, p1)
                if p4 in points:
                    min_area = min(min_area, math.hypot(*p2_p3) * math.hypot(*p2_p1))
            if not dot(p3_p1, p3_p2):
                p4 = vector_p4(p3, p2, p1)
                if p4 in points:
                    min_area = min(min_area, math.hypot(*p3_p1) * math.hypot(*p3_p2))

        return min_area if min_area < math.inf else 0


s = Solution()
print(s.minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]))
