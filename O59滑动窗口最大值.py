from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        candidates = deque(maxlen=k)
        result = []
        cnt = k
        for index, i in enumerate(nums):
            while candidates and -candidates[0] + index >= k:
                candidates.popleft()
            if not candidates:
                candidates.append(index)
            else:
                while candidates and nums[candidates[-1]] <= i:
                    candidates.pop()
                candidates.append(index)
            if cnt:
                cnt -= 1
            if not cnt:
                result.append(nums[candidates[0]])

        return result


s = Solution()
print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
