from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cnt = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1
        k %= cnt
        if not head or not head.next or k == 0:
            return head
        # 多个节点
        tmp = head
        pre = None
        while tmp or k:
            if k == 0 and not pre:
                pre = head
                if tmp == head:
                    return head
            elif k == 0 and pre:
                if tmp.next:
                    pre = pre.next
                    tmp = tmp.next
                else:
                    break
            else:
                tmp = tmp.next if tmp.next else head
                k -= 1

        result = pre.next
        pre.next = None
        tmp.next = head
        return result
