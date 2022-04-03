class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = odd_head = head
        even = even_head = head.next
        while odd_head.next or even_head.next:
            if odd_head.next:
                odd_head.next = odd_head.next.next
                odd_head = odd_head.next
            if even_head.next:
                even_head.next = even_head.next.next
                even_head = even_head.next
        odd_head.next = even

        return odd

