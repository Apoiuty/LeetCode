import math
from typing import List


def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums or len(nums) == 1:
        return
    n = len(nums)
    j = n - 1
    i = j - 1
    while i >= 0:
        if nums[i] >= nums[i + 1]:
            i -= 1
        else:
            break
    if i == -1:
        return nums.reverse()

    next_slice = nums[i + 1:]
    max_num = math.inf
    item_index = 0
    while item_index < len(next_slice):
        item = next_slice[item_index]
        if item > nums[i] and item < max_num:
            max_num = item
        if item <= nums[i]:
            break
        item_index += 1
    next_slice[item_index - 1] = nums[i]
    nums[i] = max_num
    
    nums[i + 1:] = sorted(next_slice)


nums = [1,5,1]
nextPermutation(0, nums)
print(nums)
