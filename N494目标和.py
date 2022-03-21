from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        neg = (sum(nums) - target) / 2
        if neg < 0 or int(neg) != neg :
            return 0
        neg = int(neg)

        for num in nums:
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[neg]


s = Solution()
print(s.findTargetSumWays([1], 1))
