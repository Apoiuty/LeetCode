from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        result = []
        for i in range(n+1):
            if i == 0:
                result.append(0)
            elif i % 2:
                result.append(result[i - 1] + 1)
            else:
                result.append(result[i // 2])

        return result


s = Solution()
print(s.countBits(5))
