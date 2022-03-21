from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # return self.isMatchRec(s, p, 0, 0)
        return self.isMatchDP(s, p)

    def isMatchDP(self, s: str, p: str) -> bool:
        # dp = [[False] * (len(s) + 1)] * (len(p) + 1)
        dp = [[False for col in range(len(s) + 1)] for row in range(len(p) + 1)]
        dp[0][0] = True
        for pi in range(1, len(dp)):
            for si in range(len(dp[0])):
                sci, pci = si - 1, pi - 1
                if si > 0 and (s[sci] == p[pci] or p[pci] == "?"):
                    dp[pi][si] = dp[pi - 1][si - 1]

                if p[pci] == "*":
                    dp[pi][si] = dp[pi - 1][si] or dp[pi][si - 1]

        return dp[-1][-1]

    @cache
    def isMatchRec(self, s: str, p: str, s_idx: int, p_idx: int) -> bool:
        if p_idx == len(p) and s_idx == len(s):
            return True
        if p_idx == len(p) and s_idx < len(s):
            return False

        if s_idx < len(s) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
            return self.isMatchRec(s, p, s_idx + 1, p_idx + 1)

        if p[p_idx] == "*":
            return self.isMatchRec(s, p, s_idx, p_idx + 1) or (s_idx < len(s) and self.isMatchRec(s, p, s_idx + 1, p_idx + 1)) or (s_idx < len(s) and self.isMatchRec(s, p, s_idx + 1, p_idx))
        return False


if __name__ == "__main__":
    print(Solution().isMatchDP("zacabz", "*a?b*"))
