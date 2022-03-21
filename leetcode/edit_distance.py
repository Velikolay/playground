class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for row in range(len(word1) + 1)]

        for row in range(len(word1) + 1):
            dp[row][0] = row

        for col in range(len(word2) + 1):
            dp[0][col] = col

        for row in range(1, len(word1) + 1):
            for col in range(1, len(word2) + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # min between replace(\), insert(<-), delete(|) + 1
                    dp[row][col] = min([dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]]) + 1
        # for row in dp:
        #     print(row)
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().minDistance("ore", "horse"))

