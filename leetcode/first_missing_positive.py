from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)
        i = 1
        while i in numset:
            i += 1
        return i

    def firstMissingPositiveCycleSort(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # this while loop doesn't do work on already processed ones
            while (nums[i] > 0) and (nums[i] < len(nums)) and (
                    nums[nums[i] - 1] != nums[i]):
                idx = nums[i] - 1
                nums[idx], nums[i] = nums[i], nums[idx]

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        return len(nums) + 1
