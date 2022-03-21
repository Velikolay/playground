from typing import List, Set


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpLinear(nums)
        # return self.canJumpRec(nums, set(), 0)

    def canJumpLinear(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums):
                return True
        return True

    def canJumpRec(self, nums: List[int], visited: Set[int], idx: int) -> bool:
        if idx == len(nums) - 1:
            return True

        for next_idx in range(idx + 1, min(idx + nums[idx] + 1, len(nums))):
            if next_idx not in visited:
                visited.add(next_idx)
                if self.canJumpRec(nums, visited, next_idx):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
