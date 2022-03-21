from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        self.rightSideViewRec(root, 0, view)
        return view

    def rightSideViewRec(self, root: Optional[TreeNode], level: int, view: List[int]) -> None:
        if root:
            if level >= len(view):
                view.append(root.val)

            self.rightSideViewRec(root.right, level + 1, view)
            self.rightSideViewRec(root.left, level + 1, view)
