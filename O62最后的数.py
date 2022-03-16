class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = list(range(n))
        while len(l) > 1:
            del l[m % len(l) - 1]
        return l[0]


s = Solution()
print(s.lastRemaining(5, 3))
