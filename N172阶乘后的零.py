class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if i % 5 == 0:
                cnt += 1

        return cnt
