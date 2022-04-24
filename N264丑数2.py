class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1]
        p2 = p3 = p5 = 0
        for i in range(n - 1):
            dp.append(min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5))
            if dp[-1] == dp[p3] * 3:
                p3 += 1
            if dp[-1] == dp[p5] * 5:
                p5 += 1
            if dp[-1] == dp[p2] * 2:
                p2 += 1

        return dp[-1]

s=Solution()
print(s.nthUglyNumber(10))
