class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        for num in range(left, right + 1):
            if (1 << str(bin(num)).count('1')) & 665772:
                cnt += 1

        return cnt

s=Solution()
print(s.countPrimeSetBits(10,15))
