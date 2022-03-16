from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        f = [0] + [1] * 6

        for i in range(2, n + 1):
            new_f = [0] * i
            for j in range(i, 6 * i + 1):
                num_cnt = sum(f[max(0, j - 6):j])
                new_f.append(num_cnt)
            f = new_f

        f = f[n:]
        return [i / 6 ** n for i in f]


s = Solution()
print(s.dicesProbability(1))
