import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, lst = None, None
        heap = [(lst.val, idx) for idx, lst in enumerate(lists) if lst]
        heapq.heapify(heap)

        while heap:
            val, idx = heapq.heappop(heap)

            node = ListNode(val)
            if not head:
                head, lst = node, node
            else:
                lst.next = node
                lst = node

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))

        #         while lists:
        #             val, idx = min((lst.val, idx) for idx, lst in enumerate(lists))

        #             node = ListNode(val)
        #             if not head:
        #                 head, lst = node, node
        #             else:
        #                 lst.next = node
        #                 lst = node

        #             if lists[idx].next:
        #                 lists[idx] = lists[idx].next
        #             else:
        #                 del lists[idx]

        return head
