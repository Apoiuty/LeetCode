from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 先查找第一个从负到正的

        if nums == []:
            return []
        elif nums[0] >= 0:
            return [i ** 2 for i in nums]
        elif nums[-1] <= 0:
            return [i ** 2 for i in reversed(nums)]

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= 0:
                lo = mid + 1
            elif nums[mid] > 0:
                hi = mid
            else:
                break

        below_zero = nums[:lo]
        great_zero = nums[lo:]
        great_zero.reverse()

        ans = []
        while great_zero or below_zero:
            if great_zero and below_zero:
                if abs(great_zero[-1]) < abs(below_zero[-1]):
                    ans.append(great_zero.pop() ** 2)
                else:
                    ans.append(below_zero.pop() ** 2)
            elif great_zero:
                ans.append(great_zero.pop() ** 2)
            elif below_zero:
                ans.append(below_zero.pop() ** 2)

        return ans


s = Solution()
print(s.sortedSquares([-7, -3, 2, 3, 11]))
