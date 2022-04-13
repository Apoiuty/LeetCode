class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        digits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        digit_mp = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        digits.reverse()
        digit_mp.reverse()
        for i, digit in enumerate(digits):
            if num >= digit:
                cnt = num // digit
                num %= digit
                ans =  ans+digit_mp[i] * cnt
            if num == 0:
                return ans

s=Solution()
print(s.intToRoman(1994))
