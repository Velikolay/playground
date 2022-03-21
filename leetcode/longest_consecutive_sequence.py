from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        visited = set()
        elems = set(nums)

        for num in nums:
            if num not in visited:
                visited.add(num)
                seq_len = 1

                left = num - 1
                while left in elems:
                    visited.add(left)
                    seq_len += 1
                    left -= 1

                right = num + 1
                while right in elems:
                    visited.add(right)
                    seq_len += 1
                    right += 1

                res = max(res, seq_len)
        return res
