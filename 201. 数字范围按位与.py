class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while (left >> cnt) != (right >> cnt):
            cnt += 1
        return left >> cnt << cnt

s=Solution()
print(s.rangeBitwiseAnd(1,2147483647))