from typing import *


# 2022-04-14 15:11:52

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        pre = None
        cnt = 1
        tmp = head
        left_ptr = None
        last = None
        while cnt <= right:
            if cnt >= left:
                if not left_ptr:
                    left_ptr = tmp
                if not last:
                    last = tmp
                    tmp = tmp.next
                else:
                    _ = tmp.next
                    tmp.next = last
                    last = tmp
                    tmp = _
                cnt += 1
            else:
                cnt += 1
                pre = tmp
                tmp = tmp.next

        if pre:
            pre.next = last
        left_ptr.next = tmp
        if pre:
            return head
        else:
            return last

        # leetcode submit region end(Prohibit modification and deletion)


l = ListNode(3, ListNode(5))
s = Solution()
print(s.reverseBetween(l, 1, 2))
pass
