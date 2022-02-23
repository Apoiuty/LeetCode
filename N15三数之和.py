from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        third = n - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            target = -nums[i] - nums[j]
            while j < third and nums[third] > target:
                third -= 1
            if j == third:
                break

            if not nums[i] + nums[j] + nums[third]:
                result.append([nums[i], nums[j], nums[third]])

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
