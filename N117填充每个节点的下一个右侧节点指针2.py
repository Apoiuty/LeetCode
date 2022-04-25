# Definition for a Node.
from collections import *


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque()
        q.extend([root, None])
        level = []

        while q:
            item = q.popleft()
            if item:
                level.append(item)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                for i in range(len(level) - 1):
                    level[i].next = level[i + 1]
                level = []
                if q:
                    q.append(None)

        return root
