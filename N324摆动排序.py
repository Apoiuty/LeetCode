from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        count = Counter(nums)
        # 因为只有5000个数所以这是个常数
        keys = sorted(count.keys(), reverse=True)
        i = 1
        # 逆序最多移开一位
        for key in keys:
            key_cnt = count[key]
            for k in range(key_cnt):
                if i < len(nums):
                    nums[i] = key
                    i += 2
                else:
                    i = 0
                    nums[i] = key
                    i += 2


s = Solution()
nums = [1, 3, 2, 2, 3, 1]
s.wiggleSort(nums)
print(nums)
