from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next

        el = None
        for i in range(n - 1):
            el = stack.pop()

        stack.pop()
        if stack:
            stack.pop().next = el
        else:
            return el

        return head
