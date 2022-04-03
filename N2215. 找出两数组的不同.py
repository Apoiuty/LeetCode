from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]

s=Solution()
print(s.findDifference( [1,2,3,3],[1,1,2,2]))
