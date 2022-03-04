from typing import List


def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    j = n - 1
    while j:
        if nums[j]:
            j -= 1
        else:
            i = 0
            can_jump_out = False
            while i < j:
                if nums[i] > j - i:
                    can_jump_out = True
                    break
                else:
                    i += 1
            if can_jump_out:
                j = i
            else:
                return False

    return True


print(canJump(0, [3,2,1,0,4]))
