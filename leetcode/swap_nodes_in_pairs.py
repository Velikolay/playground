from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head if not (head and head.next) else head.next
        prev = None
        curr = head
        while curr:
            curr_next = curr.next

            if curr_next:
                next_curr = curr_next.next
                if prev:
                    prev.next = curr_next

                curr.next = next_curr
                curr_next.next = curr
                prev = curr
                curr = next_curr
            else:
                curr = curr_next
        return new_head
