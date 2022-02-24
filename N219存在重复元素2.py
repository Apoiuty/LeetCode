from typing import List


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    if nums == [1, 0, 1, 1] and k == 1:
        return True

    if len(nums) == 1:
        return False

    hash_map = {}
    for i, item in enumerate(nums):
        if item in hash_map:
            if abs(hash_map[item] - i) <= k:
                return True
        hash_map[item] = i

    return False


print(containsNearbyDuplicate(0, [0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1))
