from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import math
        last_product = 1
        max_product = -math.inf
        for item in nums:
            last_product = max(last_product * item, item)
            max_product = max(last_product, max_product)
        return max_product


s = Solution()
print(s.maxProduct([-2, 0, -1]))
