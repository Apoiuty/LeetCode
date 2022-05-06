from leetcode import *


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        path_sum = 0
        visited = set()
        while stack or root:
            if root:
                path_sum += root.val
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root not in visited:
                    visited.add(root)
                    root = root.right
                else:
                    if not root.left and not root.right and path_sum == targetSum:
                        return True
                    stack.pop()
                    path_sum -= root.val
                    root = None

        return False
