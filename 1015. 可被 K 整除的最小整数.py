class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        if k == 1:
            return 1

        rem = 1
        cnt = 1
        while rem := (rem * 10 + 1) % k:
            cnt += 1

        return cnt + 1


s = Solution()
print(s.smallestRepunitDivByK(4))
