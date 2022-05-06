from leetcode import *


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_depth(root):
            if not root:
                return 0

            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)

            return min(left_depth, right_depth) + 1



