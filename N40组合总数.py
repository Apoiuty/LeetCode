from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(v, nums, path):
            if v == 0:
                ans.append(path)
            if not nums or nums[0] > v:
                return
            visited = set()
            for i, num in enumerate(nums):
                if num not in visited:
                    dfs(v - num, nums[i + 1:], path + [num])
                    visited.add(num)

        visited = set()
        for i, num in enumerate(candidates):
            if num not in visited:
                dfs(target - num, candidates[i + 1:], [num])
                visited.add(num)
        return ans


s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))
