from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class CodecV2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        arr = []
        curr = [root]
        while curr:
            nxt = []
            for node in curr:
                if node:
                    arr.append(str(node.val))
                    nxt.append(node.left)
                    nxt.append(node.right)
                else:
                    arr.append("null")
            curr = nxt
        return " ".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(" ")

        root = TreeNode(arr[0])
        curr = [root]
        idx = 1
        while curr:
            nxt = []
            for node in curr:
                if arr[idx] != "null":
                    node.left = TreeNode(int(arr[idx]))
                    nxt.append(node.left)

                if arr[idx+1] != "null":
                    node.right = TreeNode(int(arr[idx+1]))
                    nxt.append(node.right)
                idx += 2
            curr = nxt
        return root


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        arr = []
        deq = deque()
        deq.appendleft((root, 0))
        while deq:
            node, level = deq.pop()
            # if node:
            if not (level < len(arr)):
                arr.append([])
            if node:
                arr[level].append(node.val)
                deq.appendleft((node.left, level + 1))
                deq.appendleft((node.right, level + 1))
            else:
                arr[level].append(None)
        return ";".join(",".join(str(val) for val in level) for level in arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # if not data:
        #     return None

        arr = [level.split(",") for level in data.split(";")]
        root = TreeNode(arr[0][0]) if arr[0][0] != "None" else None
        deq = deque()
        deq.appendleft((root, 0))
        while deq:
            node, level = deq.pop()
            if node and level + 1 < len(arr):
                right_val = arr[level + 1].pop()
                left_val = arr[level + 1].pop()
                if left_val != "None":
                    node.left = TreeNode(left_val)
                    deq.append((node.left, level + 1))
                if right_val != "None":
                    node.right = TreeNode(right_val)
                    deq.append((node.right, level + 1))
        return root


if __name__ == '__main__':
    # root = None
    rl2 = TreeNode(4)
    rr2 = TreeNode(5)
    l1 = TreeNode(2)
    r1 = TreeNode(3, rl2, rr2)
    root = TreeNode(1, l1, r1)
    codec = CodecV2()
    data = codec.serialize(root)
    root = codec.deserialize(data)
    print(root)
