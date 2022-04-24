from typing import List
from collections import deque

from binary import *


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        q.append(None)
        result = []
        level = []
        while q:
            item = q.popleft()
            if item:
                level.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                result.append(level)
                level = []
                if q:
                    q.append(None)

        result.reverse()
        return result
