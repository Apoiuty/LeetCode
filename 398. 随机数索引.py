from typing import List
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        from collections import defaultdict
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if not randrange(cnt):
                    ans = i

        return ans
