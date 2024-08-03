"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
     
     
示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。


提示：
1 <= prices.n <= 10^5
0 <= prices[i] <= 10^4
"""
from typing import List

'''
# 思路：(画图就可以很明显看出解法)
由于我们是想获取到最大的利润，我们的策略应该是低点买入，高点卖出。
由于题目对于交易次数有限制，只能交易一次，因此问题的本质其实就是求波峰浪谷的差值的最大值。
'''



# 方法1：暴力法：O(n^2) 超时
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # 股票只能买卖一次，返回你可以从这笔交易中获取的最大利润
        ans = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(ans, prices[j] - prices[i])

        return ans


# todo 方法2：min_v记录历史最低价，然后比较每天卖出，能获得的最大利润(最优解)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 股票只能买卖一次，返回你可以从这笔交易中获取的最大利润
        ans = 0  
        # todo min_v记录过去历史最低价格
        min_v = float('inf')  

        for p in prices:
            min_v = min(min_v, p)
            ans = max(p - min_v, ans)
        return ans



# todo 方法3：动态规划：dp[i]记录手上有股票和没有股票2种状态的最大收益
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        # 股票只能买卖一次，返回你可以从这笔交易中获取的最大利润
        n = len(prices)

        # dp[i][0]代表第i天过后手上有股票时的最大收益
        # dp[i][1]代表第i天过后手上无股票时的最大收益
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [-prices[0], 0]

        for i in range(1, n):
            # dp[i-1][0] 今天的股票太贵了，买之前的股票更划算
            # - prices[i] 今天的股票更便宜，我买了，prices[i]块钱拿去
            dp[i][0] = max(dp[i-1][0], - prices[i])

            # dp[i-1][1] 今天股市不行，还是之前卖更划算
            # prices[i] + dp[i-1][0] 今天的行情不错，股票卖掉，赚prices[i]块钱，dp[i-1][0]是之前低价买入花的钱
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])

        return dp[-1][-1]

