from typing import List


class Solution:
    # TODO: Can be improved to do DFS/BFS from boundary cells only
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        n = len(board)
        m = len(board[0])
        for row in range(n):
            for col in range(m):
                if board[row][col] == "O" and (row, col) not in visited:
                    region = set()
                    region.add((row, col))
                    surrounded = True
                    curr_level = [(row, col)]

                    while curr_level:
                        next_level = []
                        for irow, icol in curr_level:
                            if self.is_border(irow, icol, board):
                                surrounded = False

                            if self.is_in_region(irow + 1, icol, board) and (irow + 1, icol) not in region:
                                region.add((irow + 1, icol))
                                next_level.append((irow + 1, icol))
                            if self.is_in_region(irow - 1, icol, board) and (irow - 1, icol) not in region:
                                region.add((irow - 1, icol))
                                next_level.append((irow - 1, icol))
                            if self.is_in_region(irow, icol + 1, board) and (irow, icol + 1) not in region:
                                region.add((irow, icol + 1))
                                next_level.append((irow, icol + 1))
                            if self.is_in_region(irow, icol - 1, board) and (irow, icol - 1) not in region:
                                region.add((irow, icol - 1))
                                next_level.append((irow, icol - 1))

                        curr_level = next_level

                    if surrounded:
                        for irow, icol in region:
                            board[irow][icol] = "X"
                    else:
                        visited.update(region)

    def is_border(self, row, col, board) -> bool:
        return row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1

    def is_in_region(self, row, col, board) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O"


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
    Solution().solve(board)
    print(board)
