class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        def isSubStructure(a, b):
            if b == None and a != A:
                return True
            elif a and b and a.val == b.val:
                return isSubStructure(a.left, b.left) and isSubStructure(a.right,
                                                                         b.right)
            else:
                return False
        return isSubStructure(A, B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
