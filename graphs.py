class DisjointSet:
    def __init__(self, vertices, parents):
        self.vertices = vertices
        self.parents = parents

    def find(self, item):
        if self.parents[item] == item:
            return item
        else:
            return self.find(self.parents[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parents[root1] = root2


def disjoin_sets(n, cities):
    vertices = [city_id for city_id in range(n + 1)]
    parents = [city_id for city_id in range(n + 1)]
    ds = DisjointSet(vertices, parents)
    for route in cities:
        ds.union(route[0], route[1])
    return ds.parents


def roads_and_libraries_ds(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return c_lib * n
    else:
        parent = disjoin_sets(n, cities)
        num_sets = len([i for i in range(1, len(parent)) if i == parent[i]])
        return num_sets * c_lib + (n - num_sets) * c_road


def dfs(city_map):
    node_sets = []
    for city_id in city_map.keys():
        if not list(filter(lambda x: city_id in x, node_sets)):
            visited = set([city_id])
            stack = [city_id]
            while stack:
                top = stack[-1]
                if top not in visited:
                    visited.add(top)

                remove_from_stack = True
                for neighbour in city_map[top]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        remove_from_stack = False
                        break

                if remove_from_stack:
                    stack.pop()
            node_sets.append(visited)
    return node_sets


def roads_and_libraries_dfs(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return c_lib * n
    else:
        city_map = {}
        for route in cities:
            if route[0] not in city_map:
                city_map[route[0]] = []
            city_map[route[0]].append(route[1])

            if route[1] not in city_map:
                city_map[route[1]] = []
            city_map[route[1]].append(route[0])

        disjoin_sets(n, cities)
        node_sets = dfs(city_map)
        # print(node_sets)
        return sum(map(lambda x: (len(x) - 1) * c_road + c_lib, node_sets)) + (n - sum(map(lambda x: len(x), node_sets))) * c_lib


if __name__ == "__main__":
    # print(roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]]))
    print(roads_and_libraries_dfs(5, 92, 23, [[2, 1], [5, 3], [5, 1], [3, 4], [3, 1], [5, 4], [4, 1], [5, 2], [4, 2]]))
    print(roads_and_libraries_ds(5, 92, 23, [[2, 1], [5, 3], [5, 1], [3, 4], [3, 1], [5, 4], [4, 1], [5, 2], [4, 2]]))
