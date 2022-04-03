from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        from random import shuffle
        ans = []
        index = list(range(len(self.nums)))
        shuffle(index)
        for i in index:
            ans.append(self.nums[i])

        return ans
