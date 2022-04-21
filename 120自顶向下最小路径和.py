from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last_row = [0]
        for row in triangle:
            next_dp = []
            row_len = len(last_row)
            for i, num in enumerate(row):
                if i == 0:
                    next_dp.append(last_row[0] + num)
                elif i == row_len:
                    next_dp.append(last_row[-1] + num)
                else:
                    next_dp.append(min(last_row[i], last_row[i - 1]) + num)
            last_row = next_dp
        return min(last_row)


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
