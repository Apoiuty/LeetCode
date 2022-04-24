import math
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        primes_ptr = {i: 0 for i in primes}

        dp = [1]
        for i in range(n - 1):
            min_value = math.inf
            min_key = []
            for value, ptr in primes_ptr.items():
                next_num = dp[ptr] * value
                if next_num < min_value:
                    min_value = next_num
                    min_key = [value]
                elif next_num == min_value:
                    min_key.append(value)
            dp.append(min_value)
            for key in min_key:
                primes_ptr[key] += 1

        return dp[-1]


s = Solution()
print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
