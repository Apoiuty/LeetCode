import bisect
from typing import List


def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    j = n - 1
    pre_ij = [i, j]
    while 1:

        mid = i + (j - i) // 2
        if nums[mid] > nums[j]:
            i = mid
        if nums[mid] < nums[i]:
            j = mid

        if [i, j] == pre_ij:
            break
        pre_ij = [i, j]

    left = nums[:i + 1]
    right = nums[i + 1:]
    l_i = bisect.bisect_left(left, target)
    r_i = bisect.bisect_left(right, target)
    if l_i != len(left) and left[l_i] == target:
        return l_i
    if r_i != len(right) and right[r_i] == target:
        return r_i + i + 1

    return -1


print(search(0,  [4,5,6,7,0,1,2], 0))
