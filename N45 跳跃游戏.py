import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1
        if len(nums) == 1:
            return 0

        i = 0
        cnt = 1
        nums_ = len(nums) - 1
        while True:
            if i >= nums_ or nums[i] + i >= nums_:
                return cnt

            next_i = i + 1
            for j in range(2, nums[i] + 1):
                if nums[j + i] + j + i >= nums[next_i] + next_i:
                    next_i = j + i
            i = next_i
            cnt += 1


s = Solution()
print(s.jump([2,3,0,1,4]))
