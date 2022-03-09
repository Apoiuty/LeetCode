class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not k:
            return None
        slow_p = None
        fast_p = head
        cnt = k
        while fast_p:
            if not cnt:
                if not slow_p:
                    slow_p = head
                else:
                    slow_p = slow_p.next
            else:
                cnt -= 1
            fast_p = fast_p.next

        return slow_p
