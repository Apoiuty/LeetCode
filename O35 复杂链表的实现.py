# Definition for a Node.
from copy import copy


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        tmp = head
        while tmp:
            copy_tmp = copy(tmp)
            copy_tmp.next = tmp.next
            tmp.next = copy_tmp
            tmp = copy_tmp.next
        tmp = head
        while tmp:
            copy_tmp = tmp.next
            if tmp.random:
                copy_tmp.random = tmp.random.next
            tmp = copy_tmp.next
            if tmp:
                copy_tmp.next = copy_tmp.next.next

        return head.next
