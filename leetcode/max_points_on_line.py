from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        lines = dict()
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                params = self.line_params(p1[0], p1[1], p2[0], p2[1])

                if params in lines:
                    pts = lines[params]
                    pts.add(p1)
                    pts.add(p2)
                else:
                    lines[params] = {p1, p2}

        return max(len(points) for points in lines.values())

    def line_eq(self, x1: int, y1: int, x2: int, y2: int):
        slope = (y1 - y2) / (x1 - x2)
        b = (x1 * y2 - x2 * y1) / (x1 - x2)

        def is_on_line(x: int, y: int) -> bool:
            return y == x * slope + b

        return is_on_line

    def line_params(self, x1: int, y1: int, x2: int, y2: int):
        slope = (y1 - y2) / (x1 - x2) if x1 - x2 != 0 else 'inf'
        b = (x1 * y2 - x2 * y1) / (x1 - x2) if x1 - x2 != 0 else x1
        return slope, b


if __name__ == "__main__":
    print(Solution().maxPoints([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]]))
