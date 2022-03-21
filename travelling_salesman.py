from sys import maxsize
from itertools import permutations

# Permutations O(n!)
# Combinations O(n choose k) => O(min(n^k, n^(n-k)))
V = 4

# Floyd-Warshall O(n^3) - shortest path all pair of nodes
# Dijkstra O(E*VLogV) - shortest path single source
# Bellman-Ford - shortest path single source - negative weights
# A* - single pair with a heuristic


# implementation of traveling Salesman Problem
# Shortest Hamiltonian Cycle
# Brute Force O(V^3 + V*V!)
def travelling_salesman(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for perm in next_permutation:

        # store current Path weight(cost)
        curr_path = 0

        # compute current path weight
        k = s
        for v in perm:
            curr_path += graph[k][v]
            k = v
        curr_path += graph[k][s]

        # update minimum
        min_path = min(min_path, curr_path)

    return min_path


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travelling_salesman(graph, s))
