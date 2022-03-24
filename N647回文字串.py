class Solution:
    def countSubstrings(self, s: str) -> int:
        i = cnt = 0
        n = len(s)
        cnt += n
        while i < len(s):
            # 偶数个扩展
            start = i
            end = i + 1
            while start >= 0 and end < n and s[start] == s[end]:
                cnt += 1
                start -= 1
                end += 1

            start = i - 1
            end = i + 1
            while start >= 0 and end < n and s[start] == s[end]:
                cnt += 1
                start -= 1
                end += 1
            i += 1
        return cnt

s=Solution()
print(s.countSubstrings('aaaaa'))