class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        begin = True
        num = 0
        for digit in s:
            if digit == '0' and begin:
                continue
            elif digit.isdigit():
                begin=False
                num = num * 10 + int(digit)
            else:
                break

        num = sign * num
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < -2 ** 31:
            return -2 ** 31

        return num


s = Solution()
print(s.myAtoi("21474836460"))
