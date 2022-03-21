from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        # 0的路径有一个，其他的路径为0个
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


s = Solution()
print(s.change(5, [1, 2, 5]))
