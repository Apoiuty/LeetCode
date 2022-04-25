from typing import List

from leetcode import *


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        to_right = True
        from collections import deque
        queue = deque()
        queue.append(root)
        queue.append(None)
        ans = []
        result = []
        next_level = deque()
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                if to_right:
                    if node.left:
                        next_level.appendleft(node.left)
                    if node.right:
                        next_level.appendleft(node.right)
                else:
                    if node.right:
                        next_level.appendleft(node.right)
                    if node.left:
                        next_level.appendleft(node.left)
            else:
                ans.append(result)
                result = []
                if not next_level:
                    break
                else:
                    queue = next_level
                    next_level = deque()
                queue.append(None)
                to_right = not to_right
        return ans


tree = build_tree([3, 9, 20, null, null, 15, 7])
s = Solution()
print(s.zigzagLevelOrder(tree))
