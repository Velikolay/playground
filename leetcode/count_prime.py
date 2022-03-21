from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        count = 0
        primes = [True] * (n + 1)

        for num in range(2, n):
            if primes[num]:
                count += 1

                for mult in range(2*num, n, num):
                    primes[mult] = False
        return count

    # def countPrimes(self, n: int) -> int:
    #     count = 0
    #     for num in range(2, n + 1):
    #         count += self.isPrime(num)
    #     return count

    def isPrime(self, n: int) -> int:
        if n < 2 or n % 2 == 0 or n % 3 == 0:
            return 0

        for num in range(2, int(sqrt(n)) + 1):
            if n % num == 0:
                return 0
        return 1


if __name__ == "__main__":
    print(Solution().countPrimes(10))
