from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for key,item in cnt.items():
            if item==1:
                return key
