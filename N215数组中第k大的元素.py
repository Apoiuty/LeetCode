from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    i = n - 1
    if k == 1:
        return nums[-1]
    while k and i:
        if nums[i] != nums[i - 1]:
            k -= 1
        i -= 1
    return nums[i + 1]


print(findKthLargest(0, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
