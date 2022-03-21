class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        pos = n > 0
        n *= 1 if n > 0 else -1
        while n > 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                if pos:
                    res *= x
                else:
                    res /= x
                n -= 1
        return res


if __name__ == '__main__':
    print(Solution().myPow(2, -2))
