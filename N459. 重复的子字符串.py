class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        from functools import cache
        @cache
        def repeatedSubString(p, s):
            if p == s:
                return True
            elif len(p) > len(s):
                return False
            else:
                if p == s[:len(p)]:
                    return repeatedSubString(p, s[len(p):])
                else:
                    return False

        for j in range(1, len(s) // 2 + 1):
            if int(len(s) / j) != len(s) / j:
                continue
            if repeatedSubString(s[:j], s):
                return True

        return False


s = Solution()
print(s.repeatedSubstringPattern("abcabcabcabc"
                                 ))
