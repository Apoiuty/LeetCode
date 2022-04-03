import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = math.inf
        for item in nums[1:]:
            if item > second:
                return True
            elif item > first:
                second = item
            else:
                first = item

        return False


s = Solution()
print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))
