class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m - 1
        n = n - 1
        from scipy.special import perm
        return int(round(perm(m + n, m + n) / perm(m, m) / perm(n, n)))


s = Solution()
print(s.uniquePaths(36, 7))
