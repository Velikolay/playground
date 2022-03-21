from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        left_head, left_tail = head, head
        while curr:
            # print(curr.val)
            # print(curr.next.val if curr.next else None)
            left_curr = left_head
            left_prev = None
            while left_curr.val < curr.val:
                left_prev = left_curr
                left_curr = left_curr.next

            if left_curr != curr:
                if left_prev:
                    left_prev.next = curr
                else:
                    left_head = curr
                curr_next = curr.next
                curr.next = left_curr
                left_tail.next = curr_next
                curr = curr_next
            else:
                left_tail = curr
                curr = curr.next
        return left_head


if __name__ == '__main__':
    # l4 = ListNode(4)
    # l3 = ListNode(2, l4)
    # l2 = ListNode(1, l3)
    # l1 = ListNode(3, l2)

    l4 = ListNode(3)
    l3 = ListNode(1, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(4, l2)

    head = Solution().insertionSortList(l1)
    while head:
        print(head.val)
        head = head.next
