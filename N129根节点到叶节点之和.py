from leetcode import *


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        result = 0
        cnt_to_leaf = 0
        stack = []
        visited = set()
        while stack or root:
            if root:
                cnt_to_leaf = cnt_to_leaf * 10 + root.val
                stack.append(root)
                root = root.left
            else:
                if stack[-1] not in visited:
                    root = stack[-1].right
                    visited.add(stack[-1])
                else:
                    item = stack.pop()
                    if not (item.right or item.left):
                        result += cnt_to_leaf
                    cnt_to_leaf = (cnt_to_leaf - item.val) // 10

        return result


tree = build_tree([1, 2, 3])
s = Solution()
print(s.sumNumbers(tree))
