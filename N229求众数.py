from typing import List


def majorityElement(self, nums: List[int]) -> List[int]:
    top1_cnt = 0
    top1 = None
    top2 = None
    top2_cnt = 0

    for item in nums:
        if item == top1:
            top1_cnt += 1
        elif item == top2:
            top2_cnt += 1
        elif not top2_cnt:
            top2 = item
            top2_cnt += 1
        elif not top1_cnt:
            top1 = item
            top1_cnt += 1
        else:
            top2_cnt -= 1
            top1_cnt -= 1

    top2_cnt = top1_cnt = 0
    result = []
    for item in nums:
        top1_cnt += 1 if item == top1 else 0
        top2_cnt += 1 if item == top2 else 0

    if top1_cnt > len(nums) // 3:
        result.append(top1)
    if top2_cnt > len(nums) // 3:
        result.append(top2)

    return result


print(majorityElement(1, [2, 1, 1, 3, 1, 4, 5, 6]))
