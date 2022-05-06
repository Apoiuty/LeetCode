from typing import *


# 2022-04-13 17:57:03

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        cnt = 1
        pre_num = None
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num != pre_num:
                pre_num = num
                nums[start] = num
                start += 1
                cnt = 1
                i += 1
            elif num == pre_num:
                if cnt < 2:
                    nums[start] = num
                    start += 1
                    cnt = 2
                    i += 1
                else:
                    while i < n and nums[i] == pre_num:
                        i += 1
        return start

        # leetcode submit region end(Prohibit modification and deletion)
