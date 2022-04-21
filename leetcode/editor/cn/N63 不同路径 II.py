from typing import *


# 2022-04-13 12:28:37

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[(0, i)] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[(i, 0)] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue

                if not obstacleGrid[i - 1][j]:
                    dp[(i, j)] += dp[(i - 1, j)]

                if not obstacleGrid[i][j - 1]:
                    dp[(i, j)] += dp[(i, j - 1)]

        return dp[(m - 1, n - 1)]

        # leetcode submit region end(Prohibit modification and deletion)

s=Solution()
print(s.uniquePathsWithObstacles([[1,0]]))