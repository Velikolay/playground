class Solution:
    class Solution:
        def myAtoi(self, s: str) -> int:
            if len(s) == 0:
                return 0

            num = 0
            sign = 1

            start = 0
            while start < len(s) and s[start] == ' ':
                start += 1

            if start < len(s):
                if s[start] == '-':
                    sign = -1
                    start += 1
                elif s[start] == '+':
                    sign = 1
                    start += 1

            end = start
            while end < len(s) and '0' <= s[end] <= '9':
                end += 1

            if start == end:
                return 0

            mult = pow(10, end - start - 1)
            for idx in range(start, end):
                num += int(s[idx]) * mult
                mult //= 10

            if sign == -1:
                return max(-num, -2147483648)
            else:
                return min(num, 2147483647)


if __name__ == "__main__":
    print(Solution().myAtoi("4193 with words"))
