from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for num_two_idx, num_two in enumerate(nums):
            num_one = target - num_two
            if num_one in nums_idx:
                return [nums_idx[num_one], num_two_idx]
            nums_idx[num_two] = num_two_idx

    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for idx, num in enumerate(nums):
            if num not in nums_idx:
                nums_idx[num] = []
            nums_idx[num].append(idx)

        for num_one_idx, num_one in enumerate(nums):
            num_two = target - num_one
            if num_two in nums_idx:
                num_two_idxes = nums_idx[num_two]
                if num_one != num_two:
                    return [num_one_idx, num_two_idxes[0]]
                if len(num_two_idxes) > 1:
                    return [num_one_idx, num_two_idxes[1]]

    def twoSumBinSearch(self, nums: List[int], target: int) -> List[int]:
        sorted_nums_with_idx = sorted(enumerate(nums), key=lambda x: x[1])

        for idx, num_one_with_index in enumerate(sorted_nums_with_idx):
            num_one = num_one_with_index[1]
            num_two = target - num_one
            num_two_idx = self.binsearch(sorted_nums_with_idx, idx + 1, len(sorted_nums_with_idx) - 1, num_two)
            if num_two_idx != -1:
                return [num_one_with_index[0], sorted_nums_with_idx[num_two_idx][0]]
            # for j in range(i, len(nums)):
            #     if nums[i] + nums[j] == target:
            #         return [i, j]

    def binsearch(self, cost: List[List[int]], i: int, j: int, el: int) -> int:
        if i > j:
            return -1

        el_idx = (i + (j - i) // 2)
        if el == cost[el_idx][1]:
            return el_idx

        if el < cost[el_idx][1]:
            return self.binsearch(cost, i, el_idx - 1, el)
        else:
            return self.binsearch(cost, el_idx + 1, j, el)


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 3], 6))
