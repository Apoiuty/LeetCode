from typing import Optional

from leetcode import *


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(v, path):
            """
            path为之前路径的字符串
            v为当前节点
            :param v:
            :param path:
            :return:
            """

            path = chr(97 + v.val) + path
            if v.left and v.right:
                return min(dfs(v.left, path), dfs(v.right, path))
            elif v.left:
                return dfs(v.left, path)
            elif v.right:
                return dfs(v.right, path)
            else:
                return path

        return dfs(root, '')
