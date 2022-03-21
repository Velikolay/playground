from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)

    def validate(self, root: Optional[TreeNode], min_val: Optional[int], max_val: Optional[int]) -> bool:
        if not root:
            return True
        if min_val is not None and root.val <= min_val or max_val is not None and root.val >= max_val:
            return False
        return self.validate(root.right, root.val, max_val) and self.validate(
            root.left, min_val, root.val)


if __name__ == '__main__':
    root = TreeNode(0)
    print(Solution().isValidBST(root))
