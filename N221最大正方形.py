from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        from collections import defaultdict
        dp = defaultdict(int)
        max_length = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[(i, j)] = 0
                    continue
                dp[(i, j)] = min(dp[(i - 1, j)], dp[(i, j - 1)], dp[(i - 1, j - 1)]) + 1
                max_length = max(max_length, dp[(i, j)])

        return max_length ** 2


s = Solution()
print(s.maximalSquare(
    [["0"]]))
