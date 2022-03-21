from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reversed_product = []
        product = 1
        for i in nums[::-1]:
            product *= i
            reversed_product.append(product)
        reversed_product.reverse()
        reversed_product.append(1)
        product = 1
        for i, item in enumerate(nums):
            reversed_product[i] = product * reversed_product[i + 1]
            product *= item

        return reversed_product[:-1]


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
