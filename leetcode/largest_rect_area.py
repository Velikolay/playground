from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mx = 0
        # sliding window technique - O(n)
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # current maxheight
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1  # num of bars
                mx = max(mx, height * width)
            stack.append(i)

        return mx
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     left, right = 0, len(heights) - 1
    #     areas = []
    #     prev_height = 0
    #
    #     while left <= right:
    #         min_height = min(heights[left], heights[right])
    #         if min_height > prev_height:
    #             areas.append([min_height, right - left + 1])
    #         else:
    #             for area in areas:
    #                 area[0] = min(area[0], min_height)
    #         prev_height = min_height
    #
    #         if heights[left + 1] < heights[right - 1]:
    #             left += 1
    #         else:
    #             right -= 1
    #
    #     return max([area[0] * area[1] for area in areas]) if areas else 0


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
