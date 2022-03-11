from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        queue = deque()
        queue.extend([root, '\n'])
        result = []
        level = []
        while queue:
            p = queue.popleft()
            if p == '\n':
                result.append(level)
                level = []
            elif isinstance(p, TreeNode):
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                if p.left:
                    level.append(p.left.val)
                if p.right:
                    level.append(p.right.val)
                if queue and queue[0] == '\n':
                    queue.append('\n')

        return result
