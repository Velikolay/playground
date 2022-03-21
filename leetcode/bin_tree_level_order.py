from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue_curr, queue_next = deque(), deque()
        queue_curr.appendleft(root)
        while queue_curr:
            level = []
            while queue_curr:
                node = queue_curr.pop()
                if node:
                    level.append(node.val)
                    queue_next.appendleft(node.left)
                    queue_next.appendleft(node.right)
            if level:
                res.append(level)
            queue_curr, queue_next = queue_next, queue_curr
        return res