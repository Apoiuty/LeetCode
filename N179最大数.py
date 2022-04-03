from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def cmp(a, b):
            if a + b > b + a:
                return 1
            elif a + b == b + a:
                return 0
            else:
                return -1

        nums = [str(i) for i in nums]
        result = ''.join(sorted(nums, key=cmp_to_key(cmp), reverse=True))
        if result.startswith('0'):
            return '0'
        else:
            return result


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
