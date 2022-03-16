from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def compare_func(a, b):
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0

        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(compare_func))
        return ''.join(nums)


s = Solution()
print(s.minNumber([3, 30, 34, 5, 9]))
