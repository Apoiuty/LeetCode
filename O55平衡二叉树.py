from binary import *


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_balanced(root, depth):
            if not root:
                return depth

            depth += 1
            left_depth = is_balanced(root.left, depth)
            right_depth = is_balanced(root.right, depth)
            if left_depth != False and right_depth != False and abs(left_depth - right_depth) <= 1:
                return max(left_depth, right_depth)
            else:
                return False

        if is_balanced(root, 0):
            return True
        else:
            return False


tree = [1, 2, null, 3, null, 4, null, 5, null]
s = Solution()
print(s.isBalanced(build_tree(tree)))
