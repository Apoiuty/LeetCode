# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or not root.right and not root.left:
            return

        cur = root

        while cur:
            if cur.left:
                if not cur.right:
                    cur.right = cur.left
                    cur.left = None
                    cur = cur.right
                else:
                    pre = cur.left
                    while pre.right:
                        pre = pre.right
                    pre.right = cur.right
                    cur.right = None
            else:
                cur = cur.right


