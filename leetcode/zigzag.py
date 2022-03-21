class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        arr = [[] for _ in range(numRows)]

        down = True
        row = 0
        for ch in s:
            arr[row].append(ch)
            if row == 0 and not down:
                down = True
            if row == numRows - 1 and down:
                down = False
            row += 1 if down else - 1

        return "".join(item for arr_2 in arr for item in arr_2)


if __name__ == '__main__':
    print(Solution().convert("ABCD", 2))
