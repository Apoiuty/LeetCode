from typing import *


# 2022-04-14 11:32:30

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        Head = None
        tmp = Head
        while head:
            if head.next and head.next.val == head.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
            else:
                if not Head:
                    tmp = Head = head
                else:
                    tmp.next = head
                    tmp = head
                head = head.next
        if tmp:
            tmp.next = None

        return Head

    # leetcode submit region end(Prohibit modification and deletion)


s = Solution()
a = ListNode(1, ListNode(2, ListNode(2)))
print(s.deleteDuplicates(a))
