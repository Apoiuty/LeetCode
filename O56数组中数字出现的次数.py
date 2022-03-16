from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        sum = 0
        for num in nums:
            sum ^= num

        cnt = 0
        while not sum % 2:
            sum >>= 1
            cnt += 1

        sum1 = sum2 = 0
        for num in nums:
            if num & 1 << cnt:
                sum1 ^= num
            else:
                sum2 ^= num

        return [sum1, sum2]
