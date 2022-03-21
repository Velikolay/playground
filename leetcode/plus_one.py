from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        idx = len(digits) - 1
        while one and idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                one = 0
            idx -= 1

        if one == 1:
            return [1] + digits
        return digits


if __name__ == "__main__":
    print(Solution().plusOne([9]))
