from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        if w % 2:
            return False
        W = w // 2
        w = nums
        from collections import defaultdict
        dp = defaultdict(lambda: False)
        dp[0] = True
        nv = len(nums)

        for i in range(nv):
            for j in range(W, w[i] - 1, -1):
                # j为不加i，j-w[i]为加i物品
                dp[j] = dp[j] or dp[j - w[i]]
                if j == W and dp[W]:
                    return True
