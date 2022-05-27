from typing import Optional
from leetcode import *


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0

        def sum_left(tmp):
            if not tmp:
                return
            nonlocal result
            if tmp.left and not tmp.left.left and not tmp.left.right:
                result += tmp.left.val
            sum_left(tmp.left)
            sum_left(tmp.right)

        sum_left(root)
        return result
