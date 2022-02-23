from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    item_index_map = {}
    for i, item in enumerate(nums):
        if target - item in item_index_map:
            return [i, item_index_map[target - item]]
        else:
            item_index_map[item] = i


print(twoSum(0, [3, 2, 4], 6))
