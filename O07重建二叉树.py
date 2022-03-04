from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None

    root = preorder[0]
    root_index = inorder.index(root)
    root = TreeNode(root)
    root.left = buildTree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
    return root


tree = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
pass
