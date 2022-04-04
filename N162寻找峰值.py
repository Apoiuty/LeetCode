import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) + 1
        nums.insert(0, -math.inf)
        nums.append(-math.inf)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid - 1
            else:
                if nums[mid + 1] > nums[mid]:
                    lo = mid + 1
                elif nums[mid - 1] > nums[mid]:
                    hi = mid - 1


s = Solution()
print(s.findPeakElement([1]))
