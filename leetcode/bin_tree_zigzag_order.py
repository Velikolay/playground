from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        ltor = True
        queue_curr, queue_next = [], []
        queue_curr.append(root)
        while queue_curr:
            level = []
            ltor = not ltor
            while queue_curr:
                node = queue_curr.pop()
                if node:
                    level.append(node.val)
                    if ltor:
                        queue_next.append(node.right)
                        queue_next.append(node.left)
                    else:
                        queue_next.append(node.left)
                        queue_next.append(node.right)

            if level:
                res.append(level)
            queue_curr, queue_next = queue_next, queue_curr
        return res
