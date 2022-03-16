from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == mid:
                lo = mid + 1
            elif nums[mid] > mid:
                hi = mid - 1
            else:
                continue
        return nums[lo]-1 if lo<len(nums) else len(nums)

s=Solution()
print(s.missingNumber([0]))
