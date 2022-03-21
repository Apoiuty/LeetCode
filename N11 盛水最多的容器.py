from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        hi = len(height) - 1
        max_water = 0
        while lo < hi:
            v = min(height[lo], height[hi]) * (hi - lo)
            max_water = max(max_water, v)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return max_water

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
