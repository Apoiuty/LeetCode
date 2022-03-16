class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        i2 = i3 = i5 = 0
        while len(result) < n:
            max_num = result[-1]
            result_len = len(result)
            while result[i2] * 2 <= max_num and i2 < result_len:
                i2 += 1
            while result[i3] * 3 <= max_num and i3 < result_len:
                i3 += 1
            while result[i5] * 5 <= max_num and i5 < result_len:
                i5 += 1
            result.append(min(result[i2] * 2, result[i3] * 3, result[i5] * 5))

        return result[-1]


s = Solution()
print(s.nthUglyNumber(10))
