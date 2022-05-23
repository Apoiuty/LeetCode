import re


class Solution:
    def reverseBits(self, num: int) -> int:
        if num < 0:
            num &= (1 << 32) - 1
        num = bin(num)[2:]
        if num.startswith('1'):
            num = '0' + num
        if num.endswith('1'):
            num += '0'
        num = num.split('0')
        max_len = 0
        i = 0
        while i < len(num) - 1:
            max_len = max(max_len, len(num[i]) + len(num[i + 1]) + 1)
            i += 1

        return min(32, max_len)


s = Solution()
print(s.reverseBits(-1))
