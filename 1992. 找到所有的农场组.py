from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    ans = [i, j]
                    while j < n - 1 and land[i][j + 1] == 1:
                        j += 1
                    while i < m - 1 and land[i + 1][j] == 1:
                        i += 1
                    ans.extend([i, j])
                    for i in range(ans[0], ans[2] + 1):
                        for j in range(ans[1], ans[-1] + 1):
                            land[i][j] = 0
                    result.append(ans)
                    i, j = ans[0], ans[1]

        return result


s = Solution()
print(s.findFarmland([[1, 1, 0, 0, 0, 1],
                      [1, 1, 0, 0, 0, 0]]))
