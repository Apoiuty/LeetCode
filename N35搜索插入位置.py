from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    import bisect
    return bisect.bisect_left(nums, target)
