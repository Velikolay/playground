from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited = set()
                    res |= self.existDFS(board, visited, i, j, word)
        return res

    def existDFS(self, board: List[List[str]], visited: Set[Tuple[int, int]],
                 i: int, j: int, word: str) -> bool:
        if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[i])) or (i, j) in visited:
            return False

        if len(word) == 1 and board[i][j] == word[0]:
            return True

        if board[i][j] == word[0]:
            visited.add((i, j))
            subword = word[1:]
            exist = self.existDFS(board, visited, i + 1, j, subword) or self.existDFS(board, visited, i - 1, j, subword) or self.existDFS(board, visited, i, j + 1, subword) or self.existDFS(board, visited, i, j - 1, subword)
            if not exist:
                visited.remove((i, j))
            return exist

        return False


if __name__ == '__main__':
    print(Solution().exist([
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"],
    ], "ABCESEEEFS"))
