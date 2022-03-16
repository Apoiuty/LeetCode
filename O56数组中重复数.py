from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        one_cnt = defaultdict(int)
        for num in nums:
            str_num = bin(num)
            for i, digit in enumerate(str_num[-1:1:-1]):
                if digit == '1':
                    one_cnt[i] += 1

        num = [0] * len(one_cnt)
        for i in range(len(num)):
            num[i] = one_cnt[i] % 3
        num = [str(i) for i in num]
        num = ''.join(num)
        num = num[::-1]
        num = int(num, 2)
        return num

s=Solution()
print(s.singleNumber( [9,1,7,9,7,9,7]))
