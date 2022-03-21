from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]], i: int = 0, j: int = 0) -> List[List[List[str]]]:
        if j > 8:
            self.print_sudoku(board)
            return

        if board[i][j] != ".":
            ni, nj = self.next_index(i, j)
            self.solveSudoku(board, ni, nj)
            return

        values = self.value_opts(board, i, j)

        for value in values:
            board[i][j] = value
            ni, nj = self.next_index(i, j)
            self.solveSudoku(board, ni, nj)
        board[i][j] = "."

    def next_index(self, i: int, j: int) -> Tuple[int, int]:
        return (0, j + 1) if i == 8 else (i + 1, j)

    def value_opts(self, board: List[List[str]], i: int, j: int) -> List[int]:
        opts = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for col in range(9):
            if board[i][col] in opts:
                opts.remove(board[i][col])
        for row in range(9):
            if board[row][j] in opts:
                opts.remove(board[row][j])
        for row in range((i // 3) * 3, (i // 3 + 1) * 3):
            for col in range((j // 3) * 3, (j // 3 + 1) * 3):
                if board[row][col] in opts:
                    opts.remove(board[row][col])
        return list(opts)

    def print_sudoku(self, board: List[List[str]]):
        for row in board:
            print("  ".join(row))


if __name__ == "__main__":
    # sudoku = [
    #     ["5","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]
    # ]
    sudoku = [
        [".",".",".","1",".",".",".",".","."],
        ["7",".",".",".",".",".",".","6","9"],
        [".",".","2",".","3","6","5",".","."],
        ["6","4",".",".",".","5",".",".","."],
        ["9",".",".",".",".",".",".",".","7"],
        [".",".",".","4",".",".",".","2","8"],
        [".",".","4","5","2",".","3",".","."],
        ["2","7",".",".",".",".",".",".","6"],
        [".",".",".",".",".","4",".",".","."]
    ]
    Solution().solveSudoku(sudoku)
