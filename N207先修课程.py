from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites.sort()
        not_learned = set()
        from itertools import groupby
        link_list = dict()
        for key, courses in groupby(prerequisites, key=lambda x: x[0]):
            link_list[key] = [j[1] for j in courses]

        stack = []
