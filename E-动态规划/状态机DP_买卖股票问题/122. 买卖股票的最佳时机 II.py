"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。

示例 1：
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     总利润为 4 。

示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。


提示：
1 <= prices.n <= 3 * 10^4
0 <= prices[i] <= 10^4
"""
from typing import List

# todo 方法1：贪心算法 =》因为交易次数不受限，如果可以把所有的上坡全部收集到，一定是利益最大化的(最优解)
# 注意：
# 虽然「贪心算法」在时间复杂度和空间复杂度上都达到了最优，但是它的应用条件非常强，
# 当前问题如果没有「不限制交易次数」这个条件，贪心算法的正确性就不成立。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最多1只股票，不限制交易次数，返回能获得的最大收益
        ans = 0
        for i in range(1, len(prices)):
            # 第二天起,每天一卖一买。ans只累加上涨的收益
            ans += max(0, prices[i] - prices[i-1])

        return ans


# todo 方法2：多状态dp, dp[i]记录手上有股票和没有股票2种状态的最大收益
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0]代表第i天过后手上有股票时的最大收益
        # dp[i][1]代表第i天过后手上无股票时的最大收益
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [-prices[0], 0]

        for i in range(1, n):
            # dp[i-1][0] 今天的股票太贵了，买之前的股票更划算
            # - prices[i] 今天的股票更便宜，我买了，prices[i]块钱拿去, dp[i-1][1]是我之前卖股票赚的钱
            dp[i][0] = max(dp[i - 1][0], - prices[i] + dp[i - 1][1])

            # dp[i-1][1] 今天股市不行，还是之前卖更划算
            # prices[i] + dp[i-1][0] 今天的行情不错，股票卖掉，赚prices[i]块钱，dp[i-1][0]是之前低价买入花的钱
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[-1][-1]
