from functools import lru_cache


class Solution:
    def __init__(self):
        self.mp = {}

    def numDecodings(self, s: str) -> int:
        if s in self.mp:
            return self.mp[s]
        if s.startswith('0'):
            self.mp[s] = 0
            return 0
        if len(s) <= 1:
            self.mp[s] = 1
            return 1
        elif s[0] > '2':
            self.mp[s] = self.numDecodings(s[1:])
            return self.mp[s]
        elif s[0] == '2' and s[1] > '6':
            self.mp[s] = self.numDecodings(s[2:])
            return self.mp[s]
        else:
            self.mp[s] = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            return self.mp[s]


s = Solution()
print(s.numDecodings("123123"))
