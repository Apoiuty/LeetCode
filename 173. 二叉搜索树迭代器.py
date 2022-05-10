from leetcode import *


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                self.root = self.stack.pop()
                root = self.root
                self.root = root.right
                return root.val

    def hasNext(self) -> bool:
        return bool(self.root or self.stack)
