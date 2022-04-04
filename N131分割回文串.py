from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(s, path):
            if s == '':
                ans.append(path)
            for i in range(1, len(s) + 1):
                # 从1开始检测是否是回文串
                pat = s[:i]
                if pat == pat[::-1]:
                    dfs(s[i:], path + [s[:i]])

        dfs(s, [])
        return ans


s = Solution()
print(s.partition('a'))
