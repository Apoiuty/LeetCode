import math
from functools import lru_cache


class Solution:
    @lru_cache
    def integerBreak(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2

        return max(max(self.integerBreak(i), i) * max(n - i, self.integerBreak(n - i)) for i in range(1, n))


s = Solution()
print(s.integerBreak(8))
