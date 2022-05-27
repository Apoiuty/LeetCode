from typing import List
import bisect
from itertools import accumulate


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left - 1] if left > 0 else self.nums[right]


s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.sumRange(0, 2))
print(s.sumRange(2, 5))
print(s.sumRange(0, 5))
