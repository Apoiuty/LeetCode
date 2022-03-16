from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0]*(n+1)
        # 这个加一太精髓了,省去了边界条件判断，完美利用了Python哈哈哈
        for i in range(m):
            for j in range(n):
                dp[j] = max(dp[j], dp[j-1]) + grid[i][j]

        return dp[n-1]
