class Solution:
    def countDigitOne(self, n: int) -> int:
        count_one = [0]
        for i in range(1, n + 1):
            if i % 10 == 1:
                count_one.append(count_one[-1] + 1)
            else:
                count_one.append(count_one[i // 10])

        return sum(count_one)


class Solution1:
    def countDigitOne(self, n: int) -> int:
        if 1 <= n < 10:
            return 1
        if n == 0:
            return 0
        str_n = str(n)
        up = str_n[0]
        down = str_n[1:]
        up = int(up)
        down = int(down)

        if up > 1:
            return self.countDigitOne(down) + up * self.countDigitOne(10 ** len(str_n[1:]) - 1) + (
                    10 ** len(str_n[1:]))
        else:
            return down + 1 + self.countDigitOne(down) + self.countDigitOne(10 ** len(str_n[1:]) - 1)


s = Solution1()
s1 = Solution()
print(s.countDigitOne(10))
print(s1.countDigitOne(234565))
