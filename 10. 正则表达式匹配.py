from functools import lru_cache


class Solution:
    @lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif s and not p:
            return False
        elif p and not s :
            if not p.endswith('*'):
                return False
            p = p.split('*')
            for char in p:
                if len(char) > 1:
                    return False
            return True

        pi = 0
        ps = 0
        ns = len(s)
        np = len(p)
        while pi < np and ps < ns:
            if pi < np - 1 and p[pi + 1] != '*' or pi == np - 1:
                if p[pi] != s[ps] and p[pi] != '.':
                    return False
                else:
                    pi += 1
                    ps += 1
            else:
                repeat_char = p[pi]
                if repeat_char != '.':
                    cnt = 0
                    i = ps
                    while i < ns and s[i] == repeat_char:
                        i += 1
                        cnt += 1

                    if cnt == 0:
                        # 不包含目标序列
                        return self.isMatch(s[ps:], p[pi + 2:])
                    else:
                        for i in range(cnt + 1):
                            if self.isMatch(s[ps:], repeat_char * i + p[pi + 2:]):
                                return True
                        return False
                else:
                    i = ps
                    while i <= ns:
                        if self.isMatch(s[i:], p[pi + 2:]):
                            return True
                        i += 1

                    return False

        # 个数完全匹配
        if pi == np and ps == ns:
            return True
        elif pi < np:
            return self.isMatch('', p[pi:])
        else:
            return False


s = Solution()
print(s.isMatch("ab", ".*c"))
