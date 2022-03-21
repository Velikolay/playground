class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        # dp = [[False] * len(s)] * len(s)
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for incr in range(len(s)):
            for i in range(len(s) - incr):
                if incr == 0:
                    dp[i][i] = True
                elif incr == 1:
                    if s[i] == s[i + 1]:
                        dp[i][i + 1] = True
                else:
                    if dp[i + 1][i + incr - 1] and s[i] == s[i + incr]:
                        dp[i][i + incr] = True

        maxp = 0
        start, end = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] and maxp < j - i + 1:
                    maxp = j - i + 1
                    start, end = i, j + 1
        return s[start:end]

    def longestPalindromeBruteForce(self, s: str) -> str:
        longest = 0
        palindrome = ""
        for i in range(len(s)):
            if len(s) - i <= longest:
                break
            for j in range(i, len(s)):
                if longest < j - i + 1 and self.isPalindrome(s, i, j):
                    longest = j - i + 1
                    palindrome = s[i:j+1]
        return palindrome

    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print(Solution().longestPalindromeDP("babad"))
