from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tidx = self.binSearch(nums, target)

        if tidx == -1:
            return [-1, -1]

        incr = - 1
        left_idx = tidx + incr
        while left_idx >= 0 and nums[left_idx] == target:
            left_idx += incr
        left_idx += 1

        incr = 1
        right_idx = tidx + incr
        while right_idx < len(nums) and nums[right_idx] == target:
            right_idx += incr
        right_idx -= 1

        return [left_idx, right_idx]

    def binSearch(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            idx = start + (end - start) // 2
            if nums[idx] == target:
                return idx

            if nums[idx] < target:
                start = idx + 1
            else:
                end = idx - 1
        return -1


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
