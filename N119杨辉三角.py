from leetcode import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        dp = [1]
        for i in range(rowIndex):
            new_dp = []
            for j in range(len(dp) - 1):
                new_dp.append(dp[j] + dp[j + 1])

            new_dp.append(1)
            new_dp.insert(0,1)

        return dp

s=Solution()
print(s.getRow(3))