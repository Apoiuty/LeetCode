from leetcode import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        order_list = []
        ptr = head
        while ptr:
            order_list.append(ptr)
            ptr = ptr.next

        reverse_list = reversed(order_list)

        for head, tail in zip(order_list, reverse_list):
            if head.next == tail or head == tail:
                tail.next = None
                break
            tail.next = head.next
            head.next = tail
