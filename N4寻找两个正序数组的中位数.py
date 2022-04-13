import bisect
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def get_kth_num(k, n1_s=None, n2_s=None):
            if n1_s is None:
                return nums2[n2_s + k - 1]
            if n2_s is None:
                return nums1[n1_s + k - 1]

            if k == 1:
                return min(nums1[n1_s], nums2[n2_s])

            i1 = min(k // 2 - 1 + n1_s, m - 1)
            i2 = min(k // 2 - 1 + n2_s, n - 1)

            if nums1[i1] <= nums2[i2]:
                k -= i1 - n1_s + 1
                n1_s = i1 + 1
            else:
                k -= i2 - n2_s + 1
                n2_s = i2 + 1
            # 下一个索引出界
            if n1_s >= m:
                return get_kth_num(k, n2_s=n2_s)
            if n2_s >= n:
                return get_kth_num(k, n1_s=n1_s)
            else:
                return get_kth_num(k, n1_s, n2_s)

        if not nums1:
            if n % 2:
                return nums2[n // 2]
            else:
                return .5 * (nums2[n // 2] + nums2[n // 2 - 1])

        if not nums2:
            if m % 2:
                return nums1[m // 2]
            else:
                return .5 * (nums1[m // 2] + nums1[m // 2 - 1])

        if (m + n) % 2 == 0:
            return .5 * (get_kth_num((m + n) // 2, 0, 0) + get_kth_num((m + n) // 2 + 1, 0, 0))
        else:
            return get_kth_num((m + n) // 2 + 1, 0, 0)


nums1 = [4]
nums2 = [1, ]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
