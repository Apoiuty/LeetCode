# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 只有一个元素或没有元素直接返回
        if not head:
            return None
        if not head.next:
            return head

        #       分割链表
        cnt = 0
        i = head
        while i:
            cnt += 1
            i = i.next

        pivot = random.randint(0, cnt)
        i = head
        while pivot:
            i = i.next
            pivot -= 1

        v = i.val
        lo = lo_i = ListNode()
        hi = hi_i = ListNode()
        e = ei = ListNode()
        # 从头开始遍历
        i = head
        while i:
            if i.val < v:
                lo_i.next = i
                lo_i = i
            elif i.val > v:
                hi_i.next = i
                hi_i = i
            else:
                ei.next = i
                ei = i
            i = i.next

        hi_i.next = None
        lo_i.next = None
        ei.next = None

        lo = self.sortList(lo.next)
        hi = self.sortList(hi.next)

        # 拼接
        if lo:
            lo_i = lo
            while lo_i.next:
                lo_i = lo_i.next
            lo_i.next = e.next
        else:
            lo = e.next

        ei.next = hi
        head = lo

        return head


def print_ListNode(head):
    while head:
        print(head.val, end=',')
        head = head.next
    print()


import random

head = ListNode(val=random.randint(0, 100))
for i in range(9):
    node = ListNode(val=random.randint(0, 100))
    node.next = head
    head = node

# while head:
#     print(head.val, end=',')
#     head = head.next

s = Solution()
head = s.sortList(head)
print_ListNode(head)
