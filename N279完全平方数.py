class Solution:
    def numSquares(self, n: int) -> int:
        tmp = n
        while tmp:
            if tmp % 8 == 7:
                return 4
            if tmp // 4 == tmp / 4:
                tmp = tmp // 4
            else:
                break

        if int(n ** .5) == n ** .5:
            return 1

        for i in range(1, int(n ** .5) + 1):
            item = n - i ** 2
            if int(item ** .5) == item ** .5:
                return 2

        return 3


s = Solution()
print(s.numSquares(12))
