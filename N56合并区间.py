from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = [intervals[0]]
    for second in intervals:
        first = res[-1]
        if first[1] >= second[0]:
            res[-1] = [first[0], max(second[1], first[1])]
        else:
            res.append(second)

    return res