from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        pre_sum = 0
        cnt = 0
        dp[0] = 1
        for num in nums:
            pre_sum += num
            cnt += dp[pre_sum - k]
            dp[pre_sum] += 1

        return cnt


s = Solution()
print(s.subarraySum([1,1,1], 2))
