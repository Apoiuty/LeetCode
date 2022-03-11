# Definition for a Node.
from binary import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        tmp = root
        begin = None
        end = None
        while tmp:
            if tmp.left:
                next_node = tmp.left
                pre_node = tmp.left
                while pre_node.right:
                    pre_node = pre_node.right
                pre_node.right = tmp
                tmp.left = None
                tmp = next_node
                continue
            else:
                if not begin:
                    begin = tmp
                if not tmp.right:
                    end = tmp
                tmp = tmp.right

        tmp = begin
        while tmp != end:
            tmp.right.left = tmp
            tmp = tmp.right
        end.right = begin
        begin.left = end
        return begin


s = Solution()
tree = build_tree([4, 2, 5, 1, 3, null, null])
tree = s.treeToDoublyList(tree)
pass