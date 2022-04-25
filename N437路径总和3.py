from leetcode import *


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = dict()
        prefix[0] = 1
        cnt = 0

        def dfs(root, cum_sum):
            nonlocal cnt
            if prefix[targetSum - root.val] == 1:
                cnt += 1

            prefix[cum_sum + root.val] = 1
            for tree in [root.left, root.right]:
                if tree:
                    dfs(tree, cum_sum + root.val)

            prefix[cum_sum + root.val] = 0

        dfs(root, 0)
        # 从根节点开始的路径
        return cnt
