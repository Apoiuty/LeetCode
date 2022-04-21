from typing import List
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def _generate(start, end):
            # 如果start>=end说明不需要生成
            if start == end:
                return [TreeNode(start)]
            elif start > end:
                return [None]

            result = []
            for i in range(start, end + 1):
                left = _generate(start, i - 1)
                right = _generate(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        result.append(root)
            return result

        return _generate(1, n)


s = Solution()
trees = s.generateTrees(3)
pass
