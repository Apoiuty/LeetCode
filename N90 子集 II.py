from typing import *


# 2022-04-14 11:52:45

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def back_trace(i, subset, not_choose):
            if i >= len(nums):
                # 给你机会你不中用啊
                ans.append(subset)
            elif nums[i] in not_choose:
                back_trace(i + 1, subset, not_choose)
            else:
                back_trace(i + 1, subset + [nums[i]], not_choose)
                back_trace(i + 1, subset, not_choose | {nums[i]})

        back_trace(0, [], set())
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
ans = s.subsetsWithDup([1,2,2])
print(sorted(ans))
