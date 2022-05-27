import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        x = math.log(n, 4)
        return math.isclose(int(x), x)


s = Solution()
print(s.isPowerOfFour(5))
