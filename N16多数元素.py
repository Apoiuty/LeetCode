from typing import List


def majorityElement(self, nums: List[int]) -> int:
    top1_cnt = 0
    top1 = nums[0]

    for item in nums[1:]:
        if item == top1:
            top1_cnt += 1
        else:
            top1_cnt -= 1
        if top1_cnt < 0:
            top1 = item
            top1_cnt = 0

    return top1


print(majorityElement(0, [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]))
