# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        queue = deque()
        queue.append(root)
        queue.append(None)
        while queue and not (len(queue) == 1 and queue[0] == None):
            tmp = queue.popleft()
            if tmp != None:
                tmp.next = queue[0]
                queue.append(tmp.left)
                queue.append(tmp.right)
            else:
                queue.append(None)

        return root
