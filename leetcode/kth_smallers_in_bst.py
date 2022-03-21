from typing import Tuple, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.kthSmallestRec(root, k)[1]
        return self.kthSmallestInOrder(root, k)

    def kthSmallestInOrder(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        arr, stack = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]
            stack.pop()
            arr.append(curr)
            if len(arr) == k:
                return curr.val

            curr = curr.right

    def kthSmallestRec(self, root: Optional[TreeNode], k: int) -> Tuple[int, int]:
        if not root:
            return 0, 0

        left, left_val = self.kthSmallestRec(root.left, k)
        if left == k:
            return left, left_val

        if left + 1 == k:
            return k, root.val

        right, right_val = self.kthSmallestRec(root.right, k - left - 1)
        return left + right + 1, right_val


if __name__ == "__main__":
    tn2 = TreeNode(2)
    root = TreeNode(1, right=tn2)
    print(Solution().kthSmallest(root, 2))
