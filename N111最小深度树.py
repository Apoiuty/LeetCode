from leetcode import *


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def get_depth(root):
            if not root:
                return 0

            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)

            if not left_depth:
                return right_depth + 1

            if not right_depth:
                return left_depth + 1

            return min(left_depth, right_depth) + 1

        return get_depth(root)
