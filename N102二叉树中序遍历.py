from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append((1, root))
        result = []
        while q:
            item = q.popleft()
            level = item[0]
            head = item[1]
            if head:
                level += 1
                q.append((level, head.left))
                q.append((level, head.right))
                result.append([level - 1, head.val])

        from itertools import groupby
        level_travel = []
        for level, val in groupby(result, key=lambda x: x[0]):
            level_travel.append(list(x[1] for x in val))

        return level_travel
