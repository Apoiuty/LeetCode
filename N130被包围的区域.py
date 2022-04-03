from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'R'
            else:
                return
            if i + 1 < m:
                dfs(i + 1, j)
            if i - 1 >= 0:
                dfs(i - 1, j)
            if j + 1 < n:
                dfs(i, j + 1)
            if j - 1 >= 0:
                dfs(i, j - 1)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m - 1][i] == 'O':
                dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


s = Solution()
b = [["X"]]
print(s.solve(b))
print(b)
