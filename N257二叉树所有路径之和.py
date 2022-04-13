from typing import Optional, List

from binary import *


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return ['']

        if not (root.left or root.right):
            return [str(root.val)]

        visited = set()
        stack = []
        ans = []
        path = []
        while root or stack:
            if root:
                stack.append(root)
                path.append(str(root.val))
                root = root.left
            else:
                if stack[-1] not in visited:
                    visited.add(stack[-1])
                    root = stack[-1].right
                else:
                    root = stack.pop()
                    if not (root.left or root.right):
                        ans.append(path[:])
                    path.pop()
                    root = None
        return ['->'.join(item) for item in ans]


tree = build_tree([1, 2, 3, null, 5])
s = Solution()
print(s.binaryTreePaths(tree))
