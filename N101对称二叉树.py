class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack_left = []
        stack_right = []
        left = right = root
        while (left or stack_left) and (right or stack_right):
            if left and not right or not left and right:
                return False
            if not left and not right:
                left = stack_left.pop().right
                right = stack_right.pop().left
            elif left.val == right.val:
                stack_left.append(left)
                left = left.left
                stack_right.append(right)
                right = right.right
            else:
                return False
        return True
