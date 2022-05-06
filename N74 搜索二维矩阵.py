from typing import *


# 2022-04-13 17:42:20

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            elif target < matrix[i][j]:
                i -= 1

        return False
# leetcode submit region end(Prohibit modification and deletion)
