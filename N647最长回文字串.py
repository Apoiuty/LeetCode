class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        n = len(s)
        i = 1
        dp[0] = 0
        cnt = 1
        all_same = False
        while i < n:
            cnt += 1
            if dp[i - 1] - 1 >= 0:
                # 扩大
                if s[dp[i - 1] - 1] == s[i]:
                    dp[i] = dp[i - 1] - 1
                    cnt += 1
                elif s[dp[i - 1]] == s[i]:
                    dp[i] = dp[i - 1]
                    cnt += i - dp[i]
                    all_same = True
                else:
                    all_same = False
                    dp[i] = i
            else:
                if s[dp[i - 1]] == s[i]:
                    if all_same:
                        cnt += i - dp[i - 1]
                        dp[i] = dp[i - 1]
                    elif i - dp[i - 1] == 1:
                        all_same = True
                        cnt += 1
                    else:
                        dp[i] = i
                else:
                    all_same = False
                    dp[i] = i

            i += 1

        return cnt


s = Solution()
print(s.countSubstrings("aaa"))
