from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    i = n - 1
    j = 0
    while i >= 0 and j < n:
        item = matrix[i][j]
        if item > target:
            i -= 1
        elif item == target:
            return True
        else:
            j += 1

    return False


print(searchMatrix(0, [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
