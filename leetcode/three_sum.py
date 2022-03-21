from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        for i in range(len(nums)):
            twoSums = self.twoSum(nums, i + 1, -nums[i])
            treeSums = [[nums[i], nums[twoSum[0]], nums[twoSum[1]]] for
                        twoSum in twoSums]
            sums.extend(treeSums)
        # dedup
        return list(set(tuple(sorted(tsum)) for tsum in sums))

    def twoSum(self, nums: List[int], from_idx: int, target: int) -> List[
        Tuple[int, int]]:
        res = []
        nums_idx = {}
        for num_two_idx in range(from_idx, len(nums)):
            num_two = nums[num_two_idx]
            num_one = target - num_two
            if num_one in nums_idx:
                res.append((nums_idx[num_one], num_two_idx))
            nums_idx[num_two] = num_two_idx
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
