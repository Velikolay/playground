from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeRec(preorder, inorder, 0, len(preorder) - 1)

    #         if len(preorder) == 0:
    #             return None

    #         subroot = TreeNode(preorder[0])

    #         idx = inorder.index(subroot.val)
    #         inleft = inorder[:idx]
    #         inright = inorder[idx+1:]

    #         left_node = self.buildTree(preorder[1: len(inleft) + 1], inleft)
    #         right_node = self.buildTree(preorder[len(inleft) + 1:], inright)
    #         subroot.left = left_node
    #         subroot.right = right_node
    #         return subroot

    def buildTreeRec(self, preorder: List[int], inorder: List[int], start: int,
                     end: int) -> Optional[TreeNode]:
        if start > end:
            return None

        subroot = TreeNode(preorder[start])

        idx = inorder.index(subroot.val)
        inleft = inorder[:idx]
        inright = inorder[idx + 1:]

        left_node = self.buildTreeRec(preorder, inleft, start + 1, start + len(inleft))
        right_node = self.buildTreeRec(preorder, inright, start + len(inleft) + 1, end)
        subroot.left = left_node
        subroot.right = right_node
        return subroot


if __name__ == '__main__':
    tree = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(tree)
