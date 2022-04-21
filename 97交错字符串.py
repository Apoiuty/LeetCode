from collections import defaultdict


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1 + s2) != len(s3):
            return False

        mp = [0] * (1 + len(s2))
        mp[0] = 1

        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i > 0:
                    # 后面一个是i-1行的j
                    mp[j] |= mp[j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    # 后面是i行的j
                    mp[j] |= mp[j - 1] and s2[j - 1] == s3[i + j - 1]

        return bool(mp[len(s2)])


s1 = "a"
s2 = ""
s3 = "a"
s = Solution()
print(s.isInterleave(s1, s2, s3))
