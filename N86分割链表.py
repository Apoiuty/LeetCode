from LeetCode.N148排序链表 import ListNode


def partition(self, head: ListNode, x: int) -> ListNode:
    v = x
    lo = lo_i = ListNode()
    hi = hi_i = ListNode()
    # 从头开始遍历
    i = head
    while i:
        if i.val < v:
            lo_i.next = i
            lo_i = i
        elif i.val >= v:
            hi_i.next = i
            hi_i = i
        i = i.next

    hi_i.next = None
    if lo.next:
        lo_i.next = hi.next

    head = lo.next

    return head

