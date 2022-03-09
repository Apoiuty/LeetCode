from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_income = 0
        for item in prices:
            if item - min_price > max_income:
                max_income = item - min_price
            elif item < min_price:
                min_price = item

        return max_income


s = Solution()
print(s.maxProfit([7,6,4,3,1]))
