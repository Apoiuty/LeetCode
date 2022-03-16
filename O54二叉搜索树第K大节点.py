class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                k -= 1
                if not k:
                    return root.val
                else:
                    root = root.left
