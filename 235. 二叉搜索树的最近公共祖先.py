from leetcode import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if p.val < root.val and q.val < root.val:
                return dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right, p, q)
            elif p.val < root.val < q.val:
                return root
            else:
                return root

        if p.val < q.val:
            return dfs(root, p, q)
        else:
            return dfs(root, q, p)
