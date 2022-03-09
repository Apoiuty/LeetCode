from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        # lo为奇hi为偶
        while lo < hi:
            if nums[lo] % 2:
                lo += 1
            else:
                while not nums[lo] % 2 and lo < hi:
                    _ = nums[lo]
                    nums[lo] = nums[hi]
                    nums[hi] = _
                    hi -= 1

        return nums


s = Solution()
print(s.exchange([]))
