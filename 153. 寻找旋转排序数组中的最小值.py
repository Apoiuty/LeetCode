from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        lo, hi = 0, len(nums) - 1
        while nums[lo] > nums[hi]:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid

        return nums[lo]


s = Solution()
print(s.findMin([3, 1, 2]))
