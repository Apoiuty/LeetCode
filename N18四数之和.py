from typing import List


def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    hash_map = {target - item: i for i, item in enumerate(nums)}
    n = len(nums)
    result = []

    for i in range(n - 3):
        third = n - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 剪枝
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        for j in range(i + 1, n - 2):
            # 剪枝
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, n - 1):
                # 剪枝
                if nums[i] + nums[j] + nums[k] + nums[n - 1] < target:
                    continue
                if nums[i] + nums[j] + nums[k] + nums[k + 1] > target:
                    break
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum in hash_map and hash_map[three_sum] > k:
                    result.append([nums[i], nums[j], nums[k], target - three_sum])

    return result


print(fourSum(0, [2, 2, 2, 2, 2], 8))
