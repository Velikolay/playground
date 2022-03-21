from collections import deque


def bfsShortestPath(vertex, node_idx, ids, val):
    found_shortest = 0
    path_len = [0] * len(vertex)
    visited = [False] * len(vertex)
    q = deque()
    q.appendleft(node_idx)

    while len(q) > 0 and not found_shortest:
        node = q.pop()
        visited[node] = True
        distance_to_node = path_len[node]
        for nnode in vertex[node]:
            if not visited[nnode]:
                q.appendleft(nnode)
                path_len[nnode] = distance_to_node + 1

                if val == ids[nnode]:
                    found_shortest = nnode
                    break

    return path_len[nnode]


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    ids.insert(0, 0)
    vertex = [[] for _ in range(graph_nodes + 1)]
    for f, t in zip(graph_from, graph_to):
        vertex[f].append(t)
        vertex[t].append(f)
    print(vertex)
    print(ids)
    print(val)

    val_list = list(filter(lambda i_x: i_x[1] == val, enumerate(ids)))
    print(val_list)
    if len(val_list) > 1:
        return min(map(lambda i_x: bfsShortestPath(vertex, i_x[0], ids, val), val_list))
    else:
        return -1


if __name__ == "__main__":
    print(findShortest(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2))
