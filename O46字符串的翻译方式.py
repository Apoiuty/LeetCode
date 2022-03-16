class Solution:
    def translateNum(self, num: int) -> int:
        mp = {}
        mp[''] = 1
        num = str(num)
        last_s = ''
        for s in num[::-1]:
            s += last_s
            first_two = s[:2]
            if 10 <= int(first_two) <= 25:
                mp[s] = mp[last_s[0:]] + mp[last_s[1:]]
            else:
                mp[s] = mp[last_s]
            last_s = s

        return mp[num]


s = Solution()
print(s.translateNum(12258))
