from collections import defaultdict
from typing import List


def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    cnt = 0
    hash_map = defaultdict(int)
    for i in nums1:
        for j in nums2:
            hash_map[i + j] += 1

    for i in nums3:
        for j in nums4:
            cd_sum = -(i + j)
            if cd_sum in hash_map:
                cnt += hash_map[cd_sum]

    return cnt
