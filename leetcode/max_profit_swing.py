from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, profit = 0, 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                max_profit += profit
                buy = prices[i]
                profit = 0
            else:
                profit = max(profit, prices[i] - buy)
        return max_profit + profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
