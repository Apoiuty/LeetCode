class Solution:
    def baseNeg2(self, n: int) -> str:
        if not n:
            return '0'
        base = -2
        result = ''
        while n:
            remainder = n % base
            remainder = 1 if remainder == -1 else 0
            n = (n - remainder) // -2

            if remainder == 1:
                result = '1' + result
            else:
                result = '0' + result

        result.lstrip('0')

        return result


s = Solution()
print(s.baseNeg2(0))
