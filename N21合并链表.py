# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = head = ListNode()
        while list1 or list2:
            if list1 and not list2:
                p.next = list1
                list1 = list1.next
                p = p.next
            elif list2 and not list1:
                p.next = list2
                list2 = list2.next
                p = p.next
            elif list1.val < list2.val:
                p.next = list1
                list1 = list1.next
                p = p.next
            else:
                p.next = list2
                list2 = list2.next
                p = p.next

        return head.next
