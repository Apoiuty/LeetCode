class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next == None:
            return True
        tmp = head
        vals = []
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next
        n = len(vals)
        if n % 2:
            return vals[:n // 2] == vals[n // 2:][::-1]
        else:
            return vals[:n // 2] == vals[n // 2 + 1:][::-1]
