class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        dp_idx = 1
        for sidx in range(len(s) - 1, -1, -1):
            if s[sidx] == '0':
                dp[dp_idx] = 0
            elif sidx + 1 < len(s) and (s[sidx] == '1' or (s[sidx] == '2' and '0' <= s[sidx + 1] <= '6')):
                dp[dp_idx] = dp[dp_idx - 1] + dp[dp_idx - 2]
            else:
                dp[dp_idx] = dp[dp_idx - 1]
            dp_idx += 1
        return dp[-1]
        # return self.numDecodingsRec(s, 0)

    def numDecodingsRec(self, s: str, idx: int) -> int:
        if idx >= len(s):
            return 1

        if s[idx] == '0':
            return 0

        res = 0
        if len(s) > idx + 1 and (
                s[idx] == '1' or (s[idx] == '2' and '0' <= s[idx + 1] <= '6')):
            res += self.numDecodingsRec(s, idx + 2)

        res += self.numDecodingsRec(s, idx + 1)
        return res


if __name__ == "__main__":
    print(Solution().numDecodings("1111111"))
