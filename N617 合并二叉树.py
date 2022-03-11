class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        from collections import deque
        tmp1 = root1
        tmp2 = root2
        stack1 = []
        stack2 = []
        while tmp1 or stack1 or tmp2 or stack2:
            if root1:
                if root2:
                    root1.val += root2.val
