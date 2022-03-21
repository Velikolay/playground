from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res

        i = 3
        while i <= numRows:
            prev = res[-1]
            nxt = [1]
            for j in range(len(prev) - 1):
                nxt.append(prev[j] + prev[j + 1])
            nxt.append(1)
            res.append(nxt)
            i += 1
        return res
