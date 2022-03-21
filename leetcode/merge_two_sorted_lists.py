from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        res_head, res_curr = None, None
        curr, other = list1, list2
        while curr or other:
            if not other or (curr and other and curr.val <= other.val):
                node = curr
            else:
                node = other
                curr, other = other, curr

            if res_head:
                res_curr.next = node
                res_curr = res_curr.next
            else:
                res_head, res_curr = node, node

            curr = curr.next
        return res_head
