#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx, max_idx = 0, 0
        max_profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] < prices[min_idx]:
                min_idx = max_idx = idx
            elif prices[idx] > prices[max_idx]:
                max_idx = idx
                profit = prices[max_idx] - prices[min_idx]
                max_profit = profit if profit > max_profit else max_profit

        return max_profit


# @lc code=end
