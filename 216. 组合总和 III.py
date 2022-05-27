from typing import List
from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = list(range(1, 9))
        for num in combinations(nums, k):
            if sum(num) == n:
                result.append(list(num))

        return result
