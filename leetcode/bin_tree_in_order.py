from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversalInPlace(self, root: Optional[TreeNode], res: List[int]) -> None:
        if root:
            self.inorderTraversalInPlace(root.left, res)
            res.append(root.val)
            self.inorderTraversalInPlace(root.right, res)


if __name__ == '__main__':
    pass
