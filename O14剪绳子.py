def cuttingRope(self, n: int) -> int:
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(max(max(j * dp[i - j], j * (i - j)) for j in range(1, i)))
    return dp[-1]


print(cuttingRope(0, 6))
