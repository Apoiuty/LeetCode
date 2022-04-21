from typing import *


# 2022-04-13 14:30:34

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        n = len(intervals)
        while left < n and intervals[left][1] < newInterval[0]:
            left += 1

        # 比所有区间都大
        if left == n:
            return intervals + [newInterval]

        right = left
        while right < n and intervals[right][1] < newInterval[1]:
            right += 1

        # 最前面且无交集
        if left == right == 0:
            if newInterval[1] < intervals[0][0]:
                intervals.insert(0, newInterval)
                return intervals

        if left == right:
            if newInterval[1] < intervals[left][0]:
                intervals.insert(left, newInterval)
            else:
                intervals[left:left + 1] = [
                    [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]]

        if right == n or newInterval[1] < intervals[right][0]:
            right -= 1

        intervals[left:right + 1] = [
            [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]]

        return intervals


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.insert([[1, 5]], [0, 0]))
