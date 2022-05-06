from leetcode import *


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        next_item = head.next
        next_pre = head
        while next_item:
            insert_ptr = head
            pre = None
            while insert_ptr.val <= next_item.val and insert_ptr != next_item:
                pre = insert_ptr
                insert_ptr = insert_ptr.next

            if insert_ptr == next_item:
                next_pre = next_item
                next_item = next_item.next
            else:
                if pre is None:
                    # 第一个元素
                    next_pre.next = next_item.next
                    next_item.next = head
                    head = next_item
                    next_item = next_pre.next
                else:
                    # 不是第一个元素
                    next_pre.next = next_item.next
                    next_item.next = insert_ptr
                    pre.next = next_item
                    next_item = next_pre.next

        return head
