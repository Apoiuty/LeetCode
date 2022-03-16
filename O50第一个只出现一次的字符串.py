class Solution:
    def firstUniqChar(self, s: str) -> str:
        from collections import OrderedDict
        mp = OrderedDict()
        for letter in s:
            if letter not in mp:
                mp[letter] = 1
            else:
                mp[letter] += 1

        if not mp:
            return ' '

        try:
            result_index = list(mp.values()).index(1)
            return list(mp.keys())[result_index]
        except:
            return ' '


s = Solution()
print(s.firstUniqChar("abaccdeff"))
