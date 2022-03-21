from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = [""]
        idx = 0
        while idx < len(digits):
            letters = digit_dict[digits[idx]]
            res = [comb + letter for comb in res for letter in letters]
            idx += 1
        return res


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
