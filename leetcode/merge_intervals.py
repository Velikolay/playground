from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            if res[-1][0] <= interval[0] <= res[-1][1]:
                res[-1] = [min(res[-1][0], interval[0]),
                           max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        return res
