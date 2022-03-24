class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i, letter in enumerate(columnTitle[::-1]):
            ans = ans + 26 ** i * (ord(letter) - ord('A') + 1)

        return ans


s = Solution()
print(s.titleToNumber('ZY'))
