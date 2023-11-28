#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for idx in range(1, len(prices)):
            if buy > prices[idx]:
                buy = prices[idx]
            elif (prices[idx] - buy) > max_profit:
                max_profit = prices[idx] - buy

        return max_profit


# @lc code=end
