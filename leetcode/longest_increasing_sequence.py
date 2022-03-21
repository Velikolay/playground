from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and arr[j] + 1 > arr[i]:
                    arr[i] = arr[j] + 1
        return max(arr)
