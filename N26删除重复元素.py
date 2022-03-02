from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    cnt = 1
    for i in range(0, n - 1):
        if nums[i] != nums[i + 1]:
            nums[cnt] = nums[i+1]
            cnt += 1


    return cnt


print(removeDuplicates(0, [1,1,2]))
