from binary import *


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            if root2:
                return root2
            else:
                return None
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


tree = build_tree([1, 3, 2, 5])
tree1 = build_tree([2, 1, 3, null, 4, null, 7])
s = Solution()
tree = s.mergeTrees(tree, tree1)
pass
