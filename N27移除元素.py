from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)

    return len(nums)


print(removeElement(0, [1, 2, 3, 1], 1))
