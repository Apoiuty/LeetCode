from typing import Optional

from leetcode import *


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build_tree(values):
            n = len(values)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(val=values[0])

            root_i = n // 2
            root = TreeNode(values[root_i])
            root.left = build_tree(values[:root_i])
            root.right = build_tree(values[root_i + 1:])
            return root

        return build_tree(values)
