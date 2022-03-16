from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero_cnt = 0
        pre_num = None
        for num in nums:
            if not num:
                zero_cnt += 1
            else:
                if not pre_num:
                    pre_num = num
                else:
                    if pre_num == num - 1:
                        pre_num = num
                    elif pre_num == num:
                        return False
                    elif zero_cnt >= num - pre_num - 1:
                        zero_cnt -= num - pre_num - 1
                        pre_num = num
                    else:
                        return False

        return True


s = Solution()
print(s.isStraight([9, 0, 6, 0, 10]))
