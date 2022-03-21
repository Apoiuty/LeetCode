from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0]]
        dp.append(max(nums[:2]))
        for item in nums[2:]:
            dp.append(max(dp[-2] + item, dp[-1]))

        return dp[-1]


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
