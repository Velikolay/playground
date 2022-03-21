class Solution:
    def isMatchRecursive(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) > 0 and len(p) == 0:
            return False

        wildcard = len(p) > 1 and p[1] == "*"

        if wildcard:
            return (s and p[0] in {s[0], '.'} and self.isMatchRecursive(s[1:], p)) or self.isMatchRecursive(s, p[2:])
        else:
            return self.isMatchRecursive(s[1:], p[1:]) if s and p[0] in {s[0], '.'} else False

    def isMatchDP(self, s: str, p: str) -> bool:
        table = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        table[0][0] = True

        for sidx in range(len(s) + 1):
            for pidx in range(1, len(p) + 1):
                if p[pidx - 1] == "*":
                    table[sidx][pidx] = table[sidx][pidx - 2] or table[sidx][pidx - 1] or (p[pidx - 2] in {s[sidx - 1], '.'} and table[sidx - 1][pidx])
                else:
                    table[sidx][pidx] = p[pidx - 1] in {s[sidx - 1], '.'} and table[sidx - 1][pidx - 1]

        return table[-1][-1]


if __name__ == '__main__':
    print(Solution().isMatchRecursive("", "a*"))
    print(Solution().isMatchRecursive("aab", "c*a*b"))
    print(Solution().isMatchRecursive("aa", "a"))
    print(Solution().isMatchRecursive("aa", "a*"))
    print(Solution().isMatchRecursive("aaa", "a*a"))

    # print(Solution().isMatchDP("", "a*")) # Test case not covered
    print(Solution().isMatchDP("aab", "c*a*b"))
    print(Solution().isMatchDP("aa", "a"))
    print(Solution().isMatchDP("aa", "a*"))
    print(Solution().isMatchDP("aaa", "a*a"))
