class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []
        if numerator * denominator < 0:
            sign = -1
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            sign = 1
        result.append(str(numerator // denominator))
        numerator %= denominator

        # 小数部分
        if numerator != 0:
            result.append('.')
            seen = dict()
            numerator *= 10
            cnt = 2
            while numerator and numerator not in seen:
                seen[numerator] = cnt
                result.append(str(numerator // denominator))
                numerator %= denominator
                numerator *= 10
                cnt += 1
            # 还能继续计算说明无限循环
            if numerator:
                result.insert(seen[numerator], '(')
                result.append(')')

        ans = ''.join(result)
        if sign == -1:
            return '-' + ans
        else:
            return ans


s = Solution()
print(s.fractionToDecimal(-1, -6))
