class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and slow_ptr:
            try:
                fast_ptr = fast_ptr.next
                fast_ptr = fast_ptr.next
            except Exception:
                pass

            slow_ptr = slow_ptr.next
            if slow_ptr==fast_ptr:
                return True

        return False
