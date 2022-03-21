from typing import Optional, Any


class Node:
    def __init__(self, key: str, val, right= None, left=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class OrderedDict:
    def __init__(self):
        self.start = None
        self.end = None
        self.node_dict = {}

    def __len__(self) -> int:
        return len(self.node_dict)

    def __contains__(self, key: str) -> bool:
        return key in self.node_dict

    def __getitem__(self, key: str) -> int:
        return self.node_dict[key].val

    def __setitem__(self, key: str, val) -> None:
        if key in self.node_dict:
            self.node_dict[key].val = val
        else:
            self.prepend(key, val)

    def prepend(self, key: str, val: Any) -> None:
        node = Node(key, val, right=self.start)

        if len(self.node_dict) > 0:
            self.start.left = node
            self.start = node
        else:
            self.start = node
            self.end = node

        self.node_dict[key] = node

    def pop(self) -> Optional[Node]:
        if len(self.node_dict) == 0:
            return None

        del self.node_dict[self.end.key]
        popped = self.end

        if len(self.node_dict) == 0:
            self.start = None
            self.end = None
        else:
            self.end = self.end.left
            self.end.right = None

        return popped

    def move_to_front(self, key: str) -> Node:
        if key not in self.node_dict:
            raise Exception("Key not found")

        node = self.node_dict[key]

        if node == self.start:
            pass
        elif node == self.end:
            self.pop()
            self.prepend(node.key, node.val)
        else:
            node.left.right, node.right.left = node.right, node.left
            self.prepend(node.key, node.val)

        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_front(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.lru.move_to_front(key)
            return

        if len(self.lru) >= self.capacity:
            self.lru.pop()

        self.lru[key] = value


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    print(lRUCache.get(1))
    print(lRUCache.get(2))
