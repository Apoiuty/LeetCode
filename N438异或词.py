from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        from collections import defaultdict
        differ = defaultdict(int)
        for i, j in zip(s, p):
            differ[i] += 1
            differ[j] -= 1

        condition = list(bool(c) for c in differ.values()).count(True)

        ans = []
        for i in range(len(s) - len(p)):
            if not i and not condition:
                ans.append(i)
            if differ[s[i]] == 1:
                condition -= 1
            elif differ[s[i]] == 0:
                condition += 1
            differ[s[i]] -= 1

            if differ[s[i + len(p)]] == -1:
                condition -= 1
            elif differ[s[i + len(p)]] == 0:
                condition += 1

            differ[s[i + len(p)]] += 1

            if not condition:
                ans.append(i + 1)

        return ans


s = Solution()
print(s.findAnagrams("abab", "ab"))
