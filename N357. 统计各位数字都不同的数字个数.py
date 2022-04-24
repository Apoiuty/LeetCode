import math


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        return 9 * math.perm(9, n - 1) + self.countNumbersWithUniqueDigits(n - 1)


s = Solution()
print(s.countNumbersWithUniqueDigits(2))
