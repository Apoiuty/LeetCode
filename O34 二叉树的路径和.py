from typing import List

from leetcode import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        get_target = []

        def match(root, path, target):
            if not root:
                return
            if not root.left and not root.right:
                if root.val == target:
                    get_target.append(path + [root.val])
                    return
                else:
                    return

            path.append(root.val)
            match(root.left, path, target - root.val)
            match(root.right, path, target - root.val)
            path.pop()

        match(root, [], target)
        return get_target


s = Solution()
print(s.pathSum(build_tree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]), 22))
