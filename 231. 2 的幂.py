import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 or (n != 1 and n % 2):
            return False

        result = math.log2(n)
        if 0 < n:
            return math.isclose(int(result), result)
