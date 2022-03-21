from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import defaultdict
        import math
        dp = defaultdict(lambda: math.inf)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = 1 + min(dp[i - j] for j in coins)

        if dp[amount] == math.inf:
            return -1
        else:
            return int(dp[amount])


s = Solution()
print(s.coinChange([1, 2, 5], 11))
pass