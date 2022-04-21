from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def cnt2_and_cnt5(num):
            cnt2 = cnt5 = 0
            while num:
                if num % 2 == 0:
                    num //= 2
                    cnt2 += 1
                    continue
                if num % 5 == 0:
                    num //= 5
                    cnt5 += 1
                    continue
                break
            return cnt2, cnt5

        m, n = len(grid), len(grid[0])
        # 横着前缀和
        row_cnt2 = [[0] * (2 + n) for i in range(m)]
        row_cnt5 = [[0] * (2 + n) for i in range(m)]
        # 竖着前缀和
        col_cnt2 = [[0] * n for i in range(m + 2)]
        col_cnt5 = [[0] * n for i in range(m + 2)]

        for i in range(m):
            for j in range(n):
                cnt2, cnt5 = cnt2_and_cnt5(grid[i][j])
                # 行2行5
                row_cnt2[i][j + 1] = row_cnt2[i][j] + cnt2
                row_cnt5[i][j + 1] = row_cnt5[i][j] + cnt5
                # 列2列5
                col_cnt2[i + 1][j] = col_cnt2[i][j] + cnt2
                col_cnt5[i + 1][j] = col_cnt5[i][j] + cnt5
                if j == n - 1:
                    row_cnt2[i][n + 1] = row_cnt2[i][n]
                    row_cnt5[i][n + 1] = row_cnt5[i][n]
                if i == m - 1:
                    col_cnt2[m + 1][j] = col_cnt2[m][j]
                    col_cnt5[m + 1][j] = col_cnt5[m][j]

        max_zero = 0
        for i in range(m):
            for j in range(n):
                item = grid[i][j]
                item_2, item_5 = cnt2_and_cnt5(item)
                left2 = row_cnt2[i][j] - row_cnt2[i][0]
                right2 = row_cnt2[i][n + 1] - row_cnt2[i][j + 1]
                up2 = col_cnt2[i][j] - col_cnt2[0][j]
                down2 = col_cnt2[m + 1][j] - col_cnt2[i + 1][j]

                left5 = row_cnt5[i][j] - row_cnt5[i][0]
                right5 = row_cnt5[i][n + 1] - row_cnt5[i][j + 1]
                up5 = col_cnt5[i][j] - col_cnt5[0][j]
                down5 = col_cnt5[m + 1][j] - col_cnt5[i + 1][j]

                left_up = min(left2 + up2 + item_2, left5 + up5 + item_5)
                left_down = min(left2 + down2 + item_2, left5 + down5 + item_5)
                right_up = min(right2 + up2 + item_2, right5 + up5 + item_5)
                right_down = min(right2 + down2 + item_2, right5 + down5 + item_5)

                max_zero = max(max_zero, left_up, left_down, right_up, right_down)

        return max_zero


s = Solution()
print(s.maxTrailingZeros(
    [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]))
