from binary import *


class Solution:
    def rob(self, root: TreeNode) -> int:

        dp = {}

        def my_rob(root):
            if not root:
                return 0
            elif root in dp:
                return dp[root]

            with_root = root.val
            if root.left:
                with_root += my_rob(root.left.left) + my_rob(root.left.right)
            if root.right:
                with_root += my_rob(root.right.left) + my_rob(root.right.right)

            without_root = my_rob(root.left) + my_rob(root.right)

            dp[root] = max(without_root, with_root)
            return max(with_root, without_root)

        return my_rob(root)


root = build_tree([3, 4, 5, 1, 3, null, 1])
s = Solution()
print(s.rob(root))
