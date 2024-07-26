"""
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。


示例 1：
输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8

示例 2：
输入：prices = [1,3,7,5,10,3], fee = 3
输出：6


提示：
1 <= prices.n <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
"""
from typing import List

# todo 多状态dp
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 手头最多一只股票，不限制交易次数，每笔交易有fee的手续费，返回可以获得的最大收益
        dp = [[0, 1] for _ in range(len(prices))]
        # dp[i][0]代表手头有股票的最大收益
        # dp[i][1]代表手头没有股票的最大收益

        # 第一天
        dp[0] = [-prices[0], 0]
        
        # 第二天起
        for i in range(1, len(prices)):
            # 手头有股票：1.之前低价买;  2.今天买（要算上之前卖的）
            dp[i][0] = max(dp[i - 1][0], -prices[i] + dp[i - 1][1])
            # 手头没有股票：1.之前高价卖； 2.今天卖:需要加之前买的成本 和 手续费
            dp[i][1] = max(dp[i - 1][1], prices[i] - fee + dp[i - 1][0])

        print(dp)
        return dp[-1][-1]



