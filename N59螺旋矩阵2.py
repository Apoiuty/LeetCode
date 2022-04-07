from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0] * n)

        di = 0
        dj = 1
        x = 0
        y = 0
        for i in range(1, n ** 2 + 1):
            try:
                # 这个位置不行
                if matrix[x][y]:
                    raise
                matrix[x][y] = i
                x += di
                y += dj
            except:
                x -= di
                y -= dj
                di, dj = dj, -di
                matrix[x + di][y + dj] = i
                x += 2 * di
                y += 2 * dj

        return matrix


s = Solution()
print(s.generateMatrix(3))
