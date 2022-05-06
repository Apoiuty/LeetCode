from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        for i, j in zip_longest(reversed(a), reversed(b)):
            if i == None:
                i = 0
            elif i == '1':
                i = 1
            else:
                i = 0
            if j == None:
                j = 0
            elif j == '1':
                j = 1
            else:
                j = 0

            ans = str(i ^ j ^ carry)+ans
            carry = (~carry & (i & j)) | (carry & (i | j))

        if carry:
            ans='1'+ans

        return ans


s = Solution()
print(s.addBinary('1010', '1011'))
