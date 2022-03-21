import math
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        import math
        m = len(grid)
        n = len(grid[0])
        dp = [math.inf] * (n + 1)
        for i in range(m):
            for j in range(n):
                if i or j:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
                else:
                    dp[j] = grid[i][j]

        return int(dp[n - 1])


s = Solution()
print(s.minPathSum(  [[1,2,3],[4,5,6]]))
