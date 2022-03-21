from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lsum = None
        prev = None
        carry_over = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            l1_l2_sum = l1_val + l2_val + carry_over
            print(l1_l2_sum)
            node_val = l1_l2_sum % 10
            print(node_val)
            carry_over = l1_l2_sum // 10
            print(carry_over)
            print()
            curr = ListNode(node_val)

            if not lsum:
                lsum = curr

            if prev:
                prev.next = curr

            prev = curr

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry_over > 0:
            prev.next = ListNode(carry_over)

        return lsum


if __name__ == '__main__':
    l1_3 = ListNode(3)
    l1_2 = ListNode(4, l1_3)
    l1_1 = ListNode(2, l1_2)

    l2_3 = ListNode(4)
    l2_2 = ListNode(6, l2_3)
    l2_1 = ListNode(5, l2_2)

    print(Solution().addTwoNumbers(l1_1, l2_1))
