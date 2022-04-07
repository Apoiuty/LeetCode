from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        result = [0, 1]

        for i in range(n - 1):
            base = 2 ** (i + 1)
            for num in result[::-1]:
                result.append(base | num)

        return result

s=Solution()
print(s.grayCode(4))
