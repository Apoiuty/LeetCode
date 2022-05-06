from leetcode import *


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack1 = []
        stack2 = []
        while stack1 or stack2 or p or q:
            if p and q and not p.val == q.val:
                return False
            elif p and not q:
                return False
            elif q and not p:
                return False

            if p:
                stack1.append(p)
                p = p.left
            else:
                p = stack1.pop().right
            if q:
                stack2.append(q)
                q = q.left
            else:
                q = stack1.pop().right

        return True
