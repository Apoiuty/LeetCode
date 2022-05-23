from leetcode import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        q = deque()
        q.extend([root, None])
        result = []
        while q:
            last = root
            root = q.popleft()
            if root:
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            else:
                result.append(last.val)
                if q:
                    q.append(None)

        return result
