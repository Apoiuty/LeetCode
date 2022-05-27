from leetcode import *


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next

        pre = tmp = head
        while tmp:
            if tmp.val == val:
                pre.next = tmp.next
            else:
                pre = tmp
            tmp = tmp.next

        return head
