from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [None] * (len(s) + 1)
        for ci in range(len(s) - 1, -1, -1):
            ps = self.find_palindromes(s, ci)
            res = []
            for p in ps:
                prev = dp[ci + len(p)]
                if not prev:
                    res.append([p])
                else:
                    res.extend([[p] + item for item in prev])
            dp[ci] = res
        return dp[0]

    def find_palindromes(self, s: str, start: int) -> List[str]:
        def is_palindrome(s: str, start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        palindromes = []
        for end in range(start, len(s)):
            if is_palindrome(s, start, end):
                palindromes.append(s[start: end + 1])
        return palindromes


if __name__ == "__main__":
    print(Solution().partition("aab"))
