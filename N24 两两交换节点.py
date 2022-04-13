class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        H = head.next
        p1 = head
        p2 = head.next
        pre = None
        while p2 and p1:
            if pre is not None:
                pre.next = p2

            p1.next = p2.next
            p2.next = p1
            pre = p1
            try:
                p1 = p1.next
                p2 = p1.next
            except:
                break

        return H


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s=Solution()
head=s.swapPairs(head)
pass