from typing import List


def findDuplicate(self, nums: List[int]) -> int:
    i = 0
    j = 0
    while True:
        i = nums[nums[i]]
        j = nums[j]
        if nums[i] == nums[j]:
            break

    i = 0
    while nums[i] != nums[j]:
        i = nums[i]
        j = nums[j]

    return nums[i]


print(findDuplicate(0,[3,1,3,4,2]))
