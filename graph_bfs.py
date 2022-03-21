from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.factor = 6
        self.vertices = [[] for _ in range(n)]

    def connect(self, v1, v2):
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)

    def find_all_distances(self, v):
        distances = [-1] * self.n
        distances[v] = 0
        visited = [False] * self.n
        visited[v] = True
        q = deque([v])
        while len(q) > 0:
            node = q.pop()
            distance_to_node = distances[node]

            for nnode in self.vertices[node]:
                if not visited[nnode]:
                    q.appendleft(nnode)
                    visited[nnode] = True
                    distances[nnode] = distance_to_node + self.factor

        del distances[v]
        print(" ".join(map(str, distances)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
