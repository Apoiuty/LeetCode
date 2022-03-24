from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        last = []
        for i in range(1, numRows + 1):
            tmp = [1]
            for j in range(1, len(last)):
                tmp.append(last[j] + last[j - 1])
            if i != 1:
                tmp.append(1)
            ans.append(tmp)
            last = tmp

        return ans


s = Solution()
print(s.generate(6))
