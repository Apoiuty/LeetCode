from LeetCode.leetcode import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(head, cur_depth):
            if not head:
                return cur_depth

            left_depth = depth(head.left, cur_depth + 1)
            right_depth = depth(head.right, cur_depth + 1)
            return max(left_depth, right_depth)

        if not root:
            return 0
        return max(depth(root.left, 0) + depth(root.right, 0), self.diameterOfBinaryTree(root.right),
                   self.diameterOfBinaryTree(root.left))


s = Solution()
tree = [1, 2, 3, 4, 5, None, None]
print(s.diameterOfBinaryTree(build_tree(tree)))
