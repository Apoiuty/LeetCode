from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        n = len(nums)
        cum_sum = 0
        min_len = n + 1
        while True:
            if cum_sum - nums[i] >= target:
                cum_sum -= nums[i]
                i += 1
                min_len = min(min_len, j - i)
                continue
            elif j == n:
                break
            else:
                cum_sum += nums[j]
                j += 1
                if cum_sum >= target:
                    min_len = min(min_len, j - i)

        return min_len if min_len != n + 1 else 0


s = Solution()
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
