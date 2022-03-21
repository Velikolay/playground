import math
from heapq import heappush, heappop


def shortestReach(n, edges, s):
    visited = [False for _ in range(n + 1)]
    shortest_dist = [math.inf for _ in range(n + 1)]
    verts = [[] for _ in range(n + 1)]
    for edge in edges:
        verts[edge[0]].append([edge[1], edge[2]])
        verts[edge[1]].append([edge[0], edge[2]])

    # curr = s
    shortest_dist[s] = 0
    heap = [(0, s)]
    while len(heap) > 0:
        min_el = heappop(heap)
        curr_shortest = min_el[0]
        curr = min_el[1]
        visited[curr] = True
        # curr_shortest = shortest_dist[curr]
        for edge in verts[curr]:
            node = edge[0]
            cost = edge[1]
            if not visited[node] and shortest_dist[node] > cost + curr_shortest:
                shortest_dist[node] = cost + curr_shortest
                heappush(heap, (cost + curr_shortest, node))

        # curr_min = math.inf
        # for node in range(1, len(shortest_dist)):
        #     if not visited[node] and shortest_dist[node] < curr_min:
        #         curr_min = shortest_dist[node]
        #         curr = node
        # n -= 1
    del shortest_dist[s]
    del shortest_dist[0]
    shortest_dist = map(lambda x: -1 if x == math.inf else x, shortest_dist)
    return shortest_dist
