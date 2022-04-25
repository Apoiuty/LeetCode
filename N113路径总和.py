from leetcode import *


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        visited = set()
        path = []
        stack = []
        result = []
        while root or stack:
            if root:
                path.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root not in visited:
                    visited.add(root)
                    if not root.left and not root.right and sum(path) == targetSum:
                        result.append(path[:])
                    root = root.right
                else:
                    stack.pop()
                    path.pop()
                    root=None

        return result
