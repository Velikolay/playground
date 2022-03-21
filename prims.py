from heapq import heappop, heappush, heapify


def prims(n, edges, start):
    verts = [[] for _ in range(n + 1)]
    for edge in edges:
        verts[edge[0]].append((edge[2], edge[1]))
        verts[edge[1]].append((edge[2], edge[0]))

    visited = set([start])
    heap = [x for x in verts[start]]
    heapify(heap)
    res = 0
    while len(heap) > 0 and len(visited) < n:
        el = heappop(heap)
        cost = el[0]
        edge = el[1]
        if edge not in visited:
            visited.add(edge)
            res += cost
            for node in verts[edge]:
                if node[1] not in visited:
                    heappush(heap, node)
    return res
