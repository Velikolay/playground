from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1
        while row_begin < row_end and col_begin < col_end:
            for col in range(col_begin, col_end):
                res.append(matrix[row_begin][col])

            for row in range(row_begin, row_end):
                res.append(matrix[row][col_end])

            for col in range(col_end, col_begin, -1):
                res.append(matrix[row_end][col])

            for row in range(row_end, row_begin, -1):
                res.append(matrix[row][col_begin])

            row_begin, row_end = row_begin + 1, row_end - 1
            col_begin, col_end = col_begin + 1, col_end - 1

        if row_begin == row_end:
            return res + [matrix[row_begin][j] for j in range(col_begin, col_end + 1)]
        if col_begin == col_end:
            return res + [matrix[i][col_begin] for i in range(row_begin, row_end + 1)]
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3]]))
    print(Solution().spiralOrder([[1], [2], [3]]))
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
