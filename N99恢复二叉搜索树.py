from typing import Optional
import bisect
from binary import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        mp = {}
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                mp[root.val] = root
                root = root.right

        values = list(mp.keys())
        left = None
        left_index = None
        right = None
        for i in range(1, len(values)):
            if values[i] < values[i - 1]:
                if left is None:
                    left = values[i - 1]
                    left_index = i - 1
                elif right is None:
                    right = values[i]

        if right is None:
            right = values[left_index + 1]
            mp[left].val, mp[right].val = mp[right].val, mp[left].val
        else:
            mp[left].val, mp[right].val = mp[right].val, mp[left].val


tree = [3, 1, 4, null, null, 2]
root = build_tree(tree)
s = Solution()
s.recoverTree(root)
