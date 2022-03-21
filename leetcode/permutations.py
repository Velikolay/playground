from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteRec(nums, 0)

    def permuteRec(self, nums: List[int], idx: int) -> List[List[int]]:
        if idx == len(nums) - 1:
            return [[nums[idx]]]

        perms = self.permuteRec(nums, idx + 1)

        return [perm[:i] + [nums[idx]] + perm[i:] for perm in perms for i
                in range(len(perm) + 1)]


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
