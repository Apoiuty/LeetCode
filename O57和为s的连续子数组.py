from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        lo = 1
        hi = 2
        while hi <= target // 2 + 1:
            item = sum(range(lo, hi + 1))
            if item == target:
                result.append(list(range(lo, hi + 1)))
                lo += 1
            elif item > target:
                while item > target:
                    lo += 1
                    item = sum(range(lo, hi + 1))
            else:
                hi += 1

        return result


s = Solution()
print(s.findContinuousSequence(15))
