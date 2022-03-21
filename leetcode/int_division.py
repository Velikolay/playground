class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = 1 if (dividend > 0) ^ (divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 0
            while dividend > divisor << k + 1:
                k += 1
            quotient += 1 << k
            dividend -= divisor << k
        return sign * quotient


if __name__ == '__main__':
    print(Solution().divide(7, -3))
