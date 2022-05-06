import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mp = {i: j for i, j in zip(range(0, 26), string.ascii_uppercase)}
        result = ''

        while columnNumber:
            columnNumber -= 1
            result = mp[columnNumber % 26]+result
            columnNumber //= 26

        return result


s = Solution()

print(s.convertToTitle(2147483647))
