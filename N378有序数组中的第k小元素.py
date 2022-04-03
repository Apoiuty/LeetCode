from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        row = len(matrix)
        col = len(matrix[0])
        while low < high:
            cnt = 0
            mid = low + (high - low) // 2
            i, j = row - 1, 0
            while i >= 0:
                while j < col:
                    if matrix[i][j] <= mid:
                        cnt += i + 1
                        j += 1
                    else:
                        break
                i -= 1


            if cnt < k:
                low = mid + 1
            elif cnt >= k:
                high = mid

        return low


s = Solution()
print(s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
