from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricST(root.left, root.right)

    def isSymmetricST(self, root_left: Optional[TreeNode], root_right: Optional[TreeNode]) -> bool:
        if root_left is None and root_right is None:
            return True

        return root_left and root_right and root_left.val == root_right.val and self.isSymmetricST(root_left.left, root_right.right) and self.isSymmetricST(root_left.right, root_right.left)
