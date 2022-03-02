from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    mp = set(nums)
    max_cnt = 0
    for item in nums:
        cnt = 0
        if item - 1 in mp:
            continue
        else:
            while item + 1 in mp:
                cnt += 1
                item += 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt

print()