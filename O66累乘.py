from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        sum = 1
        up = []
        for i in a:
            sum *= i
            up.append(sum)

        up.append(1)
        sum = 1
        down = []
        for i in a[::-1]:
            sum *= i
            down.append(sum)
        down = down[::-1]
        down.append(1)
        n = len(a)
        b = []
        for i in range(n):
            b.append(up[i - 1] * down[i + 1])

        return b


s = Solution()
print(s.constructArr([1, 2, 3, 4, 5]))
