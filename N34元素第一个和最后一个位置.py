from typing import List


def searchRange(self, nums: List[int], target: int) -> List[int]:
    import bisect
    if not nums:
        return [-1, -1]
    left = bisect.bisect_left(nums, target)
    if not (left != len(nums) and nums[left] == target):
        return [-1, -1]
    right = bisect.bisect_right(nums, target) - 1
    return [left, right]


nums = []
target = 0
print(searchRange(0, nums, target))
