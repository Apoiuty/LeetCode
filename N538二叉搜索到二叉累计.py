from typing import Optional

from binary import *


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cum_sum = 0
        stack = []
        ans = root
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root.val += cum_sum
                cum_sum += root.val
                root = root.left

        return ans


