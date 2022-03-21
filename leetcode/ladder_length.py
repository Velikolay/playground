from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}

        def connected(w1: str, w2: str) -> bool:
            diffs = 0
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    diffs += 1
            return diffs == 1

        def insert_edge(v1, v2):
            vs = graph.get(v1, [])
            vs.append(v2)
            graph[v1] = vs

        def shortest_path_bfs():
            if beginWord not in graph:
                return 0

            visited = set([beginWord])
            level = 1
            n = graph[beginWord]

            while n:
                level += 1
                nn = []
                for word in n:
                    if word == endWord:
                        return level
                    visited.add(word)
                    nn.extend(nxt for nxt in graph[word] if nxt not in visited)
                n = nn
            return 0

        nodes = list(set([beginWord] + wordList))

        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                if connected(nodes[i], nodes[j]):
                    insert_edge(nodes[i], nodes[j])
                    insert_edge(nodes[j], nodes[i])

        return shortest_path_bfs()


if __name__ == "__main__":
    print(Solution().ladderLength("hot", "dog", ["hot", "dog"]))
