from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        mode = 'right'
        i = 0
        j = 0
        result = []
        while left <= j <= right and up <= i <= down:
            result.append(matrix[i][j])
            if mode == 'right':
                if j + 1 <= right:
                    j += 1
                else:
                    mode = 'down'
                    i += 1
                    up += 1
                continue

            if mode == 'down':
                if i + 1 <= down:
                    i += 1
                else:
                    mode = 'left'
                    j -= 1
                    right -= 1
                continue

            if mode == 'left':
                if j - 1 >= left:
                    j -= 1
                else:
                    mode = 'up'
                    i -= 1
                    down -= 1
                continue

            if mode == 'up':
                if i - 1 >= up:
                    i -= 1
                else:
                    mode = 'right'
                    j += 1
                    left += 1
                continue
        return result


s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
