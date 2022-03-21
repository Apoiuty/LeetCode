class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        f_n_1 = 0
        for i in range(2, n + 1):
            fn = (f_n_1 + m) % i
            f_n_1 = fn

        return fn


s = Solution()
print(s.lastRemaining(82002, 120659))
