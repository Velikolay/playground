import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize - 1] * len(nums)
        dp[-1] = 0
        for idx in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[idx] + 1):
                if idx + jump < len(dp):
                    jumps = dp[idx + jump] + 1
                    if dp[idx] > jumps:
                        dp[idx] = jumps

        return dp[0]
