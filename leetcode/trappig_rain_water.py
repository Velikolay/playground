from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        acc = [0] * len(height)
        left, right = 0, len(height) - 1
        max_level = 0

        while left < right:
            level = min(height[left], height[right])
            max_level = max(level, max_level)
            acc[left], acc[right] = max_level, max_level

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        for idx in range(len(height)):
            acc[idx] -= min(acc[idx], height[idx])

        return sum(acc)


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
