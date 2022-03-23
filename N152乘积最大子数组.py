import math
from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return -math.inf
        if len(nums) == 1:
            return nums[0]

        cnt = 0
        first_one = last_one = None
        for i, item in enumerate(nums):
            if item == 0:
                return max(self.maxProduct(nums[:last_one]), self.maxProduct(nums[first_one+1:]))
            elif item < 0:
                cnt += 1
                if first_one == None:
                    last_one = first_one = i
                    continue

                last_one = i

        if cnt % 2:
            return max(self.maxProduct(nums[:first_one]), self.maxProduct(nums[last_one + 1:]))
        else:
            return reduce(lambda x, y: x * y, nums)

s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
