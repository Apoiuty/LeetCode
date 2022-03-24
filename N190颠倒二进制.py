class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))[2:]
        n = n[::-1] + '0' * (32 - len(n))
        return int(n, 2)


s = Solution()
print(s.reverseBits(964176192))
