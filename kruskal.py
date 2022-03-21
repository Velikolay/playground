from heapq import heappop, heapify


class DisjointSet:
    def __init__(self, g_nodes):
        self.parents = [x for x in range(g_nodes + 1)]
        self.roots = set(self.parents[1:])

    def find(self, v):
        if v == self.parents[v]:
            return v
        else:
            return self.find(self.parents[v])

    def union(self, v1, v2):
        v1_root = self.find(v1)
        v2_root = self.find(v2)
        if v1_root != v2_root:
            self.parents[v1_root] = v2_root
            self.roots.remove(v1_root)

    def cycle(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def is_tree(self):
        return len(self.roots) == 1


def kruskals(g_nodes, g_from, g_to, g_weight):
    heap = [(edge[2], (edge[0], edge[1])) for edge in zip(g_from, g_to, g_weight)]
    heapify(heap)
    ds = DisjointSet(g_nodes)
    res = 0
    while len(heap) > 0 and not ds.is_tree():
        el = heappop(heap)
        cost = el[0]
        edge = el[1]
        if not ds.cycle(edge[0], edge[1]):
            ds.union(edge[0], edge[1])
            res += cost

    return res


if __name__ == "__main__":
    print(kruskals(4, [1, 3, 4, 1, 3], [2, 2, 3, 4, 1], [1, 150, 99, 100, 200]))
