from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.searchPivotIdx(nums, 0, len(nums) - 1)
        if pivot == 0:
            return self.binsearch(nums, 0, len(nums) - 1, target)

        if nums[pivot] == target:
            return pivot

        if nums[0] <= target:
            return self.binsearch(nums, 0, pivot - 1, target)
        else:
            return self.binsearch(nums, pivot + 1, len(nums) - 1, target)

    def searchPivotIdx(self, nums: List[int], i: int, j: int) -> int:
        if i >= j:
            return 0

        if i + 1 == j:
            return j if nums[i] > nums[j] else 0

        mid = i + (j - i) // 2
        if nums[i] > nums[mid]:
            return self.searchPivotIdx(nums, i, mid)
        else:
            return self.searchPivotIdx(nums, mid, j)

    def binsearch(self, nums, i, j, el):
        if i > j:
            return -1

        el_idx = (i + (j - i) // 2)
        if el == nums[el_idx]:
            return el_idx

        if el < nums[el_idx]:
            return self.binsearch(nums, i, el_idx - 1, el)
        else:
            return self.binsearch(nums, el_idx + 1, j, el)


if __name__ == '__main__':
    print(Solution().search([3, 1], 3))
    # print(Solution().search([1], 0))
    # print(Solution().searchPivotIdx([1], 0, 0))
    # print(Solution().search([4, 5, 6, 7, 0, 1, 2], 4))
    # print(Solution().search([4, 5, 6, 7, 0, 1, 2], 1))
    # print(Solution().search([4, 5, 6, 7, 0, 1, 2], 6))
    # print(Solution().searchPivotIdx([4, 5, 6, 7, 0, 1, 2], 0, 6))
    # print(Solution().searchPivotIdx([5, 6, 7, 0, 1, 2, 4], 0, 6))
    # print(Solution().searchPivotIdx([6, 7, 0, 1, 2, 4, 5], 0, 6))
    # print(Solution().searchPivotIdx([0, 1, 2, 4, 5, 6, 7], 0, 6))
