from typing import List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        border = set()
        nstart, mstart, nend, mend = 0, 0, n - 1, m - 1

        while nstart <= nend and mstart <= mend:
            ninc, minc = 0, 1
            row, col = nstart, mstart

            while nstart <= row <= nend and mstart <= col <= mend:
                if board[row][col] == "O" and (self.is_border(row, col, n, m) or self.is_border_region(row, col, border)):
                    border.add((row, col))
                else:
                    board[row][col] = "X"

                if row == nstart and col == mend:
                    ninc, minc = 1, 0
                if row == nend and col == mend:
                    ninc, minc = 0, -1
                if row == nend and col == mstart:
                    ninc, minc = -1, 0

                row += ninc
                col += minc

            nstart += 1
            mstart += 1
            nend -= 1
            mend -= 1

    def is_border(self, row, col, n, m) -> bool:
        return row == 0 or row == n - 1 or col == 0 or col == m - 1

    def is_border_region(self, row, col, border) -> bool:
        return (row + 1, col) in border or (row - 1, col) in border or (row, col + 1) in border or (row, col - 1) in border


def iter_border(board: List[List[str]]) -> List[Tuple[int, int]]:
    row, col = 0, 0
    num_rows = len(board)
    num_cols = len(board[0])
    border_loop = [
        (0, 1, num_cols - 1),
        (1, 0, num_rows - 1),
        (0, -1, num_cols - 1),
        (-1, 0, num_rows - 1),
    ]

    nodes = []
    for border in border_loop:
        for _ in range(border[2]):
            nodes.append(board[row][col])
            row += border[0]
            col += border[1]

    return nodes


if __name__ == "__main__":
    # board = [
    #     ["X", "X", "X", "X"],
    #     ["X", "O", "O", "X"],
    #     ["X", "X", "O", "X"],
    #     ["X", "O", "X", "X"]
    # ]
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    print(iter_border(board))
    Solution().solve(board)
    print(board)
