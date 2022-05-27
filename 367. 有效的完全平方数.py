class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 0
        hi = num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            n = mid ** 2
            if n == num:
                return True
            elif n < num:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

s=Solution()
print(s.isPerfectSquare(14))
