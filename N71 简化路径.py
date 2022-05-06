from typing import *


# 2022-04-13 15:36:46

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def simplifyPath(self, path: str) -> str:
        result = path.split('/')
        ans = []
        for _dir in result:
            if _dir == '' or _dir == '.':
                continue
            elif _dir == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(_dir)

        return '/' + '/'.join(ans)

        # leetcode submit region end(Prohibit modification and deletion)


s = Solution()
print(s.simplifyPath('.'))
