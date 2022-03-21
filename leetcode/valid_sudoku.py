from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # check valid rows
        for i in range(n):
            nums = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])

        # check valid cols
        for j in range(n):
            nums = set()
            for i in range(n):
                if board[i][j] != '.':
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])

        # check valid 3x3 boxes
        ranges = [
            (range(3), range(3)), (range(3), range(3, 6)), (range(3), range(6, 9)),
            (range(3, 6), range(3)), (range(3, 6), range(3, 6)), (range(3, 6), range(6, 9)),
            (range(6, 9), range(3)), (range(6, 9), range(3, 6)), (range(6, 9), range(6, 9)),
        ]

        for range_tuple in ranges:
            nums = set()
            for i in range_tuple[0]:
                for j in range_tuple[1]:
                    if board[i][j] != '.':
                        if board[i][j] in nums:
                            return False
                        nums.add(board[i][j])

        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
