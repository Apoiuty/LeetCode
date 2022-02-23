from typing import List


def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    closed_num = 10 ** 5

    # value在和之间
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 剪枝
        # 如果最小的和开始远离目标值
        min_sum = nums[i] + nums[i + 1] + nums[i + 2]
        if min_sum >= target:
            if abs(min_sum - target) < abs(closed_num - target):
                closed_num = min_sum
                break
        max_sum = nums[i] + nums[n - 1] + nums[n - 2]
        if max_sum <= target:
            if abs(max_sum - target) < abs(closed_num - target):
                closed_num = max_sum
                continue
        j = i + 1
        k = n - 1
        while j < k:
            three_sum = nums[i] + nums[j] + nums[k]
            if abs(three_sum - target) < abs(closed_num - target):
                closed_num = three_sum
            if three_sum < target:
                j += 1
            elif three_sum == target:
                return target
            else:
                k -= 1

    return closed_num


print(threeSumClosest(0, [1, 2, 4, 8, 16, 32, 64, 128], 82))
