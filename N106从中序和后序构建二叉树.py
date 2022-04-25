from typing import List

from leetcode import *


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(val=inorder[0])

        root = postorder[-1]
        left_tree = inorder.index(root)
        root = TreeNode(val=root)
        root.left = self.buildTree(inorder[:left_tree], postorder[:left_tree])
        root.right = self.buildTree(inorder[left_tree + 1:], postorder[left_tree:-1])

        return root

