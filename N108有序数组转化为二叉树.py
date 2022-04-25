from typing import List, Optional

from leetcode import *


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(val=nums[0])
        elif len(nums) == 2:
            root = TreeNode(val=nums[1])
            root.left = TreeNode(val=nums[0])
            return root
        else:
            mid = len(nums) // 2
            root = TreeNode(val=nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root
s=Solution()
print(s.sortedArrayToBST())