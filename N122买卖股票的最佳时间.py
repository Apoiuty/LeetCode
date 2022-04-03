from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])

        return ans


s = Solution()
print(s.maxProfit([7, 6, 4, 3, 1]))
