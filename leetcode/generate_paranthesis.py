from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']

        res = set()
        gen = [self.generateParenthesis(i) for i in range(n)]
        fcombos = [(gen[i], gen[j]) for i, j in zip(range(len(gen)//2 + 1), reversed(range(len(gen)//2 - 1, len(gen))))]
        rcombos = [(combo[1], combo[0]) for combo in fcombos]

        for combo in fcombos + rcombos:
            for first_gen in combo[0]:
                for second_gen in combo[1]:
                    res.add('(' + first_gen + ')' + second_gen)
        return list(res)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
